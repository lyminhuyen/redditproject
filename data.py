import praw
import pandas as pd

# Replace these with your actual credentials
client_id = "gK4gpkYtFvY1UMyGphPBzw"
client_secret = "KyeJsjXJpyYQZpLgbAXMuWQ8Wlgr3w"
user_agent = "reddit data"

# Authenticate
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

# Target subreddit
subreddit = reddit.subreddit("MachineLearning")

# Collect posts
posts = []
for post in subreddit.hot(limit=100):  # Or use .new(limit=...), .top(limit=...)
    posts.append([post.title, post.selftext, post.score, post.num_comments, post.created_utc])

df = pd.DataFrame(posts, columns=["title", "body", "upvotes", "comments", "created_utc"])
df.to_csv("r_machinelearning_posts.csv", index=False)
#print("Saved 100 posts to r_machinelearning_posts.csv")
