#%%
import pandas as pd
from pathlib import Path
import numpy as np 

file2013 = pd.read_csv("data/aco_performance_puf/2013_SSP_ACO_PUF/Final.ACO.SSP.PUF.Y2013_with_risk_scores.csv")
file2014 = pd.read_csv("data/aco_performance_puf/2014_SSP_ACO_PUF/ACO.SSP.PUF.Y2014.FINAL.csv")
file2015 = pd.read_csv("data/aco_performance_puf/2015_SSP_ACO_PUF/ACO.SSP.PUF.Y2015.csv")
file2016 = pd.read_csv("data/aco_performance_puf/2016_SSP_ACO_PUF/ACO.SSP.PUF.Y2016.csv")
file2017 = pd.read_csv("data/aco_performance_puf/2017_SSP_ACO_PUF/ACO.SSP.PUF.Y2017.csv")


#%%
file2013['year'] = 2013
file2013['EarnSaveLoss'] = file2013.EarnShrSavings
file2013['ACO_Name'] = file2013.ACO_NAME

file2014['year'] = 2014
file2015['year'] = 2015
file2016['year'] = 2016
file2017['year'] = 2017

interesting_columns = ['year','ACO_Name','EarnSaveLoss','N_AB','CMS_HCC_RiskScore_AGND_PY']
all_frames = [file2013, file2014, file2015,file2016, file2017]
combined_frame = pd.concat([frame[interesting_columns] for frame in all_frames])


#%%
def de_comma_number(num):
    num_str = str(num)
    try:
        float(num_str.replace(",",""))
    except:
        return 0
    return float(num_str.replace(",",""))


def earning(save_loss):
    if type(save_loss) == str:
        num_val = de_comma_number(save_loss)
    else:
        num_val = save_loss
    
    if num_val > 0:
        return "Earned"
    else:
        return "No Earnings"

combined_frame['Earning'] = combined_frame.EarnSaveLoss.apply(earning)
combined_frame['members'] = combined_frame.N_AB.apply(de_comma_number)
print(combined_frame.columns)

#%%
combined_frame.to_csv("ACO-All-Years-Combined.csv")