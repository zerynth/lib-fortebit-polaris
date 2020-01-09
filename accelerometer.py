"""
.. module:: polaris_accel

*************
Accelerometer
*************

This module provides easy access to Polaris on-board accelerometer.

    """

def Accelerometer():
    """
.. function:: Accelerometer()

    Creates an instance of the on-board accelerometer device class (:any:`stm.lis2hh12.LIS2HH12`).
    
    :returns: ``LIS2HH12`` object configured for Polaris hardware
    """
    from stm.lis2hh12 import lis2hh12
    return lis2hh12.LIS2HH12(SPI1, D60)

