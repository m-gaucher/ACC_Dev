# Lab 6
_Prepared for: CSC-119 Students_ /
_Prepared by: Marshall Gaucher_


**Due: 11/1/17 at 11:59 PM MT**

## Part 1: STQ From Textbook
STQ = Self-Test Questions

> :blue_book: Section 6.1.2: Questions 1, 2, 3, 4, 5, 6

> :blue_book: Section 6.2.6: Questions 1, 2, 3, 4, 6, 9

## Part 2: Objects
### Introduction
Recall from In Class Program 13 & 14, we learned about Objects and the Turtle module.

### Procedure

1. Create a maze (e.g. 2d list)
2. Prompt the user for a start location (e.g. startx, starty)
3. Prompt the user for an end location (e.g endx, endy)
4. Mark both of these locations inside your maze
5. Move your turtle to both of these locations on the window (use setposition() to get a visual)

  _(Note: For simplicity keep your points within the first quadrant (e.g. positive values only for x and y))_

6. Have your turtle walk the indexes of your maze on the window (e.g.
maze[0][0]…the_turtle.setposition(0,0)….etc)

  _(Note: You should notice the turtle iterate over quadrant 1 of your Turtle window)_

## Hints

```python
#create a 10x10 maze
maze = [[0] * 10 for i in range(10)]

#print the 2d maze
for row in maze:
  for column in row:
    print(column, end="")
  print(end="\n")
  
#mark a location in the maze
maze[0][0]=9
```
