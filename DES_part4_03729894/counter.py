import numpy
import math


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

    def count(self, value: float):
        """
        Add a new value to the internal array.
        :param: value that should be added to the internal array
        """
        self.values.append(value)

    def get_mean(self):
        """
        Return the mean value of the internal array.
        """
        if len(self.values) > 0:
            return numpy.mean(self.values)
        else:
            return None

    def get_var(self, biased=False):
        """
        Return the variance of the internal array.
        Note, that we take the estimated variance, not the exact variance.
        :param biased: bool indicating if the calculated variance should be biased
        """
        if biased:
            return numpy.var(self.values)
        else:
            return numpy.var(self.values, ddof=1)

    def get_stddev(self):
        """
        Returns the unbiased standard deviation of the internal array.
        """
        return numpy.sqrt(self.get_var())


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
        self.first_timestamp = 0
        self.last_timestamp = 0
        self.weights = []

    def count(self, value: float, now: float):
        """
        Adds new value to internal array.
        Duration from last to current value is considered.
        :param value: value to be counted
        :param now: the timestamp when the value is counted
        """
        dt = now - self.last_timestamp
        if dt < 0:
            print("Error in calculating time dependent statistics. Current time is smaller than last timestamp.")
            raise ValueError
        self.values.append(value)
        self.weights.append(dt)
        self.last_timestamp = now

    def get_mean(self):
        """
        Return the mean value of the counter, normalized by the total duration of the simulation.
        """
        return float(sum([self.values[i] * self.weights[i] for i in range(len(self.values))])) /\
            float((self.last_timestamp - self.first_timestamp))

    def get_var(self):
        """
        Return the unbiased variance of the TDC.
        """
        dt = self.last_timestamp - self.first_timestamp
        mean = self.get_mean()
        return len(self.values) / (len(self.values) - 1) * (float(sum([self.values[i]**2 * self.weights[i]
                            for i in range(len(self.values))])) / float(dt) - mean**2)

    def get_stddev(self):
        """
        Returns the unbiased standard deviation of the internal array.
        """
        return numpy.sqrt(self.get_var())

    def reset(self):
        """
        Reset the counter to its initial state.
        """
        self.first_timestamp = 0
        self.last_timestamp = 0
        self.weights = []
        Counter.reset(self)


class TimeIndependentCrosscorrelationCounter(TimeIndependentCounter):
    """
    Counter that is able to calculate cross correlation (and covariance).
    """

    def __init__(self, name="default"):
        """
        Crosscorrelation counter contains three internal counters containing the variables
        :param name: is a string for better distinction between counters.
        """
        super(TimeIndependentCrosscorrelationCounter, self).__init__(name)
        #######################################
        # TODO Task 4.1.1: Your code goes here
        self.values_x = []
        self.values_y = []
        self.values_xy = []
        #######################################

    def reset(self):
        """
        Reset the TICCC to its initial state.
        """
        TimeIndependentCounter.reset(self)
        #######################################
        # TODO Task 4.1.1: Your code goes here
        self.values_x = []
        self.values_y = []
        self.values_xy = []
        #######################################

    def count(self, x, y):
        """
        Count two values and their product for the correlation between them. They are added to the two internal arrays.
        """
        #######################################
        # TODO Task 4.1.1: Your code goes here
        self.values_x.append(x)
        self.values_y.append(y)
        self.values_xy.append(x*y)
        #######################################

    def get_cov(self):
        """
        Calculate the covariance between the two internal arrays x and y.
        """
        #######################################
        # TODO Task 4.1.1: Your code goes here
        result = float(numpy.mean(self.values_xy)- numpy.mean(self.values_x)*numpy.mean(self.values_y))
        return result
        #######################################

    def get_cor(self):
        """
        Calculate the correlation coefficient between the two internal arrays x and y.
        """
        #######################################
        # TODO Task 4.1.1: Your code goes here
        # ddof is N-1 with N assumed to be the number of servers. In simulation study of task 4 -> ddof = 1
        result = float(self.get_cov() / numpy.sqrt(numpy.var(self.values_x,ddof=len(self.values_x-1))*numpy.var(self.values_y,ddof=len(self.values_x-1))))
        return result
        #######################################

    def report(self):
        """
        Print a report string for the TICCC.
        """
        print('Name: ' + self.name + '; covariance = ' + str(self.get_cov()) + '; correlation = ' + str(self.get_cor()))


class TimeIndependentAutocorrelationCounter(TimeIndependentCounter):
    """
    Counter, that is able to calculate auto correlation with given lag.
    """

    def __init__(self, name="default", max_lag=10):
        """
        Create a new auto correlation counter object.
        :param name: string for better distinction between multiple counters
        :param max_lag: maximum available lag (defaults to 10)
        """
        super(TimeIndependentAutocorrelationCounter, self).__init__(name)
        #######################################
        # TODO Task 4.1.2: Your code goes here
        self.max_lag = max_lag
        #######################################

    def get_auto_cov(self, lag):
        """
        Calculate the auto covariance for a given lag.
        :return: auto covariance
        """
        #######################################
        # TODO Task 4.1.2: Your code goes here
        if lag <= self.max_lag:
            values_lag = numpy.roll(self.values, lag)
            mul_result = numpy.multiply(self.values, values_lag)
            result = float(numpy.mean(mul_result)- numpy.mean(self.values)*numpy.mean(values_lag))
            return result
        else:
            raise ValueError("lag is larger than max_lag")
        #######################################

    def get_auto_cor(self, lag):
        """
        Calculate the auto correlation for a given lag.
        :return: auto correlation coefficient
        """
        #######################################
        # TODO Task 4.1.2: Your code goes here
        values_lag = numpy.roll(self.values, lag)
        result = float(self.get_auto_cov(lag) / numpy.sqrt(numpy.var(self.values,ddof=len(self.values)-1)*numpy.var(values_lag,ddof=len(values_lag-1))))
        return result
        #######################################

    def set_max_lag(self, max_lag):
        """
        Change maximum lag. Cycle length is set to max_lag + 1.
        """
        #######################################
        # TODO Task 4.1.2: Your code goes here
        self.max_lag = max_lag
        #######################################

    def report(self):
        """
        Print report for auto correlation counter.
        """
        print('Name: ' + self.name)
        for i in range(0, self.max_lag + 1):
            print('Lag = ' + str(i) + '; covariance = ' + str(self.get_auto_cov(i)) + '; correlation = ' + str(
                self.get_auto_cor(i)))
