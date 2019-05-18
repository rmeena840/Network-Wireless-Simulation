T = [[0, 0, 1, 0,1], [0,0,1,1,0], [1, 1, 0,1,0 ], [0,1,1,0,0],[1,0,0,0,0]] #matrix graph
degree=[] #storing the degree on nodes
for i in range(5):
    temp=0
    for j in range(5):
        temp=temp+T[i][j]
    degree.append(temp)

degree_info=[]

#print(degree)

#storing degree and node value in degree_info
for i in range(len(degree)):
        temp=[]
        temp.append(degree[i])
        temp.append(i+1)
        degree_info.append(temp)
        
degree_info.sort(reverse=True) #sorting in descending order as per degree on nodes


#del degree_info[0]
#print(degree_info[0][1])


#Initializing varaibles
STOP=False
vertices=[]
color_mat=[]
m=3
color=[]

for i in range(m):
    color.append([])


first_occ=1
colored_array=[]

#Initially color of nodes is NULL
for i in range(len(T)):
    colored_array.append(0)

i=0

while STOP==False:
    v=degree_info[i][1] #node having highest degree
    
    #coloring the first node
    if first_occ==1:

        first_occ=0
        color[0].append(v)
        colored_array[v-1]=1 #node colored with smallest color ID
        
        
        for j in range(len(T[v-1])):
#            print(T[v-1][j])
            if T[v-1][j]==0 and v!=j+1:
                colored_array[j]=1
                color[0].append(j+1)
                for z in range(len(degree_info)):
#                    print(degree_info[z][1])
                    if degree_info[z][1]==j+1:
#                        print(degree_info[z][1])
                        del degree_info[z] #removing the node which is colored 
                        break
                break   
                
        
#        print(degree_info)
        del degree_info[0]

    #coloring unvisited nodes
    else:
        neigh=[]
        neigh.append(v)
        
        #finding neighbour of previous node
        for j in range(len(T[v-1])):
            if T[v-1][j]==1:     
                neigh.append(j+1)
                
        #coloring the neigbour of node with minimum color ID possible
        for j in range(m):
            flag=0
         
            if len(degree_info)==0:
                break
            if len(color[j])==0:
                color[j].append(v)
                del degree_info[0]
                break
            for z in range(len(color[j])):
                for q in range(len(neigh)):                    
                    if color[j][z]==neigh[q]:
                        flag=1                        
                        break
                if flag==1:
                    break
                else:
                    color[j].append(v)
                    del degree_info[0]
    if len(degree_info)==0:
        STOP=True
    

#printing the color of nodes
            
for a in range(m):
    print("Nodes colored by:",a+1)
    for b in range(len(color[a])):
        print(color[a][b])
    
          
    
        
            
    
        
        
