def hash(s):
    power,mod,p,res,inv,p_power=0,1000000007,31,[0],[1],1
    for _ in s:
        res.append((res[power]+(ord(_)-96)*pow(p,power,mod))%mod)
        power+=1
        p_power=(p_power*p)%mod
        inv.append(pow(p_power,mod-2,mod))
    return res,inv

s=input()
mod=1000000007
print(res,inv)
while True:
    l,r=map(int,input().split())
    print(((res[r]-res[l-1])*inv[l-1])%mod)
