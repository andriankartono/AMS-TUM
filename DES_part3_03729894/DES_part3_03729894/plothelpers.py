from matplotlib import pyplot
from enum import Enum
import numpy as np

class BoxPlot(object):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

    def __init__(self, name: str = "default"):
        """
        Constructor for a boxplot
        :param name: optional name of the statistics in boxplot
        """
        #######################################
        # DONE Task 2.5.1:
        self.counters_values = []
        self.name = name
        #######################################

    def add_counter_data(self, values: list):
        """
        Add set of values of a counter to the internal array.
        :param values: list of values of a counter
        """
        #######################################
        # DONE Task 2.5.1:
        self.counters_values.append(values)
        #######################################

    def plot(self, labels: list = None):
        """
        Plot function for boxplot.
        :param labels: if not None, it defines the labels for x-axis of boxplot
        """
        #######################################
        # DONE Task 2.5.1:
        data = self.counters_values

        bp = pyplot.boxplot(data, showmeans=True, patch_artist=True, labels=labels)
        for patch, color in zip(bp['boxes'], self.colors):
            patch.set_facecolor(color)

        #######################################


class HistType(Enum):
    LINE = 1
    BAR = 2

class Histogram(object):

    """
    Histogram can take values for statistics and plot a histogram from them.

    Values are added to the internal array. The class is able to generate a histogram and plot it using pyplot.
    """

    # colors for plotting multiple plots in one figure
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

    def __init__(self):
        """
        Constructor for a simple histogram
        """
        self.counters_values = []
        self.n_bins = 0
        self.weights = None

    def add_counter_data(self, values : list, weights: list=None):
        """
        Add a value to the histogram.
        :param values: the list of values of a counter to be plotted
        :param weights: the list of weights of a counter if this counter is TDC
        """
        #######################################
        # TODO Task 3.2.1: Your code goes here.
        self.counters_values.extend(values)
        
        # only extend if list exists already. Otherwise initialize a new list
        if weights is not None:
            if self.weights is not None:
                self.weights.extend(weights)
            else:
                self.weights = weights
        
        #######################################

    def reset(self):
        """
        Reset all values to their initial state.
        """
        self.counters_values = []
        self.n_bins = 0
        self.weights = None

    def plot(self, diag_type: HistType = HistType.BAR, labels: list=None, n_bins: int=None):
        """
        Plot function for histogram.
        :param diag_type: is the type of the histogram - Bar or Line
        :param labels: if not None, specifies labels for x-axis
        :param n_bins: if not None, specifies number of bins
        """
        #######################################
        # TODO Task 3.2.2: Your code goes here.
        if n_bins is None:
            n_bins = len(self.counters_values)

        if diag_type == 1:
            pyplot.hist(self.counters_values, labels=labels, bins=n_bins, weights=self.weights, diag_type="step")
        elif diag_type ==2:
            pyplot.hist(self.counters_values, labels=labels, bins=n_bins, weights=self.weights, diag_type="bar")
        #######################################