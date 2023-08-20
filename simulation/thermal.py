import time
from math import log, atan, sqrt 
from matplotlib import pyplot as plt

def thermal_transit(
        passed_time=10, #経過時間
        emissivity_rover=0.655, #ローバー放射率
        C=1000,  #ローバー熱容量
        T_initial=300,  #ローバー初期温度
        T_env=100,  #周囲の環境温度
        Q_in=100,  #内部発熱
        threshold=0.001, #定常状態とみなす閾値
        vertical=0.3, #ローバー高さと幅
        horizontal=0.45, #ローバー奥行
        distance=0.15, #ローバーの地面との距離
        emissivity_regolith=0.925, #レゴリスの放射率 
        S_top=0.135,  #上面の面積
        S_side=0.450,  #側面積
        S_bottom=0.135, #低面積
        
        d=0.15,  # 物質の厚み (m)
        k=130,  # 熱伝導率 (W/mK)
        A=0.000256  # 温度の伝導面積 (m^2)
):
    sigma = 5.67 * 10**-8  
    
    T = T_initial
    time = 0
    dt = 0.001  

    x = vertical / distance
    y = horizontal / distance

    F_ij = log(((1+x**2)*(1+y**2))/(1+x**2+y**2)) + \
           x**2*log((x**2 * (1+x**2+y**2))/((1+x**2)*(x**2+y**2))) + \
           y**2*log((y**2 * (1+x**2+y**2))/((1+y**2)*(x**2+y**2))) + \
           4*x*atan(1/x) + 4*y*atan(1/y) - 4*sqrt(x**2+y**2)*atan(1/sqrt(x**2+y**2))

    R1 = emissivity_rover * S_top
    R2 = emissivity_rover * emissivity_regolith * S_side
    R3 = emissivity_rover * emissivity_regolith * S_bottom * F_ij

    times = [time]
    temperatures = [T]

    while time <= passed_time:
        Q_radiation = (R1+R2+R3) * sigma * (T**4 - T_env**4)
        Q_conduction = k * A * (T - T_env) / d
        
        Q_out = Q_radiation + Q_conduction
        
        dT = (Q_in - Q_out) * dt / C
        T += dT
        time += dt
        times.append(time)
        temperatures.append(T)

    plt.figure(figsize=(10, 6))
    plt.plot(times, temperatures)
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (K)')
    plt.title('Temperature of the object over time with conduction')
    plt.grid(True)
    plt.show()

    return T-273

# テスト関数の実行
thermal_transit()
