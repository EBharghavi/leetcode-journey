class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        k=len(nums)
        if k%2==1:
            return nums[k//2]
        return (nums[k//2] + nums[k//2 - 1])/2.0
