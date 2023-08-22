import thermal


def evaluate_rover(DISTANCE = 1000, CHARGE_SPEED = 20, T_CAPASITY = 1000, EMISSIVITY = 0.65  ):
    FLAG = 0  # これが1になれば強制アウト
    TIME = 0  # [s]
    SUPPLY_POWER = 0  # [As(3600Ah)]
    INITIAL_PARAM = [DISTANCE, CHARGE_SPEED, T_CAPASITY, EMISSIVITY]

    # ---<Thermal Paramaters>-----------------------
    #EMISSIVITY = 0.65  # [-]
    #T_CAPASITY = 1000  # [J/K kg]
    T_ROVER = 300  # [K]
    MASS_ROVER = 10  # [kg]

    # ---<Battery Paramaters>-----------------------
    GOAL_DISTINATION = 10e3  # [m]
    #DISTANCE = 1000  # [m]
    ROVER_SPEED = 0.2  # [m/s]
    CONSUMPTION = 30  # [W]
    #CHARGE_SPEED = 20  # [W] 後で変える
    B_CAPASITY = 40.54 * 3600  # [As(3600Ah)]
    VOLTAGE = 12  # [V]

    # ---<Magnetic Resonse>--------------------------

    EFF = 0.7  # 後で別な関数

    # -----------------------------------------------

    B_CAPASITY_AIM = 0.8 * B_CAPASITY  # [As(3600Ah)]
    INTERVAL = DISTANCE / ROVER_SPEED  # delta[m]
    CURRENT = CONSUMPTION / VOLTAGE  # [A]
    B_DECREACE = INTERVAL * CURRENT  # [As(3600Ah)]

    # -----------------------------------------------

    N_STATION = GOAL_DISTINATION / DISTANCE
    TIME += N_STATION * INTERVAL
    count = 0
    #print("回数" + str(N_STATION))
    #print(str(B_CAPASITY_AIM / 3600))

    while GOAL_DISTINATION >= 0:
        t = thermal.thermal_transit(INTERVAL, EMISSIVITY, T_CAPASITY, CONSUMPTION, T_ROVER)

        T_DECREACED = t[0]  # delta[K]
        HEATING_CONSUMPTION = -((t[1] * T_CAPASITY) / VOLTAGE)  # delta[As(3600Ah)]

        # バッテリーと温度の減少量
        B_CAPASITY -= B_DECREACE + HEATING_CONSUMPTION  # [As(3600Ah)]
        if T_DECREACED < 0:
            T_ROVER = 273
        else:
            T_ROVER = T_DECREACED + 273

        if B_CAPASITY < 0:
            FLAG = 1
            #print("battely_runout")
            break

        # 給電時間の計算
        if B_CAPASITY < B_CAPASITY_AIM:
            B_diff = B_CAPASITY_AIM - B_CAPASITY  # [As(3600Ah)]
            B_charge_time = B_diff / CHARGE_SPEED  # [s]

            # 充電時間の加算
            TIME += B_charge_time

            # 給電電力の加算
            SUPPLY_POWER += B_CAPASITY_AIM - B_CAPASITY

            # 給電中のバッテリーとローバー温度の上昇
            B_CAPASITY = B_CAPASITY_AIM
            T_ROVER += B_charge_time * CHARGE_SPEED * (1 - EFF) * MASS_ROVER / T_CAPASITY

            if T_ROVER >= 313:
                FLAG = 1

        GOAL_DISTINATION -= DISTANCE
        """count += 1
        if count < 50:
            print(count)
            B_CAP = B_CAPASITY / 3600
            print(B_CAP)"""

    B_CAPASITY /= 3600  # [Ah]
    T_ROVER  # [K]

    TIME /= 3600  # [h]
    SUPPLY_POWER /= 3600  # [Ah]

    return TIME, SUPPLY_POWER, N_STATION, FLAG, INITIAL_PARAM

print(evaluate_rover())