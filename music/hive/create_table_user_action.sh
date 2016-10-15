#!/bin/sh

cd $(dirname `ls -l $0 |awk '{print $NF;}'`)/..
WK_DIR=`pwd`
CONF_FILE=$WK_DIR/configuration/configuration.conf
source $CONF_FILE
HIVE=`which hive`
table_name="${user_action}"

hsql="drop table if exists ${table_name}"
hive -e "$hsql"

hql="create external table if not exists ${table_name}
(
	user_id string,
	song_id string,
	gmt_create int,
	action_type string,
	Ds string
)
row format delimited 
	fields terminated by ','
	lines terminated by '\n'
	location '/data/music/action/'
"
hive -e "$hql"




