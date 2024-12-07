
# https://leetcode.com/problems/longest-common-prefix/
def longestCommonPrefix(self, strs):
        strs=sorted(strs)
        prefix=[]
        if strs and len(strs)>0:
            first=strs[0]
            last=strs[-1]
            for i in range(len(first)):
                if i<len(last) and last[i]==first[i]:
                    prefix.append(first[i])
                else:
                    return "".join(prefix)    
        return "".join(prefix)
