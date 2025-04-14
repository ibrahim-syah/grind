class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr: List[int], l: int, m: int, r: int):
            leftSubarr = arr[l:m+1]
            rightSubarr = arr[m+1:r+1]
            i, j, k = l, 0, 0
            while j < len(leftSubarr) and k < len(rightSubarr):
                if leftSubarr[j] <= rightSubarr[k]:
                    arr[i] = leftSubarr[j]
                    j += 1
                else:
                    arr[i] = rightSubarr[k]
                    k += 1
                i += 1
            while j < len(leftSubarr):
                arr[i] = leftSubarr[j]
                i += 1
                j += 1
            while k < len(rightSubarr):
                arr[i] = rightSubarr[k]
                i += 1
                k += 1
        
        def mergeSort(arr: List[int], l: int, r: int):
            if l == r:
                return
            
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
            return

        mergeSort(nums, 0, len(nums))
        return nums
