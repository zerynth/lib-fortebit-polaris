"""
.. module:: polaris_ioexp

************
I/O Expander
************

This module provides easy access to Polaris on-board I/O Expander.

    """

def IOExpander():
    """
.. function:: IOExpander()

    Creates an instance of the on-board I/O Expander device class (:any:`onsemi.ncv7240.NCV7240`).
    
    :returns: ``NCV7240`` object configured for Polaris hardware
    """
    from onsemi.ncv7240 import ncv7240
    return ncv7240.NCV7240(SPI1, D76)
