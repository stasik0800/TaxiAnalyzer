# TaxiAnalyzer


documentation :
This project have two components 
1) python service that gets path with csv file and generete 2 csv file with data based on output path
2) python executed tasks over mysql:8.0.17 db on localhost (127.0.0.1:3306)
  * preLoad : taxi_zone_lookup.csv lookup table located in /Data .
    before user provide input path , python loaded lookup table and clean it.
 

connection.py	
tasks.py
reader.py	
main.py	
/data/taxi_zone_lookup.csv

bashFiles:
setEnv	
execApp

environment 
docker-compose.yml
requirements.txt

installation:
* extract project to dir
* change the permissions to allow the script to be executable for the user.
chmod +x setEnv	
chmod +x execApp	

then run bash
1) ./setEnv
it create python3 venv and installing pakages  (requirements.txt)
then it will build mysql image and run it.
when you will note message in cli [Server] X Plugin ready for connections.

then execute 
2)./execApp
input path "yellow_tripdata_2018-01Small.csv" file
then provide output path


