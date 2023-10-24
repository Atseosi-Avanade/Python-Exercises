#! /usr/bin/python
# Name:   mytimer.py
# Author: DC
# Description: Functions for measuring elapsed CPU time.
"""
    This modules describes two timer functions for measuring the
    elapsed time between a task.
"""

import os

# TIMER FUNCTIONS
def start_timer():
    """ The start_timer() function marks the start of
        a timed interval, to be completed by end_timer().
    :params: No input parameters
    :return: This function returns the start_time
    """
    (utime, stime) = os.times()[:2]
    start_time = utime + stime
    return start_time

def end_timer(start_time, txt='End time'):
    """ The end_timer() function completes a timed interval
        started by start_timer.  It prints an optional text
        message (default 'End time') followed by the CPU time
        used in seconds.
        This function has one optional parameter, the text to
        be displayed.
    """
    (utime, stime) = os.times()[:2]
    end_time = utime + stime
    print(f"{txt:<12}: {end_time-start_time:01.3f} seconds")
    return None

