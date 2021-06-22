m = input()
l = len(m)
integ = []
j = 0
while j < l:
    m_int = ''
    a = m[j]
    while '0' <= a <= '9':
        m_int += a
        j += 1
        if j < l:
            a = m[j]
        else:
            break
    j += 1
    if m_int != '':
        integ.append(int(m_int))
for d in '1234567890':
    m=m.replace(d, ' ')
m.strip(' ')
while m.find('  ') != -1:
    m = m.replace('  ', ' ')
print(integ)
print(m)
def m1(m):
 m3=""
 m2=0
 spl=str(m).split()
 for j in spl:
    for j in spl[m2].split():
        a=''.join(spl[m2])
        if len(a)==1:
                m3=s3+a[0].upper()+' '
        else:
                m3=m3+a[0].upper()+a[1:-1]+a[-1].upper()+' '
        m2=m2+1
 return m3
print(m1(m))

biggest = max(integ)
print(biggest)
integ1 = []
j = 0
for j in range(len(integ)):
    if integ[j] != biggest:
        integ1.append(integ[j]**j)
print(integ1)