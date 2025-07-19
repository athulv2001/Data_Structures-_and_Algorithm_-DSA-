from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        max_freq = max(counter.values())
        if max_freq > (len(s) + 1) // 2:
            return ""  # impossible to rearrange

        max_heap = [(-freq, ch) for ch, freq in counter.items()]
        heapq.heapify(max_heap)

        result = []
        prev_freq, prev_char = 0, ''

        while max_heap:
            freq, ch = heapq.heappop(max_heap)
            result.append(ch)

            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))

            freq += 1  # decrease frequency
            prev_freq, prev_char = freq, ch

        return ''.join(result)
