"""
Time complexity: O(n)
Space complexity: O(1)
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        breakflag=0
        for i in range(len(nums)-1,0,-1):
          
            # find decreasing element 
            if nums[i-1]<nums[i]:
                index=i-1
                breakflag=1
                
                # iterate through decreasing element till end
                for j in range(len(nums)-1,index,-1):
                  
                    # find element just greater than decreasing element
                    # swap the two
                    if nums[j]>nums[index]:
                        nums[j],nums[index]=nums[index],nums[j]
                        
                        #reverse the section from decreasing element till end
                        nums[index+1:]=nums[index+1:][::-1]
                        break
                break                    
            
        if not breakflag: nums.reverse()
