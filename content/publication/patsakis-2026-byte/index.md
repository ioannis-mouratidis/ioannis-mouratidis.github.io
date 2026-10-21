---
title: 'Byte-exact, format-aware compression for FASTA, FASTQ, BED and VCF files'
corresponding_author: true
authors:
- Michail Patsakis
- Alexandros Margaris
- Theodore Chronopoulos
- Ioannis Mouratidis
- Ilias Georgakopoulos-Soares
date: '2026-03-17'
publishDate: '2026-10-20T00:00:00Z'
publication_types:
- article-journal
publication: '*bioRxiv*'
hugoblox:
  ids:
    doi: 10.64898/2026.03.16.712193
abstract: 'Motivation: Most omics data is stored by compressors that treat it as an unstructured byte stream. Format-aware compressors close that gap but are fragmented across formats and often expect a training pass over the user''s own file. A general-purpose lossless compressor that is applicable to the most storage-intense omics data formats while beating the general codecs on ratio and speed would offer significant savings for large omics datasets storage and data retrieval. Results: We present NYX, a compressor for FASTA, FASTQ, BED and VCF files. It leverages a reversible, format-specific transform optimised for the OpenZL compression algorithm to reach compression ratios up to 2.3 times those of the strongest general-purpose codecs (zstd -19, xz -9e and 7-Zip) while compressing up to two orders of magnitude faster. On the 1000 Genomes VCF dataset NYX reaches a compression ratio of 468.67x, 2.0 times that of xz -9e while compressing 1.8 times faster. On mammalian FASTA assemblies totalling 9.3 GB, NYX is within 3-4% of NAF, the strongest purpose-built FASTA codec, while compressing 57-73 times faster. Across all 54 inputs no single codec beats NYX on ratio and compression speed together: the tools that achieve higher compression are 1.2 to 73 times slower. NYX provides fully lossless, fast and efficient compression under one easy-to-use tool for the most common omics data types. Availability and implementation: https://github.com/Georgakopoulos-Soares-lab/compression'
---
