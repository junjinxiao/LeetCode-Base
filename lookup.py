class Solution():
    def twoSum(self,nums,target):
        """
        :type nums:List[int]
        :type target: int
        :rtype lsit[int]
        """
        loopup={}
        for i,num in enumerate(nums):
            if target - num in loopup:
                return [loopup[target - num], i]
            else:
                loopup[num] = i
rlist = Solution().twoSum([2,7,11,15,3],10)
print(rlist)
print(loopup[2])
