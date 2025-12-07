class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        queue = set()
        left = 0
        result = 0

        for right in range(len(s)):
            current_chart = s[right]

            while current_chart in queue:
                queue.remove(s[left])
                left += 1


            queue.add(current_chart)

            result = max(result, len(queue))

        return result
