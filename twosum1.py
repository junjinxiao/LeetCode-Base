class Solution():
    def twoSum(self, nums, target):
    #type nums:List[int]
    #traget: int
    #rtype:List(int)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] +nums[j] == target:
                    return[i,j]
                    
rlist = Solution().twoSum([2,7,11,15,3],10)
print(rlist)
