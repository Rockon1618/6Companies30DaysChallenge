class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        count = 0
        while i <= len(nums):
            j=i+1
            while j <=len(nums):
                new_array = nums[:i]+nums[j:]

                if new_array == sorted(set(new_array)):
                    count += 1
                j=j+1
            i=i+1
        return count