from flashcard import Flashcard
from flashcard_manager import FlashcardManager
import time


flashcard_manager = FlashcardManager()


def user_menu():
    print("####### MENU #######")
    print("1. Create Flashcard")
    print("2. Edit Flashcard")
    print("3. Review Flashcard")
    print("4. Delete Flashcard")
    print("5. List Flashcards")
    print("0. Exit")
    print("####### MENU #######")


    try:
        user_input = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Invalid input! Please enter a valid choice.")
        print("Returning to main menu...")
        time.sleep(2)
        user_menu()
    else:
        return user_input


def main():
    print("Welcome to the Flash Study App!")

    while True:
        choice = user_menu()

        if choice == 0:
            print("Thank you for using the Flash Study App! Goodbye!")
            exit()
        elif choice == 1:
            question = input("Please enter question as you want it to be displayed: ")
            answer = input("Please enter answer: ")

            flashcard_manager.add_flashcard(question, answer)

            print("Flashcard added successfully. Returning to main menu...")
        elif choice == 2:
            question = input("Please enter the question you wish to edit?")
            new_question = input("Please enter the new question: ")
            new_answer = input("Please enter the new answer: ")

            flashcard_manager.edit_flashcard(question, new_question, new_answer)

            print("Flashcard edited successfully. Returning to main menu...")
        elif choice == 3:
            flashcard_manager.review_flashcard()
        elif choice == 4:
            question = input("Please enter a question to delete: ")
            print(flashcard_manager.delete_flashcard(question))

        elif choice == 5:
            flashcard_manager.list_flashcards()

        time.sleep(1)

main()