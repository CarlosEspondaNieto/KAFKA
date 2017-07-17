import json

from tweepy.streaming import StreamListener

from tweepy import OAuthHandler

from tweepy import Stream

from textblob import TextBlob

from datetime import datetime

from elasticsearch import Elasticsearch

import sys

import re

from kafka import KafkaProducer



consumer_key = 'eoNnfr55ARmSAZnVi2AO80o6W'
consumer_secret = 'iU519fOBDJqHDW3akBMnfluiq5eL4M340xEKN1IwpGUu3vIdb0'                 
access_token = '2470414327-iz4wzcJGz1yAwfzfJHFSoNT4ekaa03k0QHRADc7'
access_secret ='mSI657zrv2y9CJPVQzVJ0yuAucB5MvBcnD9vhFrveldk1'

# importa la llaves y tokes de twitter



# se define la ip y puerto para la  conexion con elastic search.

producer = KafkaProducer(bootstrap_servers='10.110.70.134:9092')

#conexion = Elasticsearch(["localhost:9200"])



#funcion que realiza la limpieza del texto en los tweets 

"""def limpia(tweet):

        tweet = tweet.lower()

        tweet = tweet.encode('utf-8').decode('utf8')

#        tweet = tweet.replace('\n', '\t')

#        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',tweet)

        tweet = tweet.replace("http:\/\/","")

        tweet = tweet.replace("https:\/\/","")
        tweet = tweet.replace('\\"',"")
        tweet = tweet.replace("\\'","")

        tweet = tweet.replace("www.","")

        tweet = re.sub('[\s]+', ' ', tweet)

        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)

        tweet = tweet.strip('\'"')
        
#        tweet = re.sub(r'<.*?>', '', tweet)



        return tweet

"""

class TweetStream(StreamListener):

    

    def on_data(self, data):



        #try:

            """

            dict_data = json.loads(data)

            if dict_data["lang"] == 'es':

                tweet = TextBlob(dict_data["text"])

            else:

                    return



            # pasa el texto a la herramienta TextBlob

            tweet = TextBlob(dict_data["text"])



            # se determina el sentimiento(positivo, negativo o neutral)

            #if tweet.sentiment.polarity < 0:

            #    sentiment = "negative"

            #elif tweet.sentiment.polarity == 0:

            #    sentiment = "neutral"

            #else:

            #    sentiment = "positive"



            # se eliminan los ceros y se ordena el formato de la fecha, pasandola formato iso

            timestamp = datetime.strptime(dict_data["created_at"].replace("+0000 ",""), "%a %b %d %H:%M:%S %Y").isoformat()

            limpieza = limpia(data)

            bdata = bytes(data, 'utf-8')
            """

            producer.send('test', data)

            return True
            print(data)          

        #except:



            # Manda un mensaje de error, si existe alguna exepcion e imprime el tweet que genera error

        #    print("processing exception")

            #print(data)

            #print("errror")



            return True



    # en caso de error imprime el estatus

    def on_error(self, status):

        print(status)
        return True



#if __name__ == '__main__':



    # create una instancia stream listener

listener = TweetStream()



    # establecer keys/tokens

auth = OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)



    

stream = Stream(auth, listener)


arg1 = sys.argv[0]

    # search twitter for the keyword
stream.filter(track=['chivas'])









    