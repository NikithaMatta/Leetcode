from collections import Counter, defaultdict

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        freq = Counter(s)
        groups = defaultdict(list)
        
        for char, count in freq.items():
            groups[count].append(char)
        
        max_group_size = 0
        chosen_freq = 0
        
        for count, chars in groups.items():
            if len(chars) > max_group_size or \
               (len(chars) == max_group_size and count > chosen_freq):
                max_group_size = len(chars)
                chosen_freq = count
        
        return "".join(groups[chosen_freq])
