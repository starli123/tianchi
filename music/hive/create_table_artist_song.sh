#!/bin/sh

cd $(dirname `ls -l $0 |awk '{print $NF;}'`)/..
WK_DIR=`pwd`
CONF_FILE=$WK_DIR/configuration/configuration.conf
source $CONF_FILE
HIVE=`which hive`
table_name="${artist_song}"

hql="create external table if not exists ${table_name}
(
	song_id string,
	artist_id string,
	pubish_time string,
	song_init_plays string,
	Language string,
	Gender string
)
row format delimited 
	fields terminated by ','
	lines terminated by '\n'
	location '/data/music/artist/'
"
hive -e "$hql"
