# TaxiAnalyzer

This project have two components 
1) Docker image mysql:8.0.17 db on localhost (127.0.0.1:3306)
2) Python service that gets path with csv file and generete 2 csv file with data based on output path
  * preLoad : taxi_zone_lookup.csv lookup table located in /Data .
    before user provide input path , python loaded lookup table and clean it.

## installation:

* extract project to dir
* change the permissions to allow the script to be executable for the user.
```bash
chmod +x setEnv	
chmod +x execApp
```

then run bash
``` ./setEnv  ```
it create python3 venv and installing pakages  (requirements.txt)
### wait till docker  build mysql-service. when you will note message in cli 

### [Server] X Plugin ready for connections.

then execute bash
``` ./execApp  ```

input path "yellow_tripdata_2018-01Small.csv" file
then provide output path


