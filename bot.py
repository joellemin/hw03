import praw
import random
import datetime
import time
import os
import pprint
from textblob import TextBlob
#print(os.getcwd())


# FIXME:
# copy your generate_comment functions from the week_07 lab here
jnames = ['Joe Biden','Joe','Biden','Former VP','Former Vice President', 'Obamas BFF']
jname = random.choice(jnames)
praises = ['best','greatest', 'finest', 'prime', 'top']
praise = random.choice(praises)
bepress = ['live in the White House', 'lead the country', 'reside at 1600 Pennsylvania Avenue', 'be Commander in Chief','represent the United States']
bepres = random.choice(bepress)
restorethecountrys = ['restore the country', 'save us', 'reestablish the US', 'rehabilitate the United States', 'save the country' ]
restorethecountry = random.choice(restorethecountrys)
chaoss = ['chaos', 'insanity', 'havoc', 'mayhem', 'pandemonium']
chaos = random.choice(chaoss)
roles = ['candidate', 'contender', 'possible leader', 'chance', 'deal']
role = random.choice(roles)
environments = ['environment', 'ecosystem', 'future', 'our home', 'biosphere']
environment = random.choice(environments)
envplans = ['build 1.5 mil sustainable homes', 'create 1 million new jobs in the auto industry to boost electric vehicles', 'invest $2 trillion over four years in green areas','push the US towards a plan of net-zero carbon emissions by 2050','seek to rejoin the Paris climate accords']
envplan = random.choice(envplans)
press = ['commander in chief', 'US leader', 'president', 'chief', 'head of state']
pres = random.choice(press)
stuffs = ['free plants', 'social security', 'iPads', 'hats', 'ice cream']
stuff = random.choice(stuffs)
reps =  ['Republicans', 'The GOP', 'The right', 'Conservatives', 'Trump supporters']
rep = random.choice(reps)
posadjs = ['great', 'fun', 'exciting', 'noteworthy', 'grand']
posadj = random.choice(posadjs)
tnames = ['Trump', 'Donald', 'Donald Trump', 'Cheeto Man','The President']
tname = random.choice(tnames)
bads = ['terrible', 'inferior', 'substandard', 'crummy', 'abominable']
bad = random.choice(bads)
badtraits = ['temper', 'instability', 'character', 'personality', 'rudeness']
badtrait = random.choice(badtraits)
leaderbads = ['authoritarian','bad','harmful', 'dangerous', 'autocratic']
leaderbad = random.choice(leaderbads)
badactions = ['spewed lies', 'undermined women', 'enabled white supremacists', 'denied science','threatened law and order']
badaction = random.choice(badactions)
badroles = ['disgrace', 'dishonor', 'shame', 'tarnish', 'disappointment']
badrole = random.choice(badroles)
places = ['country', 'United States', 'nation', 'USA', 'US']
place = random.choice(places)
covids = ['COVID-19','the pandemic', 'COVID', 'coronavirus', 'SARS-CoV-2']
covid = random.choice(covids)
persons = ['person', 'human being', 'citizen', 'individual', 'man']
person = random.choice(persons)

def generate_comment_0():
    text = jname +' is the ' +praise+ ' candidate to ' +bepres+'. He will ' +restorethecountry+ ' from ' +chaos+'.'
   # print(text)
    return text

def generate_comment_1():
    text = jname + ' is the ' +praise+ ' ' +role+ ' for the ' +environment+'. He will ' +envplan+'.'
    #print(text)
    return text

def generate_comment_2():
    text = jname + ' should be the ' +pres+ ' because he will give ' +stuff+ ' to everyone! ' +rep+ ' do not want these ' +posadj+ ' things.'
    #print(text)
    return text

def generate_comment_3():
    text = tname + ' is a ' +bad+ ' presidential ' +role+ ' because of his ' +badtrait+ '. His ' +leaderbad+ ' leadership will ruin the United States.'
    #print(text)
    return text

def generate_comment_4():
    text = tname + ' has ' +badaction+ ' throughout his presidency and is a ' +badrole+ ' to the ' +place+'. Also, he dealt with ' +covid+ ' terribly.' 
   # print(text)
    return text

def generate_comment_5():
    text = tname +' is not only a ' +bad+' ' +pres+ ' but also a bad ' +person+ '. During the debate, he was rude and created ' +chaos+ ' on stage.' 
   # print(text)
    return text

def generate_comment():
    '''
    This function should randomly select one of the 6 functions above,
    call that function, and return its result.
    '''
    num_comment = random.randint(0,5)
    if num_comment == 0:
        return generate_comment_0()
    if num_comment == 1:
        return generate_comment_1()
    if num_comment == 2:
        return generate_comment_2()
    if num_comment == 3:
        return generate_comment_3()
    if num_comment == 4:
        return generate_comment_4()
    if num_comment == 5:
        return generate_comment_5()
    
