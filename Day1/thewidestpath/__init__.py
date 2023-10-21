####################################################################################################################################
#There are N trees (numbered from 0 to N-1) in a forest. The K-th tree is located at coordinates (X[K], Y[K]). 
#We want to build the widest possible vertical path, such that there is no tree on it. 
#The path must be built somewhere between a leftmost and a rightmost tree, which means that the width of the path cannot be infinite.
#What is the width of the widest possible path that can be built?
####################################################################################################################################

 

from typing import List

def solution(x: List[int], y: List[int]) -> int:
    x.sort()
    return max (x[i+1]- x[i] for i in range(len(x) - 1))
