class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l, m, r):
            left, right = nums[l:m+1], nums[m+1:r+1]
            i, k, j = l, 0, 0

            while k < len(left) and j < len(right):
                if left[k] <= right[j]:
                    nums[i] = left[k]
                    k += 1
                else:
                    nums[i] = right[j]
                    j += 1
                i += 1
            while k < len(left):
                nums[i] = left[k]
                k+= 1
                i += 1
            while j < len(right):
                nums[i] = right[j]
                j+= 1
                i += 1
        def mergeSort(l, r):
            if l == r:
                return
            
            m = (l + r) // 2
            mergeSort(l, m)
            mergeSort(m+1, r)
            merge(l, m, r)

        mergeSort(0, len(nums))
        return nums
            