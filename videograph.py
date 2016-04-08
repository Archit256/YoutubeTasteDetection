import networkx as nx
import matplotlib.pyplot as plt
import csv
import re

G=nx.Graph()

hashmap1={}
hashmap2={}


with open('scores.csv', 'rb') as csvfile:
   reader = csv.reader(csvfile)
   i=0;
   for row in reader:
       line= re.split('@#@',str(row[0]))
       if len(line) == 4:
           videoIDUser = line[3]+'@#@'+line[0]
           score = int(line[1])
           if videoIDUser in hashmap1:
               score=int(score)+int(hashmap1[videoIDUser])   
           hashmap1[videoIDUser]=score

   
   for key in hashmap1:
       videoid = re.split('@#@',key)[0]
       username = re.split('@#@',key)[1]
       score = hashmap1[key]
       newvalue = username+'@#@'+str(score)
       if videoid in hashmap2:
           userscorelist = hashmap2[videoid]
       else:
           userscorelist = []
       userscorelist.append(newvalue)
       hashmap2[videoid] = userscorelist 
     

G.add_nodes_from(hashmap2.keys(),nodetype='videoid')

for videoid in hashmap2:
    for value in hashmap2[videoid]:
        username = re.split('@#@',value)[0]
        score = re.split('@#@',value)[1]
        G.add_node(username,nodetype="userid")
        G.add_edge(videoid,username,weight=int(score))

print len(G.edges())

nx.draw(G)
plt.savefig("graph.png")





