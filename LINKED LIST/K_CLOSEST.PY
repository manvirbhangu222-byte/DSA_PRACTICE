class Solution(object):
    def kClosest(self, points, k):
    

        heap = []

        for point in points:
            x = point[0]
            y = point[1]

            distance = x * x + y * y

            heapq.heappush(heap, (distance, point))

        answer = []

        for _ in range(k):
            distance, point = heapq.heappop(heap)
            answer.append(point)

        return answer
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        