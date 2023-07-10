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
# Approach1: We'll use an external array- a colors array we'll keep track of current color for each vertex. It is initially filled with 0 meaning no-color. Further using a row-param specifying from which vertex on are we currently running the function for, we'd use a recursive function. This recursive function starting with a row=0 will iterate over all the rows/vertices of given graph. Within each iteration of row we'll run a nested for-loop which denotes the range of color. Hence under each vertex/row we'll check for all colors and if a color could be used, we'll update the colors array and make a new recursive call with row incremented. This helps in making sure that from hereon we go to picking further possible combination of colors for remaining vertices, alongside also ensuring if they dont click the current for-loop will run over this recursion with a new color for current vertex. Further in the new recursive call as a base condition we check if row received is equal to number of Vertices, as that's when execution has went beyond last row too and so we can safely say for all vertices we were able to find suitable colors. This is where we return True. As even one True suffices, coz we even if one particular arrangement of color could be used to color whole graph it answers the question and we return True, so now we'll further not want to explore any more possibility and exit all the recursive calls. For this, at first where the recursive call is made further to get out in case of True having been returned, we'll check the return value of the recursive call which if True, from here as well we return True. If the whole color for-loop gets over then under there we return False showing that with current colors picked we dont further find suitable options. Last thing, to check if color say colorK is suitable, we dwelve in graph's current Row/Vertice and wherever 1 is specified which shows an edge from current Vertice, we'll check in colors Array if the colorK is already found, in which case we return False, and if not through any connected edge if there is no clash of colors then we return True.
def graphColoring(graph, k, V):
    colors = [0 for i in range(V)]

    def helperFunc(row):
        if row == V: return True

        for currRow in range(row, V):  # For all vertices check
            for color in range(1, k + 1):  # We'll check all colors, if any could be useful
                if (coloringPossible(currRow, colors, color, graph, V)):
                    colors[row] = color
                    if helperFunc(row + 1) == True:
                        return True
                    colors[row] = 0
            return False  # We'll reach here only if no color did suit, or else we would have gone recursively in helperFunc and hit base condition

    return helperFunc(0)


def coloringPossible(row, colors, color, graph, V):
    for i in range(V): #Checking for current subArray (as per specified by row) that wherever it has edges, they dont have this color
        if graph[row][i] == 1 and colors[i]==color: return False
    return True


print(graphColoring([[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]], 3, 4))
# TC: O(n+((n^2)m)^n) Explanation: n time for creaing colors Array. In addition, helperFunc running a for-loop to iterate over n vertex. Each iteration further having a nested loop running over m color items. Each color item iteration further running a check over n vertex (as is in coloringPass). Further recursively calling same function with same complexity uptill n times in total. TC: n + { n(m(n.... n times => (((n^2)m)^n)}
# SC: O(2n) Explanation: Recursive stack space of n at max and n space of colors Array



# Approach2: Improvement to Approach1- We dont need to use a for-loop iterating over each node. Coz a row/vertex is already passed into that function, now we should only go to next node if current vertex could find a suitable color in which case the recursive call made is already taking it to next node. So no point in using a for-loop and running executions checking from say 2nd and 3rd vertex if from 1st vertex, wherein as we found suitable color we are putting recursive call and going to such next nodes, execution didnt take them.
"""
def graphColoring(graph, k, V):
    colors = [0 for i in range(V)]

    def helperFunc(row):
        if row == V: return True
 
        for color in range(1, k + 1): 
            if (coloringPossible(row, colors, color, graph, V)):
                colors[row] = color
                if helperFunc(row + 1) == True:
                    return True
                colors[row] = 0
        return False  

    return helperFunc(0)


def coloringPossible(row, colors, color, graph, V):
    for i in range(V): 
        if graph[row][i] == 1 and colors[i]==color: return False
    return True
"""
# TC: O(n+(n^2)m) Explanation: n time for recursion to take us through n calls before which base condition will be met or False will be returned. In each recursive call running a for loop to iterate over m color-items. Within each iteration of color item, running one more iteration of n to check in colors if a given color is not repeated within elements which has edge with current vertex (as is in coloringPossible)
# SC: O(2n)