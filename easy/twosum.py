class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       answer = []
       for j in range(len(nums)):
        first = nums[j]
        for i in range(1, len(nums)):
                if (nums[i] + first) == target and nums[i] != first:
                    answer.append(nums.index(first))
                    answer.append(i)
                    return answer
                elif (nums[i] + first) == target and nums[i] == first and nums.count(first) > 1:
                    answer.append(nums.index(first))
                    nums[j] = -1000
                    answer.append(nums.index(first))
                    return answer