"""
.. module:: polaris_qspiflash

**********
QSPI Flash
**********

This module provides easy access to Polaris on-board serial Flash memory.

    """

def QSpiFlash():
    """
.. function:: QSpiFlash()

    Creates an instance of the Quad-SPI Flash device class.
    
    :returns: :any:`stdlib.QSpiFlash` object configured for Polaris hardware
    """
    import qspiflash
    return qspiflash.QSpiFlash(D34,D33,D25,D24,D74,D75,0x100000,0x10000,0x8000,0x1000,0x100,8,4,4,2,4,0xA5,0x00,0x01,0x02,0x7C,0x80,0x02,0x80)
