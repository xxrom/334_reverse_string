from typing import List


class Solution:

  def reverseString(self, s: List[str]) -> None:
    size = len(s) - 1
    middle = size // 2

    for i in range(middle):
      s[i], s[size - i] = s[size - i], s[i]

    return s


my = Solution()
n = ["h", "e", "l", "l", "o"]
trueAns = ["o", "l", "l", "e", "h"]

ans = my.reverseString(n)

print("ans", ans, ans == trueAns)
