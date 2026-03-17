import numpy as np
from math import *
# import matplotlib.pyplot as plt
# output = open('rezyltart.txt', 'w')

Ro = 8.314
T = 3807
p = p1= Mt =  207
v = 0.9
svob_ch = [2, v]
p_d = [p for i in range(6)]
ps = sum(p_d)
pribl = -1
I_k = [119297.7, 130974.9, -66676.8, 159559.7, 290927.6, 322715.9]
S_k = [211.7950, 294.0902, 300.9465, 265.7793, 167.5471, 214.6023]
Cp_k = [38.72715, 41.53474, 59.81376, 38.19555, 20.78697, 21.19048]

aij_T = [
    [2,0,2,1,1,0],
    [0,2,1,1,0,1]
    ]
aij_M = [
    [1,0,0,0,-2,0,0],
    [0,1,0,0,0,-2,0],
    [0,0,1,0,-2,-1,0],
    [0,0,0,1,-1,-1,0]
    ]

Kj = [i for i in range(4)]
for j in range(4):
    sum1 = 0
    for i in range(2):
        sum1 += aij_T[i][j] * I_k[i+4]
        Kj[j] = (sum1 - I_k[j])/(Ro * T)

ln_k = [i for i in range(4)]
for j in range(4):
    sum2 = 0
    for i in range(2):
        sum2 += aij_T[i][j] * S_k[i + 4]
    ln_k[j] = (((sum2 - S_k[j])/Ro) - Kj[j])/2.31

