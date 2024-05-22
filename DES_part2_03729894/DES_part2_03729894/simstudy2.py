import plothelpers

from matplotlib import pyplot
from simulation import Simulation
from simparam import SimParam

def task2_7_1(queue_lengths:list = [5]):
    # initialize simulation parameters
    simparam = SimParam()
    simparam.SIM_TIME = 100000

    # create box plot instance
    boxplot_waiting_time = plothelpers.BoxPlot("waiting time")
    boxplot_queue_length = plothelpers.BoxPlot("queue length")

    # create a simulation object
    sim = Simulation(simparam)

    # run the simulation 1000 times
    for queue_length in queue_lengths:
        # modify the queue length parameter
        # finite queue will be recreated when the reset command is run
        simparam.S = queue_length
        buffer_list_wt = []
        buffer_list_ql = []
        for _ in range(1000):
            sim.reset()
            sim.do_simulation()
            buffer_list_wt.append(sim.statistics_collection.mean_waiting_time)
            buffer_list_ql.append(sim.statistics_collection.mean_queue_length)
        
        boxplot_waiting_time.add_counter_data(buffer_list_wt)
        boxplot_queue_length.add_counter_data(buffer_list_ql)
    
    boxplot_waiting_time.plot(labels=queue_lengths)
    boxplot_queue_length.plot(labels=queue_lengths)

def task2_7_2(queue_lengths:list = [5]):
    # initialize simulation parameters
    simparam = SimParam()
    simparam.SIM_TIME = 1000000

    # create box plot instance
    boxplot_waiting_time = plothelpers.BoxPlot("waiting time")
    boxplot_queue_length = plothelpers.BoxPlot("queue length")

    # create a simulation object
    sim = Simulation(simparam)

    # run the simulation 1000 times
    for queue_length in queue_lengths:
        # modify the queue length parameter
        # finite queue will be recreated when the reset command is run
        simparam.S = queue_length
        buffer_list_wt = []
        buffer_list_ql = []
        for _ in range(1000):
            sim.reset()
            sim.do_simulation()
            buffer_list_wt.append(sim.statistics_collection.mean_waiting_time)
            buffer_list_ql.append(sim.statistics_collection.mean_queue_length)
        
        boxplot_waiting_time.add_counter_data(buffer_list_wt)
        boxplot_queue_length.add_counter_data(buffer_list_ql)
    
    boxplot_waiting_time.plot(labels=queue_lengths)
    boxplot_queue_length.plot(labels=queue_lengths)

def task2_7_3_1(queue_lengths:list = [5]):
    # initialize simulation parameters
    simparam = SimParam()
    simparam.SIM_TIME = 100000
    simparam.NUM_SERVERS=2
    simparam.SERVICE_RATES= [0.00075, 0.00075]

    # create box plot instance
    boxplot_waiting_time = plothelpers.BoxPlot("waiting time")
    boxplot_queue_length = plothelpers.BoxPlot("queue length")

    # create a simulation object
    sim = Simulation(simparam)

    # run the simulation 1000 times
    for queue_length in queue_lengths:
        # modify the queue length parameter
        # finite queue will be recreated when the reset command is run
        simparam.S = queue_length
        buffer_list_wt = []
        buffer_list_ql = []
        for _ in range(1000):
            sim.reset()
            sim.do_simulation()
            buffer_list_wt.append(sim.statistics_collection.mean_waiting_time)
            buffer_list_ql.append(sim.statistics_collection.mean_queue_length)
        
        boxplot_waiting_time.add_counter_data(buffer_list_wt)
        boxplot_queue_length.add_counter_data(buffer_list_ql)
    
    boxplot_waiting_time.plot(labels=queue_lengths)
    boxplot_queue_length.plot(labels=queue_lengths)

def task2_7_3_2(queue_lengths:list = [5]):
    # initialize simulation parameters
    simparam = SimParam()
    simparam.SIM_TIME = 1000000
    simparam.NUM_SERVERS=2
    simparam.SERVICE_RATES= [0.00075, 0.00075]

    # create box plot instance
    boxplot_waiting_time = plothelpers.BoxPlot("waiting time")
    boxplot_queue_length = plothelpers.BoxPlot("queue length")

    # create a simulation object
    sim = Simulation(simparam)

    # run the simulation 1000 times
    for queue_length in queue_lengths:
        # modify the queue length parameter
        # finite queue will be recreated when the reset command is run
        simparam.S = queue_length
        buffer_list_wt = []
        buffer_list_ql = []
        for _ in range(1000):
            sim.reset()
            sim.do_simulation()
            buffer_list_wt.append(sim.statistics_collection.mean_waiting_time)
            buffer_list_ql.append(sim.statistics_collection.mean_queue_length)
        
        boxplot_waiting_time.add_counter_data(buffer_list_wt)
        boxplot_queue_length.add_counter_data(buffer_list_ql)
    
    boxplot_waiting_time.plot(labels=queue_lengths)
    boxplot_queue_length.plot(labels=queue_lengths)