import time 
import random
import colorama
from colorama import Fore, Style

import os
if os.name == 'nt':
    import msvcrt

print(Fore.GREEN + "Hello user enter your nickname")
name = input()
print(Fore.CYAN + "Welcome ", name, " to the random generator")

last_generated = None

def input_with_esc(prompt):
    if os.name != 'nt':
        return input(prompt)

    print(prompt, end='', flush=True)
    chars = []
    while True:
        ch = msvcrt.getwch()
        if ch == '\r':
            print()
            return ''.join(chars).strip()
        if ch == '\x1b':
            print()
            return None
        if ch == '\x08':
            if chars:
                chars.pop()
                print('\b \b', end='', flush=True)
            continue
        print(ch, end='', flush=True)
        chars.append(ch)

# main loop continues until the user chooses to exit
while True:
    print(Fore.YELLOW + "Choose your option")
    print("1. Generate random User Name")
    print("2. Generate random password")
    print("3. Exit")
    print("4. Save last generated username or password")
    print(Fore.YELLOW + "(or type 'clear' to clear the screen)")
    option = input().strip()

    # support clear command
    if option.lower() == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    if option.lower() == "save":
        option = "4"

    while option not in ["1", "2", "3", "4"]:
        print(Fore.RED + "Invalid option. Please choose 1, 2, 3, or 4.")
        option = input().strip()
        if option.lower() == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            option = ''
        if option.lower() == "save":
            option = "4"
    
    if option == "1":
        print("Enter the length of the username")
        length = int(input("Length: "))
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        username = ""
        for i in range(length):
            if i % 2 == 0:
                username += random.choice(consonants)
            else:
                username += random.choice(vowels)
        last_generated = username
        print("Generating random username...")
        time.sleep(2)
        print(Fore.GREEN + "Your random username is: ", username)
    elif option == "2":
        print("Enter the length of the password")
        length = int(input("Length: "))
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        password = "".join(random.choice(characters) for i in range(length))
        last_generated = password
        print("Generating random password...")
        time.sleep(2)
        print(Fore.GREEN + "Your random password is: ", password)
    elif option == "3":
        print("Exiting...")
        time.sleep(2)
        break
    elif option == "4":
        if last_generated is None:
            print(Fore.RED + "No generated username or password available to save.")
            input("Press Enter to continue...")
            continue

        filename = input_with_esc("Enter file name to save to (or press ESC to cancel): ")
        if filename is None:
            print(Fore.YELLOW + "Save canceled.")
            input("Press Enter to continue...")
            continue

        if filename == "":
            filename = "saved_data.txt"
        if not filename.lower().endswith(".txt"):
            filename += ".txt"

        with open(filename, "a") as file:
            file.write(last_generated + "\n")
        print(Fore.GREEN + f"Data saved successfully to {filename}!")
        input("Press Enter to continue...")
