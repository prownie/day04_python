from FileLoader import FileLoader
import pandas as pd
import pprint


def youngestFellah(data, year):
    ret = {}
    maskf = (data['Sex'] == 'F') & (data['Year'] == year)
    maskm = (data['Sex'] == 'M') & (data['Year'] == year)
    ret['f'] = data[maskf]['Age'].min()
    ret['m'] = data[maskm]['Age'].min()
    return(ret)


fl = FileLoader()
df = fl.load("../athlete_events.csv")

filtered_dict = youngestFellah(df, 2004)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(filtered_dict)
