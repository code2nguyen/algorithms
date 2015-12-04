class AB:
	def createString(self, N, K):
		S = ["B" for i in range(N // 2)] + ["A" for i in range( (N + 1) // 2)]
		while K:
			for i in range(N - 1):
				if S[i] == "B" and S[i+1] == "A":
					S[i+1] = "B"
					S[i] = "A"
					break
			else:
				return ""
			K -= 1
		return "".join(S)

t = AB()
print(t.createString(3, 2))
print(t.createString(2, 0))
print(t.createString(5, 8))
print(t.createString(50, 501))

"""
Problem Statement
You are given two s: N and K. Lun the dog is interested in strings that satisfy the following conditions:

The string has exactly N characters, each of which is either 'A' or 'B'.
The string s has exactly K pairs (i, j) (0 <= i < j <= N-1) such that s[i] = 'A' and s[j] = 'B'.
If there exists a string that satisfies the conditions, find and return any such string. Otherwise, return an empty string.

Definition
Class: AB
Method: createString
Parameters: integer, integer
Returns: string
Method signature: def createString(self, N, K):
Limits
Time limit (s): 2.000
Memory limit (MB): 256
Constraints
- N will be between 2 and 50, inclusive.
- K will be between 0 and N(N-1)/2, inclusive.
Examples
0)
3
2
Returns: "ABB"
This string has exactly two pairs (i, j) mentioned in the statement: (0, 1) and (0, 2).
1)
2
0
Returns: "BA"
Please note that there are valid test cases with K = 0.
2)
5
8
Returns: ""
Five characters is too short for this value of K.
3)
10
12
Returns: "BAABBABAAB"
Please note that this is an example of a solution; other valid solutions will also be accepted.
This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder,
Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.

Solution:
Using try all solution, note that, with a String has X chacters A and N-X characters B, we have Y pairs.
When we switch two characters B beside A we have Y + 1 pairs, and X max  = N / 2.
"""
