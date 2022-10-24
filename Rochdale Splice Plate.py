# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:40:11 2022
Unless stated otherwise all references refer to AISC manual 15th edition
@author: USDF659971
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %% import existing members from a revit csv output edited in excel
revit_members = pd.DataFrame([
    ['W14X38', 187.71, 5.0625, '2D2C', 'EAST', 23, 0, 0, 0, False],
    ['W14X38', 631.74, 16.8958333333333, '2D2C', 'WEST', 77, 0, 0, 0, False],
    ['W14X38', 749.76, 20.0416666666667, '2E2D', 'EAST', 91, 10, 11.25, 3 / 8, False],
    ['W14X38', 297.91, 7.5, '2E2D', 'WEST', 36, 10, 11.25, 3 / 8, False],
    ['W14X38', 749.76, 20.0416666666667, '3E3D', 'EAST', 91, 10, 11.25, 3 / 8, True],
    ['W14X38', 297.91, 8, '3E3D', 'WEST', 36, 10, 11.25, 3 / 8, True],
    ['W10X22', 58.85, 2.75, '3J3I', 'EAST', 10, 10, 11.25, 3 / 8, True],
    ['W10X22', 397.2, 18.25, '3J3I', 'WEST', 65, 10, 11.25, 3 / 8, True],
    ['W14X38', 749.65, 20.0416666666667, '4E4D', 'EAST', 91, 10, 11.25, 3 / 8, True],
    ['W14X38', 297.91, 8, '4E4D', 'WEST', 36, 10, 11.25, 3 / 8, True],
    ['W14X38', 749.65, 20.0416666666667, '5E5D', 'EAST', 91, 10, 11.25, 3 / 8, True],
    ['W14X38', 297.91, 8, '5E5D', 'WEST', 36, 10, 11.25, 3 / 8, True],
    ['W10X22', 58.85, 2.75, '5J5I', 'EAST', 10, 10, 11.25, 3 / 8, True],
    ['W10X22', 397.27, 18.25, '5J5I', 'WEST', 65, 10, 11.25, 3 / 8, True],
    ['W14X38', 748.87, 20.0416666666667, '6E6D', 'EAST', 91, 10, 11.25, 3 / 8, True],
    ['W14X38', 297.13, 8, '6E6D', 'WEST', 36, 10, 11.25, 3 / 8, True],
    ['W24X68', 688.18, 10.25, '6J6I', 'EAST', 70, 10, 11.25, 3 / 8, True],
    ['W27X102', 1707.98, 16.9583333333333, '6J6I', 'WEST', 131, 10, 11.25, 3 / 8, True],
    ['W10X22', 109.28, 5.0625, '7D7C', 'EAST', 18, 10, 11.25, 3 / 8, True],
    ['W10X22', 367.68, 16.8958333333333, '7D7C', 'WEST', 60, 10, 11.25, 3 / 8, True],
    ['W14X38', 749.65, 20.0416666666667, '7E7D', 'EAST', 91, 10, 11.25, 3 / 8, True],
    ['W14X38', 297.91, 8, '7E7D', 'WEST', 36, 10, 11.25, 3 / 8, True],
    ['W10X22', 58.85, 2.75, '7J7I', 'EAST', 10, 10, 11.25, 3 / 8, True],
    ['W10X22', 397.27, 18.25, '7J7I', 'WEST', 65, 10, 11.25, 3 / 8, True],
    ['W14X48', 974.03, 20.75, '7K7J', 'EAST', 102, 10, 11.25, 3 / 8, True],
    ['W14X48', 373.3, 8, '7K7J', 'WEST', 39, 10, 11.25, 3 / 8, True],
    ['W14X38', 749.65, 20.0416666666667, '8E8D', 'EAST', 91, 10, 11.25, 3 / 8, True],
    ['W14X38', 297.91, 8, '8E8D', 'WEST', 36, 10, 11.25, 3 / 8, True],
    ['W24X68', 1228.4, 18.25, '8J8I', 'WEST', 125, 10, 11.25, 3 / 8, True],
    ['W24X68', 603.77, 9, '8J81', 'EAST', 61, 10, 11.25, 3 / 8, True],
    ['W14X38', 749.65, 20.0416666666667, '9E9D', 'EAST', 91, 10, 11.25, 3 / 8, True],
    ['W14X38', 297.91, 8, '9E9D', 'WEST', 36, 10, 11.25, 3 / 8, True],
    ['W10X22', 58.85, 2.75, '9J9I', 'EAST', 10, 10, 11.25, 3 / 8, True],
    ['W10X22', 397.2, 18.25, '9J9I', 'WEST', 65, 10, 11.25, 3 / 8, True],
    ['W16X40', 821.19, 20.75, '9K9J', 'EAST', 103, 10, 11.25, 3 / 8, True],
    ['W16X40', 313.94, 8, '9K9J', 'WEST', 39, 10, 11.25, 3 / 8, True],
    ['W14X38', 748.87, 20.0416666666667, '10E10D', 'EAST', 91, 10, 11.25, 3 / 8, True],
    ['W14X38', 297.13, 8, '10E10D', 'WEST', 36, 10, 11.25, 3 / 8, True],
    ['W24X55', 487.18, 9, '10J10I', 'EAST', 56, 10, 11.25, 3 / 8, True],
    ['W24X55', 990.85, 18.25, '10J10I', 'WEST', 113, 10, 11.25, 3 / 8, True],
    ['W14X48', 973.89, 20.75, '10K10J', 'EAST', 102, 10, 11.25, 3 / 8, True],
    ['W14X48', 373.3, 8, '10K10J', 'WEST', 39, 10, 11.25, 3 / 8, True]])
