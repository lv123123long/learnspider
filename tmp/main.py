'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。示例如下
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
'''

def find_longest_substring(s):
    if not s:
        return 0
    max_len = 0
    start = 0
    d = {}
    for i in range(len(s)):
        if s[i] in d and d[s[i]] >= start:
            start = d[s[i]] + 1
        d[s[i]] = i
        max_len = max(max_len, i - start + 1)
    return max_len

if __name__ == '__main__':
    s = "abcabcbbfeawljljflawejflawefl"
    print(find_longest_substring(s))