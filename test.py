#program ki izpiše praštevila do 200
#def je_deljivo_s_katerim_od(n, seznam):
#    if seznam == []:
#        return False
#    else:
#        return n % seznam[0] == 0 or je_deljivo_s_katerim_od(n, seznam[1:])

#def prastevila_do(n):
#    if n <= 1:
#        return []
#    manjsa_prastevila = prastevila_do(n - 1)
#    if je_deljivo_s_katerim_od(n, manjsa_prastevila):
#        return manjsa_prastevila
#    else:
#        return manjsa_prastevila + [n]

#print(prastevila_do(200))


print(2)
print(3)

for j in range(4, 200):

    je_prastevilo = True

    for mozni_deljitelj in range(2, j): #dovolj je da gremo do vključno korena
        if j % mozni_deljitelj == 0:
            je_prastevilo = False
            break

    if je_prastevilo:
        print(j)

#poženem kr z uno tipko

