#!/bin/bash

database='tutorial'
val=1
cd /usr/local/Cellar/postgresql\@10/10.12/bin/
while :
do
  ./psql -U 'postgres' -d $database -c "INSERT INTO test_mytable values (now(), 'idrac-$val', random());"
  echo "Inserted host": $val;
  val=$(($val+1))
done
