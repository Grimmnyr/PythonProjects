import praw
import easygui as eg

r=praw.Reddit(user_agent='havok1988bot1')
user = r.get_redditor('havok1988')
print user
print user.link_karma
print user.comment_karma
usersubs = user.get_submitted()
for x in usersubs:
    print str(x) + '\n'
usercoms = user.get_comments()
for x in usercoms:
    print str(x) + '\n'

submissions = r.get_subreddit('NFL').get_top(limit  = 20)
submission = next(submissions)
submission.comments
for x in submissions:
    print str(x) + "\n"
    
newsearch = r.search("patriots", subreddit='NFL', sort='none', syntax='none',period='new')
for x in newsearch:
    print str(x) + "\n"
    

raw_input()