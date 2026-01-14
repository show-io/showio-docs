#!/usr/bin/env python3
"""
Auto-generate navigation tree for mkdocs.yml based on docs/osc_api folder structure.
Extracts titles from the first line of each markdown file.
"""

import os
import re
from pathlib import Path


def get_title_from_markdown(file_path):
    """Extract the title from the first line of a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            # Strip markdown header characters (# or ##, etc.)
            if first_line.startswith('#'):
                title = first_line.lstrip('#').strip()
                return title
            return first_line
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return os.path.basename(file_path).replace('.md', '').replace('_', ' ').title()


def parse_links_from_overview(overview_path):
    """Parse markdown links from an overview.md file and return ordered list of filenames."""
    try:
        with open(overview_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all markdown links in format [text](filename.md)
        # Pattern matches [any text](filename.md)
        pattern = r'\[([^\]]+)\]\(([^\)]+\.md)\)'
        matches = re.findall(pattern, content)

        # Return list of filenames (without paths, just the filename)
        return [os.path.basename(link[1]) for link in matches]
    except Exception as e:
        print(f"Error parsing links from {overview_path}: {e}")
        return []


def build_nav_tree_yaml(base_path, indent=4):
    """Build navigation tree from the folder structure and return as YAML string."""
    base_path = Path(base_path)

    if not base_path.exists():
        raise FileNotFoundError(f"Path {base_path} does not exist")

    def format_yaml_item(title, path, indent_level):
        """Format a single navigation item as YAML."""
        indent_str = ' ' * indent_level
        return f'{indent_str}- {title}: {path}'

    def format_yaml_section(title, items, indent_level):
        """Format a navigation section with sub-items as YAML."""
        indent_str = ' ' * indent_level
        child_indent = ' ' * (indent_level + 2)

        lines = [f'{indent_str}- {title}:']
        for item in items:
            lines.append(item)

        return '\n'.join(lines)

    def process_directory(dir_path, rel_base, indent_level, skip_root=False):
        """Recursively process a directory and build YAML nav structure."""
        lines = []

        # Get all files and directories
        entries = sorted(dir_path.iterdir())

        # Separate directories and files
        directories = [e for e in entries if e.is_dir()]
        files = [e for e in entries if e.is_file() and e.suffix == '.md']

        # Check if there's an overview.md to determine ordering
        overview_path = dir_path / 'overview.md'
        if overview_path.exists():
            # Get ordered list of filenames from overview.md
            ordered_filenames = parse_links_from_overview(overview_path)

            # Create a dict of files by name for quick lookup
            files_dict = {f.name: f for f in files}

            # Process files in the order specified in overview.md
            processed_files = set()
            for filename in ordered_filenames:
                if filename in files_dict and filename != 'overview.md':
                    file_path = files_dict[filename]
                    # Skip osc_api.md at the root level if it was already processed
                    if skip_root and file_path.name == 'osc_api.md':
                        continue

                    title = get_title_from_markdown(file_path)
                    rel_path = file_path.relative_to(rel_base)
                    lines.append(format_yaml_item(title, str(rel_path), indent_level))
                    processed_files.add(filename)

            # Process any remaining files not listed in overview.md (in sorted order)
            for file_path in sorted(files, key=lambda f: f.name):
                if file_path.name not in processed_files and file_path.name != 'overview.md':
                    # Skip osc_api.md at the root level if it was already processed
                    if skip_root and file_path.name == 'osc_api.md':
                        continue

                    title = get_title_from_markdown(file_path)
                    rel_path = file_path.relative_to(rel_base)
                    lines.append(format_yaml_item(title, str(rel_path), indent_level))
        else:
            # No overview.md, process files in sorted order
            for file_path in files:
                if file_path.name == 'overview.md':
                    continue
                # Skip osc_api.md at the root level if it was already processed
                if skip_root and file_path.name == 'osc_api.md':
                    continue

                title = get_title_from_markdown(file_path)
                rel_path = file_path.relative_to(rel_base)
                lines.append(format_yaml_item(title, str(rel_path), indent_level))

        # Process subdirectories
        for dir_path_item in directories:
            # Check if there's an overview.md in this directory
            overview_path = dir_path_item / 'overview.md'

            # Recursively get items in this directory
            sub_items = process_directory(dir_path_item, rel_base, indent_level + 2, skip_root=False)

            if overview_path.exists():
                # If overview exists, use it as the index page for this section
                section_title = get_title_from_markdown(overview_path)
                rel_path = overview_path.relative_to(rel_base)

                if sub_items:
                    # Section with overview and sub-items
                    indent_str = ' ' * indent_level
                    lines.append(f'{indent_str}- {section_title}:')
                    lines.append(format_yaml_item('Overview', str(rel_path), indent_level + 2))
                    lines.extend(sub_items)
                else:
                    # Just the overview page
                    lines.append(format_yaml_item(section_title, str(rel_path), indent_level))
            else:
                # No overview, just use folder name
                if sub_items:
                    folder_name = dir_path_item.name.replace('_', ' ').title()
                    indent_str = ' ' * indent_level
                    lines.append(f'{indent_str}- {folder_name}:')
                    lines.extend(sub_items)

        return lines

    # Start building the YAML
    yaml_lines = []

    # Process the directory
    yaml_lines.extend(process_directory(base_path, base_path.parent, indent, skip_root=True))

    return '\n'.join(yaml_lines)


def update_mkdocs_nav(mkdocs_path, osc_api_path):
    """Update the mkdocs.yml file with the generated navigation tree."""

    # Read the current mkdocs.yml
    with open(mkdocs_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find the ShowIO API section
    showio_start = None
    showio_indent = None
    next_section_start = None

    for i, line in enumerate(lines):
        if 'ShowIO API:' in line and line.strip().startswith('- '):
            showio_start = i
            showio_indent = len(line) - len(line.lstrip())
        elif showio_start is not None and line.strip():
            # Check if we've hit the next top-level section
            current_indent = len(line) - len(line.lstrip())
            if line.strip().startswith('- ') and current_indent == showio_indent:
                next_section_start = i
                break
            elif line.strip().startswith('#') or not line[0].isspace():
                # Hit a comment or non-indented line (next section)
                next_section_start = i
                break

    if showio_start is None:
        print("Could not find 'ShowIO API' section in mkdocs.yml")
        return

    # Generate the new navigation tree
    new_nav_yaml = build_nav_tree_yaml(osc_api_path, indent=showio_indent + 2)

    # Build the new ShowIO API section
    new_section_lines = [
        ' ' * showio_indent + '- ShowIO API:\n',
    ]

    for line in new_nav_yaml.split('\n'):
        if line.strip():
            new_section_lines.append(line + '\n')

    # Reconstruct the file
    if next_section_start is not None:
        new_lines = lines[:showio_start] + new_section_lines + lines[next_section_start:]
    else:
        # ShowIO API is the last section in nav
        new_lines = lines[:showio_start] + new_section_lines

    # Write back
    with open(mkdocs_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f"Successfully updated {mkdocs_path}")
    print(f"Generated navigation tree for ShowIO API section")


if __name__ == '__main__':
    # Paths
    mkdocs_path = Path(__file__).parent / 'mkdocs.yml'
    osc_api_path = Path(__file__).parent / 'docs' / 'osc_api'

    # Update the navigation
    update_mkdocs_nav(mkdocs_path, osc_api_path)