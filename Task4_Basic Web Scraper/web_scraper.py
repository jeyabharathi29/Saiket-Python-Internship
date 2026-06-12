import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

LOG_FILE = "scraper_log.txt"


def log_activity(action):

    with open(LOG_FILE, "a") as log:

        log.write(
            f"{datetime.now()} - {action}\n"
        )


def scrape_headlines():

    try:

        url = "https://news.ycombinator.com/"

        response = requests.get(url)

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        headlines = []

        for item in soup.select(
            ".titleline a"
        ):

            headlines.append(
                item.text.strip()
            )

        if len(headlines) == 0:

            print(
                "No Headlines Found"
            )

            return

        print(
            "\n===== TOP HEADLINES =====\n"
        )

        for i, headline in enumerate(
            headlines,
            start=1
        ):

            print(
                f"{i}. {headline}"
            )

        df = pd.DataFrame(
            headlines,
            columns=["Headline"]
        )

        df["Scraped_Time"] = datetime.now()

        df.to_csv(
            "headlines.csv",
            index=False
        )

        with open(
            "headlines.txt",
            "w",
            encoding="utf-8"
        ) as file:

            for headline in headlines:

                file.write(
                    headline + "\n"
                )

        print(
            "\nData Saved Successfully"
        )

        print(
            "Total Headlines:",
            len(headlines)
        )

        log_activity(
            f"Scraped {len(headlines)} Headlines"
        )

        keyword_search(
            headlines
        )

    except requests.exceptions.RequestException:

        print(
            "Network Error"
        )

    except Exception as e:

        print(
            "Error:",
            e
        )


def keyword_search(headlines):

    print(
        "\n===== SEARCH HEADLINES ====="
    )

    keyword = input(
        "Enter Keyword: "
    )

    results = []

    for headline in headlines:

        if keyword.lower() in headline.lower():

            results.append(
                headline
            )

    print(
        "\n===== RESULTS ====="
    )

    if len(results) > 0:

        for item in results:

            print(item)

    else:

        print(
            "No Matching Headlines Found"
        )

    log_activity(
        f"Keyword Search: {keyword}"
    )


while True:

    print("\n==============================")
    print(" ADVANCED WEB SCRAPER ")
    print("==============================")

    print("1. Scrape News Headlines")
    print("2. Exit")

    choice = input(
        "Enter Choice: "
    )

    if choice == "1":

        scrape_headlines()

    elif choice == "2":

        print(
            "Thank You!"
        )

        break

    else:

        print(
            "Invalid Choice"
        )