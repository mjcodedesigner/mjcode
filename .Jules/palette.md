
## 2024-05-19 - Sticky Header Scroll Offset
**Learning:** When using sticky headers (like this site's `sticky top-0 z-40`), anchor links naturally scroll until the target element hits the top of the viewport. This results in the sticky header obscuring the target element. Combining this with Tailwind's `scroll-smooth` makes the issue very visually apparent.
**Action:** When implementing sticky headers and in-page anchor links, always apply a scroll-padding utility (e.g., `scroll-pt-28`) to the `<html>` or scrolling container element to provide an offset equal to the sticky header's height.

## 2024-10-21 - Form Submit Loading State
**Learning:** Instantaneous form transitions, especially for actions labeled "secure" or "processing", can feel abrupt and untrustworthy to users. Simulating a brief network request provides reassurance that an action is actually taking place behind the scenes.
**Action:** When implementing forms that lack a natural network delay, artificially delay the success state slightly (e.g., 1-1.5s) while showing a clear "Processing..." or "Loading..." indicator on the disabled submit button.
