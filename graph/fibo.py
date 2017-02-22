import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc

##sample code to deal with matplotlib

vectors = [(1,1), (-1,1), (-1,-1), (1,-1)]
angles = [270, 0, 90, 180]

box_colors = ["grey"]
quares = [{"origin":(0,0), "length":1},
           {"origin":(1,1), "length":1, "arc_origin":(0,1)},
           {"origin":(0,2), "length":2, "arc_origin":(0,0)},
           {"origin":(-2,0), "length":3, "arc_origin":(1,0)},
           {"origin":(1,-3), "length":5, "arc_origin":(1,2)},
           {"origin":(6,2), "length":8, "arc_origin":(-2,2)}]

for i, sq in enumerate(squares):
    if True:
        #draw the square
        #doc: http://matplotlib.org/api/artist_api.html#matplotlib.patches.Rectangle
        plt.gca().add_patch(Rectangle(
            sq["origin"],
            sq["length"]*vectors[i%len(vectors)][0],
            sq["length"]*vectors[i%len(vectors)][1],
            facecolor=box_colors[i%len(box_colors)]
            ))
    if "arc_origin" in sq:

        plt.gca().add_patch(Arc(
            sq["arc_origin"], #origin for the arc
            sq["length"]*2, #width
            sq["length"]*2, #length
            angle = angles[i%len(angles)], #rotation angle
            theta1 = 0,
            theta2 = 90,
            lw = 2
            ))

plt.axis([-3.5, 11, -3.5, 11])
plt.show()
