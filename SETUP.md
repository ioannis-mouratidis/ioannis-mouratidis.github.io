# Ioannis Mouratidis - Academic Personal Website

Built with [HugoBlox Academic CV Template](https://github.com/HugoBlox/theme-academic-cv)

## About

Professional academic website for Ioannis Mouratidis, Machine Learning & Genomics Researcher at the University of Texas at Austin.

## Website Features

- ✅ **Auto-updating publications** from Google Scholar
- ✅ **Mobile-responsive** design optimized for all devices
- ✅ **Fast performance** (100/100 Lighthouse scores)
- ✅ **Sections**: About, Publications, Research, Projects/Tools, CV, Contact
- ✅ **GitHub Pages** deployment with automated CI/CD

## Local Development

### Prerequisites

- Hugo Extended v0.119.0 or later ([installation guide](https://gohugo.io/installation/))
- Node.js v20+ and npm ([installation guide](https://nodejs.org/))
- Git
- Go 1.19+ (required for Hugo modules) ([installation guide](https://go.dev/dl/))

**Note**: Hugo Extended is required (not standard Hugo) for Tailwind CSS processing and advanced image handling.

### Running Locally

1. Clone the repository:
```bash
git clone https://github.com/YOUR-USERNAME/academic-website.git
cd academic-website
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
# or
hugo server --disableFastRender
```

4. Open your browser to [http://localhost:1313](http://localhost:1313)

The development server will automatically reload when you make changes to files.

### Common Issues

**"Go not found in PATH" error:**
- Install Go from https://go.dev/dl/ and ensure it's in your system PATH
- Hugo requires Go for module management

**Tailwind CSS build errors:**
- Ensure your project path contains no spaces
- If path has spaces, rename the directory (e.g., "Personal website" → "Personal-website")

**Port 1313 already in use:**
```bash
hugo server -p 1314  # Use a different port
```

## Updating Content

### Personal Information

**IMPORTANT**: This site uses two author profile files that must be kept in sync:

1. **Primary**: Edit [`data/authors/me.yaml`](data/authors/me.yaml) first
   - Used by homepage biography and all profile widgets

2. **Secondary**: Update [`content/authors/me/_index.md`](content/authors/me/_index.md) to match
   - Creates the `/authors/me/` author profile page

Always edit `me.yaml` first, then sync changes to `_index.md`.

### Publications

Three options for managing publications:

**Option 1: Automatic Import from Google Scholar (Recommended)**
```bash
pip install academic
academic import --bibtex <path/to/publications.bib>
```

**Option 2: Manual Entry**
```bash
hugo new content/publications/my-paper-2025/index.md
```

**Option 3: ORCID Integration**
Configure in [`config/_default/params.yaml`](config/_default/params.yaml)

### Projects
```bash
hugo new content/projects/my-project/index.md
```

### CV
Update PDF: [`static/uploads/resume.pdf`](static/uploads/resume.pdf)

## Deployment to GitHub Pages

### Initial Setup

1. Create a GitHub repository named `YOUR-USERNAME.github.io`

2. Push your site:
```bash
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git add .
git commit -m "Initial commit: Academic website"
git push -u origin main
```

3. Enable GitHub Pages:
   - Repository Settings > Pages
   - Select "GitHub Actions" as the source

4. Update `baseURL` in [`config/_default/hugo.yaml`](config/_default/hugo.yaml):
```yaml
baseURL: 'https://YOUR-USERNAME.github.io/'
```

### Automatic Deployment

Every push to `main` triggers automatic deployment via GitHub Actions.

## Resources

- [HugoBlox Documentation](https://docs.hugoblox.com/)
- [Hugo Documentation](https://gohugo.io/documentation/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Academic Import Tool](https://github.com/GetRD/academic-file-converter)

## Contact

**Ioannis Mouratidis**
- Email: ioannis.mouratidis [at] austin.utexas.edu
- LinkedIn: [https://www.linkedin.com/in/mouratidis-ioannis/](https://www.linkedin.com/in/mouratidis-ioannis/)
- Google Scholar: [https://scholar.google.com/citations?user=UowZjXsAAAAJ](https://scholar.google.com/citations?user=UowZjXsAAAAJ)

---

Built with [HugoBlox](https://hugoblox.com) | MIT License
