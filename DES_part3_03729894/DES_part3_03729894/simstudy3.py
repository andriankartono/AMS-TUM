from statisticscollection import StatCollection
from simulation import Simulation
from simparam import SimParam, ARR_PROCESS
from matplotlib import pyplot
from plothelpers import HistType
from statisticstest import ChiSquare, TestDist

import plothelpers
import statistics
import numpy as np

def task_3_5_1():
    simparam = SimParam()

    simparam.USERS_ARRIVAL_PROCESS = ARR_PROCESS.UNIFORM
    simparam.SIM_TIME = 10000000
    sim = Simulation(simparam)

    user_number = [1,2,5,10,20,50]

    hist = plothelpers.Histogram()
    for user in user_number:
        simparam.NUM_USERS = user
        simparam.ARRIVAL_RATES = [0.0015/user] * user
        simparam.USERS_SEEDS = [None] * user

        # reset everything
        sim.reset()
        hist.reset()

        sim.do_simulation()

        iat_values = sim.statistics_collection.cnt_iat.values
        hist.add_counter_data(iat_values)
        hist.plot(diag_type=HistType.LINE, n_bins=100, labels=f'{user} user')
        emp_n, emp_x = np.histogram(iat_values, bins = 100, range = (0,4000))

        # check the chi distribution
        if user == 50:
            chi = ChiSquare(emp_x, emp_n, TestDist.EXPONENTIAL)
            chi2_1, chicritical_1 = chi.test_distribution(0.05, statistics.mean(iat_values), 1, np.var(iat_values))
            chi2_2, chicritical_2 = chi.test_distribution(0.05, statistics.mean(iat_values), 1, np.var(iat_values))
            print(f"Zero hypothesis is {chi2_1<chicritical_1} for significance of 0.05")
            print(f"Zero hypothesis is {chi2_2<chicritical_2} for significance of 0.15")


    pyplot.xlim(0,4000) # manually set limit as values above this point is unnecessary
    pyplot.legend()
    pyplot.show()

def task_3_5_2(server_num:int = 1, display_busy_server: bool = True):
    simparam = SimParam()

    simparam.USERS_ARRIVAL_PROCESS = ARR_PROCESS.EXPONENTIAL
    simparam.SIM_TIME = 100000
    sim = Simulation(simparam)

    user_number = [2,4,6]

    # for server in server_number:
    server = server_num
    simparam.NUM_SERVERS = server
    simparam.SERVICE_RATES = [0.0015] * server
    simparam.SERVERS_SEEDS = [None] * server

    # two boxplots for each server
    box_arrival_rate = plothelpers.BoxPlot()
    box_average_busy_server = plothelpers.BoxPlot()

    for user in user_number:
        simparam.NUM_USERS = user
        simparam.ARRIVAL_RATES = [0.001] * user
        simparam.USERS_SEEDS = [None] * user
        
        buffer_list_average_arrival_rate = []
        buffer_list_busy_server = []
        # run the simulation 1000 times
        for i in range(1000):
            # reset the simulation
            sim.reset()
            sim.do_simulation()
            buffer_list_busy_server.append(sim.statistics_collection.mean_number_busy_servers)
            buffer_list_average_arrival_rate.append(sim.statistics_collection.cnt_iat.get_mean())
        
        box_arrival_rate.add_counter_data(buffer_list_average_arrival_rate)
        box_average_busy_server.add_counter_data(buffer_list_busy_server)
    
    if display_busy_server:
        box_average_busy_server.plot(labels=user_number)
        pyplot.title(f"{server} servers average busy server")
    else:
        box_arrival_rate.plot(labels= user_number)
        pyplot.title(f"{server} servers average interarrival time (1/arrival rate)")

    pyplot.show()


    
if __name__ == '__main__':
    task_3_5_1()

