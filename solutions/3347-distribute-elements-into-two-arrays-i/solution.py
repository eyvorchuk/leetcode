class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        for n in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(n)
            else:
                arr2.append(n)
        arr1.extend(arr2)
        return arr1
