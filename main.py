import praw
from dotenv import load_dotenv
import os

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="test script by u/" + os.getenv("REDDIT_USERNAME"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD")
)


SUBREDDIT = "test"
POST_TITLE = "Ez egy automatikus tesztposzt a Reddit API-val"
POST_BODY = "Ez csak teszt."


def post_test():
    subreddit = reddit.subreddit(SUBREDDIT)
    submission = subreddit.submit(title=POST_TITLE, selftext=POST_BODY)
    print(f"Sikeres posztolás: {submission.url}")


if __name__ == "__main__":
    post_test()
