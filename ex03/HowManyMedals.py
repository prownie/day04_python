from FileLoader import FileLoader
import pandas as pd
import pprint

def howManyMedals(data, name):
    ret = {}
    mask_by_name = (data['Name'] == name)
    filt = data[mask_by_name]
    for i in filt['Year'].unique():
        ret[i] = {}
        for j in ('Gold', 'Silver', 'Bronze'):
            ret[i][j] = 0
    for index, row in filt.iterrows():
        if isinstance(row['Medal'], str):
            ret[row['Year']][row['Medal']] = ret[row['Year']][row['Medal']] + 1
    return(ret)


fl = FileLoader()
df = fl.load("../athlete_events.csv")

medals = howManyMedals(df, "Kjetil Andr Aamodt")

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(medals)
