# TODO

## Future Tasks

### Fix Publications Section
- **Status:** Temporarily removed from homepage
- **Issue:** Publications section not working properly
- **Location:** Previously displayed in `content/_index.md` (lines 52-72)
- **Sections removed:**
  - Featured Publications (article-grid view)
  - Recent Publications (citation view)
- **Files affected:**
  - `content/_index.md` - Removed two collection blocks
  - Publications content still exists in `content/publications/` directory
- **Next steps:**
  - Investigate what's causing the publications section to malfunction
  - Test individual publication pages at `/publications/[slug]/`
  - Test publications archive page at `/publications/`
  - Fix and re-enable the homepage sections once issue is resolved
