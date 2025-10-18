import yaml
import argparse

def generate_claude_skill_md(data):
    """Generates a SKILL.md file content from the structured YAML data."""
    content = []

    # --- Frontmatter ---
    content.append("---")
    content.append(f"name: {data['name']}")
    content.append(f"description: {data['description']}")
    content.append(f"version: {data['version']}")
    content.append(f"dependencies: {data['dependencies']}")
    content.append("---\n")

    # --- Main Content ---
    content.append(f"# {data['name'].replace('-', ' ').title()}")
    content.append(f"{data['tagline']}\n")

    # --- Purpose ---
    content.append("## Purpose")
    for point in data['purpose_points']:
        content.append(f"- {point}")
    content.append("\n")

    # --- Instructions ---
    content.append("## Instructions")
    content.append("When a user wants to track or reduce their carbon footprint:")
    for i, instruction in enumerate(data['instructions'], 1):
        content.append(f"{i}. **{instruction.split(':')[0]}**: {instruction.split(':')[1].strip()}")
    content.append("\n")

    # --- Sections (like Gamification, etc.) ---
    for section in data.get('sections', []):
        content.append(f"### {section['title']}")
        content.append(f"{section['content']}\n")

    # --- Examples ---
    content.append("## Examples")
    for i, example in enumerate(data['examples'], 1):
        content.append(f"### Example {i}: {example['title']}")
        for turn in example['conversation']:
            if 'user' in turn:
                content.append(f"**User**: \"{turn['user']}\"\n")
            elif 'bot' in turn:
                content.append(f"**{data['name'].replace('-', ' ').title()} Response**:")
                content.append(f"{turn['bot']}\n")

    # --- Guidelines ---
    content.append("## Guidelines")
    content.append("### DO")
    for point in data['guidelines']['do']:
        content.append(f"✅ {point}")
    content.append("\n### DON'T")
    for point in data['guidelines']['dont']:
        content.append(f"❌ {point}")
    content.append("\n")

    # --- Best Practices ---
    content.append("## Best Practices")
    for practice in data.get('best_practices', []):
        content.append(f"### {practice['title']}")
        content.append(f"{practice['content']}\n")

    # --- Data Schemas ---
    content.append("## Data Schema")
    for schema in data.get('data_schemas', []):
        content.append(f"### {schema['title']}")
        content.append(f"{schema['schema']}\n")

    # --- Final Reminders ---
    content.append("---")
    for reminder in data.get('final_reminders', []):
        content.append(f"**Remember**: {reminder}")

    return "\n".join(content)

def main():
    parser = argparse.ArgumentParser(description='Generate AI skill formats from a universal skill.yaml file.')
    parser.add_argument('input_file', type=str, help='Path to the input skill.yaml file.')
    parser.add_argument('--format', type=str, default='claude_md', help='The output format (e.g., claude_md).')
    parser.add_argument('--output-file', type=str, help='Path to the output file. If not provided, prints to stdout.')

    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: Input file not found at {args.input_file}")
        return
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return

    output = None
    if args.format == 'claude_md':
        output = generate_claude_skill_md(data)
    else:
        print(f"Error: Unsupported format '{args.format}'")
        return

    if output:
        if args.output_file:
            try:
                with open(args.output_file, 'w', encoding='utf-8') as f:
                    f.write(output)
                print(f"Successfully generated {args.output_file}")
            except IOError as e:
                print(f"Error writing to file {args.output_file}: {e}")
        else:
            print(output)

if __name__ == '__main__':
    main()
