class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        area,currArea,left,right = 0,0,0,n-1
        
        for i in range(n):
            currArea = min(height[left],height[right])*(right-left)
            if currArea > area:
                area = currArea
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return area