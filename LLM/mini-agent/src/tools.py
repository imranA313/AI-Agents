
class Tools:
    def calculator(self, exp):
        try:
            return eval(exp)
        except:
            return "Calculation error"
