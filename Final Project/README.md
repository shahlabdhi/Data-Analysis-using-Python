Twitter Data Analysis on 'Snapchat'

![alt tag](https://cloud.githubusercontent.com/assets/24615819/25298919/da16a560-26c7-11e7-878a-a0ba798dca6d.png)

Collecting Data:

By first getting the required keys from twitter api, they are saved as environment variables.
The account is verified by passing the 4 keys which are : consumer key, consumer secret key, access token and access secret token.
Once the credential are verified a search word is taken for the query. 
I have collected all data for Snapchat.
Using the Search API url, the searchkeyword is passed.
I am storing the data in dictionary which helps in eliminating any duplicate data.
Once the data is stored in dictionary it is then dumped into a json file appended with unix timestamp.
This helps in maintaining unique file names.



Storing Data:

After all the files are collected, I read the data line by line and store all result in list. 
Once list is complete I create a dictionary to prevent any duplicate entries based on tweet_id.

After this is done, I dump the dictionary data into 1 json file.
So, now all analysis are done on this 1 file which contains all data.

Analysis 1:
This analysis gives most frequent tweeter of this topic along with its number of tweets. Also it finds the most influential user and time zone analysis of the top users
By iterating the user id present for each tweets, a dictionary is created for user id along with the number of unique tweets which he posted.

For each tweet present in the file, its retweet_count and user’s followers count is fetched. The product of these two generates the Influential value of the given tweet ID.
Once I have the data in dictionary I sort it using a list and then display Top 15 most Influential Tweet on this topic and analyzed the timezones for the corresponding users. 
This helps is knowing which user and from which part of the world is most influential.
A bar graph is plotted for all the timezones present and their corresponding count is noted.

![alt tag](https://cloud.githubusercontent.com/assets/24615819/25298922/e03cc672-26c7-11e7-8e23-9c010c96d099.png)


Analysis 2:
Sentimental Analysis on Stored Data
All the tweets present in the files are iterated one by one.
A dictionary is created to store the text part and sentiment of tweet.
To find the sentiment of the tweet first the tweet is cleaned i.e. all the hyperlinks and emoticons are removed from the tweet using simple regex and then we call TextBlob method present in textblob library to get TextBlob Object which helps in analyzing sentiment for the tweet.
Once we have the cleaned tweet text we check its sentiment polarity, if its greater than 0 that means its positive, if its equal to zero that means its neutral and if its less than 0 then it means its negative.
This data is then stored in the sentiment key of the dictionary for the tweet.
Once all the tweets sentiment is calculated, Percentage is calculated for each of the type: Positive, Negative and Neutral based on their sentiment type.
Along with percentage, the 10 positive and negative tweets are displayed.
A pie chart is created to understand the overall sentiment of tweets for the given data.

![alt tag](https://cloud.githubusercontent.com/assets/24615819/25298924/e4806a5e-26c7-11e7-92ef-89212e3f7f0a.png)

While doing this analysis I even developed a method to find sentimental analysis realtime using tweepy from python. In realtime we give the query word , I have executed for ‘Car’ and based on the 200 queries count the sentiment analysis is calculated.



Analysis 3:
Time Series Analysis of the data Stored.
Here I have done analysis of tweets on days of the week and what period of time were there highest number of tweets were tweeted by users.
A dictionary is initialized for the day which is divided into 4 periods- Morning, Afternoon, Evening, Night.
Here the day is divided on hour if hour is between 1 and 12 then its morning, if its between 12 and 16 then its afternoon, if its between 16 and 20 then its evening and if its between 20 and 1 then its night.
After reading the data from json file, I extract the field ‘created_at’. This field contains the day, date, time in utc format. 
So I extract the day of the week and hour of the day from ‘created_at’.
Once I have the day, I create a nested dictionary of the format{Day:{Hours_of_the_Day}}
I then convert this nested dictionary into pandas dataframe and rename columns and reset index and replace all NAN by 0.
Then I calculate its cumulative sum and plot it to find the tweets trend.

 ![alt tag](https://cloud.githubusercontent.com/assets/24615819/25298926/e90076a0-26c7-11e7-93b5-6cacdab9a6c0.png)


Analysis on number of tweets wrt time period is done by extracting the hour of the day from ‘created_at’ field and then storing in a dictionary which has keys based on time intervals – Morning, Afternoon, Evening and Night irrespective of the day

![alt tag](https://cloud.githubusercontent.com/assets/24615819/25298928/ee076b86-26c7-11e7-9162-1a5a2683a306.png)


Analysis on number of tweets with respect to day is done by extracting the day from ‘created_at’ field and then storing in a dictionary for each day.
A barchart is ploted using seaborn. 
![alt tag](https://cloud.githubusercontent.com/assets/24615819/25298931/f307fcb8-26c7-11e7-942c-40590b040590.png)

![alt tag](https://cloud.githubusercontent.com/assets/24615819/25298933/f6ed116a-26c7-11e7-952e-76750d13cf08.png)


Additional Libraries required:
Tweepy – pip install tweepy
TextBlob – pip install textblob
