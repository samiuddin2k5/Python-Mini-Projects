import time
import random

def typing_test():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is an amazing programming language.",
        "Typing fast and accurately is a useful skill.",
        "Practice makes perfect in coding and typing.",
        "Always comment your code and keep it clean."
    ]

    test_sentence = random.choice(sentences)
    print("\n Type the following sentence:")
    print( test_sentence)
    input("Press Enter when you're ready...")

    start_time = time.time()
    user_input = input("\nStart typing: ")
    end_time = time.time()

    time_taken = end_time - start_time
    time_in_minutes = time_taken / 60

    # Word count for WPM
    word_count = len(user_input.split())
    wpm = word_count / time_in_minutes

    # Accuracy
    correct_chars = 0
    for i in range(min(len(test_sentence), len(user_input))):
        if test_sentence[i] == user_input[i]:
            correct_chars += 1

    accuracy = (correct_chars / len(test_sentence)) * 100

    print("\n⌛ Time Taken: {:.2f} seconds".format(time_taken))
    print("💨 Words per Minute (WPM): {:.2f}".format(wpm))
    print("🎯 Accuracy: {:.2f}%".format(accuracy))

# Run the test
typing_test()
