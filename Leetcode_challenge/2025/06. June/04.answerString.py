'''
3403. Find the Lexicographically Largest String From the Box I
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a string word, and an integer numFriends.

Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:

word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
All the split words are put into a box.
Find the lexicographically largest string from the box after all the rounds are finished.

 

Example 1:

Input: word = "dbca", numFriends = 2

Output: "dbc"

Explanation: 

All possible splits are:

"d" and "bca".
"db" and "ca".
"dbc" and "a".
Example 2:

Input: word = "gggg", numFriends = 4

Output: "g"

Explanation: 

The only possible split is: "g", "g", "g", and "g".

 

Constraints:

1 <= word.length <= 5 * 103
word consists only of lowercase English letters.
1 <= numFriends <= word.length
'''
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        largest_length = n-numFriends+1
        min_length = 1 if numFriends > 1 else n
        largest = ''
        for i in range(n-largest_length+1):
            largest = max(largest, word[i:i+largest_length])
        for i in range(n-largest_length+1, n-min_length+1):
            largest = max(largest, word[i:])
        return largest
