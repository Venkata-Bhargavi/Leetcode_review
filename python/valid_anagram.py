########
#O(n log n): Sorting the strings is the most time-consuming operation, which takes O(n log n) time.
# space comp: O(n)
#########

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)




######
# space complexity O(1) -> fized array
# time complexity: O(n)
#####

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        return all(c == 0 for c in count)
