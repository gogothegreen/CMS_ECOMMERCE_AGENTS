import os
import markdown # type: ignore

def read_markdown_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return markdown.markdown(content)

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def create_project_structure(project_name):
    base_dir = os.path.join(os.getcwd(), project_name)
    os.makedirs(base_dir, exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'src'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'tests'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'docs'), exist_ok=True)
    
    return base_dir
