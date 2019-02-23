class Solution():
    def twoSum(self, nums, target):


    #Hash table
        dic = {}
        rlist = []
        valuelist = []
    # the index of element, and the keyword, the array elemment is the key,
    # and the index is the dict value

        for i in range(len(nums)):
            dic[nums[i]] = i 

        for i in range(len(nums)):
        # to aviod the same value
            if i not in rlist:
            #complementary element
            #the difference is the key of dict corresponding the index of conplementary element other than current element.
                if (target - nums[i]) in dic.keys() and dic[target - nums[i]] != i:
                #current element not in the complementary 
                    if nums[i] not in valuelist:
                        rlist.append(i)
                        rlist.append(dic[target -nums[i]])
                
                valuelist.append(nums[i])
        return rlist
    
def main():
    rList = Solution().twoSum([2, 7, 11, 15, 3, 2, 18, 6], 9)
    print(rList)

if __name__ == '__main__':
    main()
