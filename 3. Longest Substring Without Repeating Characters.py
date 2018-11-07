#Given a string, find the length of the longest substring without repeating characters.


#Complexity analysis
#T: O(n)
#S: O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
    #start is the position of start for current substring    
    longest, start, visited = 0, 0, {}
    
    for i, v in enumerate(s):
        # if the letter was not visited or visited but not in current substring
        if v not in visited or start > visited[v]:
            longest = max(longest, i-start+1)
        else:
            start = visited[v] + 1
        visited[v] = i
        
        
    return longest
