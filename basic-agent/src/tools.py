class Tools:

    def greet(self):
        return "Hello! Main tumhara Mini AI Agent hoon 🤖"

    def calculator(self, expression):
        try:
            return eval(expression)
        except:
            return "❌ Calculation error"