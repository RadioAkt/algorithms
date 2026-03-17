import numpy as np
# import matplotlib.pyplot as plt
import math

with open('shab1.txt', 'w', encoding='cp1251') as out_file:

    R_gas = 8.314
    Temperature = 3807.0
    P0 = 207.0
    total_pressure = P0
    base_coeff = [2.0, 0.9] 
    pressures = [P0] * 6   

    enthalpy_species = [119297.7, 130974.9, -66676.8, 159559.7, 290927.6, 322715.9]
    entropy_species = [211.7950, 294.0902, 300.9465, 265.7793, 167.5471, 214.6023]
    heat_capacity_species = [38.72715, 41.53474, 59.81376, 38.19555, 20.78697, 21.19048]

    stoich_main = [
        [2, 0, 2, 1, 1, 0],
        [0, 2, 1, 1, 0, 1]
    ]

    stoich_ext = [
        [1, 0, 0, 0, -2,  0, 0],
        [0, 1, 0, 0,  0, -2, 0],
        [0, 0, 1, 0, -2, -1, 0],
        [0, 0, 0, 1, -1, -1, 0]
    ]

    K_factor = [0.0]*4
    log10K = [0.0]*4
    for j in range(4):
        delta_I = (stoich_main[0][j] * enthalpy_species[4] +
                   stoich_main[1][j] * enthalpy_species[5] -
                   enthalpy_species[j])
        K_factor[j] = delta_I / (R_gas * Temperature)
        delta_S = (stoich_main[0][j] * entropy_species[4] +
                   stoich_main[1][j] * entropy_species[5] -
                   entropy_species[j])
        log10K[j] = ((delta_S / R_gas) - K_factor[j]) / 2.31

    conv_history = []  


    for iteration in range(8):
        sum_pressure = sum(pressures)
        sums_main = [0.0, 0.0]
        for i in range(2):
            for k in range(6):
                sums_main[i] += stoich_main[i][k] * pressures[k]

        free_coeff = [0.0]*6
        for j in range(4):
            s_s_c = 0
            for i in range(2):
                s_s_c += stoich_main[i][j] * math.log10(pressures[i + 4])
                free_coeff[j] = math.log10(pressures[j]) - s_s_c + log10K[j]
                free_coeff[i+4] = (math.log10(sums_main[i]) -
                               math.log10(total_pressure) -
                               math.log10(base_coeff[i]))
        log_ratio = math.log10(sum_pressure) - math.log10(P0)
        matrix = [[0.0]*7 for _ in range(7)]
        for i in range(4):
            for j in range(6):
                matrix[i][j] = stoich_ext[i][j]
        for i in range(2):
            for j in range(6):
                matrix[i+4][j] = stoich_main[i][j] * pressures[j]
        for i in range(2):
            matrix[i+4][6] = -sums_main[i]
        for j in range(6):
            matrix[6][j] = pressures[j]

        constants = [-free_coeff[0], -free_coeff[1], -free_coeff[2], -free_coeff[3], -free_coeff[4] * sums_main[0], -free_coeff[5]* sums_main[1], - log_ratio * sum_pressure]


