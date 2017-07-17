-----------------------------------Inside the postgres container----------------------- 
psql -U postgres

Terminal

create database twitter WITH OWNER=postgres;



CREATE TABLE chivas (
id SERIAL PRIMARY KEY, 
tweet_id BIGINT NOT NULL, 
text VARCHAR NOT NULL, 
screen_name VARCHAR NOT NULL, 
author_id BIGINT, 
created_at VARCHAR NOT NULL, 
followers_count INT NULL,
inserted_at TIMESTAMP NOT NULL)

-----------------------para correr el contendedor kafka-----------------------------


sudo docker run -p 2182:2181 -p 9092:9092 --env ADVERTISED_HOST=127.0.0.1 --env ADVERTISED_PORT=9092 spotify/kafka


sudo docker exec -it 6a50aa8e1a81 bash


checar si se debe inicar antes el topic.
para iniciar el consumer: 

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning

------------para correr el docker postgres-----------------------
 sudo docker exec -it mypostgres2 bash

psql -U postgres


archivo para extraer tweets:
 extrayendo_tuis.py en carpeta: /home/administradorcito/app_twitter_kafka

comando y archivo par enviar de kafka a postgres
python3.5 TWTR-psql2.py 

en la carpeta del proyecto.


-------------------Expresiones regulares----------------------------
Table 9-16. Regular Expression Quantifiers
Quantifier 	Matches
* 	a sequence of 0 or more matches of the atom
+ 	a sequence of 1 or more matches of the atom
? 	a sequence of 0 or 1 matches of the atom
{m} 	a sequence of exactly m matches of the atom
{m,} 	a sequence of m or more matches of the atom
{m,n} 	a sequence of m through n (inclusive) matches of the atom; m cannot exceed n
*? 	non-greedy version of *
+? 	non-greedy version of +
?? 	non-greedy version of ?
{m}? 	non-greedy version of {m}
{m,}? 	non-greedy version of {m,}
{m,n}? 	non-greedy version of {m,n}


Table 9-17. Regular Expression Constraints
Constraint 	Description
^ 	matches at the beginning of the string
$ 	matches at the end of the string
(?=re) 	positive lookahead matches at any point where a substring matching re begins (AREs only)
(?!re) 	negative lookahead matches at any point where no substring matching re begins (AREs only)
(?<=re) 	positive lookbehind matches at any point where a substring matching re ends (AREs only)
(?<!re) 	negative lookbehind matches at any point where no substring matching re ends (AREs only)






select * from chivas where followers_count::text LIKE '8%'; 






