# xmas_tree.py
# format function to solve prog4 of midterm; uses centering flag concept.

h = int(input("Enter height of tree:"))
t = int(input("Enter ornament level"))

for n in range(0,h):
    if(n == h - t):
        orn = format('_$' * (n+1),'^'+ str(h*2))
        orn = orn[:-(t)] + ' '
        print(format(orn, '^'+ str(h*2-t)))
    else:
        print(format('_ ' * (n+1),'^'+ str(h*2)))
