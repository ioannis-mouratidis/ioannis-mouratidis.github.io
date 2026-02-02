# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Hugo-based academic website using the Hugo Blox Builder framework (formerly Academic/Wowchemy). The site showcases research publications, projects, talks, and professional experience.

**Live Site**: https://ioannis-mouratidis.github.io
**Theme**: Hugo Blox Builder Academic CV Template
**Hugo Version**: Extended v0.153.4+

## Commands

### Development
```bash
# Start development server
npm run dev
# or
hugo server --disableFastRender

# Build for production
npm run build
# or
hugo --minify

# View site locally at http://localhost:1313
```

### Content Creation
```bash
# Add a new publication
hugo new content/publications/paper-name-2025/index.md

# Add a new project
hugo new content/projects/project-name/index.md

# Add a new talk
hugo new content/talks/event-name-2025/index.md

# Import publications from BibTeX
pip install academic
academic import --bibtex publications.bib
```

### Module Management
```bash
# Update Hugo modules (theme updates)
hugo mod get -u
hugo mod tidy

# Clean build cache
hugo mod clean
```

## Architecture

### Hugo Blox Builder Module System

The theme uses Hugo's module system with three main components:

1. **blox-tailwind** (v0.0.0-20251229000224-c48b65edb2ae): Core UI components, Tailwind CSS v4 integration, block system
2. **blox-plugin-netlify** (v0.0.0-20251215001347-c72b26de8d15): Security headers, deployment configuration
3. **blox-plugin-reveal** (v0.0.0-20251214235550-d15979197a2a): Presentation/slides framework

Modules are declared in `go.mod` and imported via `config/_default/module.yaml`.

### Configuration Architecture

Configuration is split across multiple files in `config/_default/`:

- **hugo.yaml**: Core Hugo settings (baseURL, build options, image processing, output formats)
- **params.yaml**: HugoBlox-specific parameters (theme, typography, SEO, analytics, etc.)
- **menus.yaml**: Navigation menu structure
- **module.yaml**: Theme module imports and mount points
- **languages.yaml**: i18n configuration

**Important**: Changes to `params.yaml` affect site-wide appearance (colors, fonts, spacing), while `hugo.yaml` affects build behavior.

### Landing Page Block System

The homepage (`content/_index.md`) uses `type: landing` with a section-based layout. Each section is a "block" component:

```yaml
sections:
  - block: resume-biography-3    # Hero/about section with gradient mesh
  - block: markdown              # Custom rich text
  - block: collection            # Dynamic content filtering
    id: papers                   # Anchor for navigation
    content:
      filters:
        folders: [publications]
        featured_only: true      # Only show featured items
    design:
      view: article-grid         # Layout: article-grid, citation, card, compact
```

**Key Block Types**:
- `resume-biography-3`: Biography with avatar, social links, education, interests
- `collection`: Query and display content (publications/talks/projects) with filters
- `markdown`: Static markdown content blocks

**Available Views for Collection Block**:
- `article-grid`: Card grid for featured publications
- `citation`: Academic citation format (APA/MLA/Chicago/IEEE)
- `card`: General card layout
- `compact`: Dense list view

### Content Structure

All content uses Markdown with YAML front matter. **Critical**: Each content type folder must have an `_index.md` file.

**Publications** (`content/publications/[slug]/index.md`):
```yaml
title: "Paper Title"
authors: ["Author 1", "Author 2", "me"]  # "me" references content/authors/me/
publication: "*Journal Name, Volume(Issue)*"
publication_types: ["article-journal"]   # Options: article-journal, conference-paper, preprint
date: "2025-01-01T00:00:00Z"            # ISO 8601 format
featured: true                           # Shows in Featured Publications section
tags: [Machine Learning, Genomics]
links:
  - type: source
    url: "https://doi.org/..."
```

**Projects** (`content/projects/[slug]/index.md`):
```yaml
title: "Project Name"
summary: "Brief description for cards"
tags: [tag1, tag2]
external_link: "http://example.com"     # External projects (omit for internal pages)
links:
  - name: Website
    url: "http://..."
  - name: Code
    url: "https://github.com/..."
```

**Talks** (`content/talks/[slug]/index.md`):
```yaml
title: "Talk Title"
event: "Conference Name"
location: "City, Country"
date: '2025-02-01T00:00:00Z'
all_day: true                            # Hides time, shows date only
authors: [me]
featured: false
```

**Author Profile** - **IMPORTANT: Three files must be kept in sync**:

1. **`data/authors/me.yaml`** (Homepage bio blurb)
   - Contains `bio` field displayed on the main homepage biography block
   - **Must be updated when publication counts or bio summary changes**

2. **`config/_default/params.yaml`** (Site-wide SEO description)
   - Contains site meta description under `hugoblox.identity.description`
   - Used for SEO, social sharing, and browser previews
   - **Must be updated when publication counts or bio summary changes**

3. **`content/authors/me/_index.md`** (Author profile page)
   - Creates standalone author profile page at `/authors/me/`
   - Contains "About Me" section in markdown below front matter
   - **Must be updated when publication counts or bio changes**

**Workflow**: When updating bio/publication counts, update ALL THREE files: `data/authors/me.yaml` (bio), `params.yaml` (identity.description), and `content/authors/me/_index.md` (About Me section)

### Date Formatting

