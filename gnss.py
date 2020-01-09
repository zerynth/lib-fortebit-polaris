"""
.. module:: polaris_gnss

****
GNSS
****

This module provides uniform access to Polaris on-board GNSS receiver, which may vary on different board variants.

    """

def init():
    """
.. function:: GNSS()

    Creates an instance of the correct GNSS receiver class for the current Polaris target board variant.
    
    :returns: :any:`quectel.l76.L76` for *Polaris 3G* and *Polaris 2G*, :any:`quectel.bg96.BG96_GNSS` for *Polaris NB-IoT*
    """
    #-if TARGET == polaris_3g
    from quectel.l76 import l76
    l = l76.L76(SERIAL4,reset=D59,reset_on=HIGH)
    return l
    #-else
    ##-if TARGET == polaris_2g
    from quectel.l76 import l76
    l = l76.L76(SERIAL4,reset=D59,reset_on=HIGH)
    return l
    ##-else
    ###-if TARGET == polaris_nbiot
    from fortebit.polaris import modem
    modem.init()
    from quectel.bg96 import bg96gnss
    l = bg96gnss.BG96_GNSS(SERIAL4,baud=115200,antpower=D80,antpower_on=HIGH)
    return l
    ###-else
    raise UnsupportedError
    ###-endif
    ##-endif
    #-endif

