## 2025-02-28 - Accessible Accordions

**Learning:** When building custom disclosure widgets (like accordions) with `<button>` elements, standard hover states aren't enough for accessibility. Buttons require explicit `aria-expanded` attributes that update dynamically via JavaScript, an `aria-controls` attribute pointing to the content ID, and clear `:focus-visible` styling so keyboard navigators can see which item has focus. Decorative icons inside buttons should also have `aria-hidden="true"`.

**Action:** Ensure all future accordion or disclosure widgets include dynamic `aria-expanded` state toggling, `aria-controls`, and use `focus-visible` ring utilities rather than just relying on generic hover classes.

## 2023-10-25 - Accessible Mobile Menu

**Learning:** Just like accordions, mobile menu toggle buttons must explicitly announce their state to screen readers. Relying solely on visual changes (like swapping a hamburger icon for an "X" or toggling the `hidden` class on the menu container) leaves keyboard and screen reader users without context.

**Action:** Ensure all mobile menu toggle buttons utilize dynamic `aria-expanded` attributes, `aria-controls` pointing to the menu ID, `aria-hidden="true"` on decorative icons, and explicit `:focus-visible` styling for clear keyboard navigation indicators.
