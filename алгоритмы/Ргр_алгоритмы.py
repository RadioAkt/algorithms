import numpy as np
import math
import matplotlib.pyplot as plt
with open('rez.txt', 'w', encoding='UTF8') as out_file:

    Ro = 8.314
    itr = 0
    T = 3807
    p = p1= Mt =  207
    v = 0.9
    b = [2, v]
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

    kj = [0 for i in range(4)]
    for j in range(4):
        s_1 = 0
        for i in range(2):
            s_1 += aij_T[i][j] * I_k[i + 4]
            kj[j] = (s_1 - I_k[j]) / (T * Ro)

    ln_k = [0 for i in range(4)]
    for j in range(4):
        s_2 = 0
        for i in range(2):
            s_2 += aij_T[i][j] * S_k[i + 4]
            ln_k[j] = (((s_2 - S_k[j]) / Ro) - kj[j]) / 2.31

    Itog = []


    while True:
        sump = 0
        for i in range(6):
            sump += p_d[i]
        B_h_o = [0 for i in range(2)]
        for i in range(2):
            for j in range(6):
                B_h_o[i] += aij_T[i][j] * p_d[j]

        
        sv_ch = [0 for i in range(6)]
        for j in range(4):
            su1 = 0
            for i in range(2):
                su1 += aij_T[i][j] * math.log10(p_d[i + 4])
                sv_ch[j] = math.log10(p_d[j]) - su1 + ln_k[j]
                sv_ch[i + 4] = math.log10(B_h_o[i]) - math.log10(Mt) - math.log10(b[i])

        s_sp = math.log10(sump) - math.log10(p)
        
        matrix = [[0] * 7 for _ in range(7)]
        for i in range(4):
            for j in range(6):
                matrix[i][j] = aij_M[i][j]
        for i in range(2):
            for j in range(6):
                matrix[i + 4][j] = aij_T[i][j] * p_d[j]
        for i in range(2):
            matrix[i + 4][6] = -B_h_o[i]
        for j in range(6):
            matrix[6][j] = p_d[j]

        const = []
        for i in range(6):
                if i < 4:
                    const.append(-sv_ch[i])
                else:
                    const.append(-sv_ch[i] * B_h_o[i - 4])
        const.append(-s_sp * sump)


        mopred = np.linalg.solve(np.array(matrix), np.array(const))

        for j in range(6):
            p_d[j] = 10 ** (math.log10(p_d[j]) + mopred[j])
            if p_d[j] > 1000:
                p_d[j] = 207
        Mt = 10 ** (math.log10(Mt) + mopred[6])

        sum_pr = [0 for i in range(7)]
        for i in range(6):
            sum_pr[i] = -sv_ch[i]
        sum_pr[-1] = -s_sp
        s_pr = sum(sum_pr)

        Itog.append(abs(s_pr))


        svob_ch = sum(const) - (-s_sp * sump)
        pribl += 1

        print(f'Приближение {pribl}', file=out_file)
        for r in matrix:
            print([f"{x:.4f}" for x in r], file=out_file)

        if abs(svob_ch)< 0.000001:
            break 
    print('', file=out_file) 
    
    Mu_t = 2 * 1.008 + b[1] * 16
    I = sum((I_k[k] / 4.184) * p_d[k] for k in range(6))
    I_itog = math.ceil(I * 4184 / (Mt * Mu_t))
    S = sum((S_k[k] / 4.184) * p_d[k] for k in range(6))
    S_itog = (S * 4184) / (Mt * Mu_t)
    Mu_itog = (Mt * Mu_t) / p
    R_itog = (Ro * 1000) / Mu_itog

    p_m = [0 for i in range(7)]
    for i in range(4):
        p_m[i] = -kj[i]
    P_matrix = np.linalg.solve(np.array(matrix), np.array(p_m))

    
    t_m = [0 for i in range(7)]
    t_m[-1] = sum(p_d)
    T_matrix = np.linalg.solve(np.array(matrix), np.array(t_m))

    cp_f = (sum((Cp_k[k]/ 4.184) * p_d[k] for k in range(6)) * 4184 / (Mt * Mu_t))


    alpha_p = (1 / T) * (1 - P_matrix[6])
    beta_t = (1 / p) * T_matrix[6]

    sum_I_n = sum(p_d[j] * (I_k[j] / 4.184) * P_matrix[j] for j in range(6))
    c_pe = cp_f + (1 / T) * ((sum_I_n * 4184 / (Mt * Mu_t)) - I_itog * P_matrix[6])

    k_f = 1 / (1 - R_itog / cp_f)
    a_f = (k_f * R_itog * T) ** 0.5
    k_r = c_pe / (c_pe - (R_itog * ((1 - P_matrix[6]) ** 2)) / T_matrix[6])
    a = math.sqrt((k_r * R_itog * T) / T_matrix[6])

    print('', file=out_file)
    print('', file=out_file)
    elem = ['H2','O2','H2O','OH','H','O']

    for id, name in enumerate(elem):
        print(f'p {name} = {p_d[id]:.4f} кг/см2', file=out_file)
    print('', file=out_file)
    print('Частные производные по P', file=out_file)
    for id, name in enumerate(elem):
        print(f' {name} = {P_matrix[id]:.4f} кг/см2', file=out_file)
    print('', file=out_file)
    print('Частные производные по T', file=out_file)
    for id, name in enumerate(elem):
        print(f' {name} = {T_matrix[id]:.4f} кг/см2', file=out_file)
    print(f'Mt ={Mt:.4f} кг/см2', file=out_file)
    print('', file=out_file)
    print(f'Число итераций- {pribl}', file=out_file)
    print(f'Mu_t = {Mu_t:.2f} кг/кмоль', file=out_file)
    print(f'I= {I_itog:.0f} Дж/кг', file=out_file)
    print(f'S = {S_itog:.0f} Дж/кг/К', file=out_file)
    print(f'Mu = {Mu_itog:.2f} кг/кмоль', file=out_file)
    print(f'R = {R_itog:.0f} Дж/кг/К', file=out_file)
    print(f'alpha_p = {alpha_p:.6f} 1/K', file=out_file)
    print(f'betta_t = {beta_t:.6f} м2/Н', file=out_file)
    print(f'cp_f = {cp_f:.2f} Дж/кг/К', file=out_file)
    print(f'k_f = {k_f:.4f}', file=out_file)
    print(f'a_f = {a_f:.2f} м/с', file=out_file)
    print(f'c_p_e = {c_pe:.2f} Дж/кг/К', file=out_file)
    print(f'k_R = {k_r:.4f}', file=out_file)
    print(f'a = {a:.2f} м/с', file=out_file)


plt.figure()
plt.plot(range(1, len(Itog)+1), Itog, color='orange', marker='o', linestyle='-')
plt.xlabel('Номер приближения')
plt.ylabel('Сумма дельт приближения')
plt.title('График значений суммы дельт по приближениям')
plt.grid(True, linestyle='--', alpha=0.9)
plt.show()
