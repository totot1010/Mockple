#!/bin/bash

echo -n "user name:"
read uname 

while read line
do
  reponame=$uname"/"$line
  gh repo-delete $reponame
  echo "Delete "$reponame
done < delete_repo.txt