s = input()
t = input()
rl=len(t)
for i in range(rl):
    k=(rl//(i+1))*t[:i+1]
    m=(len(s)//(i+1))*t[:i+1]
    if k==t and m==s:
        res=i+1
        break
else:
    res=-1
print(res)
