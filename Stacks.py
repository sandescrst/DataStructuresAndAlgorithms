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