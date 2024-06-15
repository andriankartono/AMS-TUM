from counter import TimeIndependentCounter
from simulation import Simulation
from matplotlib import pyplot

def task_5_2_1():
    sim = Simulation()

    # set parameters
    sim.sim_param.ARRIVAL_RATES = [1/1000]
    sim.sim_param.SERVICE_RATES = [1/900]
    sim.sim_param.S = 4

    epsilon = 0.0015

    number_of_runs = []
    for sim_time in [100000,1000000]:
        sim.sim_param.SIM_TIME = sim_time
        for confidence_level in [0.9, 0.95]:
            alpha = 1 - confidence_level
            counter = TimeIndependentCounter("Blocking Probability")
            counter.reset()
            confidence_interval_half_width = 1.0   # value to check if another run should be done
            while len(counter.values) < 5 or confidence_interval_half_width > epsilon: # len < 5 is required as the simulation can stop with only 1 run
                sim.reset()
                sim_result = sim.do_simulation()
                counter.count(sim_result.blocking_probability)
                confidence_interval_half_width = counter.report_confidence_interval(alpha, False)
            number_of_runs.append(len(counter.values))
            counter.report_confidence_interval(alpha=alpha, print_report = True)

    print(f"sim time 100s confidence_level 0.9; number of runs {number_of_runs[0]}")
    print(f"sim time 100s confidence_level 0.95; number of runs {number_of_runs[1]}")
    print(f"sim time 1000s confidence_level 0.9; number of runs {number_of_runs[2]}")
    print(f"sim time 1000s confidence_level 0.95; number of runs {number_of_runs[3]}")

def task_5_2_2():
    pass

if __name__ == "__main__":
    task_5_2_1()