import { useRef, useCallback } from 'react';

/**
 * Pointer-based drag-to-scroll for horizontal card carousels.
 * - Mouse: drag the track to scroll (native scrollbars hidden).
 * - Touch: native panning still wins (touch-action: pan-y on the track).
 * - Trackpad: native horizontal scroll passes through untouched.
 *
 * IMPORTANT: we never call setPointerCapture — capturing the pointer
 * retargets the subsequent CLICK to the container, which breaks real
 * clicks on child cards. Drag tracking uses window-level listeners
 * instead, so cards keep receiving their clicks.
 *
 * Also disables scroll-snap while dragging so snap doesn't fight the drag,
 * and suppresses the click that follows a real drag (so cards don't toggle
 * when the user was trying to swipe).
 */
export function useDragScroll<T extends HTMLElement>() {
  const drag = useRef<{ pointerId: number; startX: number; startScroll: number; moved: boolean } | null>(null);
  const elRef = useRef<T | null>(null);

  const onWindowPointerMove = useCallback((e: PointerEvent) => {
    const el = elRef.current;
    const d = drag.current;
    if (!el || !d || d.pointerId !== e.pointerId) return;
    const dx = e.clientX - d.startX;
    if (Math.abs(dx) > 4) d.moved = true;
    if (d.moved) el.scrollLeft = d.startScroll - dx;
  }, []);

  const endDrag = useCallback((e: PointerEvent) => {
    const el = elRef.current;
    const d = drag.current;
    if (!el || !d || d.pointerId !== e.pointerId) return;
    drag.current = null;
    elRef.current = null;
    el.style.scrollSnapType = '';
    el.classList.remove('is-dragging');
    window.removeEventListener('pointermove', onWindowPointerMove);
    window.removeEventListener('pointerup', endDrag);
    window.removeEventListener('pointercancel', endDrag);
    if (d.moved) {
      // Swallow the click that follows a drag so cards don't toggle by accident.
      const stop = (ev: MouseEvent) => { ev.preventDefault(); ev.stopPropagation(); };
      el.addEventListener('click', stop, { capture: true, once: true });
    }
  }, [onWindowPointerMove]);

  const onPointerDown = useCallback((e: React.PointerEvent<T>) => {
    const el = e.currentTarget;
    drag.current = { pointerId: e.pointerId, startX: e.clientX, startScroll: el.scrollLeft, moved: false };
    elRef.current = el;
    el.style.scrollSnapType = 'none';
    el.classList.add('is-dragging');
    window.addEventListener('pointermove', onWindowPointerMove);
    window.addEventListener('pointerup', endDrag);
    window.addEventListener('pointercancel', endDrag);
  }, [onWindowPointerMove, endDrag]);

  return { onPointerDown };
}
