
cd $(dirname `ls -l $0 |awk '{print $NF;}'`)/..
WK_DIR=`pwd`
CONF_FILE=$WK_DIR/configuration/configuration.conf
source $CONF_FILE
HIVE=`which hive`
table_name="${artist_play}"

hql="create external table if not exists ${artist_play}
(
        artist_id string,
        song_play_count int,
        song_plays_date string
)
row format delimited 
        fields terminated by ','
        lines terminated by '\n'
"
hive -e "$hql"

