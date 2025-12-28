from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
            
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        res = []
        
        # We only need to start the sliding window at offsets 0, 1, ..., word_len - 1
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            words_used = 0
            
            # Slide the window by word_len each time
            while right + word_len <= len(s):
                word = s[right : right + word_len]
                right += word_len
                
                if word in word_count:
                    current_count[word] += 1
                    words_used += 1
                    
                    # If we have too many of 'word', move 'left' pointer forward
                    while current_count[word] > word_count[word]:
                        left_word = s[left : left + word_len]
                        current_count[left_word] -= 1
                        words_used -= 1
                        left += word_len
                    
                    # If we've found all words
                    if words_used == num_words:
                        res.append(left)
                else:
                    # 'word' is not in 'words', reset the window
                    current_count.clear()
                    words_used = 0
                    left = right
                    
        return res
