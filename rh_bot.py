
# coding: utf-8

# In[17]:

#!/usr/bin/python
import praw
import pdb
import re
import os

USER_AGENT = "Ray Hudson Comments 0.1"
REDDIT_USER = "RayHudson_Bot"
REDDIT_PASSWORD = "howellNJ123"

reddit = praw.Reddit(client_id='nkuwosr_k-wo_A',
                     client_secret='WpgZRQjG33qYvcf-OHUdSSuaGnA',
                     password='howellNJ123',
                     user_agent='testscript by /u/RayHudson_Bot',
                     username='RayHudson_Bot')
# and login
#reddit.login(REDDIT_USERNAME, REDDIT_PASS)

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# Get the top 5 values from our subreddit
subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=10):
    print(submission.title)

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search
        if re.search("messi", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply("MAGESTERIAL")
            print("Bot replying to : ", submission.title)

            # Store the current id into our list
            posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")


# In[ ]:



