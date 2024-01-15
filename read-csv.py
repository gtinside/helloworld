import pandas as pd

class ReadCSV:
    def __init__(self) -> None:
        self.csv = "sample.csv"
        
    
    def printData(self):
        data = pd.read_csv(self.csv)
        print(len(data))


if __name__ == "__main__":
    rd = ReadCSV().printData()