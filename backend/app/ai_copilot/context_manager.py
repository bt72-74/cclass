from app.ai_copilot.memory import CopilotMemory

memory = CopilotMemory()


def update_context(message: str):
    memory.add(message)


def get_context():
    return memory.get_context()
