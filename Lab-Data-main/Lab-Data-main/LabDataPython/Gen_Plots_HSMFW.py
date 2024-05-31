import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

HSMFW_Acc = pd.read_csv("LabDataPython/HSMFW_Acclimated_NewHeaders.csv")
HSMFW_Acc = HSMFW_Acc.fillna(0)
HSMFW_Unacc = pd.read_csv("LabDataPython/HSMFW_Unacclimated_NewHeaders.csv")
HSMFW_Unacc = HSMFW_Unacc.fillna(0)
plt.rcParams["font.family"]= "Times New Roman"
x1 = HSMFW_Acc["Day"]
x2 = HSMFW_Unacc["Day"]
print(HSMFW_Acc)
print(HSMFW_Unacc)
######################################
#Not converted to per-gram-substrate
######################################

#COMPARE ACETIC
#Acclimated
y = HSMFW_Acc.iloc[:,3]
y2 = HSMFW_Acc.iloc[:,8]
label1_list = HSMFW_Acc.columns[3].split(" (")
label1 = "Acclimated ("+label1_list[1]
label2_list = HSMFW_Acc.columns[8].split(" (")
label2 = "Acclimated ("+label2_list[1]
plt.plot(x1,y,marker='o',color="b",label=label1)
plt.plot(x1,y2,marker='x',color="r",label=label2)
#Unacclimated
y3 = HSMFW_Unacc.iloc[:,3]
y4 = HSMFW_Unacc.iloc[:,8]
label3_list = HSMFW_Unacc.columns[3].split(" (")
label3 = "Unacclimated ("+label3_list[1]
label4_list = HSMFW_Unacc.columns[8].split(" (")
label4 = "Unacclimated ("+label4_list[1]
plt.plot(x2,y3,linestyle='--',marker="o",color='b',label=label3)
plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
#Titles, axis, etc.
plt.title("Substrate: HSMFW",loc="right")
plt.xlabel("Day")
plt.ylabel("Acetic Acid (g/L)")
plt.legend(loc="lower right")
plt.ylim(0,2)
plt.xlim(0,12)
plt.savefig('LabDataPython/Acetic_HSMFW_Acc_Unacc.png',dpi=1200)
plt.show()

# COMPARE BUTYRIC
# Acclimated
# y = HSMFW_Acc.iloc[:,4]
# y2 = HSMFW_Acc.iloc[:,9]
# label1_list = HSMFW_Acc.columns[5].split(" (")
# label1 = "Acclimated ("+label1_list[1]
# label2_list = HSMFW_Acc.columns[10].split(" (")
# label2 = "Acclimated ("+label2_list[1]
# plt.plot(x1,y,marker='o',color="b",label=label1)
# plt.plot(x1,y2,marker='x',color="b",label=label2)
# #Unacclimated
# y3 = HSMFW_Unacc.iloc[:,4]
# y4 = HSMFW_Unacc.iloc[:,9]
# label3_list = HSMFW_Unacc.columns[4].split(" (")
# label3 = "Unacclimated ("+label3_list[1]
# label4_list = HSMFW_Unacc.columns[9].split(" (")
# label4 = "Unacclimated ("+label4_list[1]
# plt.plot(x2,y3,linestyle='--',marker="o",color='r',label=label3)
# plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
# #Titles, axis, etc.
# plt.title("Substrate: HSMFW", loc="left")
# plt.xlabel("Day")
# plt.ylabel("Butyric Acid (g/L)")
# plt.legend(loc="lower right")
# plt.ylim(0,2)
# plt.xlim(0,12)
# plt.savefig('LabDataPython/Butyric_HSMFW_Acc_Unacc.png',dpi=1200)
# plt.show()

# #COMPARE CAPROIC
# #Acclimated
# y = HSMFW_Acc.iloc[:,5]
# y2 = HSMFW_Acc.iloc[:,10]
# label1_list = HSMFW_Acc.columns[5].split(" (")
# label1 = "Acclimated ("+label1_list[1]
# label2_list = HSMFW_Acc.columns[10].split(" (")
# label2 = "Acclimated ("+label2_list[1]
# plt.plot(x1,y,marker='o',color="b",label=label1)
# plt.plot(x1,y2,marker='x',color="b",label=label2)
# #Unacclimated
# y3 = HSMFW_Unacc.iloc[:,5]
# y4 = HSMFW_Unacc.iloc[:,10]
# label3_list = HSMFW_Unacc.columns[5].split(" (")
# label3 = "Unacclimated ("+label3_list[1]
# label4_list = HSMFW_Unacc.columns[10].split(" (")
# label4 = "Unacclimated ("+label4_list[1]
# plt.plot(x2,y3,linestyle='--',marker="o",color='r',label=label3)
# plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
# #Titles, axis, etc.
# plt.title("Substrate: HSMFW", loc="left")
# plt.xlabel("Day")
# plt.ylabel("Caproic Acid (g/L)")
# plt.legend(loc="upper right")
# plt.ylim(0,1)
# plt.xlim(0,12)
# plt.savefig('LabDataPython/Caproic_HSMFW_Acc_Unacc.png',dpi=1200)
# plt.show()

# #COMPARE Total VFA's
# #Acclimated
# y = HSMFW_Acc[HSMFW_Acc.columns[3]]+HSMFW_Acc[HSMFW_Acc.columns[4]]+HSMFW_Acc[HSMFW_Acc.columns[5]]
# y2 = HSMFW_Acc[HSMFW_Acc.columns[8]]+HSMFW_Acc[HSMFW_Acc.columns[9]]+HSMFW_Acc[HSMFW_Acc.columns[10]]
# label1_list = HSMFW_Acc.columns[3].split(" (")
# label1 = "Acclimated ("+label1_list[1]
# label2_list = HSMFW_Acc.columns[8].split(" (")
# label2 = "Acclimated ("+label2_list[1]
# plt.plot(x1,y,marker='o',color="b",label=label1)
# plt.plot(x1,y2,marker='x',color="b",label=label2)
# #Unacclimated
# y3 = HSMFW_Unacc[HSMFW_Unacc.columns[3]]+HSMFW_Unacc[HSMFW_Unacc.columns[4]]+HSMFW_Unacc[HSMFW_Unacc.columns[5]]
# y4 = HSMFW_Unacc[HSMFW_Unacc.columns[8]]+HSMFW_Unacc[HSMFW_Unacc.columns[9]]+HSMFW_Unacc[HSMFW_Unacc.columns[10]]
# label3_list = HSMFW_Unacc.columns[3].split(" (")
# label3 = "Unacclimated ("+label3_list[1]
# label4_list = HSMFW_Unacc.columns[8].split(" (")
# label4 = "Unacclimated ("+label4_list[1]
# plt.plot(x2,y3,linestyle='--',marker="o",color='r',label=label3)
# plt.plot(x2,y4,linestyle='--',marker="x",color='r',label=label4)
# #Titles, axis, etc.
# plt.title("Substrate: HSMFW", loc="left")
# plt.xlabel("Day")
# plt.ylabel("Total VFA's (g/L)")
# plt.legend(loc="lower right")
# plt.ylim(0,5)
# plt.xlim(0,12)
# plt.savefig('LabDataPython/TotalVFA_HSMFW_Acc_Unacc.png',dpi=1200)
# plt.show()
