import thermal

FLAG = 0  # これが1になれば強制アウト

# ---<Thermal Paramaters>-----------------------
TIME = 10  # [s]
EMISSIVITY = 0.65  # [-]
T_CAPASITY = 1000  # [J/K kg]
T_ROVER = 300  # [K]
MASS_ROVER = 10  # [kg]

# ---<Battery Paramaters>-----------------------
GOAL_DISTINATION = 10e3  # [m]
DISTANCE = 100  # [m]
ROVER_SPEED = 0.2  # [m/s]
CONSUMPTION = 30  # [W]
CHARGE_SPEED = 20  # [W] 後で変える
B_CAPASITY = 40.54 * 3600  # [As(3600Ah)]
VOLTAGE = 12  # [V]

# ---<Magnetic Resonse>--------------------------

EFF = 0.7  # 後で別な関数

# -----------------------------------------------

B_CAPASITY_AIM = 0.8 * B_CAPASITY 
INTERVAL = DISTANCE / ROVER_SPEED  # delta[m]
CURRENT = CONSUMPTION / VOLTAGE  # [A]
B_DECREACE = INTERVAL * CURRENT  # [As(3600Ah)]

# -----------------------------------------------

while GOAL_DISTINATION >= 0:
    t = thermal.thermal_transit(
        INTERVAL, 
        EMISSIVITY, 
        T_CAPASITY, 
        CONSUMPTION, 
        T_ROVER 
        )

    T_DECREACE = t[0]
    HEATING_CONSUMPTION = t[1]  # [W]

    # バッテリーと温度の減少量
    B_CAPASITY -= B_DECREACE
    T_ROVER = T_DECREACE

    if B_CAPASITY < 0:
        FLAG = 1

    # 給電時間の計算
    if B_CAPASITY < B_CAPASITY_AIM:
        B_diff = B_CAPASITY_AIM - B_CAPASITY  # [As(3600Ah)]
        B_charge_time = B_diff / CHARGE_SPEED  # [s]

    # 給電中のバッテリーとローバー温度の上昇
    B_CAPASITY = B_CAPASITY_AIM
    T_ROVER += B_charge_time * CHARGE_SPEED * (1-EFF) * MASS_ROVER / T_CAPASITY

    #  print(f"{t[0]}, {t[1]}")
