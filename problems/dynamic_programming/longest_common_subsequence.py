"""
Given two strings text1 and text2, return the length of their longest common subsequence. 
If there is no common subsequence, return 0.

Time Complexity: O(m*n)
Space Complexity: O(m*n)

In general, we have 2 choices when comparing a letter from str1 and another letter from str2:
1. If the current letters match, the answer is 1 + lcs(rest of str1, rest of str2). 

2. If the current letters don't match, the answer is 
max(lcs(exclude current letter of str1), lcs(exclude current letter of str2))
"""

def lcs(word1, word2):
  # top down approach
  memo = [[-1]*len(word2) for _ in range(len(word1))]
  ans = top_down(memo, word1, word2, 0, 0)

  #bottom up approach
  ans = bottom_up(word1, word2)

  return ans

## Top-down approach
def top_down(dp, word1, word2, i, j):
  # base case when either index is out of bounds
  if (i == len(word1) or j == len(word2)):
    return 0
  
  # if the answer is already memoized
  if dp[i][j] > -1:
    return dp[i][j]
  
  # if curr letters are the same, 
  # find the lcs given the rest of word 1 and the rest of word 2
  if (word1[i] == word2[j]):
    top_down = 1 + top_down(dp, word1, word2, i+1, j+1)
  else:
    option1 = top_down(dp, word1, word2, i, j+1) # include curr letter of word1, exclude curr letter of word2
    option2 = top_down(dp, word1, word2, i+1, j) # exclude curr letter of word1, include curr letter of word2
    top_down = max(option1, option2)
  
  dp[i][j] = top_down
  return top_down

def bottom_up(word1, word2):
  # pad left column and top row with zeros
  dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]

  for i in range(1, len(word1) + 1):
    for j in range(1, len(word2) + 1):
      if (word1[i-1] == word2[j-1]):
        # dp[i-1][j-1] represents the lcs(word1[:i], word2[:j])
        # (i.e. exclude curr letter of word1, exclude curr letter of word2)

        # +1 because the current letters match
        dp[i][j] = 1 + dp[i-1][j-1] 
      else:
        # dp[i-1][j] represents lcs(word1[:i], word2[:j+1]) 
        # (i.e. exclude curr letter of word1, include curr letter of word2)

        # dp[i][j-1] represents lcs(word1[:i+1], word2[:j]) 
        # (i.e. include curr letter of word1, exclude curr letter of word2)
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  return dp[-1][-1]