#         [[1, 0, 0, 0, -2, 0, 0.0], [0, 1, 0, 0, 0, -2, 0.0], [0, 0, 1, 0, -2, -1, 0.0], [0, 0, 0, 1, -1, -1, 0.0], [414, 0, 414, 207, 207, -1242, 0.0], [0, 414, 207, 207, 0, -1035, 0.0], [207, 207, 207, 207, 207, 207, 0.0]]
#           [2.2223838074498192, 2.3170149940612075, 4.963702159576743, 2.467278151610489, -592.5845983618204, -770.7929572180782, -966.4638529764851]
        sol = np.linalg.solve(np.array(matrix), np.array(constants))

        for j in range(6):
            pressures[j] = 10 ** (math.log10(pressures[j]) + sol[j])

        total_pressure = 10 ** (math.log10(total_pressure) + sol[6])


        conv_history.append(abs(-sum(free_coeff) - log_ratio))

        print(f'Приближение {iteration}', file=out_file)
        for row in matrix:
            print([f"{val:.4f}" for val in row], file=out_file)
        if iteration > 6:
            print('', file=out_file)  
            Mu_total = 1.008 * base_coeff[0] + 16.0 * base_coeff[1]
            I_sum = sum((enthalpy_species[k]/4.184) * pressures[k] for k in range(6))
            I_mixture = I_sum * 4184 / (total_pressure * Mu_total)
            S_sum = sum((entropy_species[k]/4.184) * pressures[k] for k in range(6))
            S_mixture = S_sum * 4184 / (total_pressure * Mu_total)
            Mu_mixture = total_pressure * Mu_total / P0
            R_mixture = R_gas * 1000 / Mu_mixture

            deriv_P = np.linalg.solve(np.array(matrix),
                                    np.array([-K_factor[0], -K_factor[1],
                                                -K_factor[2], -K_factor[3],
                                                0.0, 0.0, 0.0]))
            deriv_T = np.linalg.solve(np.array(matrix),
                                    np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                sum(pressures)]))

            cp_mixture = (sum((heat_capacity_species[k]/4.184) * pressures[k] 
                            for k in range(6)) * 4184/(total_pressure*Mu_total))
            alpha_p = (1/Temperature) * (1 - deriv_P[6])
            beta_t = (1/P0) * deriv_T[6]
            s8 = sum(pressures[j] * (enthalpy_species[j]/4.184) * deriv_P[j] for j in range(6))
            cp_effective = cp_mixture + (1/Temperature)*((s8*4184/(total_pressure*Mu_total)) - I_mixture*deriv_P[6])
            k_frozen = 1/(1 - R_mixture/cp_mixture)
            speed_frozen = math.sqrt(Temperature * R_mixture * k_frozen)
            k_R = cp_effective/(cp_effective - (R_mixture*(1-deriv_P[6])**2)/deriv_T[6])
            speed_sound = math.sqrt(Temperature * R_mixture * k_R/deriv_T[6])

            I_mixture = math.ceil(I_mixture)

            print('', file=out_file)
            print('', file=out_file)
            species = ['H2','O2','H2O','OH','H','O']
            for idx, name in enumerate(species):
                print(f'p {name} = {pressures[idx]:.4f} кг/см2', file=out_file)
            print('', file=out_file)
            print('Частные производные по P', file=out_file)
            for idx, name in enumerate(species):
                print(f' {name} = {deriv_P[idx]:.4f} кг/см2', file=out_file)
            print('', file=out_file)
            print('Частные производные по T', file=out_file)
            for idx, name in enumerate(species):
                print(f' {name} = {deriv_T[idx]:.4f} кг/см2', file=out_file)
            print(f'Mt ={total_pressure:.4f} кг/см2', file=out_file)
            print('', file=out_file)
            print(f'Число итераций- {iteration + 1}', file=out_file)
            print(f'Mu_t = {Mu_total:.2f} кг/кмоль', file=out_file)
            print(f'I= {I_mixture:.0f} Дж/кг', file=out_file)
            print(f'S = {S_mixture:.0f} Дж/кг/К', file=out_file)
            print(f'Mu = {Mu_mixture:.2f} кг/кмоль', file=out_file)
            print(f'R = {R_mixture:.0f} Дж/кг/К', file=out_file)
            print(f'alpha_p = {alpha_p:.6f} 1/K', file=out_file)
            print(f'betta_t = {beta_t:.6f} м2/Н', file=out_file)
            print(f'cp_f = {cp_mixture:.2f} Дж/кг/К', file=out_file)
            print(f'k_f = {k_frozen:.4f}', file=out_file)
            print(f'a_f = {speed_frozen:.2f} м/с', file=out_file)
            print(f'c_p_e = {cp_effective:.2f} Дж/кг/К', file=out_file)
            print(f'k_R = {k_R:.4f}', file=out_file)
            print(f'a = {speed_sound:.2f} м/с', file=out_file)

# plt.figure()
# plt.plot(range(1, len(conv_history)+1), conv_history, color='orange', marker='o', linestyle='-')
# plt.xlabel('Номер приближения')
# plt.ylabel('Сумма дельт приближения')
# plt.title('График значений суммы дельт по приближениям')
# plt.grid(True, linestyle='--', alpha=0.8)
# plt.show()
