# INPUT
# circle    : Object containing a tuple, giving the circle center's coordinates, and a scalar giving the radius
# allPoints : set of tuples giving all points

# RETURN
# nothing

import matplotlib.pyplot as plt

def draw(circle, allPoints):
    if circle is not None:
        x = []
        y = []
        for t in allPoints:
            x.append(t[0])
            y.append(t[1])
        plt.scatter(x, y, alpha=0.5)
        radius = circle[1]
        circleX = circle[0][0]
        circleY = circle[0][1]
        circle = plt.Circle((circleX, circleY), radius=radius, color='b', fill=False)
        plt.gca().add_patch(circle)
        plt.xlim(float(circleX)-float(radius)-1.0, float(circleX)+float(radius)+1.0)
        plt.ylim(float(circleY)-float(radius)-1.0, float(circleY)+float(radius)+1.0)
        plt.show()
