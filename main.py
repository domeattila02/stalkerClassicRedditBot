import praw
from dotenv import load_dotenv
import os

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="daily DayZ post bot by u/" + os.getenv("REDDIT_USERNAME"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD")
)

SUBREDDIT = "DayZServers"
POST_TITLE = "PC|UK|ExclusionZone|STALKER Classic - Hardcore Roleplay"
POST_BODY = """\
Stalker Classic is a freshly started Stalker RP server. Join now to be among the first stalkers who travel to the zone in order to conquer it and get rich! Or die like a dog? We will see... Good hunting, stalker!

**Max Players**: 100  
**IP**: 5.252.102.164  
**Restarts**: every 4 hours  
**Mods**: Stalker related mods, check the launcher for details!  
**Playstyle**: Hardcore Roleplay  
**1PP Only**

🌐 Website: [https://www.stalkerclassic.zone](https://www.stalkerclassic.zone)  
💬 Discord: [https://discord.com/invite/sclassic](https://discord.com/invite/sclassic)  
🎥 Launch trailer: [https://youtu.be/XF-BD4e2PWk?si=943aws95vnZu7Bgg](https://youtu.be/XF-BD4e2PWk?si=943aws95vnZu7Bgg)

**Whitelist required!** Join our Discord to get whitelisted and jump in!
"""
def post_daily():
    subreddit = reddit.subreddit(SUBREDDIT)
    submission = subreddit.submit(title=POST_TITLE, selftext=POST_BODY)
    submission.mod.sfw()
    print(f"✅ post output: {submission.url}")

if __name__ == "__main__":
    post_daily()
