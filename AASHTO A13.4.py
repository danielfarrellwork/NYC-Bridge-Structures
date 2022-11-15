'''In this script we are going to follow the design of a bridge railing overhanging the deck.
 for '''

import pandas as pd

n_eta_i = float(input('For N_eta_i load modifier of nonductile component enter == 0.95\n For N_eta_i load modifier of components with additional ductility enter 1.05\n Otherwise use 1'))


class AASHTO_1_3_2():  # Limit States
    #Each component and connection shall satisfy
    # Eq. 1.3.2.1-1 for each limit state, unless otherwise
    # specified. For service and extreme event limit states,
    phi = 1 # resistance factors shall be taken as 1.0  except for bolts, for which the provisions of Article 6.5.5 shall apply, and for concrete columns in Seismic Zones 2, 3, and 4, for which  the provisions of Articles 5.11.3 and 5.11.4.1.2 shall apply.

    def __init__(self, n_eta_i): #gamma_i, Q_i, limit_state, ductility
        self.n_eta_i = n_eta_i # load modifier
        # self.gamma_i = gamma_i # a factor relating to ductility, redundancy, and operational classification
        # self.Q_i = Q_i #
        # self.limit_state = limit_state
        # self.ductility = ductility

    def __str__(self):
        print('Equation 1_3_2 from p 21 in AASHTO 2020')


    @classmethod
    def get_user_input(self):
        inputting = True
        while inputting:
            try:
                n_eta_i = float(input('For N_eta_i load modifier of nonductile component enter == 0.95\n For N_eta_i load modifier of components with additional ductility enter 1.05\n Otherwise use 1: '))
                # print(f'N_eta_i == {n_eta_i}')
                # inputting = False
                return self(n_eta_i)
            except ValueError:
                print('Invalid input!')
                continue
extreme_limit_state = AASHTO_1_3_2.get_user_input()
#
#     def 1_3_2_1_1():
#         if gamma_i == True:
#             gamma_1 = 1
#         R_r = phi * R_n
#         return R_r
T_A13_2_1 = pd.DataFrame({
             'Ft_Transverse_kips'   :[13.5, 27.0, 54.0, 54.0, 124.0, 175.0],
             'FL_Longitudinal_kips' :[4.5, 9.0, 18.0, 18.0, 41.0, 58.0],
             'Fv_Vertical_kips'     :[4.5, 4.5, 4.5, 18.0, 80.0, 80.0],
             'Lt_ft'                :[4.0, 4.0, 4.0, 3.5, 8.0, 8.0],
             'LL_ft'                :[4.0, 4.0, 4.0, 3.5, 8.0, 8.0],
             'Lv_ft'                :[18.0, 18.0, 18.0, 18.0, 40.0, 40.0],
             'He_in_min'            :[18.0, 20.0, 24.0, 32.0, 42.0, 56.0],
             'H_in_min'             :[27.0, 27.0, 27.0, 32.0, 42.0, 90.0],
             }, columns=['Ft_Transverse_kips', 'FL_Longitudinal_kips', 'Fv_Vertical_kips', 'Lt_ft', 'LL_ft', 'He_in_min', 'H_in_min'])  #Design Forces for Traffic Railings
