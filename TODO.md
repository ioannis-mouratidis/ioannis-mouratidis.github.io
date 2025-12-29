# TODO

## Future Tasks

### Add Projects Section
- **Status:** Temporarily hidden from navigation
- **Location:** Commented out in `config/_default/menus.yaml` (lines 16-19)
- **Next steps:**
  - Create projects content in appropriate directory
  - Add project entries with descriptions, links, and relevant details
  - Uncomment the Projects menu item once content is ready

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
