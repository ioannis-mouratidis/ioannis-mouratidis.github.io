---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: '6rem'

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: me
      text: ''
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf
      headings:
        about: ''
        education: ''
        interests: 'Interests'
    design:
      # Use the new Gradient Mesh which automatically adapts to the selected theme colors
      background:
        gradient_mesh:
          enable: true

      # Name heading sizing to accommodate long or short names
      name:
        size: md # Options: xs, sm, md, lg (default), xl

      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
  - block: markdown
    id: research-focus
    content:
      title: 'Research Focus'
      subtitle: ''
      text: |-
        My research leverages machine learning and computational methods to advance genomic data analysis and cancer detection. I specialize in developing novel algorithms for k-mer based genomic analysis, ML for large-scale biological data analysis, and training and evaluating genomic foundation models.

        Key areas include: AI evals for genomic models, adversarial robustness in biological data, ML pipelines for liquid biopsy-based cancer detection, and analysis of non-B DNA structures. I've developed several open-source bioinformatics tools including kmerDB (a comprehensive genomic/proteomic sequence database) and Zseeker (Z-DNA detection tool).

        I'm always interested in collaborative research opportunities in computational genomics and AI applications in biology.
    design:
      columns: '1'
  - block: collection
    id: publications
    content:
      title: Publications
      text: '<div class="pub-legend" style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 0.5rem; margin-bottom: 1rem; font-size: 0.9rem;"><span><strong>*</strong> first or co-first author</span><span>✉ corresponding author (project supervision)</span></div><style>@media (min-width: 768px) { .pub-legend { flex-direction: row !important; gap: 1.5rem !important; }}</style>'
      filters:
        folders:
          - publication
        featured_only: false
    design:
      view: citation
      columns: 1
  - block: collection
    id: talks
    content:
      title: Presentations
      filters:
        folders:
          - talks
        exclude_featured: false
    design:
      view: card
      columns: 2
  - block: markdown
    id: contact
    content:
      title: 'Contact'
      subtitle: ''
      text: |-
        **Email:** ioannis.mouratidis [at] austin.utexas.edu

        **Location:** Austin, Texas

        I'm always open to discussing research collaborations, consulting opportunities, or mentoring in bioinformatics and machine learning.
    design:
      columns: '1'
  - block: markdown
    content:
      text: |-
        <script>
        (function() {
          'use strict';
          const myNames = [
            'Ioannis Mouratidis',
            'ioannis mouratidis',
            'I. Mouratidis',
            'I Mouratidis',
            'Mouratidis, I.',
            'Mouratidis, Ioannis',
            'Mouratidis I'
          ];
          function boldMyName() {
            const pubSection = document.querySelector('#publications');
            if (!pubSection) return;
            const elements = pubSection.querySelectorAll('span, p, div, .article-metadata, .pub-authors, .li-cite-author');
            elements.forEach(element => {
              const text = element.textContent.trim();
              if (!text || element.querySelector('strong.author-self')) return;
              let html = element.innerHTML;
              let modified = false;
              myNames.forEach(name => {
                const escapedName = name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
                const regex = new RegExp(`(^|[^>a-zA-Z])(${escapedName})([^<a-zA-Z]|$)`, 'gi');
                const newHtml = html.replace(regex, (match, before, nameMatch, after) => {
                  if (match.includes('<strong')) return match;
                  modified = true;
                  return `${before}<strong class="author-self">${nameMatch}</strong>${after}`;
                });
                if (newHtml !== html) html = newHtml;
              });
              if (modified) element.innerHTML = html;
            });
          }
          if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', boldMyName);
          } else {
            boldMyName();
          }
          setTimeout(boldMyName, 500);
          setTimeout(boldMyName, 1500);
        })();
        </script>
    design:
      columns: '1'
      spacing:
        padding: ['0', '0', '0', '0']
---
