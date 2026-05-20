class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        finalList = []

        for anchor in range(len(nums)):

            # Skip duplicate anchors
            if anchor > 0 and nums[anchor] == nums[anchor - 1]:
                continue

            left = anchor + 1
            right = len(nums) - 1

            while left < right:
                currSum = nums[anchor] + nums[left] + nums[right]

                if currSum == 0:
                    finalList.append([
                        nums[anchor],
                        nums[left],
                        nums[right]
                    ])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif currSum > 0:
                    right -= 1

                else:
                    left += 1

        return finalList