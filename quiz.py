class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self):
        print(self.question)
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer

quiz1 = Quiz("파이썬 창시자는?", ["귀도", "리누스"], 1)

quiz1.show()                    #
print(quiz1.is_correct(1))      # True
print(quiz1.is_correct(2))      # False