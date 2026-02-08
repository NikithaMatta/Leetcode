from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r"[a-z]+", paragraph.lower())
        count = Counter(words)

        for word, freq in count.most_common():
            if word not in banned:
                return word
