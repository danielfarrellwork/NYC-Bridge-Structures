def Shape_Factor():
    import pandas as pd
    Aisc_df = pd.read_excel(
        r"q:\STR\Structures\Structures Library\AISC (DO NOT DELETE OR MOVE)\aisc-shapes-database-v15.0.xlsx",
        sheet_name="Database v15.0", usecols="A:CF")
    Aisc_h_df = pd.read_excel(
        r"q:\STR\Structures\Structures Library\AISC (DO NOT DELETE OR MOVE)\aisc-shapes-database-v15.0h.xlsx",
        sheet_name="Database v15.0H", usecols="A:CF")
    member = str(input("Member ID in AISC_Manual_Label format: "))
    go = False
    while go == False:
        database = input("Historical Shape? (y/n): ")
        if database =='y':
            member_df = Aisc_df.loc[[Aisc_df['AISC_Manual_Label']==member]]
            member_df = Aisc_df + member_df
            go = False
        elif database =='n':
            member_df = Aisc_h_df.loc[[Aisc_h_df['AISC_Manual_Label']==member]]
            member_df = Aisc_h_df + member_df
            go = False
        else:
            go = True
    shape_factor=member_df['S']/member_df['Z']
    if member[0] == "L":
        shape_factor = 1.5
    else:
        pass
    return shape_factor

Shape_Factor()