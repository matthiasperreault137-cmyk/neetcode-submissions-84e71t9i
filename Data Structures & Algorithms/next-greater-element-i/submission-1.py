class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range(len(nums1)):
            num1 = nums1[i]
            found = False
            j = 0
            while j < len(nums2) and nums2[j] != num1:
                j += 1
            if j >= len(nums2) - 1:
                result.append(-1)
            else:
                while j < len(nums2) and nums2[j] <= num1:
                    j += 1
                if j >= len(nums2):
                    result.append(-1)
                else:
                    result.append(nums2[j])
        return result