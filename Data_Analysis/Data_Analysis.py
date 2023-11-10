"------------------------------------------------------------------------------------------------------------------"
"                                                                                                                  "
"                                          Statistical Analysis (PythonScript)                                     " 
"                                               Version: 0.1 05/16/2023                                            "
"                                                    Master Thesis                                                 "
"                                            Created by: Jerome Trudel-Brais                                       "
"                                                                                                                  "
"------------------------------------------------------------------------------------------------------------------"

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas as pd
from statsmodels.stats.anova import AnovaRM
import pingouin as pg
import seaborn as sns
import scipy
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.multivariate.manova import MANOVA
from scipy.stats import shapiro, levene, bartlett
import nolds

"0. Graphs"
"0.1 Temperature"
"0.1.1 Data : All - Location : Combined"
# NumValue = range(len(data['Test1']['Temperature']['_Combined']['_OneWeek']['_time']))
# thicks = [NumValue[i] for i in range(len(NumValue)) if i % 1052 == 0]
# ticks_label = range(0,168,20) 
# plt.plot(data['Test1']['Temperature']['_Combined']['_OneWeek']['_valueNanRemove'], label = 'Location 1')
# plt.plot(data['Test2']['Temperature']['_Combined']['_OneWeek']['_valueNanRemove'], label = 'Location 2')
# plt.plot(range(200,8618+200),data['Test3']['Temperature']['_Combined']['_valueNanRemove'], label = 'Location 3')
# plt.plot(data['Test4']['Temperature']['_Combined']['_OneWeek']['_valueNanRemove'], label = 'Location 4')
# plt.plot(data['Test5']['Temperature']['_Combined']['_OneWeek']['_valueNanRemove'], label = 'Location 5')
# plt.ylabel('Temperature ($^\circ$C)', fontsize=22)
# plt.xlabel('Time (hours)', fontsize=22)
# plt.xticks(thicks, labels = ticks_label, fontsize=22)
# plt.yticks(fontsize=22)
# plt.xlim([0,8500])
# plt.ylim([17.5,30])
# plt.legend(loc ='best',prop={'size': 12})
# plt.show()

"0.1.2 Data : 5-minutes average - Location : Combined"
# NumValue = range(len(data['Test1']['Temperature']['_OneWeek']['_combined']['_5minutes']))
# thicks = [NumValue[i] for i in range(len(NumValue)) if i % 240 == 0]
# ticks_label = range(0,168,20)
# plt.plot(data['Test1']['Temperature']['_OneWeek']['_combined']['_5minutes'], label = 'Location 1')
# plt.plot(data['Test2']['Temperature']['_OneWeek']['_combined']['_5minutes'], label = 'Location 2')
# plt.plot(range(50,2016+50),data['Test3']['Temperature']['_OneWeek']['_combined']['_5minutes'], label = 'Location 3')
# plt.plot(data['Test4']['Temperature']['_OneWeek']['_combined']['_5minutes'], label = 'Location 4')
# plt.plot(data['Test5']['Temperature']['_OneWeek']['_combined']['_5minutes'], label = 'Location 5')
# plt.ylabel('Temperature ($^\circ$C)', fontsize=22)
# plt.xlabel('Time (hours)', fontsize=22)
# plt.xticks(thicks, labels = ticks_label, fontsize=22)
# plt.yticks(fontsize=22)
# plt.xlim([0,2000])
# plt.ylim([17.5,30])
# plt.legend(loc ='best',prop={'size': 12})
# plt.show()

"0.1.3 Data : 60-minutes average - Location : Combined"
# NumValue = range(0,168)
# thicks = [NumValue[i] for i in range(len(NumValue)) if i % 20 == 0]
# ticks_label = range(0,168,20)
# plt.plot(data['Test1']['Temperature']['_Combined']['_OneWeek']['_avg60'], label = 'Location 1')
# plt.plot(data['Test2']['Temperature']['_Combined']['_OneWeek']['_avg60'], label = 'Location 2')
# plt.plot(range(3,168+3), data['Test3']['Temperature']['_Combined']['_avg60'], label = 'Location 3')
# plt.plot(data['Test4']['Temperature']['_Combined']['_OneWeek']['_avg60'], label = 'Location 4')
# plt.plot(data['Test5']['Temperature']['_Combined']['_OneWeek']['_avg60'], label = 'Location 5')
# plt.ylabel('Temperature ($^\circ$C)', fontsize=22)
# plt.xlabel('Temps (hours)', fontsize=22)
# plt.xticks(thicks, labels = ticks_label, fontsize=22)
# plt.yticks(fontsize=22)
# plt.xlim([0,168])
# plt.ylim([17.5,30])
# plt.legend(loc ='best',prop={'size': 12})
# plt.show()
'----------------------------------------------------------------------------'
"0.2 CO2"
"0.2.1 Data : All - Location : Combined"
# NumValue = range(len(data['Test1']['Temperature']['_Combined']['_OneWeek']['_time']))
# thicks = [NumValue[i] for i in range(len(NumValue)) if i % 1052 == 0]
# ticks_label = range(0,168,20)
# plt.plot(data['Test1']['CO2']['_Combined']['_OneWeek']['_valueNanRemove'], label = 'Location 1')
# plt.plot(data['Test2']['CO2']['_Combined']['_OneWeek']['_valueNanRemove'], label = 'Location 2')
# plt.plot(range(200,8618+200),data['Test3']['CO2']['_Combined']['_valueNanRemove'], label = 'Location 3')
# plt.plot(data['Test4']['CO2']['_Combined']['_OneWeek']['_valueNanRemove'], label = 'Location 4')
# plt.plot(data['Test5']['CO2']['_Combined']['_OneWeek']['_valueNanRemove'], label = 'Location 5')
# plt.ylabel('CO2 (ppm)', fontsize=22)
# plt.xlabel('Temps (hours)', fontsize=22)
# plt.xticks(thicks, labels = ticks_label, fontsize=22)
# plt.yticks(fontsize=22)
# plt.xlim([0,8500])
# plt.ylim([380,800])
# plt.legend(loc ='best',prop={'size': 12})
# plt.show()

"0.2.2 Data : 5-minutes average - Location : Combined"
# NumValue = range(len(data['Test1']['Temperature']['_OneWeek']['_combined']['_5minutes']))
# thicks = [NumValue[i] for i in range(len(NumValue)) if i % 240 == 0]
# ticks_label = range(0,168,20)
# plt.plot(data['Test1']['CO2']['_OneWeek']['_combined']['_5minutes'], label = 'Location 1')
# plt.plot(data['Test2']['CO2']['_OneWeek']['_combined']['_5minutes'], label = 'Location 2')
# plt.plot(range(50,2016+50),data['Test3']['CO2']['_OneWeek']['_combined']['_5minutes'], label = 'Location 3')
# plt.plot(data['Test4']['CO2']['_OneWeek']['_combined']['_5minutes'], label = 'Location 4')
# plt.plot(data['Test5']['CO2']['_OneWeek']['_combined']['_5minutes'], label = 'Location 5')
# plt.ylabel('CO2 (ppm)', fontsize=22)
# plt.xlabel('Time (hours)', fontsize=22)
# plt.xticks(thicks, labels = ticks_label, fontsize=22)
# plt.yticks(fontsize=22)
# plt.xlim([0,2000])
# plt.ylim([380,800])
# plt.legend(loc ='best',prop={'size': 12})
# plt.show()

"0.2.3 Data : 60-minutes average - Location : Combined"
# NumValue = range(0,168)
# thicks = [NumValue[i] for i in range(len(NumValue)) if i % 20 == 0]
# ticks_label = range(0,168,20)
# plt.plot(data['Test1']['CO2']['_Combined']['_OneWeek']['_avg60'], label = 'Location 1')
# plt.plot(data['Test2']['CO2']['_Combined']['_OneWeek']['_avg60'], label = 'Location 2')
# plt.plot(range(3,168+3), data['Test3']['CO2']['_Combined']['_avg60'], label = 'Location 3')
# plt.plot(data['Test4']['CO2']['_Combined']['_OneWeek']['_avg60'], label = 'Location 4')
# plt.plot(data['Test5']['CO2']['_Combined']['_OneWeek']['_avg60'], label = 'Location 5')
# plt.ylabel('CO2 (ppm)', fontsize=22)
# plt.xlabel('Temps (hours)', fontsize=22)
# plt.xticks(thicks, labels = ticks_label, fontsize=22)
# plt.yticks(fontsize=22)
# plt.xlim([0,168])
# plt.ylim([380,800])
# plt.legend(loc ='best',prop={'size': 12})
# plt.show()
'----------------------------------------------------------------------------'
"0.3 Humidity"
"0.3.1 Data : All - Location : Combined"
# NumValue = range(len(data['Test1']['Temperature']['_Combined']['_OneWeek']['_time']))
# thicks = [NumValue[i] for i in range(len(NumValue)) if i % 1052 == 0]
# ticks_label = range(0,168,20)
# plt.plot(data['Test1']['Humidity']['_Combined']['_OneWeek']['_valueNanRemove'], label = 'Location 1')
# plt.plot(data['Test2']['Humidity']['_Combined']['_OneWeek']['_valueNanRemove'], label = 'Location 2')
# plt.plot(range(200,8617+200),data['Test3']['Humidity']['_Combined']['_valueNanRemove'], label = 'Location 3')
# plt.plot(data['Test4']['Humidity']['_Combined']['_OneWeek']['_valueNanRemove'], label = 'Location 4')
# plt.plot(data['Test5']['Humidity']['_Combined']['_OneWeek']['_valueNanRemove'], label = 'Location 5')
# plt.ylabel('Humidity (%)', fontsize=22)
# plt.xlabel('Temps (hours)', fontsize=22)
# plt.xticks(thicks, labels = ticks_label, fontsize=22)
# plt.yticks(fontsize=22)
# plt.xlim([0,8500])
# plt.ylim([10,70])
# plt.legend(loc ='best',prop={'size': 12})
# plt.show()

