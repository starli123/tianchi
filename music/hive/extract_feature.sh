#!/bin/sh

cd $(dirname `ls -l $0 |awk '{print $NF;}'`)/..
WK_DIR=`pwd`
CONF_FILE=$WK_DIR/configuration/configuration.conf
source $CONF_FILE
user="${user_action}"
artist="${artist_song}"
play="${artist_play}"

hsql="insert overwrite table ${play}
	
	  select c.aid,count(c.type) ,from_unixtime(c.gmt,'yyyy-MM-dd') from
		(select b.artist_id as aid,a.gmt_create as gmt,a.action_type as type from
			(select * from ${user}) a 
			join
			(select * from ${artist}) b 
			on (a.song_id=b.song_id)
		)c where c.type=1 group by c.aid,from_unixtime(c.gmt,'yyyy-MM-dd')



"
echo "$hsql"
hive -e "$hsql"
