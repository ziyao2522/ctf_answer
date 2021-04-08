# -*- encoding: utf-8 -*-
'''
@File    :   有效字符串判定.py
@Time    :   2021/04/07 16:00:30
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则： 
任何左括号 ( 必须有相应的右括号 )。
任何右括号 ) 必须有相应的左括号 ( 。
左括号 ( 必须在对应的右括号之前 )。
* 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
一个空字符串也被视为有效字符串。
'''

from collections import deque


class Solution:
    def valid_string_judge(self, s: str):
        left_brackets_deque = deque()
        star_deque = deque()
        for i in range(len(s)):
            if s[i] == '(':
                left_brackets_deque.append(i)
            if s[i] == '*':
                star_deque.append(i)
            if s[i] == ')':
                if left_brackets_deque is None and star_deque is None:
                    return False
                elif left_brackets_deque is not None:
                    left_brackets_deque.pop()
                elif star_deque is not None:
                    star_deque.popleft()
        
        if len(star_deque) < len(left_brackets_deque):
            return False
        
        while left_brackets_deque is not None:
            while star_deque is not None and left_brackets_deque[0] < star_deque[0]:
                star_deque.popleft()
            if len(left_brackets_deque) > len(star_deque):
                return False
            star_deque.popleft()
            left_brackets_deque.popleft()
        return True
                    
solution = Solution()
print(solution.valid_string_judge('**(())'))