def lps(pattern):
    prev=0;now=1;l=len(pattern);pi=[0]*l
    while(now<l):
        while prev!=0 and pattern[prev]!=pattern[now]:
            prev=pi[prev-1]
        if pattern[prev]==pattern[now]:
            pi[now]=prev+1; now+=1; prev+=1
        else:
            prev=0;pi[now]=0;now+=1
    return pi

  #lps function is to generate lps array . which is also known as pi array.

def kmp(pattern,text):
    pi=lps(pattern)
    indexes=[] #this list to mark the indexes where pattern matches with text
    i,j=0,0 #i to iterate over pattern and j for text
    while(i<len(text)):
        if text[i]==pattern[j]:
            i+=1;j+=1
        else:
            if j!=0:
                j=pi[j-1]
            else:
                i+=1
        if j==len(pattern):
            indexes.append(i-len(pattern))
            j=pi[j-1]
    return indexes

pattern=input("Input pattern- ")
text=input("Input text- ")
index=kmp(pattern,text)
print(*index,sep="\n")


#https://www.youtube.com/watch?v=sMARZCTPyNI&t=556s
#It's the best video to understand this algorithm .
#Complexity of this algorithm is O(n+m) n--> len(text) m--> len(pattern)
