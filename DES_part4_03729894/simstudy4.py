import plothelpers
import counter
import numpy as np

autocor_counter_1 = counter.TimeIndependentAutocorrelationCounter("autocorr 1")
autocor_counter_2 = counter.TimeIndependentAutocorrelationCounter("autocorr 2")

heatmap_plothelper_1 = plothelpers.Heatmap()
heatmap_plothelper_2 = plothelpers.Heatmap()

seq_1 = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5]
seq_2 = [3, -5, 5, -1, 3, -5, 5, 1, 3, -5]

print(25/np.var(seq_1,ddof=1))
print(np.cov(seq_1,seq_1))

for value in seq_1:
    autocor_counter_1.count(value)

for value in seq_2:
    autocor_counter_2.count(value)

# covariance should be equal to the variance of either of the list
autocor_counter_1.report()