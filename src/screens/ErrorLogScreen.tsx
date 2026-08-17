/* ═══════════════════════════════════════════════
   GRAMLINGO — WrongBook Screen
   Filterable review of missed questions
   Export to Markdown (.md) and PDF (print-to-PDF)
   ═══════════════════════════════════════════════ */

import { useState } from 'react';
import { useAppContext } from '../app/app-state';
import { Button } from '../components/Button/Button';
import { Gramlin } from '../components/Gramlin/Gramlin';
import { Badge } from '../components/Badge/Badge';
import { Card } from '../components/Card/Card';
import { getStrings } from '../i18n/i18n';
import { GAME_DATA } from '../game/data';
import type { ErrorEntry } from '../game/types';
import './ErrorLogScreen.css';

/* ── Export helpers ───────────────────────────── */

/** Strip HTML tags/entities from question/answer strings (uses DOM, so entities decode). */
function stripHtml(html: string): string {
  const div = document.createElement('div');
  div.innerHTML = html;
  return (div.textContent || '').replace(/\s+/g, ' ').trim();
}

/** Escape a string for safe injection into the generated PDF HTML document. */
function escapeHtml(s: string): string {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

/** Trigger a client-side file download from a string blob. */
function downloadFile(filename: string, content: string, mime: string) {
  const blob = new Blob([content], { type: mime });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

export function ErrorLogScreen() {
  const { language, navigateTo, errorLog, getErrorsByModule, startPhase } = useAppContext();
  const s = getStrings(language);
  const isZh = language === 'zh';

  const [filterModule, setFilterModule] = useState<string | null>(null);

  const filtered = filterModule ? getErrorsByModule(filterModule) : errorLog;
  const sorted = [...filtered].sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime());

  const handleRetryQuestion = (entry: typeof sorted[0]) => {
    startPhase(entry.moduleId, entry.phaseId);
  };

  /* ── MD export ─────────────────────────────── */

  const exportMarkdown = () => {
    const lines: string[] = [];
    lines.push(`# ${s.appName} — ${s.errorLog}`);
    lines.push('');
    lines.push(`> ${s.exportGenerated}: ${new Date().toLocaleString()} · ${sorted.length}`);
    lines.push('');

    let lastModule: string | null = null;
    let lastPhase: string | null = null;

    sorted.forEach((entry, i) => {
      const module = GAME_DATA.modules.find((m) => m.id === entry.moduleId);
      const phase = GAME_DATA.phases.find((p) => p.id === entry.phaseId);
      const question = phase?.q[entry.questionIndex];
      const moduleName = isZh ? module?.nameZh : module?.name;
      const phaseName = isZh ? phase?.nameZh : phase?.name;

      if (moduleName !== lastModule) {
        lines.push(`## ${moduleName ?? entry.moduleId}`);
        lines.push('');
        lastModule = moduleName ?? entry.moduleId;
        lastPhase = null;
      }
      if (phaseName !== lastPhase) {
        lines.push(`### ${phaseName ?? entry.phaseId}`);
        lines.push('');
        lastPhase = phaseName ?? entry.phaseId;
      }

      lines.push(`${i + 1}. **${s.question}:** ${stripHtml(question?.q ?? '')}`);
      lines.push(`   - ${s.yourAnswer}: ${stripHtml(entry.userAnswer)}`);
      lines.push(`   - ${s.correctAnswer}: ${stripHtml(entry.correctAnswer)}`);
      lines.push(`   - ${new Date(entry.timestamp).toLocaleString()}`);
      lines.push('');
    });

    const date = new Date().toISOString().slice(0, 10);
    downloadFile(`gramlingo-error-log-${date}.md`, lines.join('\n'), 'text/markdown;charset=utf-8');
  };

  /* ── PDF export (print-to-PDF document) ─────── */

  const exportPdf = () => {
    const moduleName = (id: string) =>
      GAME_DATA.modules.find((m) => m.id === id);
    const phaseName = (id: string) =>
      GAME_DATA.phases.find((p) => p.id === id);

    let lastModule: string | null = null;
    const body: string[] = [];

    sorted.forEach((entry: ErrorEntry, i) => {
      const mod = moduleName(entry.moduleId);
      const ph = phaseName(entry.phaseId);
      const question = ph?.q[entry.questionIndex];
      const modLabel = isZh ? mod?.nameZh : mod?.name;
      const phLabel = isZh ? ph?.nameZh : ph?.name;

      if (modLabel !== lastModule) {
        body.push(`<h2 class="module">${escapeHtml(modLabel ?? entry.moduleId)}</h2>`);
        lastModule = modLabel ?? entry.moduleId;
      }

      body.push(`
        <div class="entry">
          <div class="entry-meta">
            <span class="phase">${escapeHtml(phLabel ?? entry.phaseId)}</span>
            <span class="num">#${i + 1}</span>
            <span class="date">${escapeHtml(new Date(entry.timestamp).toLocaleString())}</span>
          </div>
          <div class="q">${escapeHtml(stripHtml(question?.q ?? ''))}</div>
          <div class="ans ans--user"><span class="label">${escapeHtml(s.yourAnswer)}</span>${escapeHtml(stripHtml(entry.userAnswer))}</div>
          <div class="ans ans--correct"><span class="label">${escapeHtml(s.correctAnswer)}</span>${escapeHtml(stripHtml(entry.correctAnswer))}</div>
        </div>`);
    });

    const title = `${s.appName} — ${s.errorLog}`;
    const html = `<!DOCTYPE html>
<html lang="${language}">
<head>
<meta charset="utf-8" />
<title>${escapeHtml(title)}</title>
<style>
  * { box-sizing: border-box; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans SC", sans-serif;
    color: #1f2937;
    max-width: 780px;
    margin: 0 auto;
    padding: 32px 24px;
    line-height: 1.55;
  }
  h1 { font-size: 24px; margin: 0 0 4px; }
  .meta { color: #6b7280; font-size: 13px; margin-bottom: 24px; }
  .screen-note { background: #fff7ed; border: 1px solid #fdba74; color: #9a3412; border-radius: 8px; padding: 10px 14px; font-size: 13px; margin-bottom: 20px; }
  .module { font-size: 17px; color: #e04080; border-bottom: 2px solid #f3d1e0; padding-bottom: 4px; margin: 24px 0 12px; page-break-after: avoid; }
  .entry { border: 1px solid #e5e7eb; border-radius: 10px; padding: 12px 14px; margin-bottom: 12px; page-break-inside: avoid; }
  .entry-meta { display: flex; gap: 10px; align-items: center; margin-bottom: 8px; font-size: 12px; color: #6b7280; }
  .phase { font-weight: 600; color: #374151; }
  .num { color: #9ca3af; }
  .date { margin-left: auto; }
  .q { background: #f9fafb; border-radius: 6px; padding: 8px 10px; font-size: 14px; margin-bottom: 8px; }
  .ans { font-size: 13px; padding: 6px 10px; border-radius: 6px; margin-bottom: 6px; }
  .ans .label { font-weight: 600; margin-right: 8px; }
  .ans--user { background: #fef2f2; border: 1px solid #fecaca; }
  .ans--user .label { color: #b91c1c; }
  .ans--correct { background: #f0fdf4; border: 1px solid #bbf7d0; }
  .ans--correct .label { color: #15803d; }
  @media print {
    body { padding: 0; }
    .screen-note { display: none; }
    .entry { break-inside: avoid; }
  }
</style>
</head>
<body>
  <h1>${escapeHtml(title)}</h1>
  <div class="meta">${escapeHtml(s.exportGenerated)}: ${escapeHtml(new Date().toLocaleString())} · ${sorted.length}</div>
  <div class="screen-note">💡 ${language === 'zh' ? '在打印对话框中选择「另存为 PDF」即可导出。' : language === 'es' ? 'En el diálogo de impresión, elige «Guardar como PDF».' : 'In the print dialog, choose "Save as PDF".'}</div>
  ${body.join('')}
</body>
</html>`;

    // Open a print-ready window (trusted user-gesture context), then trigger print.
    const win = window.open('', '_blank');
    if (win) {
      win.document.open();
      win.document.write(html);
      win.document.close();
      win.focus();
      const doPrint = () => {
        try {
          win.print();
        } catch {
          /* some browsers block print on cross-origin/blank docs — fall through to iframe */
        }
      };
      if (win.document.readyState === 'complete') {
        setTimeout(doPrint, 150);
      } else {
        win.onload = doPrint;
      }
    } else {
      // Popup blocked — fall back to a hidden iframe.
      const iframe = document.createElement('iframe');
      iframe.style.position = 'fixed';
      iframe.style.right = '0';
      iframe.style.bottom = '0';
      iframe.style.width = '0';
      iframe.style.height = '0';
      iframe.style.border = '0';
      document.body.appendChild(iframe);
      const doc = iframe.contentDocument;
      if (doc) {
        doc.open();
        doc.write(html);
        doc.close();
        setTimeout(() => {
          try {
            iframe.contentWindow?.print();
          } catch {
            /* noop */
          }
          setTimeout(() => iframe.remove(), 1000);
        }, 300);
      } else {
        iframe.remove();
      }
    }
  };

  if (errorLog.length === 0) {
    return (
      <div className="errorlog-empty">
        <Gramlin pose="sleeper" size="xl" />
        <h2>{s.errorLogEmpty}</h2>
        <Button onClick={() => navigateTo('learning-path')}>{s.home}</Button>
      </div>
    );
  }

  return (
    <div className="errorlog-screen animate-fade-in">
      <div className="errorlog-header">
        <h2>📝 {s.errorLog} ({errorLog.length})</h2>
        <Button variant="ghost" size="sm" onClick={() => navigateTo('learning-path')}>
          ← {s.home}
        </Button>
      </div>

      {/* Export actions */}
      <div className="errorlog-actions">
        <Button
          size="sm"
          variant="secondary"
          onClick={exportPdf}
          disabled={sorted.length === 0}
        >
          📄 {s.exportPdf}
        </Button>
        <Button
          size="sm"
          variant="secondary"
          onClick={exportMarkdown}
          disabled={sorted.length === 0}
        >
          ⬇️ {s.exportMd}
        </Button>
      </div>

      {/* Filter chips */}
      <div className="errorlog-filters">
        <button
          className={`filter-chip ${!filterModule ? 'filter-chip--active' : ''}`}
          onClick={() => setFilterModule(null)}
        >
          All
        </button>
        {GAME_DATA.modules.map((mod) => (
          <button
            key={mod.id}
            className={`filter-chip ${filterModule === mod.id ? 'filter-chip--active' : ''}`}
            onClick={() => setFilterModule(filterModule === mod.id ? null : mod.id)}
          >
            {getErrorsByModule(mod.id).length > 0 && (
              <Badge variant="danger" size="sm">{getErrorsByModule(mod.id).length}</Badge>
            )}
            {isZh ? mod.nameZh : mod.name}
          </button>
        ))}
      </div>

      {/* Wrong entries */}
      <div className="errorlog-list">
        {sorted.map((entry, i) => {
          const phase = GAME_DATA.phases.find((p) => p.id === entry.phaseId);
          const question = phase?.q[entry.questionIndex];
          const module = GAME_DATA.modules.find((m) => m.id === entry.moduleId);
          const date = new Date(entry.timestamp).toLocaleDateString();

          return (
            <Card key={`${entry.moduleId}-${entry.phaseId}-${entry.questionIndex}-${i}`} className="error-entry">
              <div className="error-entry-header">
                <Badge variant="default">{isZh ? module?.nameZh : module?.name}</Badge>
                <Badge variant="info">{isZh ? phase?.nameZh : phase?.name}</Badge>
                <span className="error-date">{date}</span>
              </div>

              {question && (
                <div className="error-entry-question">
                  <p dangerouslySetInnerHTML={{ __html: question.q }} />
                </div>
              )}

              <div className="error-entry-answers">
                <div className="error-answer-bubble error-answer-bubble--user">
                  <span className="answer-label">{s.yourAnswer}:</span>
                  <span dangerouslySetInnerHTML={{ __html: entry.userAnswer }} />
                </div>
                <div className="error-answer-bubble error-answer-bubble--correct">
                  <span className="answer-label">{s.correctAnswer}:</span>
                  <span>{entry.correctAnswer}</span>
                </div>
              </div>

              <Button size="sm" variant="secondary" onClick={() => handleRetryQuestion(entry)}>
                🔄 {s.retryQuestion}
              </Button>
            </Card>
          );
        })}
      </div>
    </div>
  );
}
