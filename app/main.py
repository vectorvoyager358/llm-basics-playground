from app.summarizer import summarize_text
from app.qa_bot import ask_question
from app.generator import generate_content


def main():
    print("\n=== LLM Basics Playground ===")

    while True:
        print("\nChoose an option:")
        print("1. Summarize Text")
        print("2. Ask Question")
        print("3. Generate Content")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            text = input("\nEnter text:\n")
            print("\nSummary:\n", summarize_text(text))

        elif choice == "2":
            question = input("\nEnter your question:\n")
            print("\nAnswer:\n", ask_question(question))

        elif choice == "3":
            topic = input("\nEnter topic:\n")
            print("\nGenerated Content:\n", generate_content(topic))

        elif choice == "4":
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()