import pandas as pd


class FileLoader:

    def load(self, path):
        try:
            df = pd.read_csv(path)
            shape = df.shape
            print(f"Loading dataset of dimensions {shape[0]} x {shape[1]}")
            return(df)
        except:
            print("cant open file")
            return(None)

    def display(self, df, n):
        try:
            if n >= 0:
                print(df.head(n))
            else:
                print(df.tail(n))
        except:
            print("Error during display method")


fl = FileLoader()
df = fl.load("../athlete_events.csv")
fl.display(df, 5)
