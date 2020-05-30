from FileLoader import FileLoader
import pandas as pd


def proportionBySport(data, year, sport, gender):

    mask_by_sport_gender = (data['Year'] == year) &\
                           (data['Sport'] == sport) & (data['Sex'] == gender)
    mask_by_gender = (data['Year'] == year) & (data['Sex'] == gender)

    sport_gender = data[mask_by_sport_gender].copy()
    sport_gender.drop_duplicates(subset="Name", inplace=True)

    gender = data[mask_by_gender].copy()
    gender.drop_duplicates(subset="Name", inplace=True)

    return(sport_gender.shape[0] / gender.shape[0])


fl = FileLoader()
df = fl.load("../athlete_events.csv")

prop = proportionBySport(df, 2004, 'Tennis', 'F')
print(prop)
