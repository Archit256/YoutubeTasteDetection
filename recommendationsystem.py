import csv
import re
import networkx as nx
G=nx.Graph()
MG=nx.MultiGraph()

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


#Map the videos watches by each user and create a map
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
           MG.add_weighted_edges_from([(edge,friend,float(similarity))])
           similarityFriend = similarity+"@"+friend
           if edge in hashmap1:
             edgemaplist = hashmap1[edge]
           else:
             edgemaplist = []
           edgemaplist.append(similarityFriend)
           hashmap1[edge]=edgemaplist


print 'Number of nodes '+ str(MG.number_of_nodes())
print 'Number of edges '+ str(MG.number_of_edges())

uID = str(input("What's your user ID? "))

#for edgekey in hashmap1.keys():
moviesWatchedbyFriend=[]

friendsOfUser = MG.neighbors(uID)[1:100]

for friendId in friendsOfUser: #iterating over the friends list of each user
  if friendId in usermappinghashmap.keys():
    friendMappedName = usermappinghashmap[friendId]
    if friendMappedName in userMoviesWatchedMap.keys():
      moviesWatchedbyFriend.append(userMoviesWatchedMap[friendMappedName])
userVideoRecommendations[uID]=moviesWatchedbyFriend 


print userVideoRecommendations 




