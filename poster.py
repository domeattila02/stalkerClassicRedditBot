import praw
import schedule
import time

reddit = praw.Reddit(
    client_id='0Zf62eJfJFqlc9bwknZ9WQ',
    client_secret='xFQgM10Qe0iCj3AgqtO828AEmiwWWw',
    user_agent='daily poster by Gangstalker',



)


SUBREDDIT = "test"
POST_TITLE = "Napi automatikus poszt"
POST_BODY = "TESZT TEESZT LOLL!!!"



def post_daily()
    subreddit = reddit.subreddit(SUBREDDIT)
    submissions = subreddit.submit(title=POST_TITLE, body=POST_BODY)
    print(f"postr elküldve komám: {submissions.url}")

schedule.every().day.at("09:00").do(post_daily)

while true:
    schedule.run_pending()
    time.sleep(60)