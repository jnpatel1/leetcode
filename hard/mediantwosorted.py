class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        if len(nums) % 2 == 1:
            pos = len(nums) // 2
            return nums[pos]
        
        else:
            pos1 = int(len(nums) / 2)
            pos2 = pos1 - 1
            return ((nums[pos1] + nums[pos2]) / 2)