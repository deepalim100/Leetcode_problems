class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print(f'===nums1=={nums1}===nums2==={nums2}')
        i , j, k = m-1, n-1, m+n-1
        
        while i>=0 and j>=0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        
        return nums1
        

if __name__ == '__main__':
    arr1 = [1,2,3,0,0,0]
    arr2 = [2,5,6]
    res = Solution().merge(arr1, 3, arr2, 3)
    print(res)
