import praw
import datetime
import pandas as pd

def get_latest_posts(limits):
    reddit = praw.Reddit(
        client_id="gK4gpkYtFvY1UMyGphPBzw",
        client_secret="KyeJsjXJpyYQZpLgbAXMuWQ8Wlgr3w",
        user_agent="reddit-stream"
    )
    subreddit = reddit.subreddit("MachineLearning")

    posts = []
    for post in subreddit.top(limit=limits):
        posts.append({
            "username": post.author.name if post.author else "deleted",
            "title": post.title,
            "upvotes": post.ups if hasattr(post, "ups") else 0,
            "downvotes": post.downs if hasattr(post, "downs") else "0",
            "num_comments": post.num_comments,
            "created_utc": datetime.datetime.fromtimestamp(post.created_utc),
        })

    df = pd.DataFrame(posts)
    df["created_utc"] = df["created_utc"].astype(str)

    return df
