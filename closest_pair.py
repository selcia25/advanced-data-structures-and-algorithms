import math
 
# A structure to represent a Point in 2D plane
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
# Sort array of points according to X coordinate
def compareX(a, b):
    p1, p2 = a, b
    return (p1.x != p2.x) * (p1.x - p2.x) + (p1.y - p2.y)
 
# Sort array of points according to Y coordinate
def compareY(a, b):
    p1, p2 = a, b
    return (p1.y != p2.y) * (p1.y - p2.y) + (p1.x - p2.x)
 
# A utility function to find the distance between two points
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
 
# A Brute Force method to return the smallest distance between two points in P[] of size n
def bruteForce(P, n): # P is the set of points
    min = float('inf') # keep the minimum element to infinity
    for i in range(n): # iterate throught all the points
        for j in range(i+1, n): # iterate the next point
            if dist(P[i], P[j]) < min: # if distance between first and next point is less than minimum
                min = dist(P[i], P[j]) # update the value of minimum
    return min
 
# A utility function to find a minimum of two float values
def min(x, y):
    return x if x < y else y
 
# A utility function to find the distance between the closest points of strip of a given size.
# All points in strip[] are sorted according to y coordinate. They all have an upper bound on minimum distance as d.
# Note that this method seems to be a O(n^2) method, but it's a O(n) method as the inner loop runs at most 6 times
def stripClosest(strip, size, d):
    min = d  # Initialize the minimum distance as d
    # Pick all points one by one and try the next points till the difference between y coordinates is smaller than d.
    # This is a proven fact that this loop runs at most 6 times
    for i in range(size):
        for j in range(i+1, size):
            if (strip[j].y - strip[i].y) < min:
                if dist(strip[i],strip[j]) < min:
                    min = dist(strip[i], strip[j])
    return min

# A recursive function to find the smallest distance. 
# The array Px contains all points sorted according to x coordinates and Py contains all points sorted according to y coordinates
def closestUtil(Px, Py, n):
    # If there are 2 or 3 points, then use brute force
    if n <= 3:
        return bruteForce(Px, n)
 
    # Find the middle point
    mid = n // 2
    midPoint = Px[mid]
 
    # Divide points in y sorted array around the vertical line.
    # Assumption: All x coordinates are distinct.
    Pyl = [None] * mid   # y sorted points on left of vertical line
    Pyr = [None] * (n-mid)  # y sorted points on right of vertical line
    li = ri = 0  # indexes of left and right subarrays
    for i in range(n):
        if ((Py[i].x < midPoint.x or (Py[i].x == midPoint.x and Py[i].y < midPoint.y)) and li<mid):
            Pyl[li] = Py[i]
            li += 1
        else:
            Pyr[ri] = Py[i]
            ri += 1
 
    # Consider the vertical line passing through the middle point
    # calculate the smallest distance dl on left of middle point and
    # dr on right side
    dl = closestUtil(Px, Pyl, mid)
    dr = closestUtil(Px[mid:], Pyr, n-mid)
 
    # Find the smaller of two distances
    d = min(dl, dr)
 
    # Build an array strip[] that contains points close (closer than d)
    # to the line passing through the middle point
    strip = [None] * n
    j = 0
    for i in range(n):
        if abs(Py[i].x - midPoint.x) < d:
            strip[j] = Py[i]
            j += 1
 
    # Find the closest points in strip.  Return the minimum of d and closest
    # distance is strip[]
    return stripClosest(strip, j, d)
 
# The main function that finds the smallest distance
# This method mainly uses closestUtil()
def closest(P, n):
    Px = P
    Py = P
    Px.sort(key=lambda x:x.x)
    Py.sort(key=lambda x:x.y)
 
    # Use recursive function closestUtil() to find the smallest distance
    return closestUtil(Px, Py, n)
 
# Driver program to test above functions
if __name__ == '__main__':
    P = [Point(2, 3), Point(12, 30), Point(40, 50), Point(5, 1), Point(12, 10), Point(3, 4)]
    n = len(P)
    print("The smallest distance is", closest(P, n))