import praw
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

# Check for required environment variables
required_vars = ["REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET", "REDDIT_USERNAME", "REDDIT_PASSWORD"]
missing_vars = [var for var in required_vars if not os.getenv(var)]

if missing_vars:
    print(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
    print("Please check your .env file or environment variables.")
    exit(1)

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=f"daily DayZ post bot by u/{os.getenv('REDDIT_USERNAME')}",
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

def send_discord_notification(reddit_url):
    """Send notification to Discord webhook with the Reddit post link"""
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    
    if not webhook_url:
        print("⚠️ Discord webhook URL not found in environment variables")
        return False
    
    # Create Discord embed message
    embed = {
        "title": "🎯 New Reddit Post Published!",
        "description": f"A new STALKER Classic server post has been published on r/{SUBREDDIT}",
        "url": reddit_url,
        "color": 0x00ff00,  # Green color
        "fields": [
            {
                "name": "📍 Subreddit",
                "value": f"r/{SUBREDDIT}",
                "inline": True
            },
            {
                "name": "🔗 Post Link",
                "value": f"[Click here to view]({reddit_url})",
                "inline": True
            }
        ],
        "footer": {
            "text": "STALKER Classic Reddit Bot"
        }
    }
    
    payload = {
        "embeds": [embed]
    }
    
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        print(f"✅ Discord notification sent successfully")
        return True
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to send Discord notification: {e}")
        return False

def test_webhook():
    """Test Discord webhook by sending the latest Reddit post link"""
    print("🔍 Testing Discord webhook with latest post...")
    
    subreddit = reddit.subreddit(SUBREDDIT)
    
    # Get the latest post from the subreddit that matches our title or username
    latest_post = None
    for submission in subreddit.new(limit=50):  # Check last 50 posts
        if (POST_TITLE in submission.title or 
            submission.author and submission.author.name == os.getenv("REDDIT_USERNAME")):
            latest_post = submission
            break
    
    if latest_post:
        print(f"📍 Found latest post: {latest_post.title}")
        print(f"🔗 URL: {latest_post.url}")
        send_discord_notification(latest_post.url)
    else:
        print("❌ No matching posts found to test with")

def post_daily():
    subreddit = reddit.subreddit(SUBREDDIT)
    submission = subreddit.submit(title=POST_TITLE, selftext=POST_BODY)
    submission.mod.sfw()
    print(f"✅ post output: {submission.url}")
    
    # Send Discord notification
    send_discord_notification(submission.url)

if __name__ == "__main__":
    import sys
    
    # Check if test mode is requested
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_webhook()
    else:
        post_daily()
