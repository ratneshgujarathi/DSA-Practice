class Solution:
    '''reverse the words in sentence and remove the extra space'''
    def reverse_words(self, st: str):
        temp, ans = '', ''
        for ch in st:
            if ch != ' ':
                temp+=ch
            else:
                if ans == '':
                    ans = temp
                else:
                    if temp != '':
                        ans = temp + ' ' + ans
                temp = ''

        if temp != '':
            if ans != '':
                ans = temp + ' ' + ans 
        
        return ans
    

s = Solution()
sentence = "a good   example"
print(s.reverse_words(sentence))