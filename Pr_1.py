def naib_cif(a):
    max = 0
    while a > 0 :
        if (a % 10) > max:
            max = (a % 10)
        a = a // 10 
    return(max)




def pr_cf(a):
    b = 1
    while a > 0 :
        b = b*(a % 10)
        a = a // 10
    return(b)




n = int(input())
a = []
i = 0
for i in range(n):
    a.append(int(input()))

j = 0
for j in range(n-1):
    for i in range(j,n):
        if naib_cif(a[i]) > naib_cif(a[j]):
            e = a[i]
            a[i] = a[j]
            a[j] = e
        
        if naib_cif(a[i]) == naib_cif(a[j]):
            if pr_cf(a[i]) > pr_cf(a[j]):
                e = a[i]
                a[i] = a[j]
                a[j] = e
                    

            if  pr_cf(a[i]) == pr_cf(a[j]):
                if a[i] > a[j]:
                    e = a[i]
                    a[i] = a[j]
                    a[j] = e
           
print(a)

