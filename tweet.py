import tweepy
import time
import random

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def newunfollow():
    unfrndlist = []
    for user in tweepy.Cursor(api.friends, screen_name='princemalik2000').items(20):
        john = user.screen_name
        try:
            frndstatus = api.show_friendship(source_screen_name=john, target_screen_name='princemalik2000')
            time.sleep(10)
            if frndstatus[0].following is True:
                pass
            elif frndstatus[0].following is False:
                unfrndlist.append(john)
            else:
                pass
        except:
            pass
    time.sleep(100)
    for i in range(0, len(unfrndlist)):
        try:
            api.destroy_friendship(unfrndlist[i])
        except:
            pass
        time.sleep(20)

def tweetfunc():
    status = "This is a Tweet."
    api.update_status(status)

def main():
    hashtag_list = ["#follow4follow", "#followback", "#f4f", "#teamfollowback"]
    search = (random.choice(hashtag_list))
    numberofTweets = 20
    for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
        try:
            usrfrd = tweet.user.screen_name
            api.create_friendship(usrfrd)
            loadedlist.append(usrfrd)
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def finalfunct():
    print("COMMANDS: follow; unfollow")
    text = input("Enter function>>")
    type(text)
    if text == "follow":
        for i in range(0, 20):
            main()
            time.sleep(20)
    elif text == "unfollow":
        for i in range(0, 2):
            newunfollow()
            time.sleep(100)
    else:
        print("Invalid Command!")

while True:
    finalfunct()
