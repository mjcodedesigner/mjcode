## 2025-02-28 - Accessible Accordions

**Learning:** When building custom disclosure widgets (like accordions) with `<button>` elements, standard hover states aren't enough for accessibility. Buttons require explicit `aria-expanded` attributes that update dynamically via JavaScript, an `aria-controls` attribute pointing to the content ID, and clear `:focus-visible` styling so keyboard navigators can see which item has focus. Decorative icons inside buttons should also have `aria-hidden="true"`.

**Action:** Ensure all future accordion or disclosure widgets include dynamic `aria-expanded` state toggling, `aria-controls`, and use `focus-visible` ring utilities rather than just relying on generic hover classes.

## 2026-10-19 - Sticky Headers & Anchor Offsets
**Learning:** When a site has a sticky header, anchor links (like "skip to content" or navigation items) can cause the target content to be obscured by the header.
**Action:** Use CSS scroll-padding (e.g., Tailwind's `scroll-pt-24` on the `<html>` tag) to ensure all anchor link targets are offset by the height of the sticky header.
