
## 2024-05-19 - Sticky Header Scroll Offset
**Learning:** When using sticky headers (like this site's `sticky top-0 z-40`), anchor links naturally scroll until the target element hits the top of the viewport. This results in the sticky header obscuring the target element. Combining this with Tailwind's `scroll-smooth` makes the issue very visually apparent.
**Action:** When implementing sticky headers and in-page anchor links, always apply a scroll-padding utility (e.g., `scroll-pt-28`) to the `<html>` or scrolling container element to provide an offset equal to the sticky header's height.
