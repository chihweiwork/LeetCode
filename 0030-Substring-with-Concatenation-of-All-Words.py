# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
#
# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
#
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        substring_len = word_len * num_words
        word_count = Counter(words)
        res = []

        for i in range(word_len):
            left = i
            count = 0
            seen = Counter()
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j+word_len]
                if word in word_count:
                    seen[word] += 1
                    count += 1
                    while seen[word] > word_count[word]:
                        left_word = s[left:left+word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len
                    if count == num_words:
                        res.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = j + word_len
        return res
