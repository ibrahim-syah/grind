class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l: int, m: int, r: int):
            leftSubarr, rightSubarr = nums[l:m+1], nums[m+1:r+1]
            i, k, j = l, 0, 0
            while k < len(leftSubarr) and j < len(rightSubarr):
                if leftSubarr[k] <= rightSubarr[j]:
                    nums[i] = leftSubarr[k]
                    k += 1
                else:
                    nums[i] = rightSubarr[j]
                    j += 1
                i += 1
            while k < len(leftSubarr):
                nums[i] = leftSubarr[k]
                k += 1
                i += 1
            while j < len(rightSubarr):
                nums[i] = rightSubarr[j]
                j += 1
                i += 1

        def mergeSort(l: int, r: int):
            if l == r:
                return
            
            m = (l + r) // 2
            mergeSort(l, m)
            mergeSort(m+1, r)
            merge(l, m, r)

        mergeSort(0, len(nums))
        return nums