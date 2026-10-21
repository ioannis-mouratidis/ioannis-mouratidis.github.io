---
title: 'Safeguarding open-weight genomic foundation models through weight locking'
featured: true
corresponding_author: true
authors:
- Aris Karatzikos
- Aggeliki Vasilopoulou
- Candace S Y Chan
- Ioannis Mouratidis
- Ilias Georgakopoulos-Soares
date: '2026-07-10'
publishDate: '2026-10-20T00:00:00Z'
publication_types:
- article-journal
publication: '*bioRxiv*'
hugoblox:
  ids:
    doi: 10.64898/2026.07.07.736795
abstract: 'Background: Genomic foundation models can dramatically accelerate biological research by learning general-purpose representations of genomic data that transfer across tasks, enabling researchers to predict variant effects, regulatory elements, and molecular function, among others. To safeguard against potential biosecurity threats and malicious misuse of open-weight models, a common strategy involves excluding human-infecting viral genomes from the models'' training corpora. This strategy, however, can be easily circumvented by fine-tuning models on abundantly available viral data. Weight-locking with spectral deformation has been proposed as a potential method to prevent fine-tuning of neural networks, but has not been systematically evaluated in biological AI models. Methods: We applied spectral deformation locking to the Evo-1-8k-base genomic foundation model and evaluated a panel of attack configurations spanning naive fine-tuning, low-rank adaptation (LoRA), a simple inserted-layer bypass baseline, and a white-box singular value decomposition (SVD)-chain factorisation at chain lengths k ∈ {2, 3, 5}. Recovered virological capability was quantified on three Human Virome Understanding Evaluation (HVUE) tasks. Results: The lock defended against the naive attacker by either standard pipeline. Naive full fine-tuning under the strong lock drove downstream virological capability significantly below the pretrained baseline on pathogenicity and host tropism, converting the attack into a capability loss rather than a gain, while naive low-rank adaptation neither moved held-out perplexity (PPL) nor recovered downstream capability above pretrained. Thus, we conclude that by neither route does the naive attacker reach the gain achieved by fine-tuning an unlocked model. Consistent with previous results in non-biological models, an informed attacker who implements the SVD-chain construction does recover capability on pathogenicity prediction, at the cost of increased computational requirements for the fine-tuning process. Availability: https://github.com/Georgakopoulos-Soares-lab/glm-locking.'
---
