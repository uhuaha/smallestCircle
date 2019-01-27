### Method applying Welzl's algorithm for determining the smallest circle enclosing a finit set of points
#
# INPUT
# P : set of points to be enclosed (list of tuples)
# R : empty set of points (empty list)
#
# RETURN
# circle : Object containing a tuple, giving the circle center's coordinates, and a scalar giving the radius

import random
import math
from sympy.geometry import Point2D, Segment2D, Circle

def welzlAlgorithm(P, R):

    # if p is an empty list or r has >= 3 points
    if not P or len(R) >= 3:
        # P is empty, and smallest "circle" containing the one point of R has radius zero
        if len(R) == 1:
            P = R[0]
            circle = [P, 0]
            return circle
        # P is empty, and smallest circle containing the two points of R is centered at midpoint
        elif len(R) == 2:
            center = [(R[0][0]+R[1][0])/2, (R[0][1]+R[1][1])/2]
            diameter = math.sqrt(math.pow(R[1][0]-R[0][0], 2) + math.pow(R[1][1]-R[0][1], 2))
            circle = (center, diameter / 2)
            return circle
        # the points of R are cocircular, i.e., they are all on the same circle
        elif len(R) >= 3 and isCocircular(R):
            # Calculate circle center and radius
            p1 = Point2D([R[0][0], R[0][1]])
            p2 = Point2D([R[1][0], R[1][1]])
            p3 = Point2D([R[2][0], R[2][1]])
            center = calculateCircleCenter(p1, p2, p3)
            radius = p1.distance(center)
            circle = (center, radius)
            return circle
        else:
            return None
    else:
        # randomly and uniformly choose a point p from P and remove p from P
        randomInt = random.randint(0, len(P)-1)
        p = P[randomInt]
        P.remove(P.__getitem__(randomInt))

        D = welzlAlgorithm(P, R)
        if D is not None and pIsInsideCircle(p, D):
            return D
        else:
            R.append(p)
            return welzlAlgorithm(P, R)


### Method for checking a point is inside a given circle
#
# INPUT
# point     : tuple (x, y)
# circle    : Object defining the center of the circle and the radius: ((x, y), r)
#
# RETURN
# boolean   : False if the point is outside and True if the point is inside or on the border of the circle

def pIsInsideCircle(point, circle):
    radius = circle[1]
    distance = math.sqrt(math.pow(circle[0][0]-point[0], 2) + math.pow(circle[0][1]-point[1], 2))
    if distance > radius:
        return False
    else:
        return True


### Test if all points in R are on the same circle. All points are on the same circle if they have the same distance
### from the circle's center.
#
# INPUT
# R     : list of point tuples [(x, y), (x, y), ...]
#
# RETURN
# boolean   : False if it's not a circle, that is, the distances are different, and True if the distances are equal

def isCocircular(R):
    rememberRadius = -99
    for x in range(0, len(R)-2):
        # Define three points
        p1 = Point2D(R[x][0], R[x][1])
        p2 = Point2D(R[x+1][0], R[x+1][1])
        p3 = Point2D(R[x+2][0], R[x+2][1])
        circleCenter = calculateCircleCenter(p1, p2, p3)
        if not circleCenter:
            return False
        # Test if all three points have the same distance to the center, that is, the radius
        r1 = p1.distance(circleCenter)
        r2 = p2.distance(circleCenter)
        r3 = p3.distance(circleCenter)
        if r1 == r2 == r3:
            # It's a circle; go on to the next three points if there are any
            #if x + 2 >= len(R):
            #    return True
            if rememberRadius == -99 or rememberRadius == r1:
                rememberRadius = r1
                continue
            elif rememberRadius != r1:
                # It's not a circle; return False
                return False
        else:
            # It's not a circle; return False
            return False
    return True


### Calculate a circle's center by calculating the intersection of two segments' perpendiculars
#
# INPUT
# p1     : tupel of the first point (x, y)
# p2     : tupel of the second point (x, y)
# p3     : tupel of the third point (x, y)
#
# RETURN
# circleCenter  : a tupel (x, y) indicating the coordinates of the circle center or "None" if no center could be determined

def calculateCircleCenter(p1, p2, p3):
    # Calculate the line segments between these points
    s1 = Segment2D(p1, p2)
    s2 = Segment2D(p2, p3)
    # Calculate the lines perpendicular to s1 and s2
    midpoint1 = s1.midpoint
    perpLine1 = s1.perpendicular_line(midpoint1)
    midpoint2 = s2.midpoint
    perpLine2 = s2.perpendicular_line(midpoint2)
    # Calculate the point of intersection which should be the center of the circle
    circleCenter = perpLine1.intersection(perpLine2)
    try:
        circleCenter[0]
        return circleCenter[0]
    except IndexError:
        # No circle center could be determined because the segments are parallel
        return None


### Check if all points are inside a circle using sympy methods
#
# INPUT
# points    : list of tuples (x, y)
# circle    : Object defining the center of the circle and the radius: ((x, y), r)
#
# RETURN
# boolean   : False if not enclosed and not on the border; True if enclosed or on the border

def checkAllPointsInside(circle, points):
    c = Circle((circle[0][0], circle[0][1]), circle[1])
    for p in points:
        # convert list object to a Point2D object
        pp = Point2D(p[0], p[1])
        # Check if enclosed and if on border; enclosed() returns False if point is on the border
        enclosed = c.encloses_point(pp)
        onBorder = c.intersection(pp)
        if not enclosed and not onBorder:
            print("not enclosed")
            return False
    return True