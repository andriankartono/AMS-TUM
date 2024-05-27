import numpy
import scipy.stats
from enum import Enum

class TestDist(Enum):
    NORMAL = 1
    EXPONENTIAL = 2

class ChiSquare(object):

    def __init__(self, emp_x: list, emp_n: list, distr: TestDist = TestDist.NORMAL):
        """
        Initialize chi square test with observations and their frequency.
        :param emp_x: observation values (bins)
        :param emp_n: frequency
        :param distr: type of tested distribution
        """
        self.emp_x = emp_x
        self.emp_n = emp_n
        self.distr = distr
        if distr == TestDist.NORMAL:
            self.dist_f = scipy.stats.norm
        if distr == TestDist.EXPONENTIAL:
            self.dist_f = scipy.stats.expon

    def test_distribution(self, alpha: float, mean: float, est_parameters: int = 0, var: float = None):
        """
        Test, if the observations fit into a given distribution.
        :param alpha: significance level of test
        :param mean: mean value of the tested distribution
        :param est_parameters: number of the distribution parameters estimated from samples
        :param var: variance value of the tested distribution if applicable
        :return: chi2-value and the corresponding table value
        """
        #######################################
        # TODO Task 3.7.1: Your code goes here.
        
        k = len(self.emp_n)
        total_observations = sum(self.emp_n)
        expected_freq = numpy.zeros(k)
        emp_n_copy = self.emp_n # create a copy that can be modified
        emp_x_copy = self.emp_x

        # check to see if estimated frequency meets the minimum value
        if self.distr == TestDist.NORMAL:
            cdf_values = self.dist_f.cdf(self.emp_x, loc=mean, scale = numpy.sqrt(var))
        elif self.distr == TestDist.EXPONENTIAL:
            cdf_values = self.dist_f.cdf(self.emp_x, scale = mean)

        # calculate expected frequencies
        for i in range(k):
            expected_freq[i] = total_observations * (cdf_values[i+1] - cdf_values[i])

        # combine frequencies starting from the front
        for i in range(k):
            if expected_freq[0] < 5:

                # modify the values of expected_freq
                expected_freq[0] += expected_freq[1]
                expected_freq = numpy.delete(expected_freq,1)
                
                # modify the copy of emp_n to work with
                emp_n_copy[0] += emp_n_copy[1]
                emp_n_copy = numpy.delete(emp_n_copy, 1)

                # modify the endpoints of the first interval
                emp_x_copy = numpy.delete(emp_x_copy, 1)
            else:
                break

        # modify frequencies at the end of the list
        for i in range(len(expected_freq)):
            if expected_freq[-1] < 5:
                # modify value of expected_freq
                expected_freq[-2] += expected_freq[-1]
                expected_freq = numpy.delete(expected_freq,-1)

                # modify the copy of emp_n to work with
                emp_n_copy[-2] += emp_n_copy[-1]
                emp_n_copy = numpy.delete(emp_n_copy, -1)

                # modify the endpoints of the last interval
                emp_x_copy = numpy.delete(emp_x_copy, -2)
            else:
                break

        # calculate chi square statistic
        chi2 = numpy.sum((emp_n_copy-expected_freq)**2 / expected_freq)

        # degrees of freedom
        dof = k-est_parameters-1

        chi2_critical = scipy.stats.chi2.ppf(1-alpha,dof)

        return chi2, chi2_critical
            
        #######################################