"0.3.2 Data : 5-minutes average - Location : Combined"
# NumValue = range(len(data['Test1']['Temperature']['_OneWeek']['_combined']['_5minutes']))
# thicks = [NumValue[i] for i in range(len(NumValue)) if i % 240 == 0]
# ticks_label = range(0,168,20)
# plt.plot(data['Test1']['Humidity']['_OneWeek']['_combined']['_5minutes'], label = 'Location 1')
# plt.plot(data['Test2']['Humidity']['_OneWeek']['_combined']['_5minutes'], label = 'Location 2')
# plt.plot(range(50,2016+50),data['Test3']['Humidity']['_OneWeek']['_combined']['_5minutes'], label = 'Location 3')
# plt.plot(data['Test4']['Humidity']['_OneWeek']['_combined']['_5minutes'], label = 'Location 4')
# plt.plot(data['Test5']['Humidity']['_OneWeek']['_combined']['_5minutes'], label = 'Location 5')
# plt.ylabel('Humidity (%)', fontsize=22)
# plt.xlabel('Time (hours)', fontsize=22)
# plt.xticks(thicks, labels = ticks_label, fontsize=22)
# plt.yticks(fontsize=22)
# plt.xlim([0,2000])
# plt.ylim([10,70])
# plt.legend(loc ='best',prop={'size': 12})
# plt.show()

"0.3.3 Data : 60-minutes average - Location : Combined"
# NumValue = range(0,168)
# thicks = [NumValue[i] for i in range(len(NumValue)) if i % 20 == 0]
# ticks_label = range(0,168,20)
# plt.plot(data['Test1']['Humidity']['_Combined']['_OneWeek']['_avg60'], label = 'Location 1')
# plt.plot(data['Test2']['Humidity']['_Combined']['_OneWeek']['_avg60'], label = 'Location 2')
# plt.plot(range(3,168+3), data['Test3']['Humidity']['_Combined']['_avg60'], label = 'Location 3')
# plt.plot(data['Test4']['Humidity']['_Combined']['_OneWeek']['_avg60'], label = 'Location 4')
# plt.plot(data['Test5']['Humidity']['_Combined']['_OneWeek']['_avg60'], label = 'Location 5')
# plt.ylabel('Humidity (%)', fontsize=22)
# plt.xlabel('Temps (hours)', fontsize=22)
# plt.xticks(thicks, labels = ticks_label, fontsize=22)
# plt.yticks(fontsize=22)
# plt.xlim([0,168])
# plt.ylim([10,70])
# plt.legend(loc ='best',prop={'size': 12})
# plt.show()
"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
"1. Simple Statistic"
#Timestamp list for analysis
# start_time = datetime.now().replace(year = 2023, month = 5, day = 16, hour=18, minute=0, second=0, microsecond=0)
# end_time = start_time + timedelta(days=7)
# current_time = start_time
# time_list = []
# while current_time < end_time:
#     time_list.append(current_time)
#     current_time += timedelta(minutes=5)
'----------------------------------------------------------------------------'
"1.1 Temperature"
'1.1.0 Panda dataframe to ease the analysis'
# data_1 = data['Test1']['Temperature']['_OneWeek']['_combined']['_5minutes']
# data_2 = data['Test2']['Temperature']['_OneWeek']['_combined']['_5minutes']
# data_3 = data['Test3']['Temperature']['_OneWeek']['_combined']['_5minutes']
# data_4 = data['Test4']['Temperature']['_OneWeek']['_combined']['_5minutes']
# data_5 = data['Test5']['Temperature']['_OneWeek']['_combined']['_5minutes']
# data_Temp = {'_time':time_list ,'Loc1':data_1, 'Loc2':data_2, 'Loc3':data_3, 'Loc4':data_4, 'Loc5':data_5}
# df = pd.DataFrame(data_Temp)
# df.Loc1.fillna(method='ffill', inplace=True)
# df.Loc3.replace(0, method='ffill',inplace=True)
# start = df['Loc3'].values[-50:-1]
# end = df['Loc3'].values[0:-49]
# df['Loc3']=np.concatenate((start,end))

"1.1.1 All Data"
# AVG_Temp = []
# STD_Temp = []
# MED_Temp = []
# SKE_Temp = []
# KUR_Temp = []
# LYA_Temp = []
# LUI_Temp = []
# for j in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#     AVG_Temp = AVG_Temp + [df[j].mean()]
#     STD_Temp = STD_Temp + [df[j].std()]
#     MED_Temp = MED_Temp + [df[j].median()]
#     SKE_Temp = SKE_Temp + [scipy.stats.skew(df[j], axis=0, bias=True)]
#     KUR_Temp = KUR_Temp + [scipy.stats.kurtosis(df[j], axis=0, fisher=True, bias=True)]
#     LYA_Temp = LYA_Temp + [nolds.lyap_r(df[j])]
#     LUI_Temp = LUI_Temp + [sum((df[j]<24) & (df[j]>20))/len(df[j])]
# SimStats_Temp = {'Subset':['AllData','AllData','AllData','AllData','AllData'],'Location':[1,2,3,4,5],'AVG':AVG_Temp,'STD':STD_Temp,'MED':MED_Temp,'SKE':SKE_Temp,'KUR':KUR_Temp,'LYA':LYA_Temp,'LUI':LUI_Temp}
# SimStats_Temp = pd.DataFrame(SimStats_Temp)


'1.1.2 Light On/Off'
'1.1.2.1 Light On'
# hour_mask = (df['_time'].dt.hour < 2) | (df['_time'].dt.hour > 7)
# LightOn_df = df[hour_mask]
# LightOn_df = LightOn_df.dropna()
# AVG_Temp = []
# STD_Temp = []
# MED_Temp = []
# SKE_Temp = []
# KUR_Temp = []
# LYA_Temp = []
# LUI_Temp = []
# for j in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#     AVG_Temp = AVG_Temp + [LightOn_df[j].mean()]
#     STD_Temp = STD_Temp + [LightOn_df[j].std()]
#     MED_Temp = MED_Temp + [LightOn_df[j].median()]
#     SKE_Temp = SKE_Temp + [scipy.stats.skew(LightOn_df[j], axis=0, bias=True)]
#     KUR_Temp = KUR_Temp + [scipy.stats.kurtosis(LightOn_df[j], axis=0, fisher=True, bias=True)]
#     LYA_Temp = LYA_Temp + [nolds.lyap_r(LightOn_df[j])]
#     LUI_Temp = LUI_Temp + [sum((LightOn_df[j]<24) & (LightOn_df[j]>20))/len(LightOn_df[j])]
# New_rows = {'Subset':['LightOn','LightOn','LightOn','LightOn','LightOn'],'Location':[1,2,3,4,5],'AVG':AVG_Temp,'STD':STD_Temp,'MED':MED_Temp,'SKE':SKE_Temp,'KUR':KUR_Temp,'LYA':LYA_Temp,'LUI':LUI_Temp}
# New_rows = pd.DataFrame(New_rows)
# SimStats_Temp = SimStats_Temp.append(New_rows,ignore_index=True)

