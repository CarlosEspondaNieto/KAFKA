
CREATE TABLE bitcoin (
id SERIAL PRIMARY KEY, 
tweet_id BIGINT NOT NULL, 
text VARCHAR NOT NULL, 
screen_name VARCHAR NOT NULL, 
author_id BIGINT, 
created_at VARCHAR NOT NULL, 
inserted_at TIMESTAMP NOT NULL,
followers_count INT NULL,
tweet_place_type VARCHAR NULL,
tweet_place_name VARCHAR NULL, 
tweet_country VARCHAR NULL)
cursor.execute
("INSERT INTO chivas (tweet_id, text, screen_name, author_id, created_at, followers_count, tweet_place_type, tweet_place_name, tweet_country, inserted_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, current_timestamp);", (dict_data["id"], dict_data["text"], dict_data["user"]["screen_name"], dict_data["user"]["id"], dict_data["user"]["followers_count"], dict_data["place"]["place_type"], dict_data["place"]["full_name"], dict_data["place"]["country"], dict_data["created_at"]))
        cursor.execute("INSERT INTO chivas (tweet_id, text, screen_name, author_id, followers_count, tweet_place_type, tweet_place_name, tweet_country, created_at, inserted_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, current_timestamp);", (dict_data["id"], dict_data["text"], dict_data["user"]["screen_name"], dict_data["user"]["id"], dict_data["user"]["followers_count"], dict_data["place"]["place_type"], dict_data["place"]["full_name"], dict_data["place"]["country"], dict_data["created_at"]))


---------------Queries_----------------

# seleccionar el ultimo registro
#el que tenga mas de 200 followers y ordenarlos por screen_name
# los que empiecen con la letra b, traer solo los primeros 3
SELECT text, regexp_matches(text, '^[b]') FROM chivas;
SELECT text, regexp_matches(text, '^[a-z]') FROM chivas LIMIT 3;
#los que terminen con la letra c, traer los ultimos 3
#los que tengan mas de 50 seguidores y menos de 100, ordenarlos por fecha de creación
#los que hayan sido creados entre las 6 y 10 d ela noche

#seleccionar los tweets que followers empieze con 8:
select * from chivas where followers_count::text LIKE '8%'; 
#que el campo texto tenga la palabra vergara
select * from chivas where text LIKE '%vergara%';
select * from chivas where text::text LIKE '%vergara%';

que tenga mas de mil seguidores

select * from chivas where followers_count:text LIKE '[0-9][0-9][0-9][0-9]'; 

#selecciona los primeros diez caractetes  del texto de los que tengan mas de 100 followers
select text, substring(text,1,10) from chivas where followers_count>100;

#selec the position of the string "vergara" in the text colummn 
select text, position('vergara' in text) "position of vergara" from chivas where substring(text, position('vergara' in text),7)='vergara';