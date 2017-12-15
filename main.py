from util import *
from time import sleep
import sys

def main():
    print "\ninitializing..."

    # connect to twitter API
    api = get_api()
    if not api:
        print "Error: Twitter authorization failed"
        return

    # get user objects
    usernames = parse_input(sys.argv)
    users = {}
    if not usernames:
        print 'Usage: python main.py user1 [user2, user3, ...]'
        return
    for username in usernames:
        user = get_user(api, username)
        if user:
            users[username] = user
        else:
            print "Could not find user \"" + username + "\", skipping..."

    # notify and quit if no users found
    if not users:
        print "Error: no users to follow!"
        return

    # keep track of most recent tweets
    tweet_ids = {}
    for user in users.values():
        tweet_ids[user.name] = most_recent_tweet(user).id

    # print message and start loop
    msg = 'Tracking ' + ', '.join(users.keys()) + '...'
    print msg
    print 'Press ctrl-C to quit'

    while True:
        for username, user in users.iteritems():
            try:
                tweet = most_recent_tweet(user)
            except:

                # restart API in case of timeout
                print 'Error getting most recent tweet. Retrying...'
                api = get_api()
                for username in usernames:
                    users[username] = get_user(api, username)
                sleep(5)
                continue

            # check if the tweet is new
            if tweet.id != tweet_ids[user.name]:
                print_tweet(user.name, tweet.text)
                play_alarm()
		tweet_ids[user.name] = tweet.id

        sleep(15)

if __name__ == "__main__":
    main()
