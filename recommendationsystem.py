import csv
import re


hashmap1={} #store user and their friends
usermappinghashmap={}
userMoviesWatchedMap={}
userVideoRecommendations={}

#Mapping user numbers (1...10) to actual user names
with open('user_list.csv', 'rb') as csvfile:
   reader = csv.reader(csvfile)
   for row in reader:
       if len(row) == 2:
          usernumber=row[0]
          useroriginal=row[1]
          usermappinghashmap[usernumber]=useroriginal


with open ('scores_with_videoids_top50000.csv','rb') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    userid=row[0]
    moviesWatchedByUser = re.split(';',row[3])
    userMoviesWatchedMap[userid]=moviesWatchedByUser


#mapping user to their friends using .. hash[u]=array(similarity_score@friend,..)
with open('edge_list.csv', 'rb') as csvfile:
   reader = csv.reader(csvfile)
   i=0;
   for row in reader:
       line= re.split(r'\t+',str(row[0]))
       if len(line) == 3:
       	   edge=line[0]
           friend = line[1]
           similarity = line[2]
           similarityFriend = similarity+"@"+friend
           if edge in hashmap1:
             edgemaplist = hashmap1[edge]
           else:
             edgemaplist = []
           edgemaplist.append(similarityFriend)
           hashmap1[edge]=edgemaplist


uID = str(input("What's your user ID? "))

#for edgekey in hashmap1.keys():
moviesWatchedbyFriend=[]

for friend in hashmap1[uID]: #iterating over the friends list of each user
  similarity = re.split('@',friend)[0]
  friendId = re.split('@',friend)[1]
  if friendId in usermappinghashmap.keys():
    friendMappedName = usermappinghashmap[friendId]
    if friendMappedName in userMoviesWatchedMap.keys():
      moviesWatchedbyFriend.append(userMoviesWatchedMap[friendMappedName])
userVideoRecommendations[uID]=moviesWatchedbyFriend 


print userVideoRecommendations 


