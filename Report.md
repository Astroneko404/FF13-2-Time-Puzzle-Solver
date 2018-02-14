# A Test Report for FF13-2 Time Puzzle Solver

## Introduction
The time puzzle in Final Fantasy 13-2 is officially called "The Hands of Time". Players need to erase all number pads in the screen. Each time when a number pad is visited, one or two clock hand(s) will appear, pointing to the possible next number pads to visit. If both clock hands point to empty space, while there still exist other number pads in the field, it is time to retry the puzzle.

A sample video could be found [here](https://www.youtube.com/watch?v=Qtu1lGa6qto).

## How does this program work
This program will use dynamic programming to find a solution, and it will only print out the first solution found.
#### Input format
Here is a sample input:

3 3 2 1 3 1 2
  

Type all numbers clockwise (recommend starting from the 12-o-clock direction) to the command line, then seperate them with space character. There is no edge case detect, so please be careful with input.
 
#### Output format
Here is a sample output:

Here is the result:
 
3[0] 

1[3] 

2[2]

3[4]

3[1] 

1[5] 

2[6]
  
The route start from node with index 0 and value 3, which is the right top node on your screen, then the next node will be the node with index 3 and value 1, and so on.

//TODO
