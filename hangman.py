# Thanael Jean-Philippe

# CIS109-G1 Introduction to Programming

# Hangman Game Lab 4




import random

wordlist = ["python", "java", "kotlin", "javascript", "hangman", "programming"]

random_number = random.randint(0, len(wordlist) - 1)
word = wordlist[random_number]

gallows = [
    """
+---+
|   
|   
|   
|   
|   
======
""",
    """
+---+
|   |
|   
|   
|   
|   
======
""",
    """
+---+
|   |
|   0
|   
|   
|   
======
""",
    """
+---+
|   |
|   0
|   |
|   
|   
======
""",
    """
+---+
|   |
|   0
|  /|\\
|   
|   
======
""",
    """
+---+
|   |
|   0
|  /|\\
|  / \\
|   
======
"""
]

board = ["_" for letter in word]
bad_guesses = []

print("Welcome to HANGMAN!")

while "_" in board and len(bad_guesses) < 6:

    print()
    print("Board:", board)
    print(gallows[len(bad_guesses)])
    print("Bad Guesses:", bad_guesses)

    guess = input("Guess a letter: ").lower()

    # 6. Invalid Input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter one letter only.")
        input("Press [enter] to continue.")
        continue

    # Check if letter was already guessed
    if guess in board or guess in bad_guesses:
        print("⚠️ You already guessed that letter!")
        input("Press [enter] to continue.")
        continue

    # 7. Bad Guess
    if guess not in word:
        bad_guesses.append(guess)

        print(f"❌ '{guess}' is not in the word.")
        input("Press [enter] to continue.")

    # 8. Correct Guess
    else:
        for i in range(len(word)):
            if word[i] == guess:
                board[i] = guess

        print(f"✅ '{guess}' is in the word!")
        input("Press [enter] to continue.")


# 9. Player wins
if "_" not in board:
    print()
    print(f"🎉 YOU WON! The word was '{word}'")
    print("Thank you for playing!")

# 10. Player loses
elif len(bad_guesses) == 6:
    print(gallows[6 - 1])
    print()
    print(f"💀 YOU LOST! The word was '{word}'")
    print("Thank you for playing!")