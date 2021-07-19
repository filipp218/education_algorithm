
import heapq


class Solution(object):
    def way(self, i):
        a = [0, 0]
        return -(((i[0] - a[0]) ** 2) + ((i[1] - a[1]) ** 2)) ** 0.5

    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        window = [(self.way(i), i) for i in points[:k]]
        heapq.heapify(window)
        for i in points[k:]:
            distance = self.way(i)
            max_dist, _ = window[0]
            if distance > max_dist:
                heapq.heappushpop(window, (distance, i))
        for dis, point in window:
            result.append(point)
        return result










class Solution(object):
    def way(self, i):
        a = [0, 0]
        return (((i[0] - a[0]) ** 2) + ((i[1] - a[1]) ** 2)) ** 0.5

    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        a = [0, 0] 
        result = []
        window = [(self.way(i), i) for i in points[:k]]
        window = sorted(window)
        for i in points[k:]:
            distance = self.way(i)
            max_dist, _ = window[-1]
            if distance < max_dist:
                window.pop()
                window.append((distance, i))
                window = sorted(window)
        for dist, points in window:
            result.append(points)
        return result
