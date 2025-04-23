# Search Problems
- agent: entity that perceives its environment and acts upon that environment. A car representation in Google Maps. The IA or human moving the tiles in the 15 puzzle.
  
- state: a configuration of the agent and its environment. The starting position of the car and the whole map. The tiles arrangement in the beginning and after each tile move in 15 puzzle.

- initial state: the state in which the agent begins.

- actions: choices that can be made in a state. Function ACTIONS(s) returns the set of actions that can be executed in state s. In 15 puzzle, Actions of s will be the possible tile moves.

- transition model: a description of what state results from performing any applicable actions in any state. Function RESULTS(s, a) returns the state resulting from performing action a in state s.

- state space: the set of all states reachable from the initial state by any sequence of actions. In 15 puzzle it will be the diagram of all possible states connected, starting from the initial state. We'll get a state connected with the other possible states derived from it, and so on. It could be represented as a graph, where each node is a state and arrows connecting the states.

- goal state: way to determine whether a given state is a goal state. In Driving Directions In 15 puzzle, 1,2,3,4,5...15

- path cost function: numerical cost associated with a given path. Map -> shortest path, or cheaper, or faster. In 15 puzzle, number of moves (intermediate states from initial to goal state)

- solution: a sequence of actions that leads from the initial state to a goal state.
- optimal solution: a solution that has the lowest path cost among all solutions.

## node: 
a data structure that keeps track of
  - a state
  - a parent (node that generated this node)
  - an action (actions applied to parent to get node)
  - a path cost (from initial state to node)

## Approach:
- Start with a *frontier* that contains the initial state. A frontier includes all possible states that immediately follows the initial state.
- Repeat:
  - If the *frontier* is empty then no solution (no way to get to the goal)
  -  Remove a node from the frontier.
  -  If *node* contains *goal state*, return the solution.
  -  Otherwise expand node, add resulting nodes to the frontier.
  
**What could go wrong?**
_If we have bidirectional arrows between nodes we could get into an infinite loop. To avoid this we have to keep track of visited states, so we don't repeat them._
## Revised Approach:
- Start with a *frontier* that contains the initial state. A frontier includes all possible states that immediately follows the initial state.
- __Start with an empty explored set__
- Repeat:
  - If the *frontier* is empty then no solution (no way to get to the goal)
  -  Remove a node from the frontier.
  -  If *node* contains *goal state*, return the solution.
  -  __Add the node to the explored state.__
  -  Otherwise expand node, add resulting nodes to the frontier __if they aren't already in the frontier or the explored set.__

## depth-first search
search algorithm that always expands the deepest node in the frontier
the frontier is a stack fi-lo data structure

## breadth-first search
search algorithm that always expands the shallowest node in the frontier
the frontier is a queue fi-fo data structure