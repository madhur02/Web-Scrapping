from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd



def read_csv_file():
    new_data = []
    #DataFrame = pd.read_csv("CNNnews18.csv")
    #DataFrame = pd.read_csv("sardesairajdeep.csv")
    #DataFrame = pd.read_csv("airnewsalerts.csv")
    #DataFrame = pd.read_csv("businessline.csv")
    DataFrame = pd.read_csv("FCLive.csv")

    for index , row in DataFrame.iterrows():
        date = row["Date"]
        line = row["text"]
        metaData = row["metaData"]

        if line.find('https://') != -1:
            try:
                start_index = line.find('https://')
                urls = line[start_index:]
                url = urls.split(" ")[-1]
                print (url)
                html = urlopen(url)
                content = html.read()
                soup = BeautifulSoup(content)
                text = soup.find("p",{"class":"TweetTextSize TweetTextSize--jumbo js-tweet-text tweet-text"}).text


                new_data.append([date,metaData,line,text])
            except:
                pass

        else:
            new_data.append([date,metaData,line,line])

    new_DataFrame = pd.DataFrame(new_data, columns = ["Date", "MetaData","raw_text", "text"])

    #new_DataFrame.to_csv("Content_Extract_CNN_news.csv")
    new_DataFrame.to_csv("Content_Extract_businessline.csv")



read_csv_file()
