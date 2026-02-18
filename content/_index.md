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
        I'm a computational biologist working at the intersection of AI and genomics, with a particular focus on understanding and ensuring the safety of foundation models in biology.

        My academic journey has taken me from mathematics to artificial intelligence, then to bioinformatics, and now back to AI with a focus on safety and foundation models in biology. Along the way, I've lived and worked in four different countries and worn many hats: from co-founding a cancer diagnostics startup to building research infrastructure from scratch, and from developing open-source bioinformatics tools to training genomic language models.

        What drives my work is a conviction that as AI systems become increasingly capable, we need robust frameworks to evaluate their safety. Whether I'm assessing data poisoning vulnerabilities in genomic models or benchmarking the capabilities of state-of-the-art systems like Evo 2, I'm focused on ensuring these powerful tools advance science responsibly.

        I'm passionate about mentorship and collaborative science. I've had the privilege of guiding researchers from their first steps in bioinformatics to their first publications, and I thrive in environments that balance rigorous research with the rapid iteration of startup culture.

        When I'm not analyzing petabytes of genomic data, you'll find me jogging in Austin or learning new languages.
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
