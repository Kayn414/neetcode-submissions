class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(num, left, mid, right):
            n1 = mid - left + 1
            n2 = right - mid
    
            L = num[left:mid+1]
            R = num[mid+1:right+1]
    
            i = 0
            j = 0
            k = left
    
            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    num[k] = L[i]
                    i += 1
                else:
                    num[k] = R[j]
                    j += 1
                k += 1
            
            while i < n1:
                num[k] = L[i]
                i += 1 
                k +=1
            
            while j < n2:
                num[k] = R[j]
                j += 1
                k += 1
        
        def mergeSort(num, left, right):
        
            if left < right:        
                mid = left + (right - left) // 2
    
                mergeSort(num, left, mid)
        
                mergeSort(num, mid+1, right)
        
                merge(num, left, mid, right)
        mergeSort(nums, 0, len(nums) - 1)
        return nums