def check(colors,domain):
    global edges
    global nodeCount
    global indexedCount
    flag = 0
    
    count = 0
    node = indexedCount[count][1]
    i = 0
    while(1):
        print(i)
        i = i + 1
        
        adj = []
        #builds adjacency lists
        for e in edges:
            if(e[0] == node):
                adj.append(int(e[1]))
            if(e[1] == node):
                adj.append(int(e[0]))
      
        domainColor = 0
        for a in adj:
            if(int(colors[a]) == (colors[node])):
                #Infeasable
                #print("infeasable" , colors[node],domain[node])
                try:
                    colors[node] = int(domain[node][domainColor])
                except:
                    break
                #print(colors[node])
                
                if(domainColor + 1 > len(domain[node])):
                    domainColor = 0
                else:
                    domainColor = domainColor + 1
                
                continue
            else:
                #OK continue prune
                for a in adj:
                    try:
                        #pass
                        domain[a].remove(int(colors[node]))
                    except:
                        pass
        
        if(count + 1 >= nodeCount):
            if(flag == 0):
                count = 0
                flag = 1
            else:
                break
        else:
            count = count + 1
            node = indexedCount[count][1]
    
    return colors
