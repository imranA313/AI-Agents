
from tools import Tools
from memory import Memory


class Agent:
    def __init__(self):
        self.tools = Tools()
        self.memory = Memory()

    def think(self, user_input):
        user_input_lower = user_input.lower()

        if "hello" in user_input_lower or "hi" in user_input_lower:
            response = self.tools.greet()

        elif any(char.isdigit() for char in user_input):
            response = f"Result: {self.tools.calculator(user_input)}"

        else:
            response = "Main abhi basic agent hoon, seekh raha hoon 🙂"

        self.memory.save(user_input, response)
        return response


if __name__ == "__main__":
    agent = Agent()

    while True:
        user = input("You: ")
        if user.lower() in ["exit", "quit"]:
            break

        reply = agent.think(user)
        print("Agent:", reply)

    print("\n🧠 Memory:")
    print(agent.memory.get_history())