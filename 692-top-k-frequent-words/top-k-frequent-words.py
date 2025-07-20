from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = Counter(words)
        heap = [(-count, word) for word, count in freq.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]
