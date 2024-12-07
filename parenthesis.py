##https://leetcode.com/problems/valid-parentheses/

def isValid(self, s):
        maps={'{':'}','[':']','(':')'}
        brac=[]
        for char in s:
            if char in maps:
                brac.append(char)
            else:
                if not brac or maps[brac[-1]]!=char:
                    return False
                else:
                    brac.pop()
        return len(brac)==0                    


        # maps={'{':'}','[':']','(':')'}
        # brac=[]
        # if len(s)==0:
        #     return True
        # elif len(s)==1:
        #     return False    
        # for x in range(len(s)):
        #     if s[x]=='(' or s[x]=='{' or s[x]=='[':
        #         brac.append(s[x])
        #     elif len(brac)==0 and (s[x]==')' or s[x]=='}' or s[x]==']'):
        #         return False
        #     else:    
        #         if maps[brac[-1]]==s[x] :
        #             brac.pop()
        #         else:
        #             return False

        # return len(brac)==0  
