class Solution(object):
    def twoSum(self, numbers, target):
        left=0
        right=len(numbers)-1

        while left<right:
            currentsum=numbers[left]+numbers[right]

            if currentsum==target:
                return[left+1,right+1]
            elif currentsum<target:
                left+=1
            else:
                right-=1
    
        