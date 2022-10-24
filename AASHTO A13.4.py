'''In this script we are going to follow the design of a bridge railing overhanging the deck.  '''

import pandas as pd



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
inputting = True
while inputting:
    test_level = input('test level? (1-6):')
    try:
        a = int(test_level)
        if a == 1 or a == 2 or a == 3 or a == 4 or a == 5 or a == 6:
            inputting = False
    except:
        pass

Ft_Transverse_kips      = T_A13_2_1.at[int(test_level)-1, 'Ft_Transverse_kips']
FL_Longitudinal_kips    = T_A13_2_1.at[int(test_level)-1, 'FL_Longitudinal_kips']
Fv_Vertical_kips        = T_A13_2_1.at[int(test_level)-1, 'Fv_Vertical_kips']
Lt_ft                   = T_A13_2_1.at[int(test_level)-1, 'Lt_ft']
LL_ft                   = T_A13_2_1.at[int(test_level)-1, 'LL_ft']
He_in_min               = T_A13_2_1.at[int(test_level)-1, 'He_in_min']
H_in_min                = T_A13_2_1.at[int(test_level)-1, 'H_in_min']

T_13_7_2_1 = pd.DataFrame({
            'W_kips'            :[1.55, 1.8, 4.5, 18.0, 50.0, 80.0, 80.0],
            'B_ft'              :[22, 22, 27, 49, 64, 73, 81],
            'G_in'              :[22, 22, 27, 49, 64, 73, 81],
            'crash_angle_deg'   :[20, 20, 25, 15, 15, 15, 15],
            }, columns=['W_kips', 'B_ft', 'G_in', 'crash_angle_deg'])

inputting = True

while inputting:
    print('using Table 13.7.2-1 NCHRP 350 values')
    vehicle = input('vehicle? \n1 or 2 = small automobiles\n3 = pickup truck\n4 = Single unit Van truck\n5 = Tractor\n6 = Trailer\n7 = Tanker ')
    try:
        a = int(vehicle)
        if a == 1 or a == 2 or a == 3 or a == 4 or a == 5 or a == 6 or a == 7:
            inputting = False
    except:
        pass

W_kips          = T_13_7_2_1.at[int(vehicle)-1, 'W_kips']
B_ft            = T_13_7_2_1.at[int(vehicle)-1, 'B_ft']
G_in            = T_13_7_2_1.at[int(vehicle)-1, 'G_in']
crash_angle_deg = T_13_7_2_1.at[int(vehicle)-1, 'crash_angle_deg']


def A13_2_1():
    He_in = G_in-(12*W_kips*B_ft/(2*Ft_Transverse_kips))
    print(f'He = {He_in}"')


def A13_2_2():
    print(f'R_bar must be >= F_t = {Ft_Transverse_kips}')


def A13_2_3():
    print(f'Y_bar must be >= He/12 = {He_in/12}')


def A13_2_4():
    pass# R1 =
    # R2 =
    # R3 =
    # R4 =
    # R5 =
    # R_bar = R1+R2+R3+R4

def A13_2_5():
    pass# Y1 =
    # Y2 =
    # Y3 =
    # Y4 =
    # Y5 =
    # Y_bar = (R1*Y1+R2*Y2+R3*Y3+R4*Y4+R5*Y5)/R_bar


A13_2_1()


def A13_dc_1():
    gamma_p = 1


def A13_dc_1():
    gamma_p = 1

def A13_dc_1():
    gamma_p = 0
