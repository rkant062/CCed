#!/bin/bash

database = "postgres"
val = 0
cd /usr/local/Cellar/postgresql\@10/10.12/bin/
while :
do
  ./psql -U 'postgres' -d 'tutorial' -c "INSERT INTO test_mytable values (now(), 'iDRAC', random());"
  echo "Inserted host ".$val;
done
