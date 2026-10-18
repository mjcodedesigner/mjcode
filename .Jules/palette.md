## 2025-02-28 - Accessible Accordions

**Learning:** When building custom disclosure widgets (like accordions) with `<button>` elements, standard hover states aren't enough for accessibility. Buttons require explicit `aria-expanded` attributes that update dynamically via JavaScript, an `aria-controls` attribute pointing to the content ID, and clear `:focus-visible` styling so keyboard navigators can see which item has focus. Decorative icons inside buttons should also have `aria-hidden="true"`.

**Action:** Ensure all future accordion or disclosure widgets include dynamic `aria-expanded` state toggling, `aria-controls`, and use `focus-visible` ring utilities rather than just relying on generic hover classes.

## 2026-10-18 - Skip-to-Content and Sticky Headers
**Learning:** When adding a skip-to-content anchor link (or any anchor link) to a page with a sticky header, the header can obscure the target content when the link is activated. It requires a scroll padding offset on the HTML element (e.g., Tailwind's `scroll-pt-24`) to ensure the target is clearly visible.
**Action:** Ensure all skip links or anchor navigation implemented on sites with sticky/fixed headers include the appropriate CSS scroll-padding offset on the root element.
