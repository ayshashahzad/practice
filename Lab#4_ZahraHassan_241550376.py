#Name: Zahra Hassan
#Roll No.: 241550376

"""
Lab Task: 

For this lab you will be implementing A* (A Star Search) on a graph.
The picture of the graph can be found in assets directory.

For this lab you are provided with two helper classes.
One is for making a graph and the other one in an interface for Priority Queues.
You may open then these file, once opened you'll see descriptions for each function defined
and a testing code for the class in the main body. Kindly go through them to get comfortable 
with the functions

MAIN TASKS:

    1- Modify graph.py to have the ability to store heuristics
    2- Create a funciton 'get_h' in graph.py to get heuristic for a node : input will be a Node and output will be heuristic 
    3- Create the graph in graph.py to and check all the functions
    4- Implement A* function 

Your function should print the shortest path along with the cost of that path. 
A sample output is provided in the assests directory.
"""

# importing helper classes
from graph import Graph
from custom_queue import PriorityQueue

def a_star_search(graph, start_node, goal_node):
    """
    The function should take in the graph defined along with the
    start and goal nodes and print out the shorted path according 
    to the A* Search Algorithm.

    NOTE: print the path and cost

    :params graph: (Graph) defined graph
    :params start_node: (String) starting node from graphs
    :params goal_node: (String) goal node from the graph

    :return : None
    """
    
    queue = PriorityQueue()
    queue.insert(start_node, 0)

    # initialize dictionaries to keep track of visited nodes, their costs, and heuristics
    visited = {}
    visited[start_node] = None
    costs = {}
    costs[start_node] = 0
    f_values = {}
    f_values[start_node] = graph.get_h(start_node)

    while not queue.is_empty():
        # get the node with the lowest f-value from the queue
        current_node = queue.remove()[1]

        # check if the goal node has been reached
        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node)
                current_node = visited[current_node]
            # reverse the path to get the correct order
            path = path[::-1]
            # print the path and cost
            print(" -> ".join(path))
            print("Cost:", costs[goal_node])
            break

        # explore the neighbors of the current node
        for neighbor in graph.edges[current_node]:
            # calculate the cost to reach the neighbor from the current node
            cost = costs[current_node] + graph.weights[current_node + neighbor]
            # calculate the f-value of the neighbor
            f_value = cost + graph.get_h(neighbor)

            # if the neighbor has not been visited or the cost to reach it is lower than previous, update
            if neighbor not in costs or cost < costs[neighbor]:
                costs[neighbor] = cost
                f_values[neighbor] = f_value
                priority = f_value
                queue.insert(neighbor, priority)
                visited[neighbor] = current_node
            elif f_value < f_values[neighbor]:
                # if a better path to the neighbor is found, update
                f_values[neighbor] = f_value
                costs[neighbor] = cost
                queue.update(neighbor, priority)
                visited[neighbor] = current_node
	



if __name__ == "__main__":

    # Defining Graph
    graph = Graph()

    # setting up nodes and neighbours
    graph.edges = {'A':['B', 'C'],
                   'B':['C', 'E'],
                   'C':['G'],
                   'G':[],
                   'E':['G'],
                   'D':['B', 'E'],
                   'S':['A', 'D'],
                   }
    
    # setting up connection costs
    graph.weights = {
			    'AC':10, 'AB':5, 
                'BC':2, 'BE':1,
                'CG':4,
                'SA':3, 'SD':2,
                'DB':1, 'DE':4,
                'EG':3
			}
    # setting up heuristics
    graph.heuristics = {
                'A':9,
				'B':4,
				'C':2,
				'D':1,
				'E':3,
				'G':0,
				'S':7
			    }

    #Search
    a_star_search(graph,'S', 'G')
