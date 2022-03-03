# Given a string s of lower and upper case English letters.
# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
# 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
# To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.
# Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
# Notice that an empty string is also good.
# Example 1:
# Input: s = "leEeetcode"
# Output: "leetcode"
# Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

from typing import List


class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for i in s:
                if st and st[-1] != i and st[-1].lower() == i.lower():
                    st.pop()
                else:
                    st.append(i)

        return "".join(st)

b = Solution
a= (b().makeGood("leeEeetcode"))
print(a)

##############################################################################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#####################################

# You are given an array target and an integer n.

# In each iteration, you will read a number from list = [1, 2, 3, ..., n].

# Build the target array using the following operations:

# "Push": Reads a new element from the beginning list, and pushes it in the array.
# "Pop": Deletes the last element of the array.
# If the target array is already built, stop reading more elements.
# Return a list of the operations needed to build target. The test cases are generated so that the answer is unique.
# Example 1:

# Input: target = [1,3], n = 3
# Output: ["Push","Push","Pop","Push"]
# Explanation: 
# Read number 1 and automatically push in the array -> [1]
# Read number 2 and automatically push in the array then Pop it -> [1]
# Read number 3 and automatically push in the array -> [1,3]
# Example 2:

# Input: target = [1,2,3], n = 3
# Output: ["Push","Push","Push"]

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        st=[]
        res=[]
        for i in range(1, n+1):
            if i in target:
                st.append(i)
                res.append("Push")
            else:
                st.append(i)
                res.append("Push")
                st.pop()
                res.append("Pop")
            if st == target:
                break
        return res
b = Solution
a= (b().buildArray([1,3],3))
print(a)

# You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.
# At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:
# An integer x - Record a new score of x.
# "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
# "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
# "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
# Return the sum of all the scores on the record.

# Example 1:
# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.




class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for i in ops:
            if i == "+":
                stack.append(stack[-1]+stack[-2])
            elif i =='D':
                stack.append(stack[-1]*2)
            elif i == 'C':
                stack.pop()
            else:
                stack.append(int(i))
        return sum(stack)
b = Solution
a= (b().calPoints(["5","2","C","D","+"]))
print(a)
        