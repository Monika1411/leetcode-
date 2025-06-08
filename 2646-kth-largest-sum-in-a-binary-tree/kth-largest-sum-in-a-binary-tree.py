from collections import deque
import heapq

class Solution(object):
    def kthLargestLevelSum(self, root, k):
        minheap = []
        q = deque([root])
        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            heapq.heappush(minheap, level_sum)
            if len(minheap) > k:
                heapq.heappop(minheap)
        return minheap[0] if len(minheap) == k else -1
