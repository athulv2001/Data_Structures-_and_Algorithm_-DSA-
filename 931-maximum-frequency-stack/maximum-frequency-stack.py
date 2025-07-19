from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freq_map = defaultdict(int)       # val -> frequency
        self.group_map = defaultdict(list)     # freq -> list of vals (stack)
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq = self.freq_map[val] + 1
        self.freq_map[val] = freq
        self.group_map[freq].append(val)
        self.max_freq = max(self.max_freq, freq)

    def pop(self) -> int:
        val = self.group_map[self.max_freq].pop()
        self.freq_map[val] -= 1
        if not self.group_map[self.max_freq]:
            self.max_freq -= 1
        return val
