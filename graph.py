
You are given a network of n nodes, labeled from 1 to n. 
You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), 
where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. 
If it is impossible for all the n nodes to receive the signal, return -1.

https://leetcode.com/problems/network-delay-time/
  
  
from collections import deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        cost = {}
        table = {k: 0}
        path = set()
        for i in times:
            if i[0] not in graph:
                graph[i[0]] = {i[1]}
            else:
                graph[i[0]].add(i[1])
            cost[(i[0], i[1])] = i[2]

        qu = deque()
        qu.append(k)

        while qu:
            edge = qu.popleft()
            if edge in graph:
                for node in graph[edge]:
                    price = cost[(edge, node)] + table[edge]
                    if node not in table:
                        table[node] = price
                    else:
                        if table[node] > price:
                            table[node] = price
                            qu.append(node)

                    if node not in path:
                        qu.append(node)
                path.add(edge)
                
        result = max(table.values())
        if result == 0 or len(table) != n:
            return -1
        return result
                    
            
            
