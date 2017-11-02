# FF13-2-Time-Puzzle-Solver

# What does the time puzzle in game look like?
  A sample video could be found here: https://www.youtube.com/watch?v=Qtu1lGa6qto

# Input format
  Sample input:
    3 3 2 1 3 1 2
  Type all numbers clockwise (recommend starting from the 12-o-clock direction) to 
  the command line, then seperate them with space character. There is no edge case
  detect, so please be careful with input.
 
# Output format
  Sample output:
    Here is the result:
    3[0]
    1[3]
    2[2]
    3[4]
    3[1]
    1[5]
    2[6]
  The route start from node with index 0 and value 3, which is the right top node on your screen,
  then the next node will be the node with index 3 and value 1, and so on.
