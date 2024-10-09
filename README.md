# CMS E-commerce Agent System

This project uses an AI agent system to generate a Content Management System (CMS) with e-commerce functionalities.

## Setup Instructions

1. Ensure you have Python 3.7+ and Node.js installed on your system.

2. Clone this repository:
git clone <https://github.com/gogothegreen/cms_ecommerce_agents.git>
cd cms_ecommerce_agents

3. Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

4. Install required Python packages:
pip install groq python-dotenv markdown

5. Create a `.env` file in the project root and add your Groq API key:
GROQ_API_KEY=your_groq_api_key_here

6. Create a `project_requirements.md` file with your project specifications.

7. Run the main script:

python main.py

## System Description

This system uses three AI agents to generate a CMS with e-commerce features:

1. Project Manager Agent: Analyzes requirements and breaks down tasks.
2. Full-Stack Developer Agent: Generates and refactors Node.js code.
3. Quality Assurance Agent: Reviews code and generates tests.

The system reads project requirements from a Markdown file, generates code and tests, and outputs them in a structured project directory.

## Output

The system generates a `cms_ecommerce_project` directory with the following structure:

cms_ecommerce_project/
├── src/
│ └── (Generated .js files)
├── tests/
│ └── (Generated test files)
└── docs/

## Next Steps

Review the generated code and tests, then integrate them into a complete Node.js project structure. Additional manual development and testing may be required to create a fully functional application.
