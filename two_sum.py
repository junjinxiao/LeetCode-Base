class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: list[int]
        :type target: int
        :rype:list[int]
        """
        rlist = []
        #record the value spported the conition
        valuelist = []

        # ergodic
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    # the supported the condition withou in valuelist
                    if nums[i] not in valuelist:
                        rlist.append(i)
                    if nums[j] not in valuelist:
                        rlist.append(j)
                    
                    valuelist.append(nums[i])
                    valuelist.append(nums[j])
        return rlist

def main():
    # test the class
    rlist = Solution().twoSum([2,7,11,15,3],10)
    print(rlist)

if __name__ == '__main__':
    main()
