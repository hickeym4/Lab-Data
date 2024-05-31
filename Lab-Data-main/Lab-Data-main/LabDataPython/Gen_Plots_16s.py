import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("Glu_Unacc_16s.csv")
sample_list = ['Glu_D0', 'Glu_70 RPM_D2', 'Glu_70 RPM_D5', 'Glu_70 RPM_D9','Glu_400 RPM_D2','Glu_400 RPM_D5', 'Glu_400 RPM_D9']
data = data.drop(columns = ['int.slv.Species','int.slv.cnf','int.slv.lws.txn','int.slv.lws.lvl'])
threshold=.05
df = pd.DataFrame()
for i in sample_list:
    newcol = str(i)+" MC?"
    df['Genus']=data.groupby(['int.slv.Genus'], as_index=False)[i].sum()['int.slv.Genus']
    df[i] = data.groupby(['int.slv.Genus'], as_index=False)[i].sum()[i] 
    df[newcol]=(df[i]/df[i]).where(df[i]>threshold)
df["Any_Meet_Criteria?"] = (df["Glu_D0"]-df["Glu_D0"]+1).where((df["Glu_D0 MC?"]==1)|(df["Glu_70 RPM_D2 MC?"]==1)|(df["Glu_70 RPM_D5 MC?"]==1)|\
                                              (df["Glu_70 RPM_D9 MC?"]==1)|(df["Glu_400 RPM_D2 MC?"]==1)|(df["Glu_400 RPM_D5 MC?"]==1)|\
                                               (df["Glu_400 RPM_D9 MC?"]==1))
df=df[df["Any_Meet_Criteria?"]==1]
df=df[['Genus','Glu_D0', 'Glu_70 RPM_D2', 'Glu_70 RPM_D5', 'Glu_70 RPM_D9','Glu_400 RPM_D2','Glu_400 RPM_D5', 'Glu_400 RPM_D9']]
df.to_csv("Glu_Unacc_Filtered_16s.csv")
print(df)

#Plotting
index_ = df["Genus"]
df.index = index_
df = df.drop(columns="Genus")
dft = df.transpose()
dft["Other"] = 1- (dft[dft.columns[0]]+dft[dft.columns[1]]+ dft[dft.columns[2]]+ dft[dft.columns[3]]+ dft[dft.columns[4]]+ \
dft[dft.columns[5]]+ dft[dft.columns[6]]+ dft[dft.columns[7]]+ dft[dft.columns[8]]+ dft[dft.columns[9]])
dft["Other/Uncultured/Unassigned"] = dft["Other"]+dft[dft.columns[8]]+ dft[dft.columns[9]]
dft = dft.drop(columns = ['Other','uncultured','Unassigned'])
dft["Check"] = dft[list(dft.columns)].sum(axis=1)

#(0.37 W/m³)","Day 5 (67.92 W/m³)"
dft["Sample"] = ["Time Zero","Day 2","Day 5","Day 9","Day 2","Day 5","Day 9"]
y1, y2, y3, y4, y5, y6, y7, y8,y0 = dft[dft.columns[1]], dft[dft.columns[2]], dft[dft.columns[3]], dft[dft.columns[4]], \
dft[dft.columns[5]], dft[dft.columns[6]], dft[dft.columns[7]], dft[dft.columns[8]], dft[dft.columns[0]]

plt.rcParams["font.family"]= "Times New Roman"
plt.rcParams["font.size"] = 8

dft = dft.drop(columns="Check")
ax = dft.plot(x='Sample',kind='bar',stacked=True,rot=0)
sec = ax.secondary_xaxis(location=0)
sec.set_xticks([1,2,5],labels=['','\n\n\n0.37 W/m³','\n\n\n67.92 W/m³'])
sec.tick_params('x',length=0,width=0)
sec2 = ax.secondary_xaxis(location=0)
sec2.set_xticks([-0.5,0.5,3.5,6.5])
sec2.tick_params('x',length=40,width=0.75)


for c in ax.containers:
    labels=[round(v.get_height(),2) if v.get_height() >0.11 else '' for v in c]
    ax.bar_label(c,labels=labels, label_type='center')
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles[::-1], labels[::-1] ,bbox_to_anchor=(1.05,1),loc='upper left')
plt.subplots_adjust(right=0.6)
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.22)
plt.ylabel("Relative Abundance")
plt.xlabel("")
plt.savefig('16s_Glucose_Unacc.png',dpi=1200)

plt.show()
