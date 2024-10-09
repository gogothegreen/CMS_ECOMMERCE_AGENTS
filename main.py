import os
from agents.project_manager import ProjectManagerAgent
from agents.full_stack_developer import FullStackDeveloperAgent
from agents.quality_assurance import QualityAssuranceAgent
from utils.file_handler import read_markdown_file, write_to_file, create_project_structure

def main():
    # Initialize agents
    pm_agent = ProjectManagerAgent()
    dev_agent = FullStackDeveloperAgent()
    qa_agent = QualityAssuranceAgent()

    # Read project requirements
    project_req = read_markdown_file('project_requirements.md')

    # Project Manager: Analyze requirements and break down tasks
    project_plan = pm_agent.process_task(project_req)
    tasks = pm_agent.break_down_tasks(project_req)

    print("Project Plan:")
    print(project_plan)
    print("\nTasks:")
    print(tasks)

    # Create project structure
    project_dir = create_project_structure("cms_ecommerce_project")

    # Full-Stack Developer: Generate code for each task
    for i, task in enumerate(tasks.split('\n'), 1):
        if task.strip():
            code = dev_agent.generate_code(task)
            refactored_code = dev_agent.refactor_code(code)
            
            # Quality Assurance: Review code and generate tests
            code_review = qa_agent.review_code(refactored_code)
            tests = qa_agent.generate_tests(refactored_code)
            
            # Save code and tests
            write_to_file(os.path.join(project_dir, f'src/task_{i}.js'), refactored_code)
            write_to_file(os.path.join(project_dir, f'tests/test_task_{i}.js'), tests)
            
            print(f"\nTask {i} completed. Code review:")
            print(code_review)

    print("\nProject generation complete. Check the 'cms_ecommerce_project' directory for output.")

if __name__ == "__main__":
    main()
