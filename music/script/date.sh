#!/bin/sh
v=272
for i in {0..59}
do
	date=`date -d "$(($v-$i)) days ago" +%Y%m%d`
	echo $date","$((182+$i))  >> /home/star/project/music/data/textx.txt
done
