class solution:
    def runningSum(self, nums:list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        print(nums)
a=solution()
a.runningSum([1,2,3])

#op [1,3,6]
