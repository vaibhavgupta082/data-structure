nums = [-1,0,1,2,-1,-4]
nums.sort()
n = len(nums)
ans = []
for i in range(0, len(nums)-2):
    a = i
    if a==0 or (a>0 and nums[i]!=nums[i-1]):
        b = i+1
        c = n-1
        val = 0-(nums[i])
    while b<c:
        if (nums[b] + nums[c])==val:
            tri = []
            tri.append(nums[a])
            tri.append(nums[b])
            tri.append(nums[c])
            ans.append(tri)
            while b<c and nums[b] == nums[b+1]:
                b=b+1
            while b<c and nums[c]== nums[c-1]:
                c = c-1
            b=b+1
            c=c-1
        elif (nums[b] + nums[c])<val:
            b = b +1
        else:
            c=c-1
