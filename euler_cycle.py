# Algorithm finds the Euler's cycle in a graph

def dfs(G, s, E, pointers):
    for i in range(len(G[s])):
        if (G[s][i][1] == 0):
            G[s][i][1] = 1

            for j in range(len(G[G[s][i][0]])):
                if G[G[s][i][0]][j][0] == s:
                    G[G[s][i][0]][j][1] = 1
                    break
            
            pointers[s] = i + 1
            dfs(G, G[s][i][0], E, pointers)
    
    E.append(s)

def euler(G):
    n = len(G)
    E = []
    pointers = [0] * n

    for i in range(n):
        for j in range(len(G[i])):
            G[i][j] = [G[i][j], 0]

    dfs(G, 0, E, pointers)
    return E