'1.1.2.2 Light Off'
# hour_mask = (df['_time'].dt.hour > 1) & (df['_time'].dt.hour < 8)
# LightOff_df = df[hour_mask]
# LightOff_df = LightOff_df.dropna()
# AVG_Temp = []
# STD_Temp = []
# MED_Temp = []
# SKE_Temp = []
# KUR_Temp = []
# LYA_Temp = []
# LUI_Temp = []
# for j in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#     AVG_Temp = AVG_Temp + [LightOff_df[j].mean()]
#     STD_Temp = STD_Temp + [LightOff_df[j].std()]
#     MED_Temp = MED_Temp + [LightOff_df[j].median()]
#     SKE_Temp = SKE_Temp + [scipy.stats.skew(LightOff_df[j], axis=0, bias=True)]
#     KUR_Temp = KUR_Temp + [scipy.stats.kurtosis(LightOff_df[j], axis=0, fisher=True, bias=True)]
#     LYA_Temp = LYA_Temp + [nolds.lyap_r(LightOff_df[j])]
#     LUI_Temp = LUI_Temp + [sum((LightOff_df[j]<24) & (LightOff_df[j]>20))/len(LightOff_df[j])]
# New_rows = {'Subset':['LightOff','LightOff','LightOff','LightOff','LightOff'],'Location':[1,2,3,4,5],'AVG':AVG_Temp,'STD':STD_Temp,'MED':MED_Temp,'SKE':SKE_Temp,'KUR':KUR_Temp,'LYA':LYA_Temp,'LUI':LUI_Temp}
# New_rows = pd.DataFrame(New_rows)
# SimStats_Temp = SimStats_Temp.append(New_rows,ignore_index=True)

'1.1.3 Worker On/Off'
'1.1.3.1 Worker On'
# hour_mask = (df['_time'].dt.hour >= 8) & (df['_time'].dt.hour < 16) & (df['_time'].dt.weekday != 5) & (df['_time'].dt.weekday != 6)
# WorkOn_df = df[hour_mask]

# AVG_Temp = []
# STD_Temp = []
# MED_Temp = []
# for j in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#     AVG_Temp = AVG_Temp + [WorkOn_df[j].mean()]
#     STD_Temp = STD_Temp + [WorkOn_df[j].std()] 
#     MED_Temp = MED_Temp + [WorkOn_df[j].median()]
    
# New_rows = {'Subset':['WorkerOn','WorkerOn','WorkerOn','WorkerOn','WorkerOn'],'Location':[1,2,3,4,5],'AVG':AVG_Temp,'STD':STD_Temp,'MED':MED_Temp}
# New_rows = pd.DataFrame(New_rows)
# SimStats_Temp = SimStats_Temp.append(New_rows,ignore_index=True)

'1.1.3.2 Worker On/off'
# hour_mask = (((df['_time'].dt.weekday ==5) | (df['_time'].dt.weekday ==6)) | (((df['_time'].dt.weekday !=5) & (df['_time'].dt.weekday !=6)) & ((df['_time'].dt.hour < 8) | (df['_time'].dt.hour >= 16))))
# WorkOff_df = df[hour_mask]

# AVG_Temp = []
# STD_Temp = []
# MED_Temp = []
# for j in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#     AVG_Temp = AVG_Temp + [WorkOff_df[j].mean()]
#     STD_Temp = STD_Temp + [WorkOff_df[j].std()]
#     MED_Temp = MED_Temp + [WorkOff_df[j].median()]
    
# New_rows = {'Subset':['WorkerOff','WorkerOff','WorkerOff','WorkerOff','WorkerOff'],'Location':[1,2,3,4,5],'AVG':AVG_Temp,'STD':STD_Temp,'MED':MED_Temp}
# New_rows = pd.DataFrame(New_rows)
# SimStats_Temp = SimStats_Temp.append(New_rows,ignore_index=True)

'1.1.4 BOXPLOT'
'1.1.4.1 Boxplot1 - LightOn/Off'
# fig, ax = plt.subplots()
# box_param = dict(whis=(1, 99), widths=0.2, medianprops=dict(color='black'),showfliers=False, patch_artist=True)
# bp = ax.boxplot(df.loc[:,df.columns != '_time'], positions=np.arange(5)-0.36,**box_param,boxprops=dict(facecolor = 'white'))
# bp1 = ax.boxplot(LightOn_df.loc[:,LightOn_df.columns != '_time'], positions=np.arange(5)-0.12,**box_param,boxprops=dict(facecolor = 'white',hatch = 'xx'))
# bp2 = ax.boxplot(LightOff_df.loc[:,LightOff_df.columns != '_time'], positions=np.arange(5)+0.12, **box_param,boxprops=dict(facecolor = 'white',hatch = '..'))
# # bp = ax.boxplot(df.loc[:,df.columns != '_time'], positions=np.arange(5)-0.35,**box_param,boxprops=dict(facecolor='tomato'))
# # bp1 = ax.boxplot(LightOn_df.loc[:,LightOn_df.columns != '_time'], positions=np.arange(5)-0.12,**box_param,boxprops=dict(facecolor='lightblue'))
# # bp2 = ax.boxplot(LightOff_df.loc[:,LightOff_df.columns != '_time'], positions=np.arange(5)+0.12, **box_param,boxprops=dict(facecolor='lightgreen'))
# ax.set_ylim([18,29])
# plt.ylabel("Temperature ($^o$C)",fontsize=22)
# ax.set_xticks(np.arange(5))
# ax.set_xticklabels(['Location 1','Location 2','Location 3','Location 4','Location 5'], fontsize=22)
# ax.legend([bp["boxes"][0],bp1["boxes"][0], bp2["boxes"][0]], ['All Data','Light On', 'Light Off'], loc='upper right',fontsize=22)
# plt.show()

'1.1.4.2 Boxplot2 - WorkOn/Off'
# fig, ax = plt.subplots()
# box_param = dict(whis=(1, 99), widths=0.2, medianprops=dict(color='black'),showfliers=False, patch_artist=True)
# bp = ax.boxplot(df.loc[:,df.columns != '_time'], positions=np.arange(5)-0.36,**box_param,boxprops=dict(facecolor = 'white'))
# bp1 = ax.boxplot(WorkOn_df.loc[:,LightOn_df.columns != '_time'], positions=np.arange(5)-0.12,**box_param,boxprops=dict(facecolor = 'white',hatch = 'xx'))
# bp2 = ax.boxplot(WorkOff_df.loc[:,LightOff_df.columns != '_time'], positions=np.arange(5)+0.12, **box_param,boxprops=dict(facecolor = 'white',hatch = '..'))
# # bp = ax.boxplot(df.loc[:,df.columns != '_time'], positions=np.arange(5)-0.35,**box_param,boxprops=dict(facecolor='tomato'))
# # bp1 = ax.boxplot(WorkOn_df.loc[:,LightOn_df.columns != '_time'], positions=np.arange(5)-0.12,**box_param,boxprops=dict(facecolor='lightblue'))
# # bp2 = ax.boxplot(WorkOff_df.loc[:,LightOff_df.columns != '_time'], positions=np.arange(5)+0.12, **box_param,boxprops=dict(facecolor='lightgreen'))
# ax.set_ylim([18,29])
# plt.ylabel("Temperature ($^o$C)",fontsize=22)
# ax.set_xticks(np.arange(5))
# ax.set_xticklabels(['Location 1','Location 2','Location 3','Location 4','Location 5'], fontsize=22)
# ax.legend([bp["boxes"][0],bp1["boxes"][0], bp2["boxes"][0]], ['All Data','Work On', 'Work Off'], loc='upper right',fontsize=22)
# plt.show()

'1.1.4.3 Boxplot3 - All'
# fig, ax = plt.subplots()
# box_param = dict(whis=(1, 99), widths=0.12, medianprops=dict(color='black'),showfliers=False, patch_artist=True)
# bp = ax.boxplot(df.loc[:,df.columns != '_time'], positions=np.arange(5)-0.28,**box_param,boxprops=dict(facecolor = 'white'))
# bp1 = ax.boxplot(LightOn_df.loc[:,LightOn_df.columns != '_time'], positions=np.arange(5)-0.14,**box_param,boxprops=dict(facecolor = 'white',hatch = 'xx'))
# bp2 = ax.boxplot(LightOff_df.loc[:,LightOff_df.columns != '_time'], positions=np.arange(5), **box_param,boxprops=dict(facecolor = 'white',hatch = '..'))
# bp3 = ax.boxplot(WorkOn_df.loc[:,WorkOn_df.columns != '_time'], positions=np.arange(5)+0.14, **box_param,boxprops=dict(facecolor = 'white',hatch = 'oo'))
# bp4 = ax.boxplot(WorkOff_df.loc[:,WorkOn_df.columns != '_time'], positions=np.arange(5)+0.28, **box_param,boxprops=dict(facecolor = 'white',hatch = '//'))
# ax.set_ylim([18,29])
# plt.ylabel("Temperature ($^o$C)",fontsize=22)
# ax.set_xticks(np.arange(5))
# ax.set_xticklabels(['Location 1','Location 2','Location 3','Location 4','Location 5'], fontsize=22)
# ax.legend([bp["boxes"][0],bp1["boxes"][0], bp2["boxes"][0],bp3["boxes"][0],bp4["boxes"][0]], ['All Data','Light On', 'Light Off','Work On','Work Off'], loc='upper right',fontsize=16)
# plt.show()
'----------------------------------------------------------------------------'
"1.2 Humidity"
'1.1.0 Panda dataframe to ease the analysis'
# data_1 = data['Test1']['Humidity']['_OneWeek']['_combined']['_5minutes']
# data_2 = data['Test2']['Humidity']['_OneWeek']['_combined']['_5minutes']
# data_3 = data['Test3']['Humidity']['_OneWeek']['_combined']['_5minutes']
# data_4 = data['Test4']['Humidity']['_OneWeek']['_combined']['_5minutes']
# data_5 = data['Test5']['Humidity']['_OneWeek']['_combined']['_5minutes']
# data_HR = {'_time':time_list ,'Loc1':data_1, 'Loc2':data_2, 'Loc3':data_3, 'Loc4':data_4, 'Loc5':data_5}
# df_HR = pd.DataFrame(data_HR)
# df_HR.Loc1.fillna(method='ffill', inplace=True)
# df_HR.Loc3.replace(0, method='ffill',inplace=True)
# start = df_HR['Loc3'].values[-50:-1]
# end = df_HR['Loc3'].values[0:-49]
# df_HR['Loc3']=np.concatenate((start,end))

