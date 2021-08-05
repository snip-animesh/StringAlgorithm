def zlag(pattern):
    n,right,left=len(pattern),0,0;z=[0]*n
    for i in range(1,n):
        if i>right:
            left=right=i
            while right<n and pattern[right]==pattern[right-left] :
                right+=1
            z[i]=right-left
            right-=1
        else:
            k=i-left
            if z[k]<right-i+1:
                z[i]=z[k]
            else:
                left=i
                while right<n and pattern[right]==pattern[right-left]:
                    right+=1
                z[i] = right - left
                right-=1
    return z
  
  #Just the z array is completed . full program isn't completed yet
