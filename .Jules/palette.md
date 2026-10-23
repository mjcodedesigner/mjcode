
## 2024-05-19 - Sticky Header Scroll Offset
**Learning:** When using sticky headers (like this site's `sticky top-0 z-40`), anchor links naturally scroll until the target element hits the top of the viewport. This results in the sticky header obscuring the target element. Combining this with Tailwind's `scroll-smooth` makes the issue very visually apparent.
**Action:** When implementing sticky headers and in-page anchor links, always apply a scroll-padding utility (e.g., `scroll-pt-28`) to the `<html>` or scrolling container element to provide an offset equal to the sticky header's height.

## 2024-10-21 - Form Submit Loading State
**Learning:** Instantaneous form transitions, especially for actions labeled "secure" or "processing", can feel abrupt and untrustworthy to users. Simulating a brief network request provides reassurance that an action is actually taking place behind the scenes.
**Action:** When implementing forms that lack a natural network delay, artificially delay the success state slightly (e.g., 1-1.5s) while showing a clear "Processing..." or "Loading..." indicator on the disabled submit button.

## 2024-11-28 - Multi-Step Wizard Focus Management
**Learning:** When navigating between sections in a multi-step form (like a wizard) that replaces content dynamically without a page reload, screen readers and keyboard users lose context unless focus is explicitly managed.
**Action:** When creating or modifying client-side multi-step forms, always programmatically shift focus to the heading of the newly revealed step, ensuring the heading has `tabindex="-1"` and `focus:outline-none` so it can receive focus without displaying a confusing visual outline.
