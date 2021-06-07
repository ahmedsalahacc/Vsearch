# Vsearch
 Visualize AI search strategies including DFS, BFS, UCS, A*, and Greedy Search
 
 ### How to use:
  1. Left-click on the mouse to place a node on the screen, nodes have auto labelling mechanism that works alphabitically
  2. After you finish drawing two nodes, right click on the mouse on the nodes that you desire to connect. The first click is clicked on the "From" node and the second click is on the "To" node
  3. You will find the edges added in the edges drop down where you can add weights to edges and then press "add weight" to add the weight on the canvas
  4. You will also find a heuristics drop down where you can enter the heuristics of each node. This is not required as the system will automatically workk with the manhattan distance for you as a heuristic for each node
  5. specify the start node (single) and the end nodes (one or many), after choosing each end node click add to add them on the canvas 
  7. Now te final step, is to choose the serach algorithm that you want and then press search!

  After the search is done, a text will appear under the search button stating the path and the total cost.
  Under this text there are two buttons "<" and "<<", use "<" to visualize the search path of the algorithm, and use "<<" to visualize the final path.
  
  You need not to repeat the drawing process each time you want to a visualize different algorithm or a different path, just change what you want to change directly and leave the rest to us!
  
### Architecture Used
![architecture](images docs/Architecture.png?raw=true)
