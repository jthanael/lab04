
print ("Welcome to Hangman!")


import random

wordlist = ["python", "java", "kotlin", "javascript", "hangman", "programming"]


random_number = random.randint(0, len(wordlist) - 1)
word = wordlist[random_number]

bad_guesses = []


['_','_', '_', '_', '_', '_', '_']

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
""",

]