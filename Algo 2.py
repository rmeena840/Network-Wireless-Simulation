T = [[0, 1, 1, 0,1], [1,0,1,1,0], [1, 1, 0,0,0 ], [0,1,0,0,0],[1,0,0,0,0]] #matrix graph

color=[]
m=3 #number of colors

for i in range(m):
    color.append([])


#initialzing the color of some nodes
color[0].append(1)
color[0].append(4)
color[1].append(2)

uncolored_vertex=[3,5] #uncolored C0

TL=[] #Tabu list

#initializing the variables
max_itr=10 #maximum iteration=10
STOP=False
itr=1
ASP=0
i=0

while STOP==False and itr<max_itr: #checing if further coloring possible
    if len(uncolored_vertex)==0: #if no uncolored node left then break from loop
        break
    
    v=uncolored_vertex[0] #uncolored node
    del uncolored_vertex[0] #deleting from the list
    
    temp=T[v-1]
    conflicts=[]
    
    for i in range(m):
        count=0
        for j in range(len(temp)):
            for z in range(len(color[i])):
                if temp[j]==color[i][z]:
                    count=count+1
        conflicts.append([count,i+1]) #conflicts occuring if node is occured
    
    i=0
    min_conf=1000000
    color_id=0
    for i in range(len(conflicts)):
        if conflicts[i][0]<min_conf:
            min_conf=conflicts[i][0]
            color_id=i+1 #coloring the node if no conflicts found i.e nodes not having neighbour of same colors
    
    color[color_id-1].append(v)
    TL.append([v,0])
    
    if len(uncolored_vertex)==0:
        STOP=True
    itr=itr+1
    
i=0

#printing the color of nodes
for i in range(m):
    print("Node's of color: ",i+1)
    for j in range(len(color[i])):
        print(color[i][j])

