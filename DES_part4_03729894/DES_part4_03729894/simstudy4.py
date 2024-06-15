from simulation import Simulation
from simparam import SimParam, ARR_PROCESS
from matplotlib import pyplot

import plothelpers
import counter
import numpy as np

def task_4_2_1():
    # it is also possible to reset the counter but for simplicity I decide to create two counters instead
    autocor_counter_1 = counter.TimeIndependentAutocorrelationCounter("autocorr 1")
    autocor_counter_2 = counter.TimeIndependentAutocorrelationCounter("autocorr 2")
    autocor_counter_1.set_max_lag(1)
    autocor_counter_2.set_max_lag(3)

    for _ in range(5000):
        # 4 commands per loop to make both counters equal in size
        autocor_counter_1.count(5)
        autocor_counter_1.count(-5)
        autocor_counter_1.count(5)
        autocor_counter_1.count(-5)

        autocor_counter_2.count(3)
        autocor_counter_2.count(-5)
        autocor_counter_2.count(5)
        autocor_counter_2.count(-1)

    # covariance should be equal to the variance of either of the list
    # there will be minor difference here with common implementations because for the mean we are dividing by n
    # some implementations such as numpys divide by n-1 instead (assumed to be related to dof) 
    autocor_counter_1.report() # correlation value should be close to 1/-1 for lag size of 0/1
    autocor_counter_2.report() # value close to 1 for 0

def task_4_3_1(offered_traffic):
    simparam = SimParam()
    sim = Simulation(simparam)

    simparam.SIM_TIME = 10000000
    simparam.S = 10000
    simparam.SERVICE_RATES = [0.015]
    simparam.NUM_USERS = 2
    simparam.USERS_SEEDS = [None]*2

    heatmap_correlation = plothelpers.Heatmap()
    arrival_rate = offered_traffic * 0.015

    simparam.ARRIVAL_RATES = [arrival_rate/2, arrival_rate/2]
    sim.reset()
    print(f"simulation with offered traffic of {offered_traffic}")
    sim.do_simulation()
    
    # add correlation values
    heatmap_correlation.add_corr_coef("IAT", "WT", sim.statistics_collection.cnt_iat_wt.get_cor())
    heatmap_correlation.add_corr_coef("IAT", "serving_time", sim.statistics_collection.cnt_iat_st.get_cor())
    heatmap_correlation.add_corr_coef("IAT", "system_time", sim.statistics_collection.cnt_iat_syst.get_cor())
    heatmap_correlation.add_corr_coef("serving_time", "system_time", sim.statistics_collection.cnt_st_syst.get_cor())
    heatmap_correlation.add_corr_coef("WT1", "WT2", sim.statistics_collection.cnt_wt1_wt2.get_cor())

    heatmap_correlation.plot()

    # print autocorrelation values
    sim.statistics_collection.acnt_iat.report()
    sim.statistics_collection.acnt_wt.report()

def task_4_3_2(offered_traffic):
    simparam = SimParam()
    sim = Simulation(simparam)

    simparam.SIM_TIME = 10000000
    simparam.S = 10000
    simparam.SERVICE_RATES = [0.015]
    simparam.NUM_USERS = 2
    simparam.USERS_SEEDS = [None]*2

    arrival_rate = offered_traffic * 0.015

    simparam.ARRIVAL_RATES = [arrival_rate/2, arrival_rate/2]
    sim.reset()
    print(f"simulation with offered traffic of {offered_traffic}")
    sim.do_simulation()

    iat = sim.statistics_collection.cnt_iat_st.values_x
    service_time = sim.statistics_collection.cnt_iat_st.values_y
    system_time = sim.statistics_collection.cnt_iat_syst.values_y

    pyplot.subplot(121)
    pyplot.title(f"offered traffic = {offered_traffic}")
    pyplot.xlabel("IAT")
    pyplot.ylabel("service time")
    pyplot.scatter(iat, service_time)

    pyplot.subplot(122)
    pyplot.title(f"offered traffic = {offered_traffic}")
    pyplot.xlabel("service time")
    pyplot.ylabel("system time")
    pyplot.scatter(service_time, system_time)

def task_4_3_3(n):
    simparam = SimParam()
    sim = Simulation(simparam)

    simparam.SIM_TIME = 10000000
    simparam.S = 10000
    simparam.SERVICE_RATES = [0.015]
    simparam.NUM_USERS = 2
    simparam.USERS_SEEDS = [None]*2

    for offered_traffic in [0.01,0.5,0.8,0.95]:
        arrival_rate = offered_traffic * 0.015

        simparam.ARRIVAL_RATES = [arrival_rate/2, arrival_rate/2]
        sim.reset()
        print(f"simulation with offered traffic of {offered_traffic}")
        sim.do_simulation_n_limit(n)

        lag = []
        autocorr = []

        for i in range(20):
            lag.append(i+1)
            autocorr.append(sim.statistics_collection.acnt_wt.get_auto_cor(i+1))

        pyplot.plot(lag,autocorr, "-o", label= f"offered traffic {offered_traffic}")
    
    pyplot.xlabel("lag")
    pyplot.ylabel("autocorrelation")
    pyplot.legend(loc = "upper right")
    pyplot.ylim(-1,1)


if __name__ == '__main__':
    task_4_3_1()