"1.1.1 All Data"
# AVG_HR = []
# STD_HR = []
# MED_HR = []
# SKE_RH = []
# KUR_RH = []
# LYA_RH = []
# for j in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#     AVG_HR = AVG_HR + [df_HR[j].mean()]
#     STD_HR = STD_HR + [df_HR[j].std()]
#     MED_HR = MED_HR + [df_HR[j].median()]
#     SKE_RH = SKE_RH + [scipy.stats.skew(df_HR[j], axis=0, bias=True)]
#     KUR_RH = KUR_RH + [scipy.stats.kurtosis(df_HR[j], axis=0, fisher=True, bias=True)]
#     LYA_RH = LYA_RH + [nolds.lyap_r(df_HR[j])]
# SimStats_HR = {'Subset':['AllData','AllData','AllData','AllData','AllData'],'Location':[1,2,3,4,5],'AVG':AVG_HR,'STD':STD_HR,'MED':MED_HR,'SKE':SKE_RH,'KUR':KUR_RH,'LYA':LYA_RH}
# SimStats_HR = pd.DataFrame(SimStats_HR)


'1.1.2 Light On/Off'
'1.1.2.1 Light On'
# hour_mask = (df_HR['_time'].dt.hour < 2) | (df_HR['_time'].dt.hour > 7)
# LightOn_df = df_HR[hour_mask]
# LightOn_df = LightOn_df.dropna()
# AVG_HR = []
# STD_HR = []
# MED_HR = []
# for j in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#     AVG_HR = AVG_HR + [LightOn_df[j].mean()]
#     STD_HR = STD_HR + [LightOn_df[j].std()]
#     MED_HR = MED_HR + [LightOn_df[j].median()]
# New_rows = {'Subset':['LightOn','LightOn','LightOn','LightOn','LightOn'],'Location':[1,2,3,4,5],'AVG':AVG_HR,'STD':STD_HR,'MED':MED_HR}
# New_rows = pd.DataFrame(New_rows)
# SimStats_HR = SimStats_HR.append(New_rows,ignore_index=True)

'1.1.2.2 Light Off'
# hour_mask = (df_HR['_time'].dt.hour > 1) & (df_HR['_time'].dt.hour < 8)
# LightOff_df = df_HR[hour_mask]
# LightOff_df = LightOff_df.dropna()
# AVG_HR = []
# STD_HR = []
# MED_HR = []
# for j in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#     AVG_HR = AVG_HR + [LightOff_df[j].mean()]
#     STD_HR = STD_HR + [LightOff_df[j].std()]
#     MED_HR = MED_HR + [LightOff_df[j].median()]
# New_rows = {'Subset':['LightOff','LightOff','LightOff','LightOff','LightOff'],'Location':[1,2,3,4,5],'AVG':AVG_HR,'STD':STD_HR,'MED':MED_HR}
# New_rows = pd.DataFrame(New_rows)
# SimStats_HR = SimStats_HR.append(New_rows,ignore_index=True)

'1.1.3 Worker On/Off'
'1.1.3.1 Worker On'
# hour_mask = (df_HR['_time'].dt.hour >= 8) & (df_HR['_time'].dt.hour < 16) & (df_HR['_time'].dt.weekday != 5) & (df_HR['_time'].dt.weekday != 6)
# WorkOn_df = df_HR[hour_mask]
# AVG_HR = []
# STD_HR = []
# MED_HR = []
# for j in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#     AVG_HR = AVG_HR + [WorkOn_df[j].mean()]
#     STD_HR = STD_HR + [WorkOn_df[j].std()] 
#     MED_HR = MED_HR + [WorkOn_df[j].median()]
# New_rows = {'Subset':['WorkerOn','WorkerOn','WorkerOn','WorkerOn','WorkerOn'],'Location':[1,2,3,4,5],'AVG':AVG_HR,'STD':STD_HR,'MED':MED_HR}
# New_rows = pd.DataFrame(New_rows)
# SimStats_HR = SimStats_HR.append(New_rows,ignore_index=True)

'1.1.3.2 Worker On/off'
# hour_mask = (((df_HR['_time'].dt.weekday ==5) | (df_HR['_time'].dt.weekday ==6)) | (((df_HR['_time'].dt.weekday !=5) & (df_HR['_time'].dt.weekday !=6)) & ((df_HR['_time'].dt.hour < 8) | (df_HR['_time'].dt.hour >= 16))))
# WorkOff_df = df_HR[hour_mask]
# AVG_HR = []
# STD_HR = []
# MED_HR = []
# for j in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#     AVG_HR = AVG_HR + [WorkOff_df[j].mean()]
#     STD_HR = STD_HR + [WorkOff_df[j].std()]
#     MED_HR = MED_HR + [WorkOff_df[j].median()]
# New_rows = {'Subset':['WorkerOff','WorkerOff','WorkerOff','WorkerOff','WorkerOff'],'Location':[1,2,3,4,5],'AVG':AVG_HR,'STD':STD_HR,'MED':MED_HR}
# New_rows = pd.DataFrame(New_rows)
# SimStats_HR = SimStats_HR.append(New_rows,ignore_index=True)

'1.1.4 BOXPLOT'
'1.1.4.1 Boxplot1 - LightOn/Off'
# fig, ax = plt.subplots()
# box_param = dict(whis=(1, 99), widths=0.2, medianprops=dict(color='black'),showfliers=False, patch_artist=True)
# bp = ax.boxplot(df_HR.loc[:,df_HR.columns != '_time'], positions=np.arange(5)-0.36,**box_param,boxprops=dict(facecolor = 'white'))
# bp1 = ax.boxplot(LightOn_df.loc[:,LightOn_df.columns != '_time'], positions=np.arange(5)-0.12,**box_param,boxprops=dict(facecolor = 'white',hatch = 'xx'))
# bp2 = ax.boxplot(LightOff_df.loc[:,LightOff_df.columns != '_time'], positions=np.arange(5)+0.12, **box_param,boxprops=dict(facecolor = 'white',hatch = '..'))
# # bp = ax.boxplot(df.loc[:,df.columns != '_time'], positions=np.arange(5)-0.35,**box_param,boxprops=dict(facecolor='tomato'))
# # bp1 = ax.boxplot(LightOn_df.loc[:,LightOn_df.columns != '_time'], positions=np.arange(5)-0.12,**box_param,boxprops=dict(facecolor='lightblue'))
# # bp2 = ax.boxplot(LightOff_df.loc[:,LightOff_df.columns != '_time'], positions=np.arange(5)+0.12, **box_param,boxprops=dict(facecolor='lightgreen'))
# ax.set_ylim([0,70])
# plt.ylabel("Relative Humidity (%)",fontsize=22)
# ax.set_xticks(np.arange(5))
# ax.set_xticklabels(['Location 1','Location 2','Location 3','Location 4','Location 5'], fontsize=22)
# ax.legend([bp["boxes"][0],bp1["boxes"][0], bp2["boxes"][0]], ['All Data','Light On', 'Light Off'], loc='upper right',fontsize=22)
# plt.show()

