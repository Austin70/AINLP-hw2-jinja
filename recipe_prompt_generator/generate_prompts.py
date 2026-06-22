from jinja2 import Environment, FileSystemLoader
import json
import os

def load_examples():
    """Load example recipes from JSON files."""
    examples = []
    example_dir = 'examples'
    
    for filename in os.listdir(example_dir):
        if filename.endswith('.json'):
            with open(os.path.join(example_dir, filename), 'r') as f:
                examples.append(json.load(f))
    
    return examples

def generate_prompts():
    """Generate prompts using Jinja template."""
    # Load template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('prompt_template.j2')
    
    # Load examples
    examples = load_examples()
    
    # Generate prompts
    for i, example in enumerate(examples, 1):
        print(f"\n{'='*50}")
        print(f"Example {i}: {example['title']}")
        print('='*50)
        
        # Render template with example data
        prompt = template.render(**example)
        print(prompt)

if __name__ == "__main__":
    generate_prompts()