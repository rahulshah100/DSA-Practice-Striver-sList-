# https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1#

# Given an undirected graph and an integer M. The task is to determine if the graph can be colored with at most M colors such that no two adjacent vertices of the graph are colored with the same color. Here coloring of a graph means the assignment of colors to all vertices. Print 1 if it is possible to colour vertices and 0 otherwise.

# Example 1:
# Input:
# N = 4
# M = 3
# E = 5
# Edges[] = {(0,1),(1,2),(2,3),(3,0),(0,2)}
# Output: 1
# Explanation: It is possible to colour the
# given graph using 3 colours.

# Example 2:
# Input:
# N = 3
# M = 2
# E = 3
# Edges[] = {(0,1),(1,2),(0,2)}
# Output: 0

# Your Task: Your task is to complete the function graphColoring() which takes the 2d-array graph[], the number of colours and the number of nodes as inputs and returns true if answer exists otherwise false. 1 is printed if the returned value is true, 0 otherwise. The printing is done by the driver's code.
# Note: In Example there are Edges not the graph.Graph will be like, if there is an edge between vertex X and vertex Y graph[] will contain 1 at graph[X-1][Y-1], else 0. In 2d-array graph[ ], nodes are 0-based indexed, i.e. from 0 to N-1.Function will be contain 2-D graph not the edges.

# Expected Time Complexity: O(MN).
# Expected Auxiliary Space: O(N).

# Constraints:
# 1 ≤ N ≤ 20
# 1 ≤ E ≤ (N*(N-1))/2
# 1 ≤ M ≤ N
# ----------------------------------------------------------------------------------------------------------------------------------------
# Approach1: If we see graph we are given all the items as edges of corresponding items i.e. at 0th index, we have for Vertex 0 all it's edges. We can create a colors array to keep track of what color we allocate to each vertex. This colors array would be defined with all 0s at the start while for a given k, we'll assume 1 to range(k+1) as possible colors. Now in a helper function, we'll start checking for vertexes in graph, starting with vertex-0 if any of the allowed color is possible. To validate color we'll check color if for that vertex for all it's edges i.e. where in graph we've 1 for that subarray, whether those indexes/items in colors array have the same color stored. If color is not validated, next color is checked and at the end a 0 returned that solution not found. If color is found we'll mark the allocated color to this index/vertex in colors array and go to next vertex in graph. Thus while backtracking when a color didnt work and we're retracing to previous vertexes, we'll change back colors array to 0 for that entry. If color has been validated for all vertex then for base case of currentVertex == V, we return 1 and during this backtrack we check if the function call returned 1 and if so, we'll from there on return 1.
def graphColoring(graph, k, V):
    return helperfunc(0, [0 for i in range(V)], graph, k, V)

def helperfunc(currV, colors, graph, k, V):
    if currV==V:
        return 1

    for i in range(1, k+1):
        if possibleColor(currV, i, colors, graph, k, V):
            colors[currV] = i
            if helperfunc(currV + 1, colors, graph, k, V):
                return 1
            colors[currV] = 0
    return 0

def possibleColor(currV, color, colors, graph, k, V):
    for i in range(V):
        if graph[currV][i]==1 and colors[i]==color:
            return False
    return True


graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
print(graphColoring(graph, 3, 4))
# TC: O(n + m^(n^2)) Explanation: n time to create colors array initially. Further, each vertex can at max be ran for m for-loop iterations and in each iteration it calls next function which will further run for m times. Hence, m*m*m... n times is case here. Now for each helperfunc call we are also calling possibleColor which takes n time hence and there being n such iteration in helperfunc for a given node n*n + n*n + ... for m times is case here which is m^(n^2)
# SC: O(2n) Explanation: Recursive stack space of n at max and n space of colors Array