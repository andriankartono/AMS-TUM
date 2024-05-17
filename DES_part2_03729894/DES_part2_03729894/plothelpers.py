from matplotlib import pyplot


class BoxPlot(object):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

    def __init__(self, name: str = "default"):
        """
        Constructor for a boxplot
        :param name: optional name of the statistics in boxplot
        """
        #######################################
        # TODO Task 2.5.1: Your code goes here
        self.name = name
        self.counter_datas = [] # will be a list of list
        #######################################

    def add_counter_data(self, values: list):
        """
        Add set of values of a counter to the internal array.
        :param values: list of values of a counter
        """
        #######################################
        # TODO Task 2.5.1: Your code goes here
        self.counter_datas.append(values)
        #######################################

    def plot(self, labels: list = None):
        """
        Plot function for boxplot.
        :param labels: if not None, it defines the labels for x-axis of boxplot
        """
        #######################################
        # TODO Task 2.5.1: Your code goes here
        if labels is not None:
            pyplot.boxplot(self.counter_datas, labels = labels, showmeans=True, meanline = True)
        else:
            pyplot.boxplot(self.counter_datas, showmeans=True, meanline = True)

        pyplot.title(self.name)

        # limitations used to constraint the plots
        # comment if considered unnecessary
        # if self.name == "waiting time":
        #     pyplot.ylim(0,4000)
        # elif self.name == "queue length":
        #     pyplot.ylim(0,6)

        pyplot.show()
        #######################################
