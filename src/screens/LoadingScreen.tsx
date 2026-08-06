/* ═══════════════════════════════════════════════
   GRAMLINGO — Loading Screen (Logo Pulse)
   ═══════════════════════════════════════════════ */

import './LoadingScreen.css';

export function LoadingScreen() {
  return (
    <div className="loading-screen">
      <img
        className="loading-logo"
        src={`${import.meta.env.BASE_URL}assets/gramlin/gramlingo-logo.png`}
        alt="GramLingo"
        width={120}
        height={120}
      />
    </div>
  );
}
