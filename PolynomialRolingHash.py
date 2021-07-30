def hash(s):
    power,mod,p,res=0,1000000007,31,0
    for _ in s:
        res=(res+(ord(_)-96)*pow(p,power,mod))%mod
        power+=1
    return res
