import os

# yaha project ka naam change kar sakte ho
PROJECT_NAME = input("Enter the name of the AI project: ") or "ai-agent"    

# Or r"C:\Users\Name\Documents"
new_path = input("Enter the path where you want to create the project: ") or "E:\AI-Projects\Agents" 

os.chdir(new_path)

structure = [
    # Agents
    "agents/__init__.py",
    "agents/base_agent.py",
    "agents/planner_agent.py",
    "agents/executor_agent.py",
    "agents/evaluator_agent.py",
    "agents/network_defense_agent.py",

    # Tools
    "tools/__init__.py",
    "tools/llm_tool.py",
    "tools/web_tool.py",
    "tools/file_tool.py",
    "tools/network_tool.py",
    "tools/db_tool.py",

    # Memory
    "memory/__init__.py",
    "memory/short_term.py",
    "memory/long_term.py",
    "memory/episodic.py",

    # Environment
    "environment/__init__.py",
    "environment/simulator.py",
    "environment/real_time_listener.py",

    # Workflows
    "workflows/__init__.py",
    "workflows/react_loop.py",
    "workflows/task_router.py",
    "workflows/feedback_loop.py",

    # Models
    "models/__init__.py",
    "models/anomaly_model.py",
    "models/classifier.py",

    # Data
    "data/raw",
    "data/processed",
    "data/features",

    # Tests
    "tests/test_agents.py",
    "tests/test_tools.py",
    "tests/test_memory.py",

    # Configs
    "configs/agent.yaml",
    "configs/llm.yaml",
    "configs/logging.yaml",

    # Logs
    "logs/agent.log",

    # Dashboards
    "dashboards/streamlit_app.py",
    "dashboards/metrics_dashboard.py",

    # Scripts
    "scripts/run_agent.py",
    "scripts/train_models.py",

    # Docs
    "docs/architecture.md",
    "docs/threat_model.md",

    # Root files
    ".env",
    "requirements.in",
    "requirements.txt",
    "pytest.ini",
    "Dockerfile",
    "README.md"
]


def create_project_structure(base_path):
    for item in structure:
        path = os.path.join(base_path, item)

        if "." in os.path.basename(path):  # File
            os.makedirs(os.path.dirname(path), exist_ok=True)
            if not os.path.exists(path):
                with open(path, "w", encoding="utf-8") as f:
                    if path.endswith(".py"):
                        f.write("# Auto-generated file\n")
        else:  # Directory
            os.makedirs(path, exist_ok=True)

    print(f"\n✅ Industry-grade AI Agent project '{PROJECT_NAME}' created successfully!")


if __name__ == "__main__":
    create_project_structure(PROJECT_NAME)
