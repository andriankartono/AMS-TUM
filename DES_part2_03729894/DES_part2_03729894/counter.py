import numpy


class Counter(object):
    """
    Counter class is an abstract class, that counts values for statistics.

    Values are added to the internal array. The class is able to generate mean value, variance and standard deviation.
    The report function prints a string with name of the counter, mean value and variance.
    All other methods have to be implemented in subclasses.
    """

    def __init__(self, name="default"):
        """
        Initialize a counter with a name.
        The name is only for better distinction between counters.
        :param name: identifier for better distinction between various counters
        """
        self.name = name
        self.values = []

    def count(self, *args):
        """
        Count values and add them to the internal array.
        Abstract method - implement in subclass.
        """
        raise NotImplementedError("Please Implement this method")

    def reset(self, *args):
        """
        Delete all values stored in internal array.
        """
        self.values = []

    def get_mean(self):
        """
        Returns the mean value of the internal array.
        Abstract method - implemented in subclass.
        """
        raise NotImplementedError("Please Implement this method")

    def get_var(self):
        """
        Returns the variance of the internal array.
        Abstract method - implemented in subclass.
        """
        raise NotImplementedError("Please Implement this method")

    def get_stddev(self):
        """
        Returns the standard deviation of the internal array.
        Abstract method - implemented in subclass.
        """
        raise NotImplementedError("Please Implement this method")

    def report(self):
        """
        Print report for this counter.
        """
        if len(self.values) != 0:
            print("Name: " + str(self.name) + ", Mean: " + str(self.get_mean()) + ", Variance: " + str(self.get_var()))
        else:
            print("List for creating report is empty. Please check.")


class TimeIndependentCounter(Counter):
    """
    Counter for counting values independent of their duration.
    """

    def __init__(self, name="default"):
        """
        Initialize the TIC object.
        """
        super(TimeIndependentCounter, self).__init__(name)

    def count(self, value):
        """
        Add a new value to the internal array.
        :param: value that should be added to the internal array
        """
        #######################################
        # TODO Task 2.4.1: Your code goes here
        self.values.append(value)
        #######################################

    def get_mean(self):
        """
        Return the mean value of the internal array.
        """
        #######################################
        # TODO Task 2.4.1: Your code goes here
        return numpy.mean(self.values)
        #######################################

    def get_var(self, biased=False):
        """
        Return the variance of the internal array.
        Note, that we take the estimated variance, not the exact variance.
        :param biased: bool indicating if the calculated variance should be biased
        """
        #######################################
        # TODO Task 2.4.1: Your code goes here
        if biased:
            return numpy.var(self.values)
        else:
            return numpy.var(self.values, ddof=1)
        #######################################

    def get_stddev(self):
        """
        Returns the unbiased standard deviation of the internal array.
        """
        #######################################
        # TODO Task 2.4.1: Your code goes here
        return numpy.std(self.values, ddof=1)
        #######################################


class TimeDependentCounter(Counter):
    """
    Counter, that counts values considering their duration as well.

    Methods for calculating mean, variance and standard deviation are available.
    """

    def __init__(self, name="default"):
        """
        Initialize TDC with the simulation it belongs to and the name.
        :param: name is an identifier for better distinction between multiple counters.
        """
        super(TimeDependentCounter, self).__init__(name)
        #######################################
        # TODO Task 2.4.2: Your code goes here
        self.first_timestamp = 0
        self.last_timestamp = 0
        self.time_intervals = []
        #######################################

    def count(self, value: float, now: float):
        """
        Adds new value to internal array.
        Duration from last to current value is considered.
        :param value: value to be counted
        :param now: the timestamp when the value is counted
        """
        #######################################
        # TODO Task 2.4.2: Your code goes here
        self.last_timestamp = now
        self.time_intervals.append(self.last_timestamp- self.first_timestamp)
        self.first_timestamp = self.last_timestamp # update the timestamp to be used for the next interval
        self.values.append(value)

        #######################################

    def get_mean(self):
        """
        Return the mean value of the counter, normalized by the total duration of the simulation.
        """
        #######################################
        # TODO Task 2.4.2: Your code goes here
        sum = 0
        for value, time_interval in zip(self.values,self.time_intervals):
            sum += (value * time_interval)
        
        return sum / self.last_timestamp 
        #######################################

    def get_var(self):
        """
        Return the unbiased variance of the TDC.
        """
        #######################################
        # TODO Task 2.4.2: Your code goes here
        sum = 0
        n = len(self.values)
        for value, time_interval in zip(self.values, self.time_intervals):
            sum += (value ** 2) * time_interval

        return ((sum/self.last_timestamp) - (self.get_mean()**2)) *n / (n-1)
        #######################################

    def get_stddev(self):
        """
        Returns the unbiased standard deviation of the internal array.
        """
        #######################################
        # TODO Task 2.4.2: Your code goes here
        return numpy.sqrt(self.get_var())
        #######################################

    def reset(self):
        """
        Reset the counter to its initial state.
        """
        #######################################
        # TODO Task 2.4.2: Your code goes here
        self.values = []
        self.first_timestamp = 0
        self.last_timestamp = 0
        self.time_intervals = []
        #######################################

