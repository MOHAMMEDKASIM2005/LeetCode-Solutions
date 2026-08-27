class Solution:
    def reversePairs(self, nums):
        def mergeSort(left, right):
            if left >= right:
                return 0
            
            mid = (left + right) // 2
            count = mergeSort(left, mid) + mergeSort(mid + 1, right)
            
            # Count cross pairs BEFORE merging (arrays must stay sorted for this)
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - mid - 1)
            
            # Standard merge
            merged = []
            l, r = left, mid + 1
            while l <= mid and r <= right:
                if nums[l] <= nums[r]:
                    merged.append(nums[l]); l += 1
                else:
                    merged.append(nums[r]); r += 1
            merged.extend(nums[l:mid+1])
            merged.extend(nums[r:right+1])
            nums[left:right+1] = merged
            
            return count
        
        return mergeSort(0, len(nums) - 1)