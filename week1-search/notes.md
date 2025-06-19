# Search
## Search Algorithm  
### Classical Search
#### Uninformed Search
A search strategy that uses no problem-specific knowledge.
##### DFS (Depth-First Search)
A search algorithm that always expands the **deepest** node in the frontier.
It uses a **stack** data structure -- last in, first out.
*Note: It is possible that DFS might not find the optimal solution.*
##### BFS (Breadth-Frist Search)
A search algorithm that always expands the **shallowest** node in the frontier.
It uses a **queue** data structure -- first in, first out.
#### Informed Search
A search stratrgy that uses problem-specifc knowledge.
##### Greedy Best-First Search
A search algorithm that expands the node that is closet to the goal, as estimated by a heuristic function h(n). 
- Heuristic funtion is also called Manhatten distance, where the heuristic is how many squares vertically and horizontally to get from each of these cells to the goal, or in short terms, the geographical distance to the goal.
![Greedy Best-First Search](./images/GreedyBestFirstSearch.JPG)
*Note: The search algorithm is not going to know for sure whether it is the closest thing to the goal, it is just esimating. So how good is the heuristic is, is going to affect how good this algorithm is.*
##### A* Search
A search algorithm that expands node with lowest value of g(n) + h(n), wherein,
g(n) = cost that has already been taken to the current node,
h(n) = estimated cost to goal.
![A* Search](./images/ASearch.JPG)

### Adversarial Search
#### Minimax
One player wants to minimise the game, while the other wants to maximise.
![Minimax](./images/MiniMax.JPG)
Pseudocode:
- Given a status s:
 - MAX picks action *a* in ACTIONS(s) that produces **highest** value of MIN-VALUE(RESULT(s,a))
 - MIN picks action *a* in ACTIONS(s) that produces **smallest** value of MAX-VALUE(RESULT(s,a)) 
 #### Alpha-Beta Pruning - Optimization to Minimax
 ![Alpha-Beta Pruning](./images/AlphaBetaPruning.JPG)
 #### Depth-Limited Minimax 
 The original Minimax is depth-unlimited until we get to the end of the game. While depth-limited minimax is going to stop and not consider additional moves that might come after certain movements ahead.
