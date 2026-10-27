## 2026-10-27 - Programmatic Focus Management for Multi-Step Forms
**Learning:** When implementing or modifying dynamic multi-step client-side forms, screen readers and keyboard users lose context if focus isn't managed during transitions.
**Action:** Always programmatically shift focus to the heading of the newly revealed step (using tabindex="-1" and focus:outline-none) to maintain context.
