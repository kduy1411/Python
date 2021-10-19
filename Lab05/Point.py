import math

class Point:

    def __init__(self,Number1,Number2):
        self.Number1 = Number1
        self.Number2 = Number2

class LineSegment:

    def __init__(self,segmentStart: Point,segmentEnd: Point):
        self.segmentStart = segmentStart
        self.segmentEnd = segmentEnd

    def slope(self):
        result = (self.segmentStart.Number1 - self.segmentEnd.Number1) / (self.segmentStart.Number2 - self.segmentEnd.Number2)
        return result

    def length(self):
        distance = math.sqrt( pow((self.segmentStart.Number1 - self.segmentEnd.Number1),2) + pow((self.segmentStart.Number2 - self.segmentEnd.Number2),2 ))
        return distance
