

from tools import Tools
from memory import Memory
from llm import openai_llm, gemini_llm

LLM_PROVIDER = "openai" 

class Agent:
    def __init__(self):
        self.tools = Tools()
        self.memory = Memory()

    def think(self, user_input):
        # Tool detection
        if any(ch.isdigit() for ch in user_input):
            result = self.tools.calculator(user_input)
            response = f"Calculation result: {result}"
        else:
            context = self.memory.context()
            prompt = f""" You are a helpful AI agent. Conversation so far: {context} User: {user_input}
            Agent: """

            if LLM_PROVIDER == "openai":
                response = openai_llm(prompt)
            else:
                response = gemini_llm(prompt)

        self.memory.save(user_input, response)
        return response


if __name__ == "__main__":
    agent = Agent()
    print("🤖 LLM AI Agent started (type 'exit' to quit)\n")

    while True:
        user = input("You: ")
        if user.lower() == "exit":
            break
        print("Agent:", agent.think(user))
