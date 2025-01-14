import praw

# Set up the Reddit API client
reddit = praw.Reddit(
    client_id='pRY8QLRjec0ryuvLHjobLA',  # Your client_id
    client_secret='VM-q0J-74lzyQ-VWxad41qjTGu-Vtg',  # Your client_secret
    user_agent='my-reddit-script by /u/yourusername'  # Your user agent
)

# Example: Fetch posts from a subreddit (e.g., "python")
subreddit = reddit.subreddit('python')  # Replace 'python' with your desired subreddit

# Fetch the top 5 hot posts
for submission in subreddit.hot(limit=5):
    print(f"Title: {submission.title}")
    print(f"URL: {submission.url}")
    print(f"Score: {submission.score}")
    print(f"Posted by: {submission.author}")
    print("-" * 80)
