## 2025-02-28 - Accessible Accordions

**Learning:** When building custom disclosure widgets (like accordions) with `<button>` elements, standard hover states aren't enough for accessibility. Buttons require explicit `aria-expanded` attributes that update dynamically via JavaScript, an `aria-controls` attribute pointing to the content ID, and clear `:focus-visible` styling so keyboard navigators can see which item has focus. Decorative icons inside buttons should also have `aria-hidden="true"`.

**Action:** Ensure all future accordion or disclosure widgets include dynamic `aria-expanded` state toggling, `aria-controls`, and use `focus-visible` ring utilities rather than just relying on generic hover classes.

## 2026-10-17 - Skip to Content & Sticky Headers
**Learning:** When adding 'Skip to main content' links for keyboard accessibility, if the site uses a fixed/sticky header, jumping to the target  anchor can result in the header obscuring the top of the content.
**Action:** Combine hidden-until-focused skip links with the `scroll-padding-top` CSS property (e.g. `scroll-pt-24` in Tailwind) on the `<html>` element to ensure anchor targets are positioned correctly below the sticky header.
