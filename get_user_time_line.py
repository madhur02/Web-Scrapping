import sys
import json
from tqdm import tqdm
from tweepy import Cursor
from twitter_auth import get_twitter_client


if __name__ == "__main__":

    user = sys.argv[1]
    client = get_twitter_client()

    fname = "user_timeline_{}.json".format(user)

    with open(fname, 'w') as f:
        for page in Cursor(client.user_timeline , screen_name= user).pages(1000):
            for status in tqdm(page):
                #print (status._json)
                f.write(json.dumps(status._json)+"\n")
