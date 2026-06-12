import requests
from datetime import datetime

HISTORY_FILE = "conversion_history.txt"
FAVORITE_FILE = "favorites.txt"
LOG_FILE = "converter_log.txt"


def log_activity(action):

    with open(LOG_FILE, "a") as log:

        log.write(
            f"{datetime.now()} - {action}\n"
        )


def convert_currency():

    try:

        base = input(
            "Base Currency (Example: INR): "
        ).upper()

        target = input(
            "Target Currency (Example: USD): "
        ).upper()

        amount = float(
            input("Amount: ")
        )

        url = (
            f"https://open.er-api.com/v6/latest/{base}"
        )

        response = requests.get(url)

        data = response.json()

        if "rates" not in data:

            print("Invalid Currency Code")
            return

        rate = data["rates"].get(target)

        if rate is None:

            print("Target Currency Not Found")
            return

        converted = round(
            amount * rate,
            2
        )

        print("\n===== RESULT =====")

        print(
            f"{amount} {base} = "
            f"{converted} {target}"
        )

        with open(
            HISTORY_FILE,
            "a"
        ) as file:

            file.write(
                f"{datetime.now()} | "
                f"{amount} {base} = "
                f"{converted} {target}\n"
            )

        log_activity(
            f"Converted {base} to {target}"
        )

    except ValueError:

        print(
            "Enter Valid Amount"
        )

    except Exception as e:

        print(
            "Error:",
            e
        )


def view_history():

    try:

        print(
            "\n===== CONVERSION HISTORY =====\n"
        )

        with open(
            HISTORY_FILE,
            "r"
        ) as file:

            print(file.read())

        log_activity(
            "Viewed History"
        )

    except:

        print(
            "No History Found"
        )


def save_favorite():

    pair = input(
        "Enter Favorite Pair (Example INR-USD): "
    )

    with open(
        FAVORITE_FILE,
        "a"
    ) as file:

        file.write(pair + "\n")

    print(
        "Favorite Pair Saved"
    )

    log_activity(
        f"Saved Favorite {pair}"
    )


def view_favorites():

    try:

        print(
            "\n===== FAVORITE PAIRS =====\n"
        )

        with open(
            FAVORITE_FILE,
            "r"
        ) as file:

            print(file.read())

        log_activity(
            "Viewed Favorites"
        )

    except:

        print(
            "No Favorites Found"
        )


def statistics():

    try:

        with open(
            HISTORY_FILE,
            "r"
        ) as file:

            records = file.readlines()

        print(
            "\n===== STATISTICS ====="
        )

        print(
            "Total Conversions:",
            len(records)
        )

        log_activity(
            "Viewed Statistics"
        )

    except:

        print(
            "No Statistics Available"
        )


while True:

    print("\n==============================")
    print(" ADVANCED CURRENCY CONVERTER ")
    print("==============================")

    print("1. Convert Currency")
    print("2. View History")
    print("3. Save Favorite Pair")
    print("4. View Favorite Pairs")
    print("5. Statistics")
    print("6. Exit")

    choice = input(
        "Enter Choice: "
    )

    if choice == "1":

        convert_currency()

    elif choice == "2":

        view_history()

    elif choice == "3":

        save_favorite()

    elif choice == "4":

        view_favorites()

    elif choice == "5":

        statistics()

    elif choice == "6":

        print("Thank You!")
        break

    else:

        print(
            "Invalid Choice"
        )