'1.1.4.2 Boxplot2 - WorkOn/Off'
# fig, ax = plt.subplots()
# box_param = dict(whis=(1, 99), widths=0.2, medianprops=dict(color='black'),showfliers=False, patch_artist=True)
# bp = ax.boxplot(df_HR.loc[:,df_HR.columns != '_time'], positions=np.arange(5)-0.36,**box_param,boxprops=dict(facecolor = 'white'))
# bp1 = ax.boxplot(WorkOn_df.loc[:,LightOn_df.columns != '_time'], positions=np.arange(5)-0.12,**box_param,boxprops=dict(facecolor = 'white',hatch = 'xx'))
# bp2 = ax.boxplot(WorkOff_df.loc[:,LightOff_df.columns != '_time'], positions=np.arange(5)+0.12, **box_param,boxprops=dict(facecolor = 'white',hatch = '..'))
# # bp = ax.boxplot(df.loc[:,df.columns != '_time'], positions=np.arange(5)-0.35,**box_param,boxprops=dict(facecolor='tomato'))
# # bp1 = ax.boxplot(WorkOn_df.loc[:,LightOn_df.columns != '_time'], positions=np.arange(5)-0.12,**box_param,boxprops=dict(facecolor='lightblue'))
# # bp2 = ax.boxplot(WorkOff_df.loc[:,LightOff_df.columns != '_time'], positions=np.arange(5)+0.12, **box_param,boxprops=dict(facecolor='lightgreen'))
# ax.set_ylim([0,70])
# plt.ylabel("Relative Humidity (%)",fontsize=22)
# ax.set_xticks(np.arange(5))
# ax.set_xticklabels(['Location 1','Location 2','Location 3','Location 4','Location 5'], fontsize=22)
# ax.legend([bp["boxes"][0],bp1["boxes"][0], bp2["boxes"][0]], ['All Data','Work On', 'Work Off'], loc='upper right',fontsize=22)
# plt.show()

'1.1.4.3 Boxplot3 - All'
# fig, ax = plt.subplots()
# box_param = dict(whis=(1, 99), widths=0.12, medianprops=dict(color='black'),showfliers=False, patch_artist=True)
# bp = ax.boxplot(df_HR.loc[:,df_HR.columns != '_time'], positions=np.arange(5)-0.28,**box_param,boxprops=dict(facecolor = 'white'))
# bp1 = ax.boxplot(LightOn_df.loc[:,LightOn_df.columns != '_time'], positions=np.arange(5)-0.14,**box_param,boxprops=dict(facecolor = 'white',hatch = 'xx'))
# bp2 = ax.boxplot(LightOff_df.loc[:,LightOff_df.columns != '_time'], positions=np.arange(5), **box_param,boxprops=dict(facecolor = 'white',hatch = '..'))
# bp3 = ax.boxplot(WorkOn_df.loc[:,WorkOn_df.columns != '_time'], positions=np.arange(5)+0.14, **box_param,boxprops=dict(facecolor = 'white',hatch = 'oo'))
# bp4 = ax.boxplot(WorkOff_df.loc[:,WorkOn_df.columns != '_time'], positions=np.arange(5)+0.28, **box_param,boxprops=dict(facecolor = 'white',hatch = '//'))
# ax.set_ylim([0,70])
# plt.ylabel("Relative Humidity (%)",fontsize=22)
# ax.set_xticks(np.arange(5))
# ax.set_xticklabels(['Location 1','Location 2','Location 3','Location 4','Location 5'], fontsize=22)
# ax.legend([bp["boxes"][0],bp1["boxes"][0], bp2["boxes"][0],bp3["boxes"][0],bp4["boxes"][0]], ['All Data','Light On', 'Light Off','Work On','Work Off'], loc='upper right',fontsize=16)
# plt.show()
'----------------------------------------------------------------------------'
"1.2 CO2"
'1.1.0 Panda dataframe to ease the analysis'
# data_1 = data['Test1']['CO2']['_OneWeek']['_combined']['_5minutes']
# data_2 = data['Test2']['CO2']['_OneWeek']['_combined']['_5minutes']
# data_3 = data['Test3']['CO2']['_OneWeek']['_combined']['_5minutes']
# data_4 = data['Test4']['CO2']['_OneWeek']['_combined']['_5minutes']
# data_5 = data['Test5']['CO2']['_OneWeek']['_combined']['_5minutes']
# data_Temp = {'_time':time_list ,'Loc1':data_1, 'Loc2':data_2, 'Loc3':data_3, 'Loc4':data_4, 'Loc5':data_5}
# df_CO2 = pd.DataFrame(data_Temp)
# df_CO2.Loc1.fillna(method='ffill', inplace=True)
# df_CO2.Loc3.replace(0, method='ffill',inplace=True)
# start = df_CO2['Loc3'].values[-50:-1]
# end = df_CO2['Loc3'].values[0:-49]
# df_CO2['Loc3']=np.concatenate((start,end))

"1.1.1 All Data"
# AVG_CO2 = []
# STD_CO2 = []
# MED_CO2 = []
# SKE_CO2 = []
# KUR_CO2 = []
# LYA_CO2 = []
# # LUI_CO2 = []
# for j in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#     AVG_CO2 = AVG_CO2 + [df_CO2[j].mean()]
#     STD_CO2 = STD_CO2 + [df_CO2[j].std()]
#     MED_CO2 = MED_CO2 + [df_CO2[j].median()]
#     SKE_CO2 = SKE_CO2 + [scipy.stats.skew(df_CO2[j], axis=0, bias=True)]
#     KUR_CO2 = KUR_CO2 + [scipy.stats.kurtosis(df_CO2[j], axis=0, fisher=True, bias=True)]
#     LYA_CO2 = LYA_CO2 + [nolds.lyap_r(df_CO2[j])]
#     # LUI_CO2 = LUI_CO2 + [sum((df_CO2[j]<24) & (df_CO2[j]>20))/len(df_CO2[j])]
# SimStats_CO2 = {'Subset':['AllData','AllData','AllData','AllData','AllData'],'Location':[1,2,3,4,5],'AVG':AVG_CO2,'STD':STD_CO2,'MED':MED_CO2,'SKE':SKE_CO2,'KUR':KUR_CO2,'LYA':LYA_CO2}
# SimStats_CO2 = pd.DataFrame(SimStats_CO2)


'1.1.2 Light On/Off'
'1.1.2.1 Light On'
# hour_mask = (df_CO2['_time'].dt.hour < 2) | (df_CO2['_time'].dt.hour > 7)
# LightOn_df = df_CO2[hour_mask]
# LightOn_df = LightOn_df.dropna()
# AVG_CO2 = []
# STD_CO2 = []
# MED_CO2 = []
# for j in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#     AVG_CO2 = AVG_CO2 + [LightOn_df[j].mean()]
#     STD_CO2 = STD_CO2 + [LightOn_df[j].std()]
#     MED_CO2 = MED_CO2 + [LightOn_df[j].median()]
# New_rows = {'Subset':['LightOn','LightOn','LightOn','LightOn','LightOn'],'Location':[1,2,3,4,5],'AVG':AVG_CO2,'STD':STD_CO2,'MED':MED_CO2}
# New_rows = pd.DataFrame(New_rows)
# SimStats_CO2 = SimStats_CO2.append(New_rows,ignore_index=True)

'1.1.2.2 Light Off'
# hour_mask = (df_CO2['_time'].dt.hour > 1) & (df_CO2['_time'].dt.hour < 8)
# LightOff_df = df_CO2[hour_mask]
# LightOff_df = LightOff_df.dropna()
# AVG_CO2 = []
# STD_CO2 = []
# MED_CO2 = []
# for j in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#     AVG_CO2 = AVG_CO2 + [LightOff_df[j].mean()]
#     STD_CO2 = STD_CO2 + [LightOff_df[j].std()]
#     MED_CO2 = MED_CO2 + [LightOff_df[j].median()]
# New_rows = {'Subset':['LightOff','LightOff','LightOff','LightOff','LightOff'],'Location':[1,2,3,4,5],'AVG':AVG_CO2,'STD':STD_CO2,'MED':MED_CO2}
# New_rows = pd.DataFrame(New_rows)
# SimStats_CO2 = SimStats_CO2.append(New_rows,ignore_index=True)

'1.1.3 Worker On/Off'
'1.1.3.1 Worker On'
# hour_mask = (df_CO2['_time'].dt.hour >= 8) & (df_CO2['_time'].dt.hour < 16) & (df_CO2['_time'].dt.weekday != 5) & (df_CO2['_time'].dt.weekday != 6)
# WorkOn_df = df_CO2[hour_mask]
# AVG_CO2 = []
# STD_CO2 = []
# MED_CO2 = []
# SKE_CO2 = []
# KUR_CO2 = []
# LYA_CO2 = []
# for j in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#     AVG_CO2 = AVG_CO2 + [WorkOn_df[j].mean()]
#     STD_CO2 = STD_CO2 + [WorkOn_df[j].std()] 
#     MED_CO2 = MED_CO2 + [WorkOn_df[j].median()]
#     SKE_CO2 = SKE_CO2 + [scipy.stats.skew(WorkOn_df[j], axis=0, bias=True)]
#     KUR_CO2 = KUR_CO2 + [scipy.stats.kurtosis(WorkOn_df[j], axis=0, fisher=True, bias=True)]
#     LYA_CO2 = LYA_CO2 + [nolds.lyap_r(WorkOn_df[j])]
# New_rows = {'Subset':['WorkerOn','WorkerOn','WorkerOn','WorkerOn','WorkerOn'],'Location':[1,2,3,4,5],'AVG':AVG_CO2,'STD':STD_CO2,'MED':MED_CO2,'SKE':SKE_CO2,'KUR':KUR_CO2,'LYA':LYA_CO2}
# New_rows = pd.DataFrame(New_rows)
# SimStats_CO2 = SimStats_CO2.append(New_rows,ignore_index=True)

