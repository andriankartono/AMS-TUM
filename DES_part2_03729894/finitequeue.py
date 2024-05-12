from queue import PriorityQueue
from packet import Packet
import queue


class FiniteQueue(object):
    """
    Class representing a finite queue with the system buffer.

    It is a priority queue with finite capacity. Methods contain adding and removing packets
    as well as checking the current number of packets in the buffer. Clearing the queue is implemented with the method flush.
    """

    def __init__(self, max_size: int):
        """
        Initialize the finite queue
        :param max_size: buffer spaces in queue
        :return: FiniteQueue object
        """
        #######################################
        # TODO Task 2.2.1: Your code goes here
        self.finitequeue = PriorityQueue(maxsize=max_size)
        #######################################

    def add(self, packet: Packet):
        """
        Try to add a packet to the queue
        :param packet: packet which is supposed to be queued
        :return: true if packet has been enqueued, false if rejected
        """
        #######################################
        # TODO Task 2.2.1: Your code goes here
        try:
            self.finitequeue.put(packet, False)
            return True
        except queue.Full:
            return False

        #######################################

    def remove(self):
        """
        Pull the smallest packet from buffer and return it
        :return: the smallest packet
        """
        #######################################
        # TODO Task 2.2.1: Your code goes here
        # It is possible to use 
        try:
            return self.finitequeue.get(False)
        except queue.Empty:
            return None
        #######################################

    def get_queue_length(self):
        """
        :return: current number of packets in the queue
        """
        #######################################
        # TODO Task 2.2.1: Your code goes here
        return self.finitequeue.qsize()
        #######################################

    def is_empty(self):
        """
        :return: true if queue is empty
        """
        #######################################
        # TODO Task 2.2.1: Your code goes here
        return self.finitequeue.empty()
        #######################################

    def flush(self):
        """
        erase all packets from the buffer
        """
        #######################################
        # TODO Task 2.2.1: Your code goes here
        self.finitequeue.queue.clear()
        #######################################