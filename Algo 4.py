#ID_Set=[[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]]]

points=[(122, 164),(132, 189),(159, 191),(216, 178),(207, 139),(168, 133),
             (138, 136),(163, 151),(185, 161),(180, 190),(123, 210),(153, 166),
             (146, 205),(182, 206),(199, 195),(200, 168),(192, 139),(215, 156),
             (174, 173),(136, 153),(230, 197),(257, 199),(266, 194),(285, 191),
             (292, 196),(298, 208),(301, 218),(284, 222),(267, 213),(279, 205),
             (263, 185),(281, 177),(301, 175),(325, 182),(330, 204),(293, 225),
             (321, 222),(307, 196),(313, 185),(317, 198),(301, 184),(230, 210),
             (224, 220),(221, 229),(218, 241),(221, 256),(235, 267),(238, 215),
             (252, 241),(251, 254),(242, 273),(240, 232),(226, 251),(217, 270),
             (223, 289),(234, 303),(244, 307),(263, 304),(263, 283),(251, 271)]

INT_MAX=9223372036854775807
import networkx as nx
import math

def distance(pt_1, pt_2):
    #pt_1 = np.array((pt_1[0], pt_1[1]))
    #pt_2 = np.array((pt_2[0], pt_2[1]))
    d=math.sqrt(abs(math.pow((pt_1[0]-pt_2[0]),2)+math.pow((pt_1[1]-pt_2[1]),2)))
    #return np.linalg.norm(pt_1-pt_2)
    return(math.ceil(d))
    ############
   
   

#code for Artifulation Point

visited=[]
disc=[]
low=[]
parent=[]
ap=[]
Art_points=[]
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
#            print(i)
            Art_points.append(i)


#code for articulation point ends here

#points=[(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18),(19,20),(21,22),(23,24),(25,26)]
#points=[(59, 42),(43, 53),(43, 84),(70, 100),(103, 87),(138, 54),(112, 27),(48, 33),(65, 70),(84, 68),(96, 52),(77, 20),(71, 29),(73, 47),(68, 61),(46, 68),(68, 87),(101, 80),(104, 51),(118, 57),(110, 76),(90, 25),(125, 36),(94, 36),(87, 93),(446, 28),(408, 35),(387, 62),(405, 94),(439, 99),(461, 82),(477, 53),(459, 24),(407, 51),(403, 71),(424, 87),(452, 75),(472, 27),(437, 47),(449, 59),(451, 46),(411, 64),(420, 56),(432, 82),(447, 84),(436, 60),(423, 73),(465, 72),(465, 38),(427, 33),(147, 217),(136, 232),(146, 263),(170, 269),(195, 249),(189, 221),(160, 214),(149, 244),(162, 257),(180, 252),(178, 231),(152, 231),(149, 252),(164, 266),(178, 261),(165, 237),(176, 223),(189, 239),(166, 243),(170, 254),(139, 248),(142, 236),(168, 223),(175, 241),(158, 221),(319, 207),(285, 249),(315, 264),(329, 263),(357, 252),(358, 229),(332, 213),(321, 230),(305, 242),(316, 254),(345, 249),(345, 227),(327, 223),(322, 248),(305, 251),(332, 254),(322, 242),(346, 236),(358, 238),(336, 242),(339, 232),(353, 245),(339, 251),(347, 261),(346, 217),(33, 432),(27, 450),(44, 473),(80, 479),(88, 469),(90, 448),(59, 434),(49, 444),(56, 463),(79, 464),(72, 445),(55, 415),(35, 463),(59, 470),(73, 471),(79, 431),(44, 454),(58, 451),(37, 439),(53, 457),(66, 455),(84, 456),(46, 422),(61, 428),(45, 434),(426, 435),(369, 452),(378, 474),(401, 478),(426, 475),(437, 453),(411, 430),(385, 436),(378, 452),(403, 462),(411, 457),(399, 444),(393, 478),(409, 466),(393, 456),(393, 450),(413, 440),(416, 466),(385, 482),(380, 458),(372, 480),(391, 468),(395, 433),(374, 443),(424, 450)]

Range=30 #range of nodes

x=[]
y=[]
x.extend([i[0] for i in points])
y.extend([i[1] for i in points])

G=nx.Graph()
for i in range(len(points)):
    G.add_node(i)

#print(G.nodes())

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

#nx.draw_networkx(G)



#print("Articulation Points:")
articulaiotnPoint(len(edge),edge)

art_point=Art_points[len(Art_points)-1]

print("Articulation Point:")
print(art_point)

slope=[]

ID_set=[]


#finding slopes of cluster, LB and RB of each cluster
for i in range(len(points)):
#    print((points[i][1]-points[20][1])/(points[i][0]-points[20][0]))
    k=points[i][0]-points[20][0]
    if k==0:
        k=k+0.001
    slope.append([(points[i][1]-points[20][1])/k,i])
    
    if i==19: #first cluster
        slope.sort(reverse=False)
#        print(slope)
        ID_set.append([[0,slope[len(slope)-1][1]],[0,15],[0,slope[0][1]]])
        slope.clear()
    
    if i==39: #second cluster
        slope.sort(reverse=False)
#        print(slope)
        ID_set.append([[1,slope[len(slope)-1][1]],[1,35],[1,slope[0][1]]])
        slope.clear()
        
    
    if i==59: #third cluster
        slope.sort(reverse=False)
#        print(slope)
        ID_set.append([[2,slope[len(slope)-1][1]],[2,55],[2,slope[0][1]]])
        slope.clear()
        break
      
#print(ID_set)

print("-----Before Rotation:\n")

#positions of nodes before rotation
for i in range(len(ID_set)):
    print("\nPoints in Sector: ",i+1)
    for j in range(len(ID_set[i])):
        print(points[ID_set[i][j][1]]) 

#Applying rotation algorithm

temp=ID_set[0][2][1]
for i in range(len(ID_set)):
    temp1=ID_set[(i+1)%(len(ID_set))][2][1]
    ID_set[(i+1)%(len(ID_set))][2][1]=temp
    temp=temp1
    
#print(ID_set)      
       
print("-----After Rotation:\n")

#position of nodes after rotation
for i in range(len(ID_set)):
    print("\nPoints in Sector: ",i+1)
    for j in range(len(ID_set[i])):
        print(points[ID_set[i][j][1]]) 
    