omega = []
s_p = 0
while True:
    su = 0
    for i in range(6):
        su += p_d[i]
    svob_ch = [0 for i in range(2)]
    for i in range(2):
        for j in range(6):
            svob_ch[i]+= aij_T[i][j] * p_d[j]

    sv_ch = [0 for i in range(6)]
    for j in range(4):
        su2 = 0
        for i in range(2):
            su2 += aij_T[i][j] * log10(p_d[i+4])
            sv_ch[j] = log10(p_d[j]) - su2 + ln_k[j]
            sv_ch[i+4] = log10(svob_ch[i]) - log10(Mt) - log10(svob_ch[i])

    s_om = log10(su) - log10(p)

    def mopred(matrix, s_ch):
        Matrix = np.array(matrix)
        svob_ch = np.array(s_ch)
        delta = np.linalg.solve(Matrix,svob_ch)
        return delta
    matrix = [[0 for i in range(7)] for j in range(7)]

    for i in range(4):
        for j in range(6):
            matrix[i][j] = aij_M[i][j]

    for i in range(2):
        for j in range(6):
            matrix[i +4][j] = aij_T[i][j] * p_d[j]
    
    for i in range(2):
        matrix[i+ 4][6] = - svob_ch[i]

    for i in range(6):
        matrix[6][i] = p_d[i]

    s_ch = [-sv_ch[0], -sv_ch[1],-sv_ch[2],-sv_ch[3],-sv_ch[4] * svob_ch[0],-sv_ch[5]*svob_ch[1], -s_om * su]
    result = mopred(matrix,s_ch)

    for i in range(6):
        p_d[i] = 10 **(log10(p_d[i])+ result[i])
        if p_d[i] > 1000:
            p_d[i] = 207
    Mt = 10 **(log10(Mt)+ result[6])
    
    s_pr=-sv_ch[0]+ -sv_ch[1]+ -sv_ch[2]+ -sv_ch[3] + -sv_ch[4] + -sv_ch[5] + -s_om
    
    omega.append(abs(s_pr))

    svob_chlen = sum(s_ch) - (-s_om * su)
    pribl +=1
    print(f'Приближение {pribl}')
    for i in matrix:
        print([f"{delta:.4f}" for delta in i])

    if abs(svob_chlen)< 0.001:
        break

    def P_const(cf1, cs1):
        A = np.array(cf1)
        B = np.array(cs1)
        y = np.linalg.solve(A,B)
        return y
    
    cf1 = [[0 for i in range(7)] for j in range(7)]

    for i in range(4):
        for j in range(6):
            cf1[i][j] = aij_M[i][j]

    for i in range(2):
        for j in range(6):
            cf1[i +4][j] = aij_T[i][j] * p_d[j]
        
    for i in range(2):
        cf1[i+ 4][6] = - svob_ch[i]

    for i in range(6):
        cf1[6][i] = p_d[i]
        
    cs1 = [0 for i in range(7)]
    for i in range(4):
        for j in range(4,6):
            cs1[i] = - Kj[i]
            cs1[j] = 0
    cs1[6] = 0
    res1 = np.linalg.solve(cf1, cs1)

    
    def T_const(cf2, cs2):
        A = np.array(cf2)
        B = np.array(cs2)
        z = np.linalg.solve(A,B)
        return z
    cf2 = [[0 for i in range(7)] for j in range(7)]

    for i in range(4):
        for j in range(6):
            cf2[i][j] = aij_M[i][j]

    for i in range(2):
        for j in range(6):
            cf2[i +4][j] = aij_T[i][j] * p_d[j]
        
    for i in range(2):
        cf2[i+ 4][6] = - svob_ch[i]
        
    for i in range(6):
        cf2[6][i] = p_d[i]

    cs2 = [0,0,0,0,0,0,su]


    res2 = T_const(cf2,cs2)
    Mu_t = 1.008 * svob_ch[0] + svob_ch[1] * 16 
    s3= 0
    for j in range(6):
        s3 += (I_k[j]/4.184) * p_d[j]
    I = (s3*4184/(Mt*Mu_t)) 
    s4=0
    for j in range(6):
        s4+= (S_k[j]/4.184) * p_d[j]
    S = (s4*4184/(Mt*Mu_t)) 
    Mu = Mt * Mu_t/p1 
    R = (Ro/Mu)*10**3 
    alpha_p = (1/T)*(1 - res1[6]) 
    betta_t = (1/p1)*(res2[6]) 
    s5 = 0
    for j in range(6):
        s5 += (Cp_k[j]/4.184) * p_d[j]
    cp_f = (s5*4184/(Mt*Mu_t)) 
    k_f = 1/(1-(R/cp_f)) 
    a_f = (T*R*k_f)**0.5 
    s6 = 0
    for j in range(6):
        s6 +=  p_d[j] * (I_k[j]/4.184) *res1[j]
    c_p_e = cp_f+(1/T)*(s6*4184/(Mt *Mu_t) - I*res1[6])
    k_R = c_p_e/(c_p_e - ((R*(1-res1[6])**2)/res2[6])) 
    Matrix =(T*R*k_R/res2[6])**0.5 
    print('')
    b_c = ['H2', 'O2', 'H2O', 'OH', 'H','O']
    for i in range(6):
        print(f'p {b_c[i]} = {p_d[i]:.4f} кг/см2')
    print('')
    print('Частные производные по P')
    for i in range(6):
        print(f' {b_c[i]} = {res1[i]:.4f} кг/см2') 
    print('')
    print('Частные производные по T')
    for i in range(6):
        print(f' {b_c[i]} = {res2[i]:.4f} кг/см2') 
    print(f'Mt ={Mt:.4f} кг/см2') 
    print('') 
    print(f'Число итераций- {pribl}')
    print(f'Mu_t = {Mu_t:.2f} кг/кмоль')
    print(f'I= {I:.0f} Дж/кг')
    print(f'S = {S:.0f} Дж/кг/К')
    print(f'Mu = {Mu:.2f} кг/кмоль')
    print(f'R = {R:.0f} Дж/кг/К')
    print(f'alpha_p = {alpha_p:.6f} 1/K')
    print(f'betta_t = {betta_t:.6f} м2/Н')
    print(f'cp_f = {cp_f:.2f} Дж/кг/К')
    print(f'k_f = {k_f:.4f}')
    print(f'a_f = {a_f:.2f} м/с')
    print(f'c_p_e = {c_p_e:.2f} Дж/кг/К')
    print(f'k_R = {k_R:.4f}')
    print(f'Matrix = {Matrix:.2f} м/с')
        
        # delta = [1,2,3,4,5,6]
        # y = omega
        # plt.figure()
        # plt.plot(delta, y)
        # plt.xlabel('Номер приближения')
        # plt.ylabel('Сумма дельт приближения')
        # plt.title('График значений суммы дельт по приближениям')
        # plt.grid()
        # plt.show()
