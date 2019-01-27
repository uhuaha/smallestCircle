# Smallest circle problem solved by Welzl's algorithm

import welzlAlgorithm
import draw

# list of triangles in 3D, i.e., it is a list of points
allPoints = [{"a":3,"b":4,"c":1}, {"a":2,"b":1,"c":5}, {"a":2,"b":4,"c":4},
             {"a":2,"b":1,"c":3}, {"a":2,"b":2,"c":1}, {"a":1,"b":1,"c":1},
             {"a":2,"b":1,"c":2}, {"a":1,"b":1,"c":2}, {"a":3,"b":1,"c":4},]

# dimension to skip - a, b or c - because we have to reduce the problem to a 2D problem
dimToSkip = "c"

# before we go into Welzl's algorithm, we need to convert the dictionaries into lists and we need to remove one dimension
# in order to reduce the problem to a problem in 2D
allPoints2D = []
for points in allPoints:
    tempList = []
    for key, value in points.items():
        if key != dimToSkip:
            tempList.append(value)
    allPoints2D.append(tempList)
print(allPoints2D)

# Check for double points and remove them from the list
seen = []
keep = []
for point in allPoints2D:
    if point in seen:
        print(point)
    else:
        seen.append(point)
        keep.append(point)


# Execute the algorithm until a defined smallest circle was found
circleFound = False
while not circleFound:
    pointsToKeep = keep.copy()
    print(pointsToKeep)

    # The boundary points is an empty list at the start
    boundaryPoints = []

    # Call Welzl's algorithm
    circle = welzlAlgorithm.welzlAlgorithm(pointsToKeep, boundaryPoints)

    # Check if really all points are inside the circle; if not repeat the algorithm
    allPointsInside = False
    if circle:
        allPointsInside = welzlAlgorithm.checkAllPointsInside(circle, seen)

    # Draw to check
    if circle is not None and allPointsInside:
        circleFound = True
        draw.draw(circle, seen)
