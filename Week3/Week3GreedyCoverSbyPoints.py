'''
Problem Introduction
You are given a set of segments on a line and your goal is to mark as few points on a line as possible so that
each segment contains at least one marked point.
Problem Description
Task. Given a set of n segments {[a0, b0], [a1, b1], . . . , [an−1, bn−1]} with integer coordinates on a line, find
the minimum number m of points such that each segment contains at least one point. That is, find a
set of integers X of the minimum size such that for any segment [ai, bi] there is a point x ∈ X such
that ai ≤ x ≤ bi.
Input Format: The first line of the input contains the number n of segments. Each of the following n lines
contains two integers ai and bi (separated by a space) defining the coordinates of endpoints of the i-th
segment.
Constraints: 1 ≤ n ≤ 100; 0 ≤ ai ≤ bi ≤ 109 for all 0 ≤ i < n.
Output Format: Output the minimum number m of points on the first line and the integer coordinates of
m points (separated by spaces) on the second line. You can output the points in any order. If there
are many such sets of points, you can output any set. (It is not difficult to see that there always exist
a set of points of the minimum size such that all the coordinates of the points are integers.)
'''
def Min_Covered_Segment(seg):
    seg.sort(key = lambda elm: elm[1])
    point_list = [seg[0][1]] 
    for item in seg:
        if point_list[-1] >= item[0]: continue
        else: point_list.append(item[1])
    return point_list    
num_of_segment = int(input('Please enter number of segments: '))
Segments = list()
for num in range(num_of_segment):
    start,end = map(int, input('Enter the starting and ending point of your segment seperated by space,respectively: ').split())
    Segments.append((start,end))
#print(*Min_Covered_Segment(Segments)) 
print('number of points =',len(Min_Covered_Segment(Segments)), 'The points are:', *Min_Covered_Segment(Segments)) 
#print(f'Minimum number of points = {*Min_Covered_Segment(Segments)}')