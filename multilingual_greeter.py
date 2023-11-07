def language_input():
    lang_inp = input("Enter 1 for English, 2 for Spanish, and 3 for Deutsch: ")
    return lang_inp

"""
greet(name) - context: human name works best, will take any type argument and return it embedded in a greeting.  
"""
def greet(name, lang_inp):
    if (lang_inp == "1"):
        print(f"Hey, {name}! I'm walking here.")
    elif (lang_inp == "2"):
        print(f"Hola, {name}! Lo siento para todo.")
    else:
        print(f"Hallo, {name}! Wie gehts es ihnen?.")
    
"""
name_input - prompts the user to enter their name, returns it in variable name_inputted
"""
def name_input():
    name_inputted = input("Tell me your name: ")
    return name_inputted

name = name_input()
language = language_input()
greet(name, language)



