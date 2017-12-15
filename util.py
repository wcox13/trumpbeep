import tweepy
from creds import *

def get_api():
    """
    Return an authenticated API object.
    """
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return tweepy.API(auth)
    except:
        return None

def get_user(api, username):
    """
    Get user, returning None if not found.
    """
    try:
        return api.get_user(username)
    except:
        return None

def parse_input(argv):
    """
    Get list of usernames from input.
    """
    if len(argv) > 1:
        usernames = []
        for i in range(1, len(argv)):
            usernames.append(argv[i])
        return usernames
    else:
        return None

def most_recent_tweet(user):
    """
    Get the most recent tweet of a given user.
    """
    return user.timeline(count=1)[0]

def play_alarm():
    """
    Sound a system alarm.
    """
    print "ALARM"

def print_tweet(username, text):
    """
    Print a new tweet message.
    """
    print 'NEW TWEET from @' + username + ': ' + text
