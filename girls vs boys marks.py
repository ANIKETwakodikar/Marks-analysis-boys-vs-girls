import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/content/exams.csv')
df['avgscore']=(df['math score']+df['reading score']+df['writing score'])//3
boys=df.loc[df['gender']=='male']['avgscore']
plt.plot(boys,'xr')
girls=df.loc[df['gender']=='female']['avgscore']
plt.plot(girls,'xb')
plt.xticks([0,100,200,300,400,500,600,700,800,900,1000])

