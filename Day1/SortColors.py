"""
Time complexity: O(N)
Space complexity: O(1)
"""
#3 pointer algo- rightmost 0, leftmost 2, current element
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0=curr=0
        p2=len(nums)-1
        
        while curr<=p2:
            #If current element is 0, swap curr and p0 elements, increment p0 and curr
            if nums[curr]==0:
                nums[curr],nums[p0]=nums[p0],nums[curr]
                p0+=1
                curr+=1
            #If current element is 2, swap curr and p2 elements, decrement p2 
            elif nums[curr]==2:
                nums[curr],nums[p2]=nums[p2],nums[curr]
                p2-=1
            #Else if current element is 1, increment curr
            else:
                curr+=1
