import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from ai_model import AIModel

CONFUSION_MATRIX_TITLE =  'Confusion Matrix'
CANT_SHOW_CONFUSION_MATRIX_MSG =  (
    'No confusion matrix to plot. '
    'Loaded Models are not tested, and so, don\'t has confusion matrix'
) 
SCATTER_PLOT_UNAVAILABLE_MSG = 'Scatter Plot not available'
PLOTTING_DATA_MSG = 'Plotting data...'
TITLE = 'KNN Model'

class Layout:
    def __init__(self, figure: plt.Figure = None, rows = 1, columns = 1):
        self.rows = rows
        self.columns = columns
        self.index = 1
        self.figure: plt.Figure = figure
        self.gs = gridspec.GridSpec(rows, columns)

    def get_ax(self, projection = None):
        total = self.rows * self.columns
        if self.index <= total:
            ax = self.figure.add_subplot(
                self.gs[self.index - 1],
                projection=projection
            )
            self.index += 1
            return ax

class Plot:
    def __init__(self, model: AIModel, scatter_plot_len=200):
        self.X_test, self.y_test = model.get_test_data()
        self.y_pred = model.get_predicted_data()
        self.scatter_plot_len = scatter_plot_len

    def plot_confusion_matrix(self):
        if self.should_plot_confusion_matrix():
            ax = self.layout.get_ax()
            ax.set_title(CONFUSION_MATRIX_TITLE)
            cm = confusion_matrix(self.y_test, self.y_pred)
            ConfusionMatrixDisplay(
                confusion_matrix=cm,
                display_labels=['healthy', 'unhealthy']
            ).plot(ax=ax)
        else:
            print(CANT_SHOW_CONFUSION_MATRIX_MSG)

    def prepare_scatter_data(self, scatter_plot_len=200):
        if len(self.X_test) < scatter_plot_len:
            plot_len = len(self.X_test)
        else:
            plot_len = scatter_plot_len

        # Healthy rows from Test DataFrame pointed by y_pred indexes with 0 label
        healthyIndexes = np.where(self.y_pred == 0)[0].tolist()
        self.healthy = self.X_test.iloc[
            healthyIndexes[0:plot_len], :]

        # UnHealthy rows from Test DataFrame pointed by y_pred indexes with 1 label
        unhealthyIndexes = np.where(self.y_pred == 1)[0].tolist()
        self.unhealthy = self.X_test.iloc[
            unhealthyIndexes[0:plot_len], :]

    def plot_scatter(self):
        if self.should_plot_scatter():
            self.prepare_scatter_data(self.scatter_plot_len)

            ax = self.layout.get_ax(projection='3d')
            ax.set_title('Scatter Plot')

            ax.scatter(
                self.healthy.iloc[:, 0],
                self.healthy.iloc[:, 1],
                self.healthy.iloc[:, 2],
                color='blue',
                marker='x',
                label='Healthy'
            )

            ax.scatter(
                self.unhealthy.iloc[:, 0],
                self.unhealthy.iloc[:, 1],
                self.unhealthy.iloc[:, 2],
                color='red',
                marker='o',
                label='Unhealthy',
                alpha=0.3
            )

            ax.set_xlabel('Heart Rate')
            ax.set_ylabel('Body Temperature')
            ax.set_zlabel('spo2')
            ax.set_title('Scatter Plot')
        else:
            print(SCATTER_PLOT_UNAVAILABLE_MSG)

    def should_plot_scatter(self, print_scatter=True):
        return print_scatter and self.y_pred is not None

    def should_plot_confusion_matrix(self, print_confusion_matrix=True):
        return print_confusion_matrix and self.y_pred is not None and self.y_test is not None

    def make_layout(self, fig: plt.Figure):
        total_plots = 0

        if self.should_plot_scatter():
            total_plots += 1
        if self.should_plot_confusion_matrix():
            total_plots += 1

        self.layout = Layout(figure=fig, rows=1, columns=total_plots)

    def show(self):
        print(PLOTTING_DATA_MSG)

        fig = plt.figure(figsize=(8, 6))

        fig.suptitle(TITLE)

        self.make_layout(fig)

        self.plot_scatter()
        self.plot_confusion_matrix()    
        
        plt.subplots_adjust(wspace=0.3, left=0.1, right=0.9, bottom=0.1, top=0.9)
        plt.tight_layout(pad=2)

        plt.show()