**Current Configuration**: `date_format: "Jan 2006"` (Month Year format, no day)

Dates are configured in `config/_default/params.yaml` under `hugoblox.locale`. The format uses Go's time layout syntax:
- `"Jan 2006"` = "Feb 2025"
- `"Jan 2, 2006"` = "Feb 15, 2025"
- `"2006"` = "2025"

This affects all date displays except citation views (which always show year only).

## Deployment

### GitHub Pages (Current Setup)

Automated deployment via `.github/workflows/hugo.yml`:

1. Triggers on push to `main` or `master` branch
2. Installs Hugo Extended v0.153.4, Dart Sass, Node.js v22
3. Builds with `hugo --gc --minify`
4. Deploys to GitHub Pages automatically

**Repository**: `ioannis-mouratidis.github.io`
**Branch for deployment**: `gh-pages` (auto-created by Actions)

### Netlify (Alternative)

Configuration in `netlify.toml`. Key settings:
- Build command includes `npm install` + `hugo --gc --minify`
- Uses `netlify-plugin-hugo-cache-resources` for caching
- Pagefind for site search indexing
- Environment: Hugo 0.153.4, Go 1.21.5, Node 22

## Common Workflows

### Adding Publications

**Method 1 - Google Scholar Import** (Recommended):
```bash
pip install academic
academic import --bibtex publications.bib
```
Creates folder structure automatically with front matter populated from BibTeX.

**Method 2 - Manual**:
1. `hugo new content/publications/paper-slug-2025/index.md`
2. Edit front matter (title, authors, publication, date, featured, tags)
3. Add abstract and summary
4. Optionally add image (`featured.jpg` in same folder)

**Method 3 - ORCID**: Configure ORCID ID in `config/_default/params.yaml`

**Important**: To show on homepage, set `featured: true`. The homepage has TWO publication sections:
- "Featured Publications" (article-grid view, featured_only: true)
- "Recent Publications" (citation view, all publications)

### Updating Navigation Menu

Edit `config/_default/menus.yaml`:

```yaml
main:
  - name: Papers
    url: /#papers          # Hash links to sections on homepage
    weight: 11             # Lower weight = appears first
```

Weight determines order. Current menu: Bio (10), Papers (11), Talks (12), Experience (20), Projects (30).

### Theming and Appearance

All visual customization in `config/_default/params.yaml` under `hugoblox`:

```yaml
theme:
  mode: system               # light | dark | system (follows OS)
  pack: "default"           # Theme pack from data/themes/
  colors:
    primary: ""             # Tailwind color name or hex
```

```yaml
typography:
  font: "sans"              # sans (Inter) | serif (Roboto Slab) | native
  size: "md"                # sm | md | lg | xl
```

```yaml
layout:
  radius: "md"              # Border radius: none | sm | md | lg | full
  spacing: "comfortable"    # compact | comfortable | spacious
```

### Updating Resume/CV PDF

Place PDF at: `static/uploads/resume.pdf`

This is referenced in the biography block's download button:
```yaml
button:
  text: Download CV
  url: uploads/resume.pdf
```

## Important Notes

### Hugo Extended Required

This site **requires Hugo Extended** (not the standard version) due to:
- Tailwind CSS processing via Hugo Pipes
- Dart Sass compilation
- Advanced image processing

Install from: https://gohugo.io/installation/

### Module Updates

When updating Hugo Blox modules:

```bash
hugo mod get -u github.com/HugoBlox/hugo-blox-builder/modules/blox-tailwind@latest
hugo mod tidy
```

The `go.mod` file pins specific commit hashes for reproducible builds. Update with care.

### Content Folder Requirements

Each content type folder MUST have an `_index.md` file:
- `content/publications/_index.md`
- `content/projects/_index.md`
- `content/talks/_index.md`

Without this, Hugo won't generate list pages or properly index content.

### Image Processing

Images in content folders (e.g., `featured.jpg`) are processed by Hugo's image pipeline:
- Automatic resizing for responsive layouts
- WebP conversion for performance
- Processed images cached in `resources/_gen/images/`

To add images to publications/projects, place them in the same folder as `index.md`.

### Analytics and SEO

Configured in `config/_default/params.yaml`:

```yaml
analytics:
  google:
    measurement_id: "G-XXXXXXXXXX"  # Google Analytics 4
```

```yaml
verification:
  google: ""                         # Google Search Console
```

### Security Headers

Security headers (CSP, frame-options) require the `blox-plugin-netlify` module and are configured in `params.yaml`:

```yaml
security:
  frame_options: sameorigin          # Allows embedding slides
```

## File Paths Reference

Critical files that Claude Code may need to modify:

- **Navigation**: `config/_default/menus.yaml`
- **Site Config**: `config/_default/hugo.yaml`
- **Appearance/Theme**: `config/_default/params.yaml`
- **Homepage Layout**: `content/_index.md`
- **Personal Info (Primary)**: `data/authors/me.yaml`
- **Personal Info (Page)**: `content/authors/me/_index.md`
- **Module Dependencies**: `go.mod`
- **Build Scripts**: `package.json`
- **GitHub Actions**: `.github/workflows/hugo.yml`
- **Netlify Config**: `netlify.toml`
- **Custom Block Overrides**: `layouts/_partials/hbx/blocks/*/block.html`
