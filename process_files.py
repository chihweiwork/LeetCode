import os

def create_markdown_file(py_file):
    # Extract problem number and name from the filename
    parts = os.path.basename(py_file).replace('.py', '').split('-')
    problem_number = parts[0]
    problem_name = ' '.join(parts[1:])

    # Read the content of the python file
    with open(py_file, 'r') as f:
        code_content = f.read()

    # Format the content in markdown
    markdown_content = f"# {problem_number}. {problem_name}\n\n```python\n{code_content}\n```"

    # Write the markdown content to a new file
    md_filename = os.path.join('notebooklm-source', f'{os.path.basename(py_file).replace(".py", ".md")}')
    with open(md_filename, 'w') as f:
        f.write(markdown_content)

def main():
    # Create the output directory if it doesn't exist
    if not os.path.exists('notebooklm-source'):
        os.makedirs('notebooklm-source')

    # List all files in the current directory
    files = os.listdir('.')

    # Filter for python files from 0001 to 0050
    for i in range(1, 51):
        filename = f'{i:04d}'
        for file in files:
            if file.startswith(filename) and file.endswith('.py'):
                create_markdown_file(file)

if __name__ == "__main__":
    main()
