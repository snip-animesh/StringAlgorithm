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
  
string=input('enter string ')
pattern=input('pattern ')
combined=pattern+'$'+string
z=zlag(combined)
for i in range(len(z)):
    if z[i]==len(pattern):
        print(i-len(pattern)-1)

      
#https://www.youtube.com/watch?v=CpZh4eF8QBw&t=846s
#Logic from this video
