import random
import time
import os

HIGH_SCORE_FILE = "highscore.txt"
HISTORY_FILE = "game_history.txt"


def get_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as file:
            try:
                return int(file.read())
            except:
                return 0
    return 0


def save_high_score(score):
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(score))


def save_history(name, score, attempts, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(
            f"Player: {name} | Score: {score} | Attempts: {attempts} | Result: {result}\n"
        )


print("\n=================================")
print(" ADVANCED GUESS THE NUMBER GAME ")
print("=================================")

player_name = input("Enter Your Name: ")

while True:

    print("\nSelect Difficulty")
    print("1. Easy (1-50) - 10 Chances")
    print("2. Medium (1-100) - 8 Chances")
    print("3. Hard (1-500) - 6 Chances")

    choice = input("Choose Level: ")

    if choice == "1":
        max_num = 50
        max_attempts = 10

    elif choice == "2":
        max_num = 100
        max_attempts = 8

    elif choice == "3":
        max_num = 500
        max_attempts = 6

    else:
        print("Invalid Choice")
        continue

    secret_number = random.randint(1, max_num)

    attempts = 0

    start_time = time.time()

    print(f"\nWelcome {player_name}")
    print(f"Guess a number between 1 and {max_num}")

    while attempts < max_attempts:

        try:

            guess = int(input("\nEnter Guess: "))

            attempts += 1

            remaining = max_attempts - attempts

            if guess < secret_number:
                print("Too Low")

            elif guess > secret_number:
                print("Too High")

            else:

                end_time = time.time()

                time_taken = round(
                    end_time - start_time,
                    2
                )

                score = max(
                    150 -
                    (attempts * 5) -
                    int(time_taken),
                    10
                )

                print("\nCorrect Guess!")
                print("Attempts:", attempts)
                print("Time Taken:", time_taken, "seconds")
                print("Score:", score)

                high_score = get_high_score()

                if score > high_score:
                    save_high_score(score)
                    print("New High Score!")

                print(
                    "Current High Score:",
                    get_high_score()
                )

                if score >= 130:
                    print("Badge: Master Guesser")

                elif score >= 100:
                    print("Badge: Smart Player")

                else:
                    print("Badge: Rising Star")

                save_history(
                    player_name,
                    score,
                    attempts,
                    "WIN"
                )

                break

            if attempts == 3:

                if secret_number % 2 == 0:
                    print("Hint: Secret Number is EVEN")

                else:
                    print("Hint: Secret Number is ODD")

            print(
                "Remaining Chances:",
                remaining
            )

        except ValueError:
            print(
                "Please Enter Numbers Only!"
            )

    else:

        print("\nGame Over!")
        print(
            "The Correct Number Was:",
            secret_number
        )

        save_history(
            player_name,
            0,
            attempts,
            "LOSE"
        )

    again = input(
        "\nPlay Again? (y/n): "
    )

    if again.lower() != "y":
        print("\nThank You For Playing!")
        break