T_A13_2_1.to_csv('T_A13_2_1.csv')
# inputting = True
# while inputting:
#     test_level = input('test level? (1-6):')
#     try:
#         a = int(test_level)
#         if a == 1 or a == 2 or a == 3 or a == 4 or a == 5 or a == 6:
#             inputting = False
#     except:
#         pass
#
# Ft_Transverse_kips      = T_A13_2_1.at[int(test_level)-1, 'Ft_Transverse_kips']
# FL_Longitudinal_kips    = T_A13_2_1.at[int(test_level)-1, 'FL_Longitudinal_kips']
# Fv_Vertical_kips        = T_A13_2_1.at[int(test_level)-1, 'Fv_Vertical_kips']
# Lt_ft                   = T_A13_2_1.at[int(test_level)-1, 'Lt_ft']
# LL_ft                   = T_A13_2_1.at[int(test_level)-1, 'LL_ft']
# He_in_min               = T_A13_2_1.at[int(test_level)-1, 'He_in_min']
# H_in_min                = T_A13_2_1.at[int(test_level)-1, 'H_in_min']
#
# T_13_7_2_1 = pd.DataFrame({
#             'W_kips'            :[1.55, 1.8, 4.5, 18.0, 50.0, 80.0, 80.0],
#             'B_ft'              :[22, 22, 27, 49, 64, 73, 81],
#             'G_in'              :[22, 22, 27, 49, 64, 73, 81],
#             'crash_angle_deg'   :[20, 20, 25, 15, 15, 15, 15],
#             }, columns=['W_kips', 'B_ft', 'G_in', 'crash_angle_deg'])
#
# inputting = True
#
# while inputting:
#     print('using Table 13.7.2-1 NCHRP 350 values')
#     vehicle = input('vehicle? \n1 or 2 = small automobiles\n3 = pickup truck\n4 = Single unit Van truck\n5 = Tractor\n6 = Trailer\n7 = Tanker ')
#     try:
#         a = int(vehicle)
#         if a == 1 or a == 2 or a == 3 or a == 4 or a == 5 or a == 6 or a == 7:
#             inputting = False
#     except:
#         pass
#
# W_kips          = T_13_7_2_1.at[int(vehicle)-1, 'W_kips']
# B_ft            = T_13_7_2_1.at[int(vehicle)-1, 'B_ft']
# G_in            = T_13_7_2_1.at[int(vehicle)-1, 'G_in']
# crash_angle_deg = T_13_7_2_1.at[int(vehicle)-1, 'crash_angle_deg']
#
#
# def A13_2_1():
#     He_in = G_in-(12*W_kips*B_ft/(2*Ft_Transverse_kips))
#     print(f'He = {He_in}"')
#
#
# def A13_2_2():
#     print(f'R_bar must be >= F_t = {Ft_Transverse_kips}')
#
#
# def A13_2_3():
#     print(f'Y_bar must be >= He/12 = {He_in/12}')
#
#
# def A13_2_4():
#     pass# R1 =
#     # R2 =
#     # R3 =
#     # R4 =
#     # R5 =
#     # R_bar = R1+R2+R3+R4
#
# def A13_2_5():
#     pass# Y1 =
#     # Y2 =
#     # Y3 =
#     # Y4 =
#     # Y5 =
#     # Y_bar = (R1*Y1+R2*Y2+R3*Y3+R4*Y4+R5*Y5)/R_bar
#
#
# A13_2_1()
#
#
# def A13_dc_1():
#     gamma_p = 1
#
#
# def A13_dc_1():
#     gamma_p = 1
#
#
# def A13_dc_1():
#     gamma_p = 0
#
#
# def A13_4_1_1():
#     N_eta = []  # load modifier specified in Article 1.3.2
#     gamma = []  # load factors specified in Tables 3.4.1-1 and 3.4.1-2, unless specified elsewhere
#     Q = []  # force effects from loads specified herein
#     for i in Q:
#         Q_factored_total = N_eta[i]*gamma[i]*Q[i]
#
#
# def A13_4_2(R_w_kips, L_c_ft, H_ft):
#     ''' For Design Case 1, the deck overhang may be
#     designed to provide a flexural resistance, Ms, in kip-ft/ft
#     which, acting coincident with the tensile force, T, in kip/ft,
#     specified herein, exceeds Mc of the parapet at its base.'''
#     T_kip_ft = R_w_kips/(L_c_ft+2*H_ft)  # The axial tendile force
#     return T_kip_ft
#
# def A13_4_3_1():
#     # skip
#
#
# def A
#
#
#
