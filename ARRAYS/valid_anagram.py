class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        count={}
        for i in s:
            count[i]=count.get(i,0)+1
        for j in t:
            if j not in count:
                return False
            count[j]-=1
            if count[j]<0:
                return False
        return True

        
        