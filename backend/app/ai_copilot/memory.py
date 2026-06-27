class CopilotMemory:
    def __init__(self):
        self.last_messages = []

    def add(self, message: str):
        self.last_messages.append(message)
        if len(self.last_messages) > 5:
            self.last_messages.pop(0)

    def get_context(self):
        return " | ".join(self.last_messages)
