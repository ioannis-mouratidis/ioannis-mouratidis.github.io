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
    id: about-me
    content:
      title: 'About Me'
      subtitle: ''
      text: |-
        I'm a research engineer working on AI safety and alignment at Resolution, where I study how capabilities and values emerge during model training and help build scalable interventions to align frontier models.

        I came to alignment from the frontier of AIxBio. Through a PhD in bioinformatics and years leading computational genomics teams, I built deep expertise in biological foundation models and biosecurity—red-teaming agentic AI scientists, evaluating the dual-use capabilities and adversarial robustness of genomic language models, studying data-poisoning and backdoor attacks, and developing tamper-resistant weight-locking for open-weight biological AI. That domain grounding is what I now bring to general questions of AI safety.

        My path has run from mathematics to artificial intelligence to bioinformatics and back to AI safety, across four countries and many hats: from co-founding a cancer-diagnostics startup to building research infrastructure from scratch, and from publishing open-source bioinformatics tools to evaluating state-of-the-art systems like Evo 2. What drives my work is a conviction that as AI systems become increasingly capable, we need rigorous, empirical frameworks to evaluate and ensure their safety.

        I'm passionate about mentorship and collaborative science. I've had the privilege of guiding researchers from their first steps in the field to their first lead-author publications, and I thrive in environments that balance rigorous research with rapid iteration.

        When I'm not working, you'll find me running or learning a new language.
    design:
      columns: '1'
  - block: collection
    id: selected-publications
    content:
      title: Selected Publications
      text: '<div class="pub-legend" style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 0.5rem; margin-bottom: 1rem; font-size: 0.9rem;"><span><strong>*</strong> first or co-first author</span><span>✉ corresponding author (project supervision)</span></div><style>@media (min-width: 768px) { .pub-legend { flex-direction: row !important; gap: 1.5rem !important; }}</style>'
      count: 0
      filters:
        folders:
          - publication
        featured_only: true
    design:
      view: citation
      columns: 1
  - block: markdown
    id: all-publications-toggle
    content:
      text: |-
        <style>
          #all-publications { display: none; }
          #all-publications.pubs-expanded { display: block; }
          .show-all-pubs-wrap { text-align: center; margin: 0.5rem 0 0.5rem; }
          #show-all-pubs-btn { display: inline-flex; align-items: center; gap: 0.4em; padding: 0.55rem 1.4rem; font-size: 0.95rem; font-weight: 600; border: 1px solid currentColor; border-radius: 9999px; background: transparent; color: inherit; cursor: pointer; transition: opacity 0.15s ease; }
          #show-all-pubs-btn:hover { opacity: 0.65; }
          #all-pubs-note { display: none; text-align: center; font-size: 0.95rem; margin: 0.85rem auto 1rem; max-width: 42rem; }
          #all-pubs-note.pubs-expanded { display: block; }
        </style>
        <div class="show-all-pubs-wrap">
          <button id="show-all-pubs-btn" type="button" aria-expanded="false" aria-controls="all-publications">Show all publications</button>
        </div>
        <p id="all-pubs-note">For an up-to-date list of publications, also see <a href="https://scholar.google.com/citations?user=UowZjXsAAAAJ" target="_blank" rel="noopener">Google Scholar</a>.</p>
        <script>
        (function() {
          function init() {
            var btn = document.getElementById('show-all-pubs-btn');
            var sec = document.getElementById('all-publications');
            var note = document.getElementById('all-pubs-note');
            if (!btn || !sec) return;
            btn.addEventListener('click', function() {
              var expanded = sec.classList.toggle('pubs-expanded');
              if (note) { note.classList.toggle('pubs-expanded', expanded); }
              btn.setAttribute('aria-expanded', expanded ? 'true' : 'false');
              btn.textContent = expanded ? 'Hide all publications' : 'Show all publications';
            });
          }
          if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', init); } else { init(); }
        })();
        </script>
    design:
      columns: '1'
      spacing:
        padding: ['0', '0', '0', '0']
  - block: collection
    id: all-publications
    content:
      title: ''
      count: 0
      filters:
        folders:
          - publication
        exclude_featured: true
    design:
      view: citation
      columns: 1
      spacing:
        padding: ['0', '0', '0', '0']
  - block: markdown
    id: patents
    content:
      title: 'Patents'
      subtitle: ''
      text: |-
        1. Georgakopoulos-Soares, I., **Mouratidis, I.**, & Provatas, K. (2025). *System and Method for Extracting Neomers.* U.S. Provisional Patent.
        2. Ahituv, N., Yizhar-Barnea, O., Georgakopoulos-Soares, I., **Mouratidis, I.**, & Hemberg, M. (2023). *Systems for mutation caller and methods of using the same.* WO2024103003A3.
        3. Ahituv, N., Yizhar-Barnea, O., Georgakopoulos-Soares, I., **Mouratidis, I.**, & Hemberg, M. (2022). *Compositions comprising nullomers and methods of using the same for cancer detection and diagnosis.* WO2022235718A3.
    design:
      columns: '1'
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
        **Location:** Austin, Texas

        Reach me on [LinkedIn](https://www.linkedin.com/in/mouratidis-ioannis/). I'm always open to discussing AI safety and alignment research, including AIxBio safety.
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
            const pubSections = document.querySelectorAll('#selected-publications, #all-publications');
            if (!pubSections.length) return;
            const elements = [];
            pubSections.forEach(section => {
              section.querySelectorAll('span, p, div, .article-metadata, .pub-authors, .li-cite-author').forEach(el => elements.push(el));
            });
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
