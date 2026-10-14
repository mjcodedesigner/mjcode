## 2025-02-28 - Accessible Accordions

**Learning:** When building custom disclosure widgets (like accordions) with `<button>` elements, standard hover states aren't enough for accessibility. Buttons require explicit `aria-expanded` attributes that update dynamically via JavaScript, an `aria-controls` attribute pointing to the content ID, and clear `:focus-visible` styling so keyboard navigators can see which item has focus. Decorative icons inside buttons should also have `aria-hidden="true"`.

**Action:** Ensure all future accordion or disclosure widgets include dynamic `aria-expanded` state toggling, `aria-controls`, and use `focus-visible` ring utilities rather than just relying on generic hover classes.
