from collections import Counter
import pandas as pd
from datetime import datetime

FILE_NAME = "sample.txt"
LOG_FILE = "activity_log.txt"

STOP_WORDS = {
    "is", "the", "and", "of",
    "to", "in", "a", "an",
    "for", "on", "with"
}


def log_activity(action):

    with open(LOG_FILE, "a") as log:

        log.write(
            f"{datetime.now()} - {action}\n"
        )


try:

    with open(
        FILE_NAME,
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read()

    words = content.lower().split()

    clean_words = []

    for word in words:

        word = word.strip(
            ".,!?;:()[]{}\"'"
        )

        if word not in STOP_WORDS:

            clean_words.append(word)

    word_count = len(words)

    char_count = len(content)

    line_count = len(
        content.splitlines()
    )

    sentence_count = (
        content.count(".")
        + content.count("!")
        + content.count("?")
    )

    frequency = Counter(
        clean_words
    )

    print("\n===== TEXT ANALYSIS REPORT =====")

    print(
        "Word Count      :",
        word_count
    )

    print(
        "Character Count :",
        char_count
    )

    print(
        "Line Count      :",
        line_count
    )

    print(
        "Sentence Count  :",
        sentence_count
    )

    print(
        "\n===== TOP 10 WORDS ====="
    )

    for word, count in frequency.most_common(10):

        print(
            f"{word} : {count}"
        )

    keyword = input(
        "\nEnter Keyword To Search: "
    ).lower()

    if keyword in content.lower():

        print(
            "Keyword Found"
        )

    else:

        print(
            "Keyword Not Found"
        )

    with open(
        "report.txt",
        "w",
        encoding="utf-8"
    ) as report:

        report.write(
            "TEXT ANALYSIS REPORT\n\n"
        )

        report.write(
            f"Word Count: {word_count}\n"
        )

        report.write(
            f"Character Count: {char_count}\n"
        )

        report.write(
            f"Line Count: {line_count}\n"
        )

        report.write(
            f"Sentence Count: {sentence_count}\n\n"
        )

        report.write(
            "TOP WORDS\n"
        )

        for word, count in frequency.most_common(10):

            report.write(
                f"{word} : {count}\n"
            )

    df = pd.DataFrame(
        frequency.items(),
        columns=[
            "Word",
            "Frequency"
        ]
    )

    df.to_csv(
        "word_frequency.csv",
        index=False
    )

    print(
        "\nReport Generated Successfully"
    )

    print(
        "CSV Export Completed"
    )

    log_activity(
        "Text Analysis Completed"
    )

except FileNotFoundError:

    print(
        "File Not Found"
    )

except Exception as e:

    print(
        "Error:",
        e
    )