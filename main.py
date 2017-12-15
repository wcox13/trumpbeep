from util import *
from time import sleep
import sys

def main():
    print

    # connect to twitter API
    api = get_api()
    if not api:
        print "Error: Twitter authorization failed"
        return

    # get user objects
    usernames = parse_input(sys.argv)
    users = []
    if not usernames:
        print 'Usage: python main.py user1 [user2, user3, ...]'
        return
    for username in usernames:
        user = get_user(api, username)
        if user:
            users.append(user)
        else:
            print "Could not find user \"" + username + "\", skipping..."

    # notify and quit if no users found
    if not users:
        print "Error: no users to follow!"
        return

    # keep track of most recent tweets
    tweet_ids = {}
    for user in users:
        tweet_ids[user.name] = most_recent_tweet(user).id

    # print message and start loop
    msg = 'Tracking ' + ', '.join([user.name for user in users]) + '...'
    print msg
    print 'Press ctrl-C to quit'

    while True:
        for user in users:
            tweet = most_recent_tweet(user)

            # check if the tweet is new
            if tweet.id != tweet_ids[user.name]:
                play_alarm()
                print_tweet(user.name, tweet.text)

        sleep(15)

if __name__ == "__main__":
    main()
