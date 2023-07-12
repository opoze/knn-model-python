import matplotlib.pyplot as plt

class Descriptive:
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame
    
    def histogram(self, columnName):
        self.dataFrame[columnName].hist(bins=15)
        plt.title('Histogram of ' + columnName)
        plt.grid(visible=False, axis='y', alpha=0.75)
        plt.show()

    def correlation(self, columnName):
        correlation = self.dataFrame.corr()
        print(correlation[columnName])
