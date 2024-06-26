# Johanes Andrian Kartono 03729894

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from simulation import Simulation

from event import ServiceCompletion


class Server(object):
    """
    This class represents the server.

    It contains information about service rate and whether the server is busy.
    """

    def __init__(self, sim: Simulation, service_rate: float):
        """
        Create a server object
        :param service_rate: parameter for the service rate - how many packets are served in millisecond
        (rate[pkt/ms] = 1 / mean_service_time[ms])
        :param sim: Simulation object the server belongs to
        """
        #######################################
        # TODO Task 1.1.2: Your code goes here
        self.sim = sim
        self.service_rate = service_rate

        # At the beginning the server should be considered as free
        self.server_busy = False

        #######################################

    def reset(self, service_rate: float):
        """
        reset Server object
        """
        #######################################
        # TODO Task 1.1.2: Your code goes here
        self.server_busy = False
        self.service_rate = service_rate
        #######################################

    def start_service(self, pkt_arrived: bool = False):
        """
        Start service by the server.
        :param pkt_arrived: if true, a new packet arrived to the empty system and should be served directly;
        if false, the packet from buffer should be served if the buffer is not empty
        :return: True if server starts the service, false if server was busy or there is no packet to serve
        """
        #######################################
        # TODO Task 1.1.3: Your code goes here
        
        if not self.server_busy:
            if pkt_arrived:
                self.server_busy = True
                self.generate_service_completion()
                return True
            else:
                if self.sim.sys_state.buffer_content > 0:
                    self.server_busy = True
                    self.sim.sys_state.buffer_content = self.sim.sys_state.buffer_content - 1
                    self.generate_service_completion()
                    return True
                else:
                    return False
        else:
            return False

        #######################################

    def complete_service(self):
        """
        Reset server status to idle after a service completion.
        """
        #######################################
        # TODO Task 1.1.4: Your code goes here
        self.server_busy = False
        #######################################

    def generate_service_completion(self):
        """
        Generate next service completion event and insert it to event chain
        """
        #######################################
        # TODO Task 1.3.3: Your code goes here
        service_completion = ServiceCompletion(self.sim, self.sim.sys_state.now + (1/self.service_rate), self)
        self.sim.event_chain.insert(service_completion)
        #######################################
