class Solution:
    def search(self, nums: List[int], target: int) -> int:
        orig = nums
        nums = sorted(nums)
        pivot = orig.index(nums[0])

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                if (mid + pivot) >= len(nums):
                    return (mid + pivot) % len(nums)
                    
                else:
                    return mid + pivot
            
            elif nums[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1
        
        return -1