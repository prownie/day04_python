from FileLoader import FileLoader
import pandas as pd


class SpatioTemporalData:

    def __init__(self, data):
        self.data = data

    def when(self, location):
        mask_loc = self.data['City'] == location
        return (self.data[mask_loc]['Year'].unique().tolist())

    def where(self, date):
        mask_date = self.data['Year'] == date
        return (self.data[mask_date]['City'].unique()[0])


fl = FileLoader()
df = fl.load("../athlete_events.csv")

sp = SpatioTemporalData(df)

print(sp.where(1896))
print(sp.where(2016))
print(sp.when('Athina'))
print(sp.when('Paris'))
