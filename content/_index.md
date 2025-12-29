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
        interests: ''
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
    content:
      title: 'Research Focus'
      subtitle: ''
      text: |-
        My research leverages machine learning and computational methods to advance genomic data analysis and cancer detection. I specialize in developing novel algorithms for k-mer based genomic analysis, training and evaluating genomic foundation models, and creating compression tools for large-scale genomic data.

        Key areas include: AI evals for genomic models, adversarial robustness in biological data, ML pipelines for liquid biopsy-based cancer detection, and analysis of non-B DNA structures. I've developed several widely-used bioinformatics tools including kmerDB (a comprehensive genomic/proteomic sequence database) and Zseeker (Z-DNA detection tool).

        I'm always interested in collaborative research opportunities in computational genomics and AI applications in biology.
    design:
      columns: '1'
  - block: collection
    id: papers
    content:
      title: Featured Publications
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: article-grid
      columns: 2
  - block: collection
    content:
      title: Recent Publications
      text: ''
      filters:
        folders:
          - publications
        exclude_featured: false
    design:
      view: citation
  - block: collection
    id: talks
    content:
      title: Recent & Upcoming Talks
      filters:
        folders:
          - talks
        exclude_featured: false
    design:
      view: compact
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
---
