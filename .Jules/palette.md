## 2026-10-24 - Dynamic Form Focus Management
**Learning:** When implementing or modifying dynamic multi-step client-side forms, newly revealed steps must have their focus programmatically shifted to the heading of the new step (using `tabindex="-1"` and `focus:outline-none`). Without this, screen readers and keyboard users lose their context within the form when the DOM updates asynchronously.
**Action:** Always ensure any client-side step transition in forms includes a `.focus()` call to the new section's heading or container to maintain accessible navigation.
