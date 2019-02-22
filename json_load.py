import pandas as pd
import json

#tweets_data_path = 'user_timeline_EconomicTimes.json'
tweets_data_path = 'user_timeline_CNNnews18.json'
tweets_data_path = 'user_timeline_sardesairajdeep.json'
tweets_data_path = 'user_timeline_airnewsalerts.json'
tweets_data_path = 'user_timeline_indianExpress.json'
tweets_data_path = 'user_timeline_FCLive.json'
tweets_data_path = 'user_timeline_moneycontrolcom.json'
tweets_data_path = 'user_timeline_forbes_india.json'
tweets_data_path = 'user_timeline_livemint.json'
tweets_data_path = 'user_timeline_BT_India.json'
tweets_data_path = 'user_timeline_businessline.json'
tweets_data_path = 'user_timeline_FCLive.json'
tweets_data = []
tweets_file = open(tweets_data_path, "r")


for line in tweets_file:
    #try:
    tweet = json.loads(line)
    #print (tweet.keys())
    created_at = tweet["created_at"]
    text       = tweet["text"]
    entities       = tweet["entities"]
    place       = tweet["place"]
    lang       = tweet["lang"]
    location       = tweet.get("user",{}).get("location","")
    #print (tweet["user"]['location'])
    #sys.exit()
    tweets_data.append([created_at,text,entities,place,lang,location])

#print (len(tweets_data))
tweets = pd.DataFrame(tweets_data)

#tweets.to_csv("CNNnews18.csv")
#tweets.to_csv("airnewsalerts.csv")
#tweets.to_csv("FCLive.csv")
#tweets.to_csv("livemint.csv")
#tweets.to_csv("businessline.csv")
tweets.to_csv("FCLive.csv")
