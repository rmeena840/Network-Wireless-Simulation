INT_MAX=9223372036854775807
import networkx as nx
import math
import queue

def distance(pt_1, pt_2):
    #pt_1 = np.array((pt_1[0], pt_1[1]))
    #pt_2 = np.array((pt_2[0], pt_2[1]))
    d=math.sqrt(abs(math.pow((pt_1[0]-pt_2[0]),2)+math.pow((pt_1[1]-pt_2[1]),2)))
    #return np.linalg.norm(pt_1-pt_2)
    return(math.ceil(d))
    ############
   
def minDistance(dist,vis):
    min=INT_MAX
    min_index=0
    for i in range(len(dist)):
        if vis[i]==0 and dist[i]<=min:
            min=dist[i]
            min_index=i
    return min_index

def shortestdistance(graph,src,dest):
   dist = []
   vis = []
   for i in range(len(graph)):
          dist.append(INT_MAX)
          vis.append(0)
   dist[src]=0
   for i in range(len(graph)-1):
       u=minDistance(dist,vis)
       vis[u]=1
       for v in range(len(graph)):
           if vis[v]==0 and graph[u][v] and dist[u]!=INT_MAX and dist[u]+graph[u][v]<dist[v]:
               dist[v]=dist[u]+graph[u][v]               
   return dist[dest]
   
def minHops(graph,src,dest):    
    vis=[]
    level=[]
    q=queue.Queue()
    for i in range(len(graph)):
        vis.append(0)
        level.append(0)
    level[src]=0
    vis[src]=1
    q.put(src)
    while q.empty()==0:
        p=q.get()
        for i in range(len(graph)):
            if vis[i]==0 and graph[p][i] and graph[p][i] != math.inf :
                level[i]=level[p]+1;                
                q.put(i)
                vis[i]=1
 #   for i in range(len(graph)):
#        print(level[i])
    return(level[dest])

#code for Artifulation Point

visited=[]
disc=[]
low=[]
parent=[]
ap=[]
time = 0
children = 0

def APUtil(u,x,edge):
   global visited
   global disc
   global low
   global parent
   global ap  
   global time
   global children
   
   visited[u] = 1
   
   #Initialize discovery time and low value
   disc[u] = time+1
   low[u] = time+1
   
   time=time+1
 
   for i in range(x):
       if edge[u][i]==1:
           v = i
           #Applying DFS for the count of connected componenets
           if visited[v]==0:
                children=children+1
                parent[v] = u
                APUtil(v,x,edge)
                low[u]  = min(low[u], low[v])
                if parent[u] == None and children > 1:
                   ap[u] = 1
                if parent[u] != None and low[v] >= disc[u]:
                   ap[u] = 1
           elif v!=parent[u]:
                low[u]  = min(low[u], disc[v])
    

def articulaiotnPoint(x,edge):
    global visited
    global disc
    global low
    global parent
    global ap
    
    for i in range(x):
        parent.append(None)
        visited.append(0)
        ap.append(0)
        disc.append(0)
        low.append(0)

    for i in range(x):
        if visited[i] == 0:
            APUtil(i,x,edge)
 

    for i in range(x):
        if ap[i] == 1:
            print(i)


#code for articulation point ends here

#points=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18),(19,20),(21,22),(23,24),(25,26)]
points=[(59, 42),(43, 53),(43, 84),(70, 100),(103, 87),(138, 54),(112, 27),(48, 33),(65, 70),(84, 68),(96, 52),(77, 20),(71, 29),(73, 47),(68, 61),(46, 68),(68, 87),(101, 80),(104, 51),(118, 57),(110, 76),(90, 25),(125, 36),(94, 36),(87, 93),(446, 28),(408, 35),(387, 62),(405, 94),(439, 99),(461, 82),(477, 53),(459, 24),(407, 51),(403, 71),(424, 87),(452, 75),(472, 27),(437, 47),(449, 59),(451, 46),(411, 64),(420, 56),(432, 82),(447, 84),(436, 60),(423, 73),(465, 72),(465, 38),(427, 33),(147, 217),(136, 232),(146, 263),(170, 269),(195, 249),(189, 221),(160, 214),(149, 244),(162, 257),(180, 252),(178, 231),(152, 231),(149, 252),(164, 266),(178, 261),(165, 237),(176, 223),(189, 239),(166, 243),(170, 254),(139, 248),(142, 236),(168, 223),(175, 241),(158, 221),(319, 207),(285, 249),(315, 264),(329, 263),(357, 252),(358, 229),(332, 213),(321, 230),(305, 242),(316, 254),(345, 249),(345, 227),(327, 223),(322, 248),(305, 251),(332, 254),(322, 242),(346, 236),(358, 238),(336, 242),(339, 232),(353, 245),(339, 251),(347, 261),(346, 217),(33, 432),(27, 450),(44, 473),(80, 479),(88, 469),(90, 448),(59, 434),(49, 444),(56, 463),(79, 464),(72, 445),(55, 415),(35, 463),(59, 470),(73, 471),(79, 431),(44, 454),(58, 451),(37, 439),(53, 457),(66, 455),(84, 456),(46, 422),(61, 428),(45, 434),(426, 435),(369, 452),(378, 474),(401, 478),(426, 475),(437, 453),(411, 430),(385, 436),(378, 452),(403, 462),(411, 457),(399, 444),(393, 478),(409, 466),(393, 456),(393, 450),(413, 440),(416, 466),(385, 482),(380, 458),(372, 480),(391, 468),(395, 433),(374, 443),(424, 450)]

Range=30

x=[]
y=[]
x.extend([i[0] for i in points])
y.extend([i[1] for i in points])

G=nx.Graph()
for i in range(len(points)):
    G.add_node(i)

print(G.nodes())

dist=[ [ 0 for i in range(len(points)) ] for j in range(len(points)) ]
edge=[ [ 0 for i in range(len(points)) ] for j in range(len(points)) ]
for i in range(len(points)):
    for j in range(len(points)):
        if i!=j:
            pt_1=(points[i][0],points[i][1])
            pt_2=(points[j][0],points[j][1])
            d=distance(pt_1, pt_2)
            if d<Range:
                dist[i][j]=d
                G.add_edge(i, j)
                edge[i][j]=1
            else:
                dist[i][j]=math.inf

nx.draw_networkx(G)

src=0
dest=8

print("Shortest Distance between ",src,'and',dest,'=')
print(shortestdistance(dist,src,dest))

print("minimum Hops between ",src,'and',dest,'=')
minh=minHops(edge,src,dest)
print(minh)

print("Articulation Points:")
articulaiotnPoint(len(edge),edge)