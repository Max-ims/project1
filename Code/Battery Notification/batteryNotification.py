#Importing necessary modules
import time
import psutil
from plyer import notification


# returns a tuple
battery = psutil.sensors_battery()

while True:
    """
    Two conditions:
    1. Checks if battery percentage is 30 or below 30. If true, and power plug is False, notifies the user to
    plug the adapter.
    2. Checks if battery is 85 or above 85. If true, and power plug is True, notifies the user to
    unplug the adapter.
    """
    if battery.percent <= 30:
        if battery.power_plugged == True:
            pass
        else:
            notification.notify(
            title= f'Battery Low at {battery.percent}',
            message= 'Adapter is plugged',
            timeout=8
        )
    elif battery.percent >= 85:
        if battery.power_plugged == False:
            pass
        else:
            notification.notify(
            title= f'Battery High at {battery.percent}',
            message= 'Unplug the adapter',
            timeout=8
        )
    else:
        pass
    time.sleep(10)



