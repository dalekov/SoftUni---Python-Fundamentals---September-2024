from flashcard import Flashcard
import random

class FlashcardManager:
    def __init__(self):
        self.flashcards = {}


    def add_flashcard(self, question: str, answer: str):
        self.flashcards[question] = Flashcard(question, answer)


    def edit_flashcard(self, question: str, new_question: str, new_answer: str):
        if question in self.flashcards:
            self.flashcards[new_question] = Flashcard(new_question, new_answer)
            if new_question != question:
                del self.flashcards[question]


    def delete_flashcard(self, question: str) -> str:
        if question in self.flashcards:
            del self.flashcards[question]
            return "Question deleted successfully. Returning to main menu..."
        return "Question not found. Please try again!"


    def list_flashcards(self):
        if not self.flashcards:
            return "No flashcards found. Returning to main menu..."

        for question, flashcard in self.flashcards.items():
            print(flashcard.display_question())


    def review_flashcard(self):
        if self.flashcards:
            question = random.choice(list(self.flashcards.keys()))
            flashcard = self.flashcards[question]

            print(flashcard.display_question())
            input("Press Enter to show the answer...")
            print(flashcard.display_answer())

        else:
            print("No flashcards to review! Returning to main menu...")