'1.1.3.2 Worker off'
# hour_mask = (((df_CO2['_time'].dt.weekday ==5) | (df_CO2['_time'].dt.weekday ==6)) | (((df_CO2['_time'].dt.weekday !=5) & (df_CO2['_time'].dt.weekday !=6)) & ((df_CO2['_time'].dt.hour < 8) | (df_CO2['_time'].dt.hour >= 16))))
# WorkOff_df = df_CO2[hour_mask]
# AVG_CO2 = []
# STD_CO2 = []
# MED_CO2 = []
# MED_CO2 = []
# SKE_CO2 = []
# KUR_CO2 = []
# LYA_CO2 = []
# for j in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#     AVG_CO2 = AVG_CO2 + [WorkOff_df[j].mean()]
#     STD_CO2 = STD_CO2 + [WorkOff_df[j].std()]
#     MED_CO2 = MED_CO2 + [WorkOff_df[j].median()]
#     SKE_CO2 = SKE_CO2 + [scipy.stats.skew(WorkOff_df[j], axis=0, bias=True)]
#     KUR_CO2 = KUR_CO2 + [scipy.stats.kurtosis(WorkOff_df[j], axis=0, fisher=True, bias=True)]
#     LYA_CO2 = LYA_CO2 + [nolds.lyap_r(WorkOff_df[j])]
# New_rows = {'Subset':['WorkerOff','WorkerOff','WorkerOff','WorkerOff','WorkerOff'],'Location':[1,2,3,4,5],'AVG':AVG_CO2,'STD':STD_CO2,'MED':MED_CO2,'SKE':SKE_CO2,'KUR':KUR_CO2,'LYA':LYA_CO2}
# New_rows = pd.DataFrame(New_rows)
# SimStats_CO2 = SimStats_CO2.append(New_rows,ignore_index=True)

'1.1.4 BOXPLOT'
'1.1.4.1 Boxplot1 - LightOn/Off'
# fig, ax = plt.subplots()
# box_param = dict(whis=(1, 99), widths=0.2, medianprops=dict(color='black'),showfliers=False, patch_artist=True)
# bp = ax.boxplot(df_CO2.loc[:,df_CO2.columns != '_time'], positions=np.arange(5)-0.36,**box_param,boxprops=dict(facecolor = 'white'))
# bp1 = ax.boxplot(LightOn_df.loc[:,LightOn_df.columns != '_time'], positions=np.arange(5)-0.12,**box_param,boxprops=dict(facecolor = 'white',hatch = 'xx'))
# bp2 = ax.boxplot(LightOff_df.loc[:,LightOff_df.columns != '_time'], positions=np.arange(5)+0.12, **box_param,boxprops=dict(facecolor = 'white',hatch = '..'))
# # bp = ax.boxplot(df.loc[:,df.columns != '_time'], positions=np.arange(5)-0.35,**box_param,boxprops=dict(facecolor='tomato'))
# # bp1 = ax.boxplot(LightOn_df.loc[:,LightOn_df.columns != '_time'], positions=np.arange(5)-0.12,**box_param,boxprops=dict(facecolor='lightblue'))
# # bp2 = ax.boxplot(LightOff_df.loc[:,LightOff_df.columns != '_time'], positions=np.arange(5)+0.12, **box_param,boxprops=dict(facecolor='lightgreen'))
# ax.set_ylim([350,800])
# plt.ylabel("CO2 level (ppm)",fontsize=22)
# ax.set_xticks(np.arange(5))
# ax.set_xticklabels(['Location 1','Location 2','Location 3','Location 4','Location 5'], fontsize=22)
# ax.legend([bp["boxes"][0],bp1["boxes"][0], bp2["boxes"][0]], ['All Data','Light On', 'Light Off'], loc='upper right',fontsize=22)
# plt.show()

'1.1.4.2 Boxplot2 - WorkOn/Off'
# fig, ax = plt.subplots()
# box_param = dict(whis=(1, 99), widths=0.2, medianprops=dict(color='black'),showfliers=False, patch_artist=True)
# bp = ax.boxplot(df_CO2.loc[:,df_CO2.columns != '_time'], positions=np.arange(5)-0.36,**box_param,boxprops=dict(facecolor = 'white'))
# bp1 = ax.boxplot(WorkOn_df.loc[:,LightOn_df.columns != '_time'], positions=np.arange(5)-0.12,**box_param,boxprops=dict(facecolor = 'white',hatch = 'xx'))
# bp2 = ax.boxplot(WorkOff_df.loc[:,LightOff_df.columns != '_time'], positions=np.arange(5)+0.12, **box_param,boxprops=dict(facecolor = 'white',hatch = '..'))
# # bp = ax.boxplot(df.loc[:,df.columns != '_time'], positions=np.arange(5)-0.35,**box_param,boxprops=dict(facecolor='tomato'))
# # bp1 = ax.boxplot(WorkOn_df.loc[:,LightOn_df.columns != '_time'], positions=np.arange(5)-0.12,**box_param,boxprops=dict(facecolor='lightblue'))
# # bp2 = ax.boxplot(WorkOff_df.loc[:,LightOff_df.columns != '_time'], positions=np.arange(5)+0.12, **box_param,boxprops=dict(facecolor='lightgreen'))
# ax.set_ylim([350,800])
# plt.ylabel("CO2 level (ppm)",fontsize=22)
# ax.set_xticks(np.arange(5))
# ax.set_xticklabels(['Location 1','Location 2','Location 3','Location 4','Location 5'], fontsize=22)
# ax.legend([bp["boxes"][0],bp1["boxes"][0], bp2["boxes"][0]], ['All Data','Work On', 'Work Off'], loc='upper right',fontsize=22)
# plt.show()

'1.1.4.3 Boxplot3 - All'
# fig, ax = plt.subplots()
# box_param = dict(whis=(1, 99), widths=0.12, medianprops=dict(color='black'),showfliers=False, patch_artist=True)
# bp = ax.boxplot(df_CO2.loc[:,df_CO2.columns != '_time'], positions=np.arange(5)-0.28,**box_param,boxprops=dict(facecolor = 'white'))
# bp1 = ax.boxplot(LightOn_df.loc[:,LightOn_df.columns != '_time'], positions=np.arange(5)-0.14,**box_param,boxprops=dict(facecolor = 'white',hatch = 'xx'))
# bp2 = ax.boxplot(LightOff_df.loc[:,LightOff_df.columns != '_time'], positions=np.arange(5), **box_param,boxprops=dict(facecolor = 'white',hatch = '..'))
# bp3 = ax.boxplot(WorkOn_df.loc[:,WorkOn_df.columns != '_time'], positions=np.arange(5)+0.14, **box_param,boxprops=dict(facecolor = 'white',hatch = 'oo'))
# bp4 = ax.boxplot(WorkOff_df.loc[:,WorkOn_df.columns != '_time'], positions=np.arange(5)+0.28, **box_param,boxprops=dict(facecolor = 'white',hatch = '//'))
# ax.set_ylim([350,800])
# plt.ylabel("CO2 (ppm)",fontsize=22)
# ax.set_xticks(np.arange(5))
# ax.set_xticklabels(['Location 1','Location 2','Location 3','Location 4','Location 5'], fontsize=22)
# ax.legend([bp["boxes"][0],bp1["boxes"][0], bp2["boxes"][0],bp3["boxes"][0],bp4["boxes"][0]], ['All Data','Light On', 'Light Off','Work On','Work Off'], loc='upper right',fontsize=16)
# plt.show()
"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
"2. Vapor Pressure Deficit"

# NumValue = range(len(data['Test1']['Temperature']['_OneWeek']['_combined']['_5minutes']))
# thicks = [NumValue[i] for i in range(len(NumValue)) if i % 240 == 0]
# ticks_label = range(0,168,20)

# Vapor = []
# for j in range(len(data['Test2']['Temperature']['_OneWeek']['_combined']['_5minutes'])):
#         Vapor = Vapor + [(1-data['Test2']['Humidity']['_OneWeek']['_combined']['_5minutes'][j]/100)*610.7*10**(7.5*data['Test1']['Temperature']['_OneWeek']['_combined']['_5minutes'][j]/(273.3+data['Test1']['Temperature']['_OneWeek']['_combined']['_5minutes'][j]))/1000]

