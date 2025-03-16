import os
import shutil

SCAFFOLD_DIR = os.path.join(os.path.dirname(__file__), "scaffold")

def create_project(project_name, template):
    project_path = os.path.join(os.getcwd(), project_name)
    template_path = os.path.join(SCAFFOLD_DIR, template)

    if not os.path.exists(template_path):
        print(f"Error: Template '{template}' does not exist.")
        return
    
    if not os.path.exists(project_path):
        print(f"Error: The directory '{project_name}' doest not exists.")
        return

    shutil.copytree(template_path, project_path, dirs_exist_ok=True)