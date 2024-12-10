#https://leetcode.com/problems/search-insert-position/

def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # for x in range(len(nums)):
        #     if nums[x]< target:
        #         continue
        #     if  nums[x]==target:
        #         return x
        #     if nums[x]>target:
        #         return x
        # return len(nums)         
        left=0
        right=len(nums)-1
        while left<=right:
            mid= (left + right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1

        return left                
