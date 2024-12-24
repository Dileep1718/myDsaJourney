list=[1,8,6,2,5,4,8,3,7]
def maxArea(height):
    max=0
    sum=0
    for i in range(0,len(height)-1):
        if height[i]>=height[i+1] and max<=height[i]:
            max=height[i]
    for i in range(height.index(max),len(height)):
        sum+=height[i]
    return sum


ans=maxArea(list)
print(ans)
