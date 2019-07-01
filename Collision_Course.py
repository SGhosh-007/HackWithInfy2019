speed_count = int(input().strip())
speed = []
for _ in range(speed_count):
    speed_item = int(input().strip())
    speed.append(speed_item)
pos = int(input().strip())
s=list(range(0,speed_count))
m=list(map(sum,zip(speed,s)))
l=m[:pos]
r=m[pos+1:]
def leftchk(l,pos,m):
    c=0
    if min(l)>m[pos]:
        c=pos
    else:
        while len(l)>0 and max(l)>m[pos]:
            c+=1
            l.remove(max(l))
    return c
def rightchk(r,pos,m):
    c=0
    if max(r)<m[pos]:
        c=len(r)
    else:
        while len(r)>0 and min(r)<m[pos]:
            c+=1
            r.remove(max(r))
    return c
print(leftchk(l,pos,m)+rightchk(r,pos,m))
