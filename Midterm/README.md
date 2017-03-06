Midterm Q1:

Analysis of data:

1. Using the sent_items folder, determined who has sent the highest number of emails along with the count.
2. Found the top 10 recipents of email sent by Kaminski-v
3. Did a bi-variant analysis on number of emails which were sent internally and externally by each individual and then generated a report on the same.
4. Details of Emails having keyword 'Report' or 'Off Books' in their email content


Midterm Q2:

I am collecting data from Article Search API and storing it under Article Search Data.
Since the limit is 120 pages at a time, I am collecting pages 0 to 120 at a time.

Once I have the required data I am storing it based on id under Article Search Data Storage. 
The id is unique for each article, this also helps in avoid duplication of data. 
I am creating a dictionary for all the releated json values and dumping it in a json file per id
All the analysis is done on this folder.


I am collecting data from Archive API.
While Collecting, I am storing data with year and month name which helps in not creating another method for storing data
Also I can automate the process by running it for each month and year till required year.
I have collected data for 2014-2017 and have done analysis on the same.


Analysis of data:

1. In the Archive API, I have found web-url of all articles which had keyword Photography and articles dated between 2015 to 2017. 
I have stored the results in a text file 


2. Generated a report based on various articles sources based on Article Search API such as The New York Times, AP, Reuters and Others. 
Created a pie-chart to understand contribution of each sources.

3. Created folders based on different types of articles - Review, Sports, News etc.
Then Determined the highest numbers of articles belong to which category.

4. A word count analysis to find the most common used word in 2015 from Archive API

