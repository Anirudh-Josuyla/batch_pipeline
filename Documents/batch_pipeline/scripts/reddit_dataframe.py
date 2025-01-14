import praw
import pandas as pd

# Setup for Reddit API (use your credentials here)
client_id = 'pRY8QLRjec0ryuvLHjobLA'  # Your client_id
client_secret = 'VM-q0J-74lzyQ-VWxad41qjTGu-Vtg'  # Your client_secret
user_agent = 'my-reddit-script by /u/yourusername'  # Your user agent

# Initialize Reddit API client using praw
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

# Fetch posts from a specific subreddit
subreddit = reddit.subreddit('learnpython')  # You can change this to any subreddit
posts_data = []

# Limit to 10 most recent posts (you can change this)
for post in subreddit.new(limit=10):
    posts_data.append({
        'title': post.title,
        'upvotes': post.score,
        'comments': post.num_comments,
        'url': post.url
    })

# Convert the list of posts into a DataFrame
posts_df = pd.DataFrame(posts_data)

# Display the top 5 posts
print("Top 5 Reddit Posts:")
print(posts_df.head())

# Save the data to a CSV file
posts_df.to_csv('reddit_posts.csv', index=False)
print("Data saved to 'reddit_posts.csv'.")
