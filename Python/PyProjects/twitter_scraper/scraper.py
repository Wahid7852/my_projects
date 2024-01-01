from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv

# Configure the driver
chrome_options = Options()

# Initialize the driver
chrome_options.add_argument(
    "user-data-dir=C:/Users/wahid/AppData/Local/Google/Chrome/User Data/Profile 2")
driver = webdriver.Chrome(options=chrome_options)

# Scrape user's tweets using JavaScript


def scrape_tweets(username):
    url = f"https://twitter.com/{username}"
    driver.get(url)
    time.sleep(2)  # Allow the page to load

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Delay to allow more tweets to load
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height

    tweet_elements = driver.execute_script(
        'return Array.from(document.querySelectorAll("div[data-testid=cellInnerDiv]")).map(e => e.innerText);'
    )

    return tweet_elements


# Scrape user's followings using JavaScript
def scrape_followings(username):
    url = f"https://twitter.com/{username}/following"
    driver.get(url)
    time.sleep(3)  # Allow the page to load

    following_elements = driver.execute_script(
        'return Array.from(document.querySelectorAll("div[data-testid=\'UserCell\']")).map(e => e.innerText);'
    )
    return following_elements


if __name__ == "__main__":
    try:
        target_username = "divyachawla08"

        tweets = scrape_tweets(target_username)
        print(f"Tweets of {target_username}:\n")
        for tweet in tweets:
            print(tweet)

        followings = scrape_followings(target_username)
        print(f"\nFollowings of {target_username}:\n")
        for user in followings:
            print(user)

        # Write tweets and followings to CSV
        with open(f"{target_username}_tweets_followings.csv", "w", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Tweets", "Followings"])

            # Write tweets and followings in separate rows
            for tweet, following in zip(tweets, followings):
                csv_writer.writerow([tweet, following])

    finally:
        driver.quit()  # Close the browser when done
