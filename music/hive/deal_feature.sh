#!/bin/sh

cd $(dirname `ls -l $0 |awk '{print $NF;}'`)/..
WK_DIR=`pwd`


#hsql="select distinct(artist_id) from artist_play"

#hive -e "$hsql" >> /home/star/project/music/data/artist.csv

hsql="select artist_id,song_play_count,datediff(cast(song_plays_date as date),'2015-03-01') x from artist_play sort by x "

hive -e "$hsql">>  /home/star/project/music/data/11.csv

