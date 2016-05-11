# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments.sort(segmentComp)
    for s in segments:
        if len(points) == 0:
            points.append(s.end)
            continue
        if s.start > points[len(points)-1]:
            points.append(s.end)
            continue
        if s.end < points[len(points)-1]:
            points[len(points)-1] = s.end

    return points

def segmentComp(a,b):
    if a.start < b.start:
        return -1
    if a.start == b.start:
        return 0
    if a.start > b.start:
        return 1

inputData = raw_input()
data = map(int, inputData.split())
n = data.pop(0)
segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
print(segments)
print(segments[0].start)
points = optimal_points(segments)
print(len(points))
print(points)