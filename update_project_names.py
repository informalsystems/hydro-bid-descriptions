#!/usr/bin/env python3
import os
import re
import yaml
from pathlib import Path

# Read the mapping from the file
project_names = {}
with open('project_names_mapping.txt', 'r') as f:
    for line in f:
        if line.strip():
            bid_id, project_name = line.strip().split(' ', 1)
            project_names[bid_id] = project_name if project_name != 'null' else None

def update_bid_file(file_path, bid_id, expected_project_name):
    """Update a bid file with the correct projectName property"""
    with open(file_path, 'r') as f:
        content = f.read()

    # Extract frontmatter
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not frontmatter_match:
        print(f"Warning: No frontmatter found in {file_path}")
        return False

    frontmatter_text = frontmatter_match.group(1)

    # Parse frontmatter
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as e:
        print(f"Warning: Invalid YAML in frontmatter for {file_path}: {e}")
        return False

    current_project_name = frontmatter.get('projectName')

    # Check if update is needed
    if expected_project_name is None:
        # Should not have projectName
        if 'projectName' in frontmatter:
            print(f"Removing projectName from {file_path}")
            del frontmatter['projectName']
            needs_update = True
        else:
            print(f"✓ {file_path} correctly has no projectName")
            return True
    else:
        # Should have projectName
        if current_project_name != expected_project_name:
            print(f"Updating projectName in {file_path}: '{current_project_name}' -> '{expected_project_name}'")
            frontmatter['projectName'] = expected_project_name
            needs_update = True
        else:
            print(f"✓ {file_path} already has correct projectName: '{expected_project_name}'")
            return True

    if needs_update:
        # Reconstruct frontmatter
        new_frontmatter = yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)

        # Replace the frontmatter in the content
        new_content = re.sub(r'^---\n.*?\n---\n', f'---\n{new_frontmatter}---\n', content, flags=re.DOTALL)

        # Write back to file
        with open(file_path, 'w') as f:
            f.write(new_content)

        return True

    return False

def main():
    bids_dir = Path('bids')
    updated_count = 0

    for file_path in bids_dir.glob('*.md'):
        # Extract bid ID from filename
        filename = file_path.name
        match = re.match(r'(\d+)--', filename)
        if not match:
            print(f"Warning: Could not extract bid ID from {filename}")
            continue

        bid_id = match.group(1)
        expected_project_name = project_names.get(bid_id)

        if expected_project_name is None:
            print(f"Warning: No project name mapping found for bid {bid_id}")
            continue

        if update_bid_file(file_path, bid_id, expected_project_name):
            updated_count += 1

    print(f"\nUpdated {updated_count} files")

if __name__ == '__main__':
    main()
