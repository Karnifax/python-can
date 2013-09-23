import logging
logging.getLogger(__file__)

import can

logging.debug("RC: {}".format(can.rc))

if can.rc['interface'] == 'kvaser':
    from can.interfaces.kvaser import *
elif can.rc['interface'] == 'socketcan_ctypes':
    from can.interfaces.socketcan_ctypes import *
elif can.rc['interface'] == 'socketcan_native':
    from can.interfaces.socketcan_native import *
elif can.rc['interface'] == 'socketcan':
    # try both
    try:
        from can.interfaces.socketcan_native import *
    except ImportError:
        from can.interfaces.socketcan_ctypes import *
elif can.rc['interface'] == 'serial':
    from can.interfaces.serial_can import *
else:
    raise ImportError("CAN interface not found")
    