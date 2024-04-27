# Johanes Andrian Kartono 03729894

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from statistics import mean
from simparam import SimParam
from simulation import Simulation

"""
This file is used to keep code that is necessary to answer the simulation study part of the exercise from Analysis Modeling and Simulation of Computer Networks part 1
"""

def task_1_7_1_1():
    """
    Execute task 1.7.1
    """

    lower_bound = 1
    upper_bound = 100
    helper_list = range(lower_bound, upper_bound)
    percentage_list = [i * 0.01 for i in helper_list] # only 0.01 to 0.99 is possible based on task description
    candidate_list = [i * 0.0015 for i in percentage_list] # obtain the arrival rate
    
    for index, candidate in enumerate(candidate_list):
        # initialize the simulation
        sim_param = SimParam(ARRIVAL_RATE=candidate)
        sim = Simulation(sim_param)

        counter = 0
        for simulation_no in range(sim_param.NUM_RUNS):
            sim.reset()
            sim.do_simulation()
            if sim.sys_state.packets_dropped < 5:
                counter += 1
        
        print(f"Utilization Rate = {percentage_list[index]} | {counter} successes out of {sim_param.NUM_RUNS} runs ")

def task_1_7_1_2(lower_bound:int, upper_bound:int):
    """
    Execute task 1.7.1
    """

    helper_list = range(lower_bound, upper_bound)
    percentage_list = [i * 0.01 for i in helper_list] # only 0.01 to 0.99 is possible based on task description
    candidate_list = [i * 0.0015 for i in percentage_list] # obtain the arrival rate
    
    for index, candidate in enumerate(candidate_list):
        # initialize the simulation
        sim_param = SimParam(ARRIVAL_RATE=candidate)
        sim = Simulation(sim_param)

        success_count = []
        for repeat_simulation in range(10):
            counter = 0
            for simulation_no in range(sim_param.NUM_RUNS):
                sim.reset()
                sim.do_simulation()
                if sim.sys_state.packets_dropped < 5:
                    counter += 1
            success_count.append(counter)
        
        print(f"Utilization Rate = {percentage_list[index]} | {mean(success_count)} successes out of {sim_param.NUM_RUNS} runs ")

def task_1_7_2_1():
    """
    Execute task 1.7.2
    """

    lower_bound = 1
    upper_bound = 100
    helper_list = range(lower_bound, upper_bound)
    percentage_list = [i * 0.01 for i in helper_list] # only 0.01 to 0.99 is possible based on task description
    candidate_list = [i * 0.015 for i in percentage_list] # obtain the arrival rate
    
    for index, candidate in enumerate(candidate_list):
        # initialize the simulation
        sim_param = SimParam(ARRIVAL_RATE=candidate, SERVICE_RATE=0.015)
        sim = Simulation(sim_param)

        counter = 0
        for simulation_no in range(sim_param.NUM_RUNS):
            sim.reset()
            sim.do_simulation()
            if sim.sys_state.packets_dropped < 50:
                counter += 1
        
        print(f"Utilization Rate = {percentage_list[index]} | {counter} successes out of {sim_param.NUM_RUNS} runs ")

def task_1_7_2_2(lower_bound:int, upper_bound:int):
    """
    Execute task 1.7.2
    """

    helper_list = range(lower_bound, upper_bound)
    percentage_list = [i * 0.01 for i in helper_list] # only 0.01 to 0.99 is possible based on task description
    candidate_list = [i * 0.015 for i in percentage_list] # obtain the arrival rate
    
    for index, candidate in enumerate(candidate_list):
        # initialize the simulation
        sim_param = SimParam(ARRIVAL_RATE=candidate, SERVICE_RATE=0.015)
        sim = Simulation(sim_param)

        success_count = []
        for repeat_simulation in range(10):
            counter = 0
            for simulation_no in range(sim_param.NUM_RUNS):
                sim.reset()
                sim.do_simulation()
                if sim.sys_state.packets_dropped < 50:
                    counter += 1
            success_count.append(counter)
        
        print(f"Utilization Rate = {percentage_list[index]} | {mean(success_count)} successes out of {sim_param.NUM_RUNS} runs ")

def task_1_7_3():
    service_rate_1 = 0.0015
    service_rate_2 = 0.015
    # unsure if arrival rate should be set the same or different between runs
    arrival_rate_1 = 0.87 * service_rate_1
    arrival_rate_2 = 0.95 * service_rate_2
    
    NO_OF_SIMULATION = 500

    sim_s1_a1 = []
    sim_s2_a2 = []

    # do simulation 1 with parameter service rate 1 and arrival rate 1
    sim_param = SimParam(SERVICE_RATE=service_rate_1, ARRIVAL_RATE=arrival_rate_1)
    sim = Simulation(sim_param)
    for i in range(NO_OF_SIMULATION):
        sim.reset()
        sim.do_simulation()
        p_b = sim.sys_state.get_blocking_probability()
        sim_s1_a1.append(p_b)

    # do simulation 2 with parameter service rate 2 and arrival rate 2
    sim_param = SimParam(SERVICE_RATE=service_rate_2, ARRIVAL_RATE=arrival_rate_2)
    sim = Simulation(sim_param)
    for i in range(NO_OF_SIMULATION):
        sim.reset()
        sim.do_simulation()
        p_b = sim.sys_state.get_blocking_probability()
        sim_s2_a2.append(p_b)

    x1 = np.sort(sim_s1_a1)
    x2 = np.sort(sim_s2_a2)
    y = np.linspace(0,1,num= NO_OF_SIMULATION)

    plt.xlabel('Blocking probability') 
    plt.ylabel('CDF') 
    
    plt.title('CDF of blocking probability') 
    plt.plot(x1, y, label="87% utilization and 0.0015") 
    plt.plot(x2, y, label="95% utilization and 0.015")
    plt.legend(loc="lower right")

    plt.show() 
        
if __name__ == '__main__':
    task_1_7_3()