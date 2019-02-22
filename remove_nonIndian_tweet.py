

import pandas as pd
import wikipedia
import ast
import nltk
from tweepy import Cursor
from twitter_auth import get_twitter_client
client = get_twitter_client()

def read_csv():
    #DataFrame = pd.read_csv("Content_Extract.csv")
    DataFrame = pd.read_csv("Before_Remove_Indian1.csv")
    return DataFrame


def get_all_country():
    country = list(map(lambda x: x.strip("\n").strip().lower(), open("countries.txt").readlines()))
    return country

def word_tokenizer(summary,country):
    summary = summary.lower()

    tokens = nltk.word_tokenize(summary)
    #print ("Rahul::::"  ,tokens)
    other_country = set(tokens) & set(country)
    return other_country


def wiki_search(keyword):
    search_keywords = wikipedia.search(keyword)[0:3]
    print ("Search- Keyword:::" , search_keywords)
    summary = ''
    for search in search_keywords:
        s1 = ''
        try:

            s1= wikipedia.summary(search, sentences=2)
            summary += s1
        except:
            pass
    return summary

def get_location(metaData):
    user_mentions_dict = metaData['user_mentions']
    flag = True
    if user_mentions_dict:
        print (user_mentions_dict)
        user_Flag = []
        for user_dict in user_mentions_dict:
            user = user_dict['screen_name']
            print ("user:::", user)
            for page in Cursor(client.user_timeline , screen_name= user,count=1).pages(1):
                print ('======================='*20)
                for status in page[:1]:
                    location =  status._json["user"]['location']
                    if location:
                        location = location.split(",")
                        if len(location)>1:
                            location = location[-2] +" " +location[-1]
                        else:
                            location = location[0]

                        print ("location:::", location)
                        location_txt = ''
                        try:
                            location_txt = wikipedia.summary(location, sentences=2)
                            location_txt = location_txt.lower()
                        except:
                            pass
                        if len(location_txt)<2:
                            continue

                        if 'india'  in location_txt:
                            flag = True
                            print ("Flag::" , flag)
                            user_Flag.append(flag)
                        else:
                            flag = False
                            print ("Flag::" , flag)
                            user_Flag.append(flag)


        if False in user_Flag:
            return False
        else:
            return True
    else:
        return flag





def mainHandler(DataFrame):
#def mainHandler():
    all_data = []
    country = get_all_country()
    client = get_twitter_client()
    #DataFrame = read_csv()
    for index , row in DataFrame.iterrows():
        Date = row["Date"]
        text = row["text"]
        matched_keyword = row["keyword"]


        other_country1  = word_tokenizer(text,country)
        if other_country1:
            print ("other_country1::::::::::", text)
            continue

        metaData = ast.literal_eval(row["MetaData"])
        location_Flag = get_location(metaData)
        #print ("location_Flag::::",location_Flag)
        hash_tags =metaData["hashtags"]
        hash_Flag = []
        for hash_dict in hash_tags:
            keyword = hash_dict['text']
            #print (text)
            #print ('-----------------------------------------------------')
            summary = ''
            try:
                summary = wikipedia.summary(keyword, sentences=2)
            except:
                #print ("keyword not present", keyword)
                summary  = wiki_search(keyword)
                #pass
            other_country = word_tokenizer(summary,country)
            if other_country:
                hash_Flag.append('T')
            else:
                hash_Flag.append('F')

        #print (hash_Flag)
        if 'T' in hash_Flag and location_Flag == False:
            print ('Not Indian Statement...')
            continue
        elif location_Flag == False:
            print ('Not Indian Statement...')
            continue

        elif 'T' in hash_Flag:
            print ('Not Indian Statement...')
            continue
        else:
            all_data.append([Date,text,matched_keyword])
            print ("Indian Statement....")

        print ('------------------------------------------')
    print (all_data)
    return (all_data)


#mainHandler()

#print (get_location({}))