# connect to reddit 
reddit = praw.Reddit('bot1')

# connect to the debate thread
#reddit_debate_url = 'https://www.reddit.com/r/politics/comments/fuchj5/hi_rpolitics_im_lucy_diavolo_a_politics_editor_at/'
#reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jhb20w/2020_debate_thread/'
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jnnbfq/vermont_gov_phil_scott_becomes_first_incumbent/'
submission = reddit.submission(url=reddit_debate_url)

   # generate_comment()

while True:
# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once

#for i in range(1):

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('start sleep')
    time.sleep(5)
    print('end sleep')
    print('new iteration at: ', datetime.datetime.now())
    print('submission.title: ', submission.title)
    print('submission.url: ', submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    
    #all_comments = []
    #submission.comments.replace_more(limit = None)
    #for comment in submission.comments:
        #print(comment.body)
    all_comments = []
    print('Start')
    submission.comments.replace_more(limit=10)
    #print(submission_comments)
    print('End')
    all_comments = submission.comments.list()


    # HINT:
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    
    not_my_comments = []
    for c in submission.comments.list():
        if type(c) is praw.models.reddit.comment.Comment:
            #print(str(c.author))
            if str(c.author) != 'cs40joellebot':
                not_my_comments.append(c)

            else:
                continue
    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (you bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit
        # and the .reply() function to post it to reddit
        #try: 
        text = generate_comment() 
        submission.reply(text)
        print('Task 2 submission success')
        #try: 
        #submission.reply(text)
            #print('Task 2 submission success')
        #except:
            #print('Task 2 exception found')
            # print('starting to sleep')
            # time.sleep(5)
            # print('done sleeping')
    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        for c in not_my_comments:
            me = False
            for reply in not_my_comments:
                if str(reply.author) == 'cs40joellebot':
                    me = True
                    #not_my_comments.remove(c)
            #if me == True:
                #not_my_comments.remove(c)
            if me == False:
                comments_without_replies.append(c)
        print('len(comments_without_replies)=',len(comments_without_replies))
    
    # FIXME (task 4): randomly select a comment from the comments_without_replies list,
    # and reply to that comment
    # HINT:
    # use the generate_comment() function to create the text,
    # and the .reply() function to post it to reddit
    #try: 
        #op = reddit.comment(random.choice(comments_without_replies))
    try:
        op = random.choice(comments_without_replies)
        text = generate_comment() 
        #print(op.body, text)
        op.reply(text)
        print('task 4 random reply success')
    except: 
        print('taks 4 fail')
        time.sleep(5)


    # FIXME (task 5): select a new submission for the next iteration;
    #REPLY TO A DIFFERENT SUBMISSION INSTEAD OF THE ELECTION DEBATE THREAD
    # your newly selected submission should have a 50% chance of being the original submission
    # (url in the reddit_debate_url variable)
    # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
    # HINT: 
    # use random.random() for the 50% chance,
    # if the result is less than 0.5,
    # then create a submission just like is done at the top of this page;
    # otherwise, create a subreddit instance for the csci40 subreddit,
    # use the .top() command with appropriate parameters to get the list of all submissions,
    # then use random.choice to select one of the submissions
    try: 
        a = random.random()
        topc = []
        if a >= 0.5:
            print('Task 5 Top')
            for c in reddit.subreddit('csci040temp').top(time_filter='month'):
                topc.append(c)
            submission = random.choice(topc)
            print('submission =', submission)
            t = (submission.title)
            print('title =', t)
            time.sleep(5)
        else:
            comment = generate_comment()
            submission.reply(comment)
            #submission = reddit.submission(url=reddit_debate_url)
            #time.sleep(5)
    except:
        print('Task 5 Original exception found')
        print('starting to sleep')
        time.sleep(5)
        print('done sleeping')

"""
    biden = ['Biden','Joe Biden','Former VP']
    for comment in submission.comments.list():
        if biden in comment.body.lower():
            comment.upvote() 
            print('submission upvoted')
    
    trump = ['Trump', 'Donald Trump', 'President Trump']
    for comment in submission.comments.list():
        if trump in comment.body.lower():
            comment.downvote()
            print('submission downvoted')

    for submission in reddit.subreddit('csci040temp'):
        if 'biden' in submission: 
            submission.upvote()
        if 'trump' in submission:
            submission.downvote()
   
    for comment in submission.comments.list():
        blob = TextBlob(str(comment.body))
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        if trump in comment.body.lower() and polarity > 0.5:
            comment.upvote()
        if biden in comment.body.lower() and polarity > 0.5:
            comment.downvote()
        if trump in comment.body.lower() and subjectivity > 0:
            comment.upvote()
        if biden in comment.body.lower() and subjectivity > 0:
            comment.downvote()
"""