# rename columns
revit_columns = {0: "AISC_Manual_Label", 1: "TOTAL_WEIGHT", 2: 'LENGTH_FT', 3: 'COMMENTS', 4: 'SIDE', 5: 'PAINT_AREA',
                 6: 'SPLICE_X', 7: 'SPLICE_Y', 8: 'SPLICE_T', 9: 'DOUBLE_SIDED'}
revit_members = revit_members.rename(revit_columns, axis="columns")
# get a list of unique existing members
unique_revit_members = set(list(revit_members['AISC_Manual_Label']))
# import the AISC shapes database
Aisc_df = pd.read_excel(
    r"q:\STR\Structures\Structures Library\AISC (DO NOT DELETE OR MOVE)\aisc-shapes-database-v15.0.xlsx",
    sheet_name="Database v15.0", usecols="A:CF")
filtered_Aisc = Aisc_df[Aisc_df['AISC_Manual_Label'].isin(unique_revit_members)]
# merger the two dataframes into one with a AISC manual row corresponding to the member id
revit_aisc_merged = pd.merge(revit_members, Aisc_df, how='left', on='AISC_Manual_Label')
# trim the df to only include imperial measurments & revit columns revit_columns.count()
revit_aisc_merged = revit_aisc_merged[0:83 + revit_members.shape[1]]
# now the members and splices imported from revit each have their associated member properties includeded in each row according to the AISC manual V15
# %%
mn

# %% bending assume the strong axis under ASD
gamma_b
Cb = 1.0  # F1-1 assume uniform moment

# %%non compact check
noncompact_shapes = ['W21X48', 'W14X99', 'W14X90', 'W12X65', 'W10X12', 'W8X31', 'W8X10', 'W6X15', 'W6X9', 'W6X8.5',
                     'M4X6']
filtered_manual = revit_merged_pull_df[revit_merged_pull_df['AISC_Manual_Label'].isin([noncompact_shapes)]
Fy_ksi = 50  # F.2.1
E_ksi = 29000  # General nomenclature
width_thickness_ratio = b / t  # Case 1 Table B4.1a
limiting_width_thickness_ratio = 0.56 * sqrt(E_ksi / F_ksi)
filtered
manual[Mp] = Fy * filtered_manual[Zx]
filtered
manual[Mp] = Fy * filtered_manual[Zx]
Mn = Mp
ry = \
    Lp = 300 * ry / (sqrt(Fy_ksi))


def bending_moments(Sx_in3):
    if Lb <= Lp, ;:
        ASD_bending = 0.66 * Fy_ksi * Sx_in3

    elif Lp < Lb and Lb <= Lr:
        ASD_bending = "use linear interpolation"
    elif Lb = Lr;:
        ASD_bending = 0.42 * Fy_ksi * Sx_in3
    else ;
    print('failed to sort length')


Ma =
dm
Paf = Ma / dm

