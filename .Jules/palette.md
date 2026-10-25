## 2026-10-25 - Dynamic Form Focus Management
**Learning:** When navigating between sections in a multi-step single page form, screen reader and keyboard users lose their contextual place on the page unless focus is explicitly managed.
**Action:** Always programmatically shift focus to the heading of the newly revealed step using `tabindex="-1"` and a focus outline zeroing class (e.g. `focus:outline-none`).
