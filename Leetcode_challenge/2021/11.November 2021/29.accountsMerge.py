'''
721. Accounts Merge
Medium

Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

 

Constraints:

    1 <= accounts.length <= 1000
    2 <= accounts[i].length <= 10
    1 <= accounts[i][j] <= 30
    accounts[i][0] consists of English letters.
    accounts[i][j] (for j > 0) is a valid email.

'''
#from leetcode solution
# class Solution:
#     def accountsMerge(self, accounts: [[str]]) -> [[str]]:
#         visited = set()
#         adjacent = {}

#         def dfs(merged_account, email):
#             visited.add(email)
#             merged_account.append(email)

#             if email not in adjacent:
#                 print("Hi")
#                 return

#             for neighbor in adjacent[email]:
#                 if neighbor not in visited:
#                     dfs(merged_account, neighbor)

#         for account in accounts:
#             first_email = account[1]
#             for j in range(2, len(account)):
#                 if first_email not in adjacent:
#                     adjacent[first_email] = []
#                 account_email = account[j]
#                 adjacent[first_email].append(account_email)
#                 if account_email not in adjacent:
#                     adjacent[account_email] = []
#                 adjacent[account_email].append(first_email)

#         print("ajacent is {}".format(adjacent))

#         merged_accounts = []
#         for account in accounts:
#             account_name = account[0]
#             first_email = account[1]

#             if first_email not in visited:
#                 merged_account = []

#                 dfs(merged_account, first_email)
#                 merged_account.sort()
#                 merged_account = [account_name] + merged_account[:]
#                 merged_accounts.append(merged_account)

#         return merged_accounts


#my try of above
# class Solution:
#     def accountsMerge(self, accounts: [[str]]) -> [[str]]:
#         mail_map = {}
#         visited = set()

#         def dfs(mail, mail_list):
#             visited.add(mail)
#             mail_list.append(mail)

#             if mail not in mail_map: return

#             for neighbor in mail_map[mail]:
#                 if neighbor not in visited:
#                     dfs(neighbor, mail_list)


#         for account in accounts:
#             first_mail = account[1]
#             for j in range(2, len(account)):
#                 mail = account[j]
#                 if first_mail not in mail_map:
#                     mail_map[first_mail] = []
#                 mail_map[first_mail].append(mail)
#                 if mail not in mail_map:
#                     mail_map[mail] = []
#                 mail_map[mail].append(first_mail)

#         ans = []
#         for account in accounts:
#             name = account[0]
#             mail_list = []
#             first_mail = account[1]
#             if first_mail not in visited:
#                 dfs(first_mail, mail_list)
#                 mail_list.sort()
#                 ans.append([name]+mail_list)
#         return ans

# Using union find
from collections import defaultdict
class DSU:

    def __init__(self, sz):
        # // Initially each group is its own representative
        self.rep = [i for i in range(sz)]
        # // Intialize the size of all groups to 1
        self.size = [1] * sz

    # // Finds the representative of group x
    def find_rep(self, x):
        if x == self.rep[x]:
            return x
        self.rep[x] = self.find_rep(self.rep[x])
        return self.rep[x]

# // Unite the group that contains "a" with the group that contains "b"
    def union_by_size(self, a, b):
        rep_a, rep_b = self.find_rep(a), self.find_rep(b)

        # If nodes a and b already belong to the same group, do nothing.
        if rep_a == rep_b: return

    #    // Union by size: point the representative of the smaller
        # // group to the representative of the larger group.
        if self.size[rep_a] >= self.size[rep_b]:
            self.size[rep_a] += self.size[rep_b]
            self.rep[rep_b] = rep_a
        else:
            self.size[rep_b] += self.size[rep_a]
            self.rep[rep_a] = rep_b


class Solution:
    def accountsMerge(self, accounts: [[str]]) -> [[str]]:
        dsu = DSU(len(accounts))
        mail_map = {}
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                mail = account[j]

                # // If this is the first time seeing this email then
                # // assign component group as the account index
                if mail not in mail_map:
                    mail_map[mail] = i
                else:
                    # // If we have seen this email before then union this
                    # // group with the previous group of the email
                    dsu.union_by_size(i, mail_map[mail])

        #// Store emails corresponding to the component's representative
        components = defaultdict(list)
        for mail, group in mail_map.items():
            components[dsu.find_rep(group)].append(mail)

        # Sort the components and add the account name
        merged_accounts = []
        for group, mails in components.items():
            name = accounts[group][0]
            merged_accounts.append([name] + sorted(mails))

        return merged_accounts
        
accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
Output = [["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]

# accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output = [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

# accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
# Output = [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

sol = Solution()
ans = sol.accountsMerge(accounts)
print(Output)
print(ans)
print(ans == Output)