# fig, ax = plt.subplots()
# ax.plot(Vapor, label='VPD')
# ax.set_xlabel('Time (hours)', fontsize=22)
# ax.set_ylabel('VPD (kPa)', fontsize = 20)
# ax.legend(loc=(0.91,0.94),prop={'size': 16})
# ax.set_xticks(thicks, labels = ticks_label, fontsize=22)
# ax.set_xlim(0, 2016)
# ax.tick_params(axis='y',labelsize=22)
# ax.xlabel('Time (hours)', fontsize=22)

# ax2=ax.twinx()
# ax2._get_lines.prop_cycler = ax._get_lines.prop_cycler
# ax2.plot(data['Test2']['Humidity']['_OneWeek']['_combined']['_5minutes'], label='RH')
# ax2.set_ylabel('Relative humidity ($\%$)', fontsize = 20)
# ax2.legend(loc=(0.92,0.88),prop={'size': 16})

# plt.show()
"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
"3. ANOVA for plant growth"

# file_path = 'ExperimentData_TrudelBrais.xlsx'

"3.1 Mass"
# df = pd.DataFrame()
# column_index = [0]
# df['MagentasNumber'] = pd.read_excel(file_path, usecols=column_index)
# column_index = [1]
# df['Position'] = pd.read_excel(file_path, usecols=column_index)
# column_index = [11]
# df['Plantlet1'] = pd.read_excel(file_path, usecols=column_index, dtype={'Plantlet1': 'float64'})
# column_index = [12]
# df['Plantlet2'] = pd.read_excel(file_path, usecols=column_index, dtype={'Plantlet1': 'float64'})
# column_index = [13]
# df['Plantlet3'] = pd.read_excel(file_path, usecols=column_index, dtype={'Plantlet1': 'float64'})
# df = df.drop([24,25,30,31,36,47,72,73,74,75,76,77,78,79,80])
# df = df.reset_index(drop=True)

# location1 = np.concatenate((df[(df['Position']==1)]['Plantlet1'].values, df[(df['Position']==1)]['Plantlet2'].values,df[(df['Position']==1)]['Plantlet3'].values), axis=0)
# location2 = np.concatenate((df[(df['Position']==2)]['Plantlet1'].values, df[(df['Position']==2)]['Plantlet2'].values,df[(df['Position']==2)]['Plantlet3'].values), axis=0)
# location3 = np.concatenate((df[(df['Position']==3)]['Plantlet1'].values, df[(df['Position']==3)]['Plantlet2'].values,df[(df['Position']==3)]['Plantlet3'].values), axis=0)
# Mass = np.concatenate((location1,location2,location3))

# fStatistic, pvalue = stats.f_oneway(location1, location2, location3)
# kStatistic, pvalue2 = stats.kruskal(location1, location2, location3)

# df_Mass = pd.DataFrame({
#     'Location': ['Location1'] * len(location1) + ['Location2'] * len(location2) + ['Location3'] * len(location3),
#     'Mass': Mass})

# model = ols('Mass ~ Location', data=df_Mass).fit()
# aov_table = sm.stats.anova_lm(model, typ=2)
# aov_table

# ANOVA_Mass = {
#      'fValue':fStatistic,
#     'pValue':pvalue,
#     'leveneP':stats.levene(location1, location2, location3).pvalue,
#     'leveneValue':stats.levene(location1, location2, location3).statistic,
#     'shapiroP':stats.shapiro(model.resid).pvalue,
#     'shapiroValue':stats.shapiro(model.resid).statistic,
#     'kValue':kStatistic,
#     'pValue2':pvalue2
#     }

"3.2 Node"
# df = pd.DataFrame()
# column_index = [0]
# df['MagentasNumber'] = pd.read_excel(file_path, usecols=column_index)
# column_index = [1]
# df['Position'] = pd.read_excel(file_path, usecols=column_index)
# column_index = [18]
# df['Plantlet1'] = pd.read_excel(file_path, usecols=column_index, dtype={'Plantlet1': 'float64'})
# column_index = [19]
# df['Plantlet2'] = pd.read_excel(file_path, usecols=column_index, dtype={'Plantlet1': 'float64'})
# column_index = [20]
# df['Plantlet3'] = pd.read_excel(file_path, usecols=column_index, dtype={'Plantlet1': 'float64'})
# df = df.drop([24,25,30,31,36,47,72,73,74,75,76,77,78,79,80])
# df = df.reset_index(drop=True)

# location1 = np.concatenate((df[(df['Position']==1)]['Plantlet1'].values, df[(df['Position']==1)]['Plantlet2'].values,df[(df['Position']==1)]['Plantlet3'].values), axis=0)
# location2 = np.concatenate((df[(df['Position']==2)]['Plantlet1'].values, df[(df['Position']==2)]['Plantlet2'].values,df[(df['Position']==2)]['Plantlet3'].values), axis=0)
# location3 = np.concatenate((df[(df['Position']==3)]['Plantlet1'].values, df[(df['Position']==3)]['Plantlet2'].values,df[(df['Position']==3)]['Plantlet3'].values), axis=0)
# Node = np.concatenate((location1,location2,location3))

# fStatistic, pvalue = stats.f_oneway(location1, location2, location3)
# kStatistic, pvalue2 = stats.kruskal(location1, location2, location3)

# df_Node = pd.DataFrame({
#     'Location': ['Location1'] * len(location1) + ['Location2'] * len(location2) + ['Location3'] * len(location3),
#     'Node': Node})

# model = ols('Node ~ Location', data=df_Node).fit()

# ANOVA_Node = {
#     'fValue':fStatistic,
#     'pValue':pvalue,
#     'leveneP':stats.levene(location1, location2, location3).pvalue,
#     'leveneValue':stats.levene(location1, location2, location3).statistic,
#     'shapiroP':stats.shapiro(model.resid).pvalue,
#     'shapiroValue':stats.shapiro(model.resid).statistic,
#     'kValue':kStatistic,
#     'pValue2':pvalue2
#     }

"3.3 Height"
# df = pd.DataFrame()
# column_index = [0]
# df['MagentasNumber'] = pd.read_excel(file_path, usecols=column_index)
# column_index = [1]
# df['Position'] = pd.read_excel(file_path, usecols=column_index)
# column_index = [21]
# df['Plantlet1'] = pd.read_excel(file_path, usecols=column_index, dtype={'Plantlet1': 'float64'})
# column_index = [22]
# df['Plantlet2'] = pd.read_excel(file_path, usecols=column_index, dtype={'Plantlet1': 'float64'})
# column_index = [23]
# df['Plantlet3'] = pd.read_excel(file_path, usecols=column_index, dtype={'Plantlet1': 'float64'})
# df = df.drop([24,25,30,31,36,47,72,73,74,75,76,77,78,79,80])
# df = df.reset_index(drop=True)

# location1 = np.concatenate((df[(df['Position']==1)]['Plantlet1'].values, df[(df['Position']==1)]['Plantlet2'].values,df[(df['Position']==1)]['Plantlet3'].values), axis=0)
# location2 = np.concatenate((df[(df['Position']==2)]['Plantlet1'].values, df[(df['Position']==2)]['Plantlet2'].values,df[(df['Position']==2)]['Plantlet3'].values), axis=0)
# location3 = np.concatenate((df[(df['Position']==3)]['Plantlet1'].values, df[(df['Position']==3)]['Plantlet2'].values,df[(df['Position']==3)]['Plantlet3'].values), axis=0)
# Height = np.concatenate((location1,location2,location3))

# fStatistic, pvalue = stats.f_oneway(location1, location2, location3)
# kStatistic, pvalue2 = stats.kruskal(location1, location2, location3)

# df_Height = pd.DataFrame({
#     'Location': ['Location1'] * len(location1) + ['Location2'] * len(location2) + ['Location3'] * len(location3),
#     'Height': Height})

# model = ols('Height ~ Location', data=df_Height).fit()

# statistic12, p_value12 = stats.wilcoxon(location1, location2)
# statistic13, p_value13 = stats.wilcoxon(location1, location3)
# statistic23, p_value23 = stats.wilcoxon(location2, location3)

# fig, ax = plt.subplots()
# # box_param = dict(whis=(1, 99), widths=0.2, medianprops=dict(color='black'),showfliers=False, patch_artist=True)
# bp = ax.boxplot([location1,location2,location3],positions=np.arange(3),showfliers=False)
# ax.set_ylim([0,7])
# plt.ylabel("Plantlet Height (cm)",fontsize=22)
# ax.tick_params(axis='y', labelsize=22)
# ax.set_xticks(np.arange(3))
# ax.set_xticklabels(['Location 1','Location 2','Location 3'], fontsize=22)
# plt.show()

