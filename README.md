# Research_Algo_Ex7

### Q1 - Runtime Comparison - q1.py

   This question is about understanding the difference of efficiency between 2 available algorithm aproaches;
        
        1. NumPy.
        2. CVXPY.
        
   The timing procedure made by using 'time' library and substracting the start timestamp from the end timestamp.
   Each library's algorithm is being applied on the same randomly created set of Coefficients.
   
   Times Graph:   
   ![image](https://user-images.githubusercontent.com/71274563/207470363-7e5b4aee-2fac-4914-92cf-6e037fba9833.png)

   
   By looking at the final plot of times, it is clear that for heavy equations numpy is exponentially faster than cvxpy.
    
### Q2 - Approximation Algorithms - q2.py
   This question is about testing the reliability of approximation algorithm.
   Specifically - The Maximum Clique algorithm, by 2 approaches:
        
        1. NetworkX's Bron and Kerbosch based algorithm for finding max clique. (find_clique)
        2. NetworkX's Approximations Algorithm. (max_clique)
    
   [find_clique](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.clique.find_cliques)
   
   [max_clique](https://networkx.org/documentation/networkx-1.10/reference/generated/networkx.algorithms.approximation.clique.max_clique.html#networkx.algorithms.approximation.clique.max_clique)
   
   
      

### Q3: CodinGame

![image](https://user-images.githubusercontent.com/71274563/207473451-04b549fa-2f1c-4a8f-a8f2-8a7612db1d64.png)


    import sys
    import math


    # Auto-generated code below aims at helping you parse
    # the standard input according to the problem statement.

    # w: width of the building.
    # h: height of the building.
    w, h = [int(i) for i in input().split()]
    n = int(input())  # maximum number of turns before game over.
    x0, y0 = [int(i) for i in input().split()]

    x, y = x0, y0

    x_area, y_area = range(w), range(h)


    def step(x0, y0, x, y, x_area, y_area, bomb_dir):
        # print(f'step: x0={x0}, y0={y0} x={x} y={y} bomb_dir={bomb_dir}')

        if len(x_area) != 1:
            if bomb_dir == "UNKNOWN":
                pass
            elif bomb_dir == "SAME":
                x_area = [i for i in x_area if abs(x0 - i) == abs(x - i)]
            elif bomb_dir == "WARMER":
                x_area = [i for i in x_area if abs(x0 - i) > abs(x - i)]
            else:
                x_area = [i for i in x_area if abs(x0 - i) < abs(x - i)]

        else:
            if bomb_dir == "UNKNOWN":
                pass
            elif bomb_dir == "SAME":
                y_area = [i for i in y_area if abs(y0 - i) == abs(y - i)]
            elif bomb_dir == "WARMER":
                y_area = [i for i in y_area if abs(y0 - i) > abs(y - i)]
            else:
                y_area = [i for i in y_area if abs(y0 - i) < abs(y - i)]

        return x_area, y_area


    # game loop
    while True:
        # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)
        bomb_dir = input()

        x_area, y_area = step(x0, y0, x, y, x_area, y_area, bomb_dir)

        x0, y0 = x, y

        if len(x_area) != 1:

            if (x0 == 0 and len(x_area) != w):
                x = (3*x_area[0] + x_area[-1]) // 2 - x0
            elif (x0 == w-1 and len(x_area) != w):
                x = (x_area[0] + 3*x_area[-1]) // 2 - x0
            else:
                x = x_area[0] + x_area[-1] - x0

            if x == x0:
                x += 1
            x = min(max(x, 0), w-1)

        else:
            if x != x_area[0]:
                x = x0 = x_area[0]
                print(x, y)
                bomb_dir = input()

            if len(y_area) == 1:
                y = y_area[0]

            else:
                if (y0 == 0 and len(y_area) != h):
                    y = (3*y_area[0] + y_area[-1])//2 - y0
                elif (y0 == h-1 and len(y_area) != h):
                    y = (y_area[0] + 3*y_area[-1])//2 - y0
                else:
                    y = y_area[0] + y_area[-1] - y0
                y = min(max(y, 0), h-1)

        print(x, y)
