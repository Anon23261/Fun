import random
import time

# Helper function to pause between messages
def print_pause(message):
    print(message)
    time.sleep(1.5)

# Introduction to the game
def intro():
    print_pause("Welcome to the Cybersecurity Challenge!")
    print_pause("You are an ethical hacker tasked with securing a company from cyber threats.")
    print_pause("Your mission is to identify and neutralize various hacking attempts!")
    print_pause("Let's see if you have what it takes to protect the network.")

# Inventory system
inventory = []

# Player rank and score
player_score = 0
player_rank = "Novice"

# Display inventory
def show_inventory():
    if inventory:
        print_pause("Your cybersecurity toolkit includes:")
        for item in inventory:
            print(f"- {item}")
    else:
        print_pause("Your toolkit is empty.")

# Update player rank based on score
def update_rank():
    global player_rank
    if player_score >= 30:
        player_rank = "Expert"
    elif player_score >= 15:
        player_rank = "Intermediate"
    else:
        player_rank = "Novice"

# Phishing Challenge (Realistic Scenario)
def phishing_challenge(difficulty):
    print_pause("You've received a corporate email that looks suspicious.")
    print_pause("Choose wisely: This could be a phishing attempt!")
    options = ["Click the link", "Verify the sender", "Report to IT"]
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    choice = input("What do you choose? (1/2/3): ")
    if choice == "1":
        print_pause("You've been phished! Your credentials are compromised.")
        print_pause("GAME OVER.")
        return False
    elif choice == "2":
        print_pause("You verified the sender and found it was spoofed.")
        return points_based_on_difficulty(difficulty, 5)
    else:
        print_pause("You reported the email to IT. Well done!")
        return points_based_on_difficulty(difficulty, 3)

# Network Security Challenge (Technical Task)
def network_security_challenge(difficulty):
    print_pause("You are tasked with securing a network from a potential attack.")
    print_pause("Identify the vulnerabilities in the following network setup:")
    vulnerabilities = [
        "Unpatched operating systems",
        "Weak passwords",
        "Open ports on the firewall",
        "No intrusion detection system"
    ]
    print("Vulnerabilities:")
    for v in vulnerabilities:
        print(f"- {v}")

    choice = input("Which vulnerability do you want to address? (unpatched/weak/open/ids): ").lower()
    if choice == "unpatched":
        print_pause("You applied necessary patches. Good job!")
        return points_based_on_difficulty(difficulty, 4)
    elif choice == "weak":
        print_pause("You enforced a strong password policy. Good choice!")
        return points_based_on_difficulty(difficulty, 3)
    elif choice == "open":
        print_pause("You closed the unnecessary ports. Well done!")
        return points_based_on_difficulty(difficulty, 5)
    elif choice == "ids":
        print_pause("You installed an IDS to monitor traffic. Great work!")
        return points_based_on_difficulty(difficulty, 6)
    else:
        print_pause("Invalid choice. You missed an opportunity to secure the network.")
        return 0  # No points for invalid choice

# Encryption Challenge (Technical Concept)
def encryption_challenge(difficulty):
    print_pause("You intercepted an encrypted message:")
    encrypted_message = "Uifsf jt b tfdsfu! (There is a secret!)"
    print(f"Encrypted: {encrypted_message}")
    print("Can you decrypt the message using a Caesar cipher with a shift of 1?")

    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            decrypted_message += chr(ord(char) - 1)
        else:
            decrypted_message += char

    print(f"Decrypted: {decrypted_message}")
    return points_based_on_difficulty(difficulty, 4)

# Capture the Flag Challenge (Realistic CTF)
def capture_the_flag(difficulty):
    print_pause("You've entered a high-security server room for a Capture the Flag challenge.")
    print_pause("To capture the flag, you must solve the following challenge:")
    
    # A basic CTF challenge with realistic context
    print_pause("You need to find the flag in the log files of a compromised server.")
    print_pause("The flag format is CTF{...}. Search for the keyword 'flag' in the logs.")

    # Simulating a log file search
    flag_found = random.choice([True, False])  # Randomly determine if the player finds the flag
    if flag_found:
        print_pause("Congratulations! You found the flag: CTF{You_Captured_The_Flag!}")
        inventory.append("CTF Flag")
        return points_based_on_difficulty(difficulty, 10)
    else:
        print_pause("No flag found in the logs. You failed to capture it.")
        return 0  # No points for failure

# Points based on difficulty level
def points_based_on_difficulty(difficulty, base_points):
    if difficulty == "easy":
        return base_points  # Base points for easy
    elif difficulty == "medium":
        return base_points + 2  # Moderate points for medium
    elif difficulty == "hard":
        return base_points + 4  # More points for hard
    return 0

# Choose a challenge
def choose_challenge():
    print_pause("Choose a difficulty level:")
    print_pause("1. Easy")
    print_pause("2. Medium")
    print_pause("3. Hard")
    difficulty_choice = input("Enter 1, 2, or 3: ")

    if difficulty_choice == "1":
        difficulty = "easy"
    elif difficulty_choice == "2":
        difficulty = "medium"
    elif difficulty_choice == "3":
        difficulty = "hard"
    else:
        print_pause("Invalid choice. Defaulting to Easy.")
        difficulty = "easy"

    print_pause("Which challenge would you like to tackle?")
    print_pause("1. Phishing Challenge")
    print_pause("2. Network Security Challenge")
    print_pause("3. Encryption Challenge")
    print_pause("4. Capture the Flag Challenge")
    choice = input("Enter 1, 2, 3, or 4: ")
    points = 0
    if choice == "1":
        points = phishing_challenge(difficulty)
    elif choice == "2":
        points = network_security_challenge(difficulty)
    elif choice == "3":
        points = encryption_challenge(difficulty)
    elif choice == "4":
        points = capture_the_flag(difficulty)
    else:
        print_pause("Invalid choice. Please select a valid challenge.")
    
    return points

# Start the adventure
def start_adventure():
    global player_score
    while True:
        print_pause("You are in the Cybersecurity Command Center.")
        show_inventory()  # Show inventory before choosing a challenge
        points = choose_challenge()
        player_score += points
        print_pause(f"You earned {points} points!")
        update_rank()
        print_pause(f"Your current rank is: {player_rank}")

# Game loop
def play_game():
    intro()
    start_adventure()

    # Ask if the player wants to play again
    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again == "y":
        print_pause("Restarting the game...")
        inventory.clear()  # Clear inventory for a fresh start
        global player_score, player_rank
        player_score = 0
        player_rank = "Novice"
        play_game()
    else:
        print_pause("Thank you for playing! Goodbye.")

# Start the game
play_game()
