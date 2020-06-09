# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 9:46 上午
# @Author  : ZolHo
# @FileName: 929-unique-email-addresses.py

class Solution:
    def numUniqueEmails(self, emails) -> int:
        ans_set = set([])
        for email in emails:
            head = email.split("@")
            name = head[0].split("+")
            ans_set.add(name[0].replace(".","")+"@"+head[1])
        return len(ans_set)

solu = Solution()
print(solu.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))