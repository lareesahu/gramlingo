import { useRef, useCallback } from 'react';

/**
 * Pointer-based drag-to-scroll for horizontal card carousels.
 * - Mouse: drag the track to scroll (native scrollbars hidden).
 * - Touch: native panning still wins (we never capture touch pointers).
 * - Trackpad: native horizontal scroll passes through untouched.
 * Also disables scroll-snap while dragging so snap doesn't fight the drag,
 * and suppresses child clicks after a real drag (so cards don't toggle
 * when the user was trying to swipe).
 */
export function useDragScroll<T extends HTMLElement>() {
  const drag = useRef<{ pointerId: number; startX: number; startScroll: number; moved: boolean } | null>(null);

  const onPointerDown = useCallback((e: React.PointerEvent<T>) => {
    const el = e.currentTarget;
    drag.current = { pointerId: e.pointerId, startX: e.clientX, startScroll: el.scrollLeft, moved: false };
    if (e.pointerType === 'mouse' && typeof el.setPointerCapture === 'function') {
      el.setPointerCapture(e.pointerId);
    }
    el.style.scrollSnapType = 'none';
    el.classList.add('is-dragging');
  }, []);

  const onPointerMove = useCallback((e: React.PointerEvent<T>) => {
    const d = drag.current;
    const el = e.currentTarget;
    if (!d || d.pointerId !== e.pointerId || !el) return;
    const dx = e.clientX - d.startX;
    if (Math.abs(dx) > 4) d.moved = true;
    if (d.moved) el.scrollLeft = d.startScroll - dx;
  }, []);

  const endDrag = useCallback((e: React.PointerEvent<T>) => {
    const d = drag.current;
    const el = e.currentTarget;
    if (!d || d.pointerId !== e.pointerId) return;
    drag.current = null;
    el.style.scrollSnapType = '';
    el.classList.remove('is-dragging');
    if (d.moved) {
      // Swallow the click that follows a drag so cards don't toggle by accident.
      const stop = (ev: MouseEvent) => { ev.preventDefault(); ev.stopPropagation(); };
      el.addEventListener('click', stop, { capture: true, once: true });
    }
  }, []);

  return { onPointerDown, onPointerMove, onPointerUp: endDrag, onPointerCancel: endDrag };
}
