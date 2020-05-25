operations = {
    'Q1': {"name": "top_tipping_zones",
           "query": """select Borough,Zone,sum(tip_amount) total_amt from {uploadedtbl} d
                            join {lookuptbl} l on d.DoLocationid= l.locationid
                            group by 1,2
                            order by 3 desc
                            limit 5;"""},

    'Q2': {"name": "longest_trips_per_day",
           "query": """select  dropoff_date,
                            tpep_dropoff_datetime ,
                            Borough,
                            Zone,
                            trip_distance
                                    from (
                                            select date(tpep_dropoff_datetime) as dropoff_date ,tpep_dropoff_datetime,trip_distance ,Borough,Zone,
                                            row_number() over (partition by date(tpep_dropoff_datetime)  order by  trip_distance desc) as ranks
                                            from {uploadedtbl} d
                                            join {lookuptbl} l on d.DoLocationid= l.locationid
                                            where tpep_dropoff_datetime between '2018-01-01' and '2018-01-08'
                                    ) a
                                    where ranks <=5
                                    order by 1 asc;"""}
}

