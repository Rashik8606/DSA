class Solution:
    def search(self, nums: list[int], target:int)->int:
        left,right = 0, len(nums)-1  #first index and last index 

        while left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            # if mid is in left in the left 
            if nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    #go to right 
                    left = mid+1
                else:
                    # stay left 
                    right = mid-1
            
            else: #right
                if target > nums[right] or target < nums[mid]:
                    # go to left 
                    right = mid-1
                else:
                    # stay right
                    left = mid+1
        return -1  # if not in the array return -1

        
obj = Solution()
print(obj.search([4,5,6,7,0,1,2],0))
