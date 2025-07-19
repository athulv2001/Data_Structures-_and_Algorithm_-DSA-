from collections import defaultdict

class Solution:
    def findDuplicate(self, paths):
        content_map = defaultdict(list)

        for entry in paths:
            parts = entry.split(" ")
            root = parts[0]

            for file_str in parts[1:]:
                name, content = file_str.split("(")
                content = content[:-1]  # remove trailing ')'
                full_path = root + "/" + name
                content_map[content].append(full_path)

        return [group for group in content_map.values() if len(group) > 1]
