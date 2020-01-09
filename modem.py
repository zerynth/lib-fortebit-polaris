"""
.. module:: polaris_modem

*****
Modem
*****

This module provides uniform access to Polaris on-board modem, which may vary on different board variants.

.. function:: init()

    Initializes the correct Modem library for the current Polaris target board variant and
    returns the module object.
    
    :returns: :any:`quectel.m95.M95` for *Polaris 2G*, :any:`quectel.ug96.UG96` for *Polaris 3G*, :any:`quectel.bg96.BG96` for *Polaris NB-IoT*

    """
_initialized = False
_PIN_NC = -1

#-if TARGET == polaris_3g
from quectel.ug96 import ug96
def init():
    global _initialized
    if not _initialized:
        ug96.init(SERIAL3, _PIN_NC, _PIN_NC, D67, D38, D37, power_on=HIGH, kill_on=HIGH, status_on=LOW)
    _initialized = True
    return ug96
#-else 
##-if TARGET == polaris_2g
from quectel.m95 import m95
def init():
    global _initialized
    if not _initialized:
        m95.init(SERIAL3, _PIN_NC, _PIN_NC, D67, D38, D37, power_on=HIGH, kill_on=HIGH, status_on=LOW)
    _initialized = True
    return m95
##-else
###-if TARGET == polaris_nbiot
from quectel.bg96 import bg96
def init():
    global _initialized
    if not _initialized:
        bg96.init(SERIAL3, _PIN_NC, _PIN_NC, D67, D38, D37, power_on=HIGH, reset_on=HIGH, status_on=LOW)
    _initialized = True
    return bg96
###-else
raise UnsupportedError
###-endif
##-endif
#-endif

