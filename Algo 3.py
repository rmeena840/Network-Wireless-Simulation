T = [[0, 0, 1, 0,1], [0,0,1,1,0], [1, 1, 0,1,0 ], [0,1,1,0,0],[1,0,0,0,0]] #matrix graph

color=[]
m=3

for i in range(m):
    color.append([])
    
color[0].append(3)
color[0].append(5)
color[1].append(1)
color[1].append(4)
color[2].append(2)

f0=0 #number of conflicts before relocation (before failure of nodes)

#finding color of i and j 

for i in range(5):
    temp=T[i]
    color_of_i=0
    for j in range(len(color)):
        for z in range(len(color[j])):
            if color[j][z]==i+1:
                color_of_i=j+1
                break
#    print(color_of_i)
    color_of_j=0
    for j in range(len(temp)):
        if temp[j]==1:
            for z in range(m):
                for k in range(len(color[z])):
                    if color[z][k]==j+1:
                        color_of_j=z+1
                        break
            if color_of_i==color_of_j:
                f0=f0+1
#            print(f0)

L=[]

# Assuming 1st node is out of order


for i in range(len(T)):
    for j in range(len(T)):
        T[i][0]=0

for i in range(len(T)):
    for j in range(len(T)):
        T[0][j]=0

degree=[] #finding degree of nodes
for i in range(len(T)):
    temp=0
    for j in range(len(T)):
        temp=temp+T[i][j]
    degree.append(temp)

#print(degree)

L=[]

for i in range(len(degree)):
        temp=[]
        temp.append(degree[i])
        temp.append(i+1)
        if degree[i]!=0:    
            L.append(temp)

L.sort(reverse=True)
print(L)        
            
STOP=False
max_str=10
itr=1

color_of_nodes=[]

for i in range(len(T)):
    color_of_nodes.append(-1)


for i in range(m):
    for j in range(len(color[i])):
#        print(color[i][j]-1)
        color_of_nodes[color[i][j]-1]=i
        
color_of_nodes[0]=-1

print(color_of_nodes)
print(L)

TL=[]

while STOP==False and itr<max_str:
    
    if len(L)==0:
        break
    
    v=L[0][1]
    conflicts=0
    
    for i in range(m):
        if i!=color_of_nodes[v-1]:
            count=0
            for j in range(len(T[v-1])):
                if T[v-1][j]==1 and color_of_nodes[j]==i:
                    conflicts=conflicts+1
                    
    print(conflicts)
    if conflicts<=f0:
        break
    else:
        TL.append([v,color_of_nodes[v-1]])
        del L[0]
        itr=itr+1
        
for i in range(m):
    print("Node's of color: ",i+1)
    for j in range(len(color[i])):
        print(color[i][j])