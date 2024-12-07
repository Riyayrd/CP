def romanToInt(self, s):
        
        #Leetcode Problem : https://leetcode.com/problems/roman-to-integer/
        # Method 1
        dict={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
        num=0
        for x in range(len(s)-1):
            if dict[s[x]]<dict[s[x+1]]:
                num=num-dict[s[x]]
            else: 
                num=num+dict[s[x]]
        return num+dict[s[-1]]        


        #Method 2
        # num=0
        # x=0
        # while x < len(s):
        #     if s[x]=='I':
        #         if  x<len(s)-1 and s[x+1]=='V':
        #             num=num+4
        #             x+=2
        #         elif x<len(s)-1 and s[x+1]=='X':
        #             num=num+9
        #             x+=2
        #         else:
        #             num=num+1
        #             x+=1
        #     elif  s[x]=='X':
        #         if x<len(s)-1 and s[x+1]=='L':
        #             num=num+40 
        #             x+=2
        #         elif x<len(s)-1 and s[x+1]=='C':
        #             num=num+90
        #             x+=2                
        #         else:
        #             num=num+10
        #             x+=1
        #     elif  s[x]=='C':
        #         if x<len(s)-1 and s[x+1]=='D':
        #             num=num+400 
        #             x+=2
        #         elif x<len(s)-1 and s[x+1]=='M':
        #             num=num+900
        #             x+=2
        #         else:
        #             num=num+100
        #             x+=1
        #     elif s[x]=='V':
        #         num=num+5
        #         x+=1
        #     elif s[x]=='L':
        #         num=num+50
        #         x+=1
        #     elif s[x]=='D':
        #         num=num+500
        #         x+=1
        #     else:
        #         num=num+1000
        #         x+=1            
        # return num
        """
        :type s: str
        :rtype: int
        """
