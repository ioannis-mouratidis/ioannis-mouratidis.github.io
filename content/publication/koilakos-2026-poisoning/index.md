---
title: 'Poisoning the Genome: Targeted Backdoor Attacks on DNA Foundation Models'
featured: true
corresponding_author: true
authors:
- Charalampos Koilakos
- Ioannis Mouratidis
- Ilias Georgakopoulos-Soares
date: '2026-03-29'
publishDate: '2026-03-29T00:00:00Z'
publication_types:
- article-journal
publication: '*arXiv preprint arXiv:2603.27465*'
hugoblox:
  ids:
    doi: 10.48550/arXiv.2603.27465
abstract: 'Foundation models trained on DNA sequences have achieved strong performance across biological tasks including variant effect prediction and genome design. These models rely on massive public genomic datasets comprising trillions of nucleotide tokens. Unlike natural language, DNA sequences lack semantic transparency, making corrupted or adversarially crafted entries difficult to detect during data curation. We present the first systematic study of training data poisoning in genomic language models, targeting both pre-training and fine-tuning stages. At pre-training, using Evo 2 and GENERator architectures, we show that less than 1% adversarially crafted sequences in the training corpus can selectively degrade generative performance on targeted genomic contexts while leaving unrelated sequences unaffected. We evaluate three scenarios: corruption of TATA-box promoter motifs, disruption of CTCF binding sites, and insertion of synthetic sequences absent from all training genomes. At fine-tuning, we demonstrate two additional attacks. First, poisoning a subset of CTCF sites in a ClinVar-derived corpus installs a conditional backdoor in a LoRA-adapted model that activates almost exclusively when the trigger sequence is present. Second, using frozen Evo 2 7B embeddings, targeted label corruption of downstream training data selectively compromises a clinically relevant variant classification task, demonstrated on BRCA1 variant effect prediction. These results show genomic foundation models are susceptible to targeted data poisoning with minimal footprint. We urge the field to adopt data provenance tracking, integrity verification, and adversarial robustness evaluation as standard components of the genomic model development pipeline.'
---
