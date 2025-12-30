#!/usr/bin/env python3
"""
Extract DOIs from bibliography and add them to publication markdown files.
"""

import re
import os
import yaml
from pathlib import Path

# Read the bibliography file
with open('IM bibliography.txt', 'r', encoding='utf-8') as f:
    bib_content = f.read()

# Extract publications with DOIs
publications = []
for line in bib_content.strip().split('\n'):
    # Match DOI pattern
    doi_match = re.search(r'https://doi\.org/([\w\.\-/]+)', line)
    if doi_match:
        doi = doi_match.group(1)

        # Extract author names - look for patterns like "Mouratidis, I." or "Georgakopoulos-Soares, I."
        # Get the first author's last name to help match
        author_match = re.search(r'^\d+\.\s+([^,]+),', line)
        if author_match:
            first_author = author_match.group(1).strip()

            # Extract year
            year_match = re.search(r'\((\d{4})\)', line)
            year = year_match.group(1) if year_match else ''

            publications.append({
                'first_author': first_author,
                'year': year,
                'doi': doi,
                'full_line': line
            })

print(f"Found {len(publications)} publications with DOIs\n")

# Now update each publication folder
content_dir = Path('content/publication')
updated_count = 0
not_found = []

for pub in publications:
    # Try to find matching folder
    # Common patterns: firstname-year-keyword, lastname-year-keyword
    first_author_lower = pub['first_author'].lower().replace(' ', '-').replace('.', '')
    year = pub['year']

    # Find folders that might match
    possible_folders = list(content_dir.glob(f"*{year}*"))

    matched_folder = None
    for folder in possible_folders:
        folder_name = folder.name.lower()
        # Check if first author name is in folder name
        if first_author_lower.split('-')[0] in folder_name:
            matched_folder = folder
            break

    if matched_folder:
        index_file = matched_folder / 'index.md'
        if index_file.exists():
            # Read the markdown file
            with open(index_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Parse front matter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    front_matter = parts[1]
                    body = parts[2] if len(parts) > 2 else ''

                    # Parse YAML
                    data = yaml.safe_load(front_matter)

                    # Add DOI if not already present
                    if 'doi' not in data or not data['doi']:
                        data['doi'] = pub['doi']

                        # Write back
                        with open(index_file, 'w', encoding='utf-8') as f:
                            f.write('---\n')
                            f.write(yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False))
                            f.write('---')
                            f.write(body)

                        print(f"[OK] Updated {matched_folder.name} with DOI: {pub['doi']}")
                        updated_count += 1
                    else:
                        print(f"  Skipped {matched_folder.name} (already has DOI)")
    else:
        not_found.append(f"{pub['first_author']} ({pub['year']})")

print(f"\n\nSummary:")
print(f"  Updated: {updated_count}")
print(f"  Not found: {len(not_found)}")

if not_found:
    print(f"\nPublications not matched to folders:")
    for item in not_found:
        print(f"  - {item}")
