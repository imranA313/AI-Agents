class Memory:
    def __init__(self):
        self.history = []

    def save(self, user_input, agent_response):
        self.history.append({
            "user": user_input,
            "agent": agent_response
        })

    def get_history(self):
        return self.history