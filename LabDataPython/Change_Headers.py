import pandas as pd 
import numpy as np
import matplotlib as mp

GluUnacc = pd.read_csv("RawData_Python_Glucose_Unacc.csv")
GluAcc = pd.read_csv("RawData_Python_Glucose_Acc.csv")
HSMFW_mi_Acc = pd.read_csv("RawData_Python_HSMFWmarine_Acc.csv")
HSMFW_mi_Unacc = pd.read_csv("RawData_Python_HSMFWmarine_Unacc.csv")
HSMFW_Acc = pd.read_csv("RawData_Python_HSMFW_Acc.csv")
Glucose = [GluAcc,GluUnacc]
HSMFW_MI_RT = [HSMFW_Acc]
HSMFW_MI = [HSMFW_mi_Acc,HSMFW_mi_Acc]
VFA_HSMFW = ["Acetic","Butyric","Caproic","Ethanol","Lactic"]
VFA_Glu = ["Glucose","Acetic","Butyric","Caproic","Ethanol","Lactic"]

#P/V Calculation
def Power_per_Volume(RPM,Volume,PowerNumber,ImpellerDiameter):
    mu = .001
    rho = 1000
    Re = RPM/60*ImpellerDiameter*ImpellerDiameter*rho/mu
    P= PowerNumber*rho*((RPM/60)**3)*(ImpellerDiameter**5)
    PV = round(P*1000/Volume,4)
    return PV

def RenameCol_toPV(df,colname,colsep,PV):
    list_ = colname.split(colsep)
    PV_str = str(PV)
    newname = str(list_[0])+" (" + PV_str + " W/m\u00B3)"
    df = df.rename(columns={colname:newname})
    return df

#Glucose Experiments
df = GluAcc
# df = GluUnacc
for v in VFA_Glu:
    for i in range(0,len(df.columns)-1):
        testname = df.columns[i]  
        list_= testname.split("_")
        if list_[0] == v:
            df = RenameCol_toPV(df,df.columns[i],"_",Power_per_Volume(float(list_[1]),2,3.9,.0397)+Power_per_Volume(float(list_[1]),2,0.4,.045))
GluAcc_Renamed = df[df.columns.drop(list(df.filter(regex="_")))]
GluAcc_Renamed.to_csv("Glucose_Acclimated_NewHeaders.csv")
# GluUnacc_Renamed = df[df.columns.drop(list(df.filter(regex="_")))]
# GluUnacc_Renamed.to_csv("Glucose_Unacclimated_NewHeaders.csv")
GluLowInitial_COD = df[df.columns[2]].iloc[0]
GluHighInitial_COD = df[df.columns[12]].iloc[0]
for i in range(2,20):
    if i <11:
        df[df.columns[i]] = df[df.columns[i]]/GluLowInitial_COD
    else:
        df[df.columns[i]] = df[df.columns[i]]/GluHighInitial_COD
GluAcc_perGlu_Renamed = df[df.columns.drop(list(df.filter(regex="_")))]
GluAcc_perGlu_Renamed.to_csv("Glucose_Acclimated_NewHeaders_PerGlucoseFed.csv")
#HSMFW Experiments, MI & RT
df = HSMFW_Acc
for v in VFA_HSMFW:
    for i in range(0,len(df.columns)-1):
        testname = df.columns[i]  
        list_= testname.split("_")
        if list_[0] == v:
            df = RenameCol_toPV(df,df.columns[i],"_",Power_per_Volume(float(list_[1]),2,3.9,.0397)+Power_per_Volume(float(list_[1]),2,0.4,.045))
HSMFW_Acc_Renamed = df[df.columns.drop(list(df.filter(regex="_")))]
HSMFW_Acc_Renamed.to_csv("HSMFW_Acclimated_NewHeaders.csv")


PV_RT = Power_per_Volume(355,2,0.40,.045)
print(PV_RT)
