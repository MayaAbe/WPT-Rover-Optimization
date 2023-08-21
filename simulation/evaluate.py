import thermal

# ---<Thermal Paramaters>-----------------------
TIME = 10
EMISSIVITY = 0.65
T_CAPASITY = 1000

# ---<Battery Paramaters>-----------------------
GOAL_DISTINATION = 10e3  # [m]
DISTANCE = 100  # [m]
ROVER_SPEED = 0.2  # [m/s]
CONSUMPTION = 30  # [W]
CHARGE_SPEED = 20  # [W] 後で変える
B_CAPASITY = 40.54 * 3600  # [As(3600Ah)]
VOLTAGE = 12  # [V]

# ----------------------------------------------

INTERVAL = DISTANCE / ROVER_SPEED # delta[m]
CURRENT = CONSUMPTION / VOLTAGE  # [A]
B_DECREACE = INTERVAL * CURRENT # [As(3600Ah)]

# ----------------------------------------------

t = thermal.thermal_transit(INTERVAL, EMISSIVITY, T_CAPASITY, CONSUMPTION)

TEMPARETURE = t[0]
HEATING_CONSUMPTION = t[1] # [W]



# print(f"{t[0]}, {t[1]}")
