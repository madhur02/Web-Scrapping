# Web-Scrapping
Scrapping From twitter 
Getting Data from Twitter Streaming API

## Hardware Requirement:
•	200 GB Hard disk storage
•	4 GB RAM 
•	Quad core (Optional)

## Software Installation:
•	Anaconda 3.6
•	Tweepy: pip install tweepy
•	Urllib: pip install urllib
•	Beautiful Soup: pip install beautifulsoup4

## Twitter API
It is a tool that makes the interaction with computer programs and web services easy. Many web services provide APIs to developers to interact with their services and to access data in programmatic way.

## Limitation of API:
•	It has commercial licensing fees, Free for one month.
•	For a user/page we can extract maximum 3000 tweets.

## Step 1: How to Get the Twitter API Keys 
•	Create a twitter account if you do not already have one.
•	Go to https://apps.twitter.com/ and log in with your twitter credentials.
•	Click "Create New App".\n
•	Fill out the form, agree to the terms, and click "Create your Twitter application".
•	In the next page, click on "API keys" tab, and copy your "API key" and "API secret".
•	Scroll down and click "Create my access token and copy your "Access token" and "Access token secret".

## Step 2: Connecting to twitter Streaming API:
We will be using a Python library called Tweepy to connect to Twitter Streaming API. 
 
## Step 3: Get Home timeline:
First, we connect to twitter streaming using step 2, if you want your home timeline used below script and generated output file is “home_timeline.json”.
	    Output File
## Step 4: Get User timeline
Get_user_timeline data is dependent on twitter_auth file which we are generating in step 2. This file contains the authentication keys.
Run get_use_time_line.py script as pass the username( Newspaper name “livemint” ) through the command line argument. It’s will generate output file is “user_timeline_livemint.json”

Output File
## Step 5: Reading JSON Data:
The data home_timeline.json , user_timeline_livemint.json is in JSON format. We are converting JSON to CSV format by using below script.
    Output File
## Step 6: Extract the complete tweet text:
In the step 4 and 5 we are not getting complete tweet text (means they provided half of tweet and URL link), for complete tweet we are using below script, it runs on each tweet’s URL and extract complete text from the tweet. We are passing the input file that has been generated in step 5 to get_twitter_data.py. Here we are getting the complete tweet text data as an output (Content_Extract_livemint.csv) it contains (contain Date, tweet text, metadata, raw text).
    Output File
## Step 7: Analyze Indian tweet or News:
We will get all the tweet of a user or page in step 6. Then we find whether a tweet based on India or Not. We are using #(hash) tag and @(targeting keyword) to determine the location of the tweet. Here we are using the Wikipedia API and user location.
	 

