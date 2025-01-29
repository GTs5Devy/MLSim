import ac
import acsys
from third_party.sim_info import SimInfo 

# Set app name
appName = "Lap Time Optimizer"
width, height = 300, 150  # App window size

# Initialize SimInfo for telemetry
simInfo = SimInfo()

# Define labels globally
speed_label = None
gear_label = None
lap_time_label = None

def acMain(ac_version):
    global appWindow, speed_label, gear_label, lap_time_label 

    # Create App Window
    appWindow = ac.newApp(appName)
    ac.setTitle(appWindow, appName)
    ac.setSize(appWindow, width, height)

    # Add labels to display telemetry data
    speed_label = ac.addLabel(appWindow, "Speed: 0 km/h")
    ac.setPosition(speed_label, 20, 30)

    gear_label = ac.addLabel(appWindow, "Gear: N")
    ac.setPosition(gear_label, 20, 60)

    lap_time_label = ac.addLabel(appWindow, "Lap Time: 0:00.000")
    ac.setPosition(lap_time_label, 20, 90)

    return appName

def acUpdate(deltaT):
    """
    This function updates the app window with live data from Assetto Corsa.
    """
    global speed_label, gear_label, lap_time_label 

    # Get speed (in km/h)
    speed = simInfo.physics.speedKmh
    ac.setText(speed_label, f"Speed: {int(speed)} km/h")

    # Get gear (N for neutral, 1-6 for gears, R for reverse)
    gear = simInfo.physics.gear
    gear_text = "N" if gear == 0 else "R" if gear == -1 else str(gear)
    ac.setText(gear_label, f"Gear: {gear_text}")

    # Get lap time (in milliseconds, convert to mm:ss.sss format)
    lap_time_ms = simInfo.physics.lapTime
    if lap_time_ms > 0:
        minutes = (lap_time_ms // 60000) % 60
        seconds = (lap_time_ms // 1000) % 60
        milliseconds = lap_time_ms % 1000
        ac.setText(lap_time_label, f"Lap Time: {minutes}:{seconds:02d}.{milliseconds:03d}")
    else:
        ac.setText(lap_time_label, "Lap Time: 0:00.000")
