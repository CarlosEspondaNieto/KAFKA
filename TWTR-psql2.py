import tweepy
import psycopg2
from kafka import KafkaConsumer as kc
import json
from kafka import KafkaProducer as kp
import re
# Tweepy API doc here: http://pythonhosted.org/tweepy/html/api.html
# psycopg2 API doc here: http://initd.org/psycopg/docs/

# Keys
#consumer_key = 'eoNnfr55ARmSAZnVi2AO80o6W'
#consumer_secret = 'iU519fOBDJqHDW3akBMnfluiq5eL4M340xEKN1IwpGUu3vIdb0'                 
#access_token = '2470414327-iz4wzcJGz1yAwfzfJHFSoNT4ekaa03k0QHRADc7'
#access_secret ='mSI657zrv2y9CJPVQzVJ0yuAucB5MvBcnD9vhFrveldk1'

# Twitter initialization
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_secret)
#api = tweepy.API(auth)

# Postgresql initialization
#Here is returned an object to let the connection

connection = psycopg2.connect("dbname=twitter host=10.110.70.134 user=postgres password=beeva2014 port=5433")
cursor = connection.cursor()   #Cursor is an python class that allows to execute PostgreSQL command in a database session. 
print("connection succesful")

consumer = kc('test')

producer = kp(bootstrap_servers='localhost:9092')
# The table schema: CREATE TABLE tweets (id SERIAL PRIMARY KEY, tweet_id BIGINT NOT NULL, text VARCHAR NOT NULL, screen_name VARCHAR NOT NULL, author_id INTEGER, created_at VARCHAR NOT NULL, inserted_at TIMESTAMP NOT NULL)

def limpia(tweet):
        tweet = tweet.encode('utf-8').decode('utf8')
        tweet = tweet.replace("\\\\u00c1","Á")
        tweet = tweet.replace("\\\\u00e1","á")
        tweet = tweet.replace("\\\\u00c9","É")
        tweet = tweet.replace("\\\\u00e9","é")
        tweet = tweet.replace("\\\\u00cd","Í")
        tweet = tweet.replace("\\\\u00ed","í")
        tweet = tweet.replace("\\\\u00d3","Ó")
        tweet = tweet.replace("\\\\u00f3","ó")
        tweet = tweet.replace("\\\\u00da","Ú")
        tweet = tweet.replace("\\\\u00fa","ú")
        tweet = tweet.replace("\\\\u00d1","Ñ")
        tweet = tweet.replace("\\\\u00f1","ñ")
        tweet = tweet.replace("\\\\u00bf","¿")
        tweet = tweet.replace("\n"," ")
        


        return tweet

    #statuses = api.user_timeline(id="realDonaldTrump", count=10000)
    #statuses = api.user_timeline(api.get_user().screen_name, 'realDonaldTrump') #it's without the at at the begining.
for s in consumer:
    tuit = s.value
    try:
        res = str(s.value)[2:-1]
        res2 = limpia(res)
        #res2 = res.encode('utf-8').decode('utf8')
        dict_data = json.loads(res2)
        # To remove duplicate entries
        # See http://initd.org/psycopg/docs/faq.html for "not all arguments converted during string formatting"
        #cursor.execute("SELECT id FROM tweets_trump WHERE text = %s;", [s.text]) #este select comprueba que no haya una tweet igual
        #if cursor.rowcount == 0: #This read-only attribute (rowcount) specifies the number of rows that the last .execute*() produced (for DQL statements like 'select') or affected (for DML statements like 'update' or 'insert').
    
        cursor.execute("INSERT INTO chivas (tweet_id, text, screen_name, author_id, followers_count, created_at, inserted_at) VALUES (%s, %s, %s, %s, %s, %s, current_timestamp);", (dict_data["id"], dict_data["text"], dict_data["user"]["screen_name"], dict_data["user"]["id"], dict_data["user"]["followers_count"], dict_data["created_at"]))
        print("exito")
        connection.commit()

    except tweepy.error.TweepError:
        print("Whoops, could not fetch news!")
    except: # UnicodeEncodeError:
        pass
#finally:
cursor.close()
connection.close()



#notes: checar mandarlo a kafka usando parte del script anterior (checar el modulo kafka-python) y despues, usando la clase cursor enviarlo de kafka
#a postgres 

#http://initd.org/psycopg/docs/cursor.html
