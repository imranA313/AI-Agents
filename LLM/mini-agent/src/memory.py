
class Memory:
    def __init__(self):
        self.history = []

    def save(self, user, agent):
        self.history.append({"user": user, "agent": agent})

    def context(self):
        return "\n".join(
            [f"User: {h['user']}\nAgent: {h['agent']}" for h in self.history[-5:]]
        )
