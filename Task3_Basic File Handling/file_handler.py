import shutil
from datetime import datetime

FILE_NAME = "sample.txt"
BACKUP_FILE = "backup.txt"
LOG_FILE = "activity_log.txt"


def log_activity(action):

    with open(LOG_FILE, "a") as log:

        log.write(
            f"{datetime.now()} - {action}\n"
        )


def read_file():

    try:

        with open(FILE_NAME, "r") as file:

            content = file.read()

            print("\n===== FILE CONTENT =====\n")
            print(content)

            log_activity("Viewed File")

    except FileNotFoundError:

        print("File Not Found")


def find_replace():

    try:

        with open(FILE_NAME, "r") as file:

            content = file.read()

        find_word = input(
            "Find Word: "
        )

        replace_word = input(
            "Replace With: "
        )

        new_content = content.replace(
            find_word,
            replace_word
        )

        with open(FILE_NAME, "w") as file:

            file.write(new_content)

        print("Replacement Successful")

        log_activity(
            f"Replaced '{find_word}' with '{replace_word}'"
        )

    except FileNotFoundError:

        print("File Not Found")


def backup_file():

    try:

        shutil.copy(
            FILE_NAME,
            BACKUP_FILE
        )

        print(
            "Backup Created Successfully"
        )

        log_activity(
            "Backup Created"
        )

    except:

        print(
            "Backup Failed"
        )


def restore_backup():

    try:

        shutil.copy(
            BACKUP_FILE,
            FILE_NAME
        )

        print(
            "Backup Restored"
        )

        log_activity(
            "Backup Restored"
        )

    except:

        print(
            "Restore Failed"
        )


def search_keyword():

    try:

        keyword = input(
            "Enter Keyword: "
        )

        with open(
            FILE_NAME,
            "r"
        ) as file:

            content = file.read()

        if keyword.lower() in content.lower():

            print(
                "Keyword Found"
            )

        else:

            print(
                "Keyword Not Found"
            )

        log_activity(
            f"Keyword Search: {keyword}"
        )

    except:

        print(
            "Error Searching Keyword"
        )


def file_statistics():

    try:

        with open(
            FILE_NAME,
            "r"
        ) as file:

            content = file.read()

        words = len(
            content.split()
        )

        characters = len(
            content
        )

        lines = len(
            content.splitlines()
        )

        print("\n===== FILE STATISTICS =====")

        print(
            "Word Count      :",
            words
        )

        print(
            "Character Count :",
            characters
        )

        print(
            "Line Count      :",
            lines
        )

        log_activity(
            "Viewed Statistics"
        )

    except:

        print(
            "Error Reading Statistics"
        )


while True:

    print("\n==============================")
    print(" ADVANCED FILE HANDLER ")
    print("==============================")

    print("1. Read File")
    print("2. Find & Replace")
    print("3. Create Backup")
    print("4. Restore Backup")
    print("5. Search Keyword")
    print("6. File Statistics")
    print("7. Exit")

    choice = input(
        "Enter Choice: "
    )

    if choice == "1":

        read_file()

    elif choice == "2":

        find_replace()

    elif choice == "3":

        backup_file()

    elif choice == "4":

        restore_backup()

    elif choice == "5":

        search_keyword()

    elif choice == "6":

        file_statistics()

    elif choice == "7":

        print(
            "Thank You!"
        )

        break

    else:

        print(
            "Invalid Choice"
        )