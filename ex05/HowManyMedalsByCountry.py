from FileLoader import FileLoader
import pandas as pd
import pprint

def countMedals(data, ret):
    for index, row in data.iterrows():
        if isinstance(row['Medal'], str):
            ret[row['Year']][row['Medal']] = ret[row['Year']][row['Medal']] + 1
    return(ret)


def howManyMedalsByCountry(data, country):
    ret = {}
    mask_country = (data["Team"] == country)
    filt = data[mask_country]
    for i in filt['Year'].unique():
        ret[i] = {}
        for j in ('Gold', 'Silver', 'Bronze'):
            ret[i][j] = 0
    mask_country = (data["Team"] == country) & (data["Year"] == 2000)
    ret = countMedals(filt, ret)
    return(ret)


def howManyMedalsByCountryWithGroup(data, country):
    ret = {}
    mask_country = (data["Team"] == country) & (data["Year"].isin([2000,2004,2006]))
    grouped = data[mask_country].groupby(["Year","Medal"])["Year","Medal"]
    print(grouped.size())

    masked = data[mask_country]
    test = pd.MultiIndex.from_product((masked.Year.unique(), masked.Medal.unique()))
    grouped.size().reindex(test).fillna(0)
    print(test)

fl = FileLoader()
df = fl.load("../athlete_events.csv")
pp = pprint.PrettyPrinter(indent=4)

without_group = howManyMedalsByCountry(df, "Kenya")
pp.pprint(without_group)

with_group = howManyMedalsByCountryWithGroup(df, "Kenya")