# AVG = []
# STD = []
# MED = []
# for j in ['Location1','Location2','Location3']:
#     AVG = AVG + [df_Height[(df_Height['Location'] == j)]['Height'].mean()]
#     STD = STD + [df_Height[(df_Height['Location'] == j)]['Height'].std()]
#     MED = MED + [df_Height[(df_Height['Location'] == j)]['Height'].median()]
# SimStats = {'Location':[1,2,3],'AVG':AVG,'STD':STD,'MED':MED}
# SimStats = pd.DataFrame(SimStats)

# ANOVA_Height = {
#     'fValue':fStatistic,
#     'pValue':pvalue,
#     'leveneP':stats.levene(location1, location2, location3).pvalue,
#     'leveneValue':stats.levene(location1, location2, location3).statistic,
#     'shapiroP':stats.shapiro(model.resid).pvalue,
#     'shapiroValue':stats.shapiro(model.resid).statistic,
#     'kValue':kStatistic,
#     'pValue2':pvalue2
#     }

"3.4 Score"
# df = pd.DataFrame()
# column_index = [0]
# df['MagentasNumber'] = pd.read_excel(file_path, usecols=column_index)
# column_index = [1]
# df['Position'] = pd.read_excel(file_path, usecols=column_index)
# column_index = [24]
# df['Plantlet1'] = pd.read_excel(file_path, usecols=column_index, dtype={'Plantlet1': 'float64'})
# column_index = [25]
# df['Plantlet2'] = pd.read_excel(file_path, usecols=column_index, dtype={'Plantlet1': 'float64'})
# column_index = [26]
# df['Plantlet3'] = pd.read_excel(file_path, usecols=column_index, dtype={'Plantlet1': 'float64'})
# df = df.drop([24,25,30,31,36,47,72,73,74,75,76,77,78,79,80])
# df = df.reset_index(drop=True)

# location1 = np.concatenate((df[(df['Position']==1)]['Plantlet1'].values, df[(df['Position']==1)]['Plantlet2'].values,df[(df['Position']==1)]['Plantlet3'].values), axis=0)
# location2 = np.concatenate((df[(df['Position']==2)]['Plantlet1'].values, df[(df['Position']==2)]['Plantlet2'].values,df[(df['Position']==2)]['Plantlet3'].values), axis=0)
# location3 = np.concatenate((df[(df['Position']==3)]['Plantlet1'].values, df[(df['Position']==3)]['Plantlet2'].values,df[(df['Position']==3)]['Plantlet3'].values), axis=0)
# Score = np.concatenate((location1,location2,location3))

# fStatistic, pvalue = stats.f_oneway(location1, location2, location3)
# kStatistic, pvalue2 = stats.kruskal(location1, location2, location3)

# df_Score = pd.DataFrame({
#     'Location': ['Location1'] * len(location1) + ['Location2'] * len(location2) + ['Location3'] * len(location3),
#     'Score': Score})

# model = ols('Score ~ Location', data=df_Score).fit()

# ANOVA_Score = {
#     'fValue':fStatistic,
#     'pValue':pvalue,
#     'leveneP':stats.levene(location1, location2, location3).pvalue,
#     'leveneValue':stats.levene(location1, location2, location3).statistic,
#     'shapiroP':stats.shapiro(model.resid).pvalue,
#     'shapiroValue':stats.shapiro(model.resid).statistic,
#     'kValue':kStatistic,
#     'pValue2':pvalue2
#     }

"3.4 MANOVA"
# df_MANOVA = pd.DataFrame({
#     'Location': ['Location1'] * len(location1) + ['Location2'] * len(location2) + ['Location3'] * len(location3),
#     'Mass': Mass,
#     'Quality': Quality,
#     'Height': Height,
#     'Score': Score})

# dependent_vars = ['Mass', 'Height','Score']
# manova = MANOVA.from_formula('Mass + Height + Score ~ Location', data=df_MANOVA)
# print(manova.mv_test())

# y = df_MANOVA[dependent_vars].values
# X = sm.add_constant(pd.get_dummies(df_MANOVA['Location'], drop_first=True).values)
# model = sm.OLS(y, X)
# results = model.fit()
# residuals = results.resid

# # Check multivariate normality assumption
# for i in range(residuals.shape[1]):
#     # Q-Q plot for each dependent variable
#     sm.qqplot(residuals[:, i], line='s')
#     plt.title(f'Q-Q Plot for Residuals of {dependent_vars[i]}')
#     plt.show()

#     # Shapiro-Wilk test for each dependent variable
#     shapiro_test = shapiro(residuals[:, i])
#     p_value = shapiro_test.pvalue
#     if p_value > 0.05:
#         print(f"Residuals for {dependent_vars[i]} appear to be normally distributed (fail to reject the null hypothesis).")
#     else:
#         print(f"Residuals for {dependent_vars[i]} do not appear to be normally distributed (reject the null hypothesis).")

# # Check homogeneity of covariance matrices (homoscedasticity) assumption
# predicted = y - residuals
# for i in range(residuals.shape[1]):
#     # Scatterplot of residuals vs. predicted values for each dependent variable
#     plt.scatter(predicted[:, i], residuals[:, i])
#     plt.xlabel(f'Predicted {dependent_vars[i]}')
#     plt.ylabel(f'Residuals {dependent_vars[i]}')
#     plt.title(f'Residuals vs. Predicted Values for {dependent_vars[i]}')
#     plt.show()

#     # Levene's test for homogeneity of variance
#     levene_test = levene(residuals[:, i], df_MANOVA['Location'])
#     bartlett_test = bartlett(residuals[:, i], df_MANOVA['Location'])
#     if (levene_test.pvalue > 0.05) and (bartlett_test.pvalue > 0.05):
#         print(f"Homogeneity of variance is met for {dependent_vars[i]}.")
#     else:
#         print(f"Homogeneity of variance is not met for {dependent_vars[i]}.")
"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
"4. TIME SERIES ANALYSIS"
"Fonctions for distance metrics"
# def calc_euclidean(actual, predic):
#     return np.sqrt(np.sum((actual - predic) ** 2))

# def calc_mape(actual, predic):
#     return np.mean(np.abs((actual - predic) / ((actual+predic)/2)))

# def calc_correlation(actual, predic):
#     a_diff = actual - np.mean(actual)
#     p_diff = predic - np.mean(predic)
#     numerator = np.sum(a_diff * p_diff)
#     denominator = np.sqrt(np.sum(a_diff ** 2)) * np.sqrt(np.sum(p_diff ** 2))
#     return numerator / denominator

"4.1 Temperature"
# ind = 0
# num = 5
# euclidean_Temp = np.zeros([num,num])
# euclidean_Temp[:,:] = np.nan
# mape_Temp = np.zeros([num,num])
# mape_Temp[:,:] = np.nan
# person_Temp = np.zeros([num,num])
# person_Temp[:,:] = np.nan
# for j in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#     for m in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#         euclidean_Temp[(ind//num),(ind%num)]= calc_euclidean(df[j], df[m])
#         mape_Temp[(ind//num),(ind%num)] = calc_mape(df[j], df[m])
#         person_Temp[(ind//num),(ind%num)] = calc_correlation(df[j], df[m])
#         ind = ind +1
        
"4.2 CO2"
# ind = 0
# num = 5
# euclidean_CO2 = np.zeros([num,num])
# euclidean_CO2[:,:] = np.nan
# mape_CO2 = np.zeros([num,num])
# mape_CO2[:,:] = np.nan
# person_CO2 = np.zeros([num,num])
# person_CO2[:,:] = np.nan
# for j in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#     for m in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#         euclidean_CO2[(ind//num),(ind%num)]= calc_euclidean(df_CO2[j], df_CO2[m])
#         mape_CO2[(ind//num),(ind%num)] = calc_mape(df_CO2[j], df_CO2[m])
#         person_CO2[(ind//num),(ind%num)] = calc_correlation(df_CO2[j], df_CO2[m])
#         ind = ind +1

"4.1 Humidity"
# ind = 0
# num = 5
# euclidean_HR = np.zeros([num,num])
# euclidean_HR[:,:] = np.nan
# mape_HR = np.zeros([num,num])
# mape_HR[:,:] = np.nan
# person_HR = np.zeros([num,num])
# person_HR[:,:] = np.nan
# for j in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#     for m in ['Loc1','Loc2','Loc3','Loc4','Loc5']:
#         euclidean_HR[(ind//num),(ind%num)]= calc_euclidean(df_HR[j], df_HR[m])
#         mape_HR[(ind//num),(ind%num)] = calc_mape(df_HR[j], df_HR[m])
#         person_HR[(ind//num),(ind%num)] = calc_correlation(df_HR[j], df_HR[m])
#         ind = ind +1
"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"