class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


    def display_question(self) -> str:
        return f"Q: {self.question}"


    def display_answer(self) -> str:
        return f"A: {self.answer}"
