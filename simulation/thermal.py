import time
from math import log, atan, sqrt 
from matplotlib import pyplot as plt

start_time = time.time()

def thermal_transit(
        passed_time=1000,
        emissivity_rover=0.655,
        C=1000,
        T_initial=300,  
        T_env=100,    
        Q_in=100,  
        threshold=0.001,    
        vertical=0.3,  
        horizontal=0.45,  
        distance=0.15,  
        emissivity_regolith=0.925,  
        S_top=0.135,  
        S_side=0.450,  
        S_bottom=0.135,
        d=0.15,
        k=130,
        A=0.000256):

    sigma = 5.67 * 10**-8  
    
    T = T_initial
    time = 0
    dt = 1  

    x = vertical / distance
    y = horizontal / distance

    F_ij = log(((1+x**2)*(1+y**2))/(1+x**2+y**2)) +            x**2*log((x**2 * (1+x**2+y**2))/((1+x**2)*(x**2+y**2))) +            y**2*log((y**2 * (1+x**2+y**2))/((1+y**2)*(x**2+y**2))) +            4*x*atan(1/x) + 4*y*atan(1/y) - 4*sqrt(x**2+y**2)*atan(1/sqrt(x**2+y**2))

    R1 = emissivity_rover * S_top
    R2 = emissivity_rover * emissivity_regolith * S_side
    R3 = emissivity_rover * emissivity_regolith * S_bottom * F_ij

    time_below_273 = 0
    dT_when_below_273 = 0

    while time <= passed_time:
        Q_radiation = (R1+R2+R3) * sigma * (T**4 - T_env**4)
        Q_conduction = k * A * (T - T_env) / d
        
        Q_out = Q_radiation + Q_conduction
        
        dT = (Q_in - Q_out) * dt / C
        T += dT
        time += dt

        if T < 273 and time_below_273 == 0:
            time_below_273 = passed_time - time
            dT_when_below_273 = dT/dt

    return T-273, time_below_273, dT_when_below_273

    """
    plt.figure(figsize=(10, 6))
    plt.plot(times, temperatures)
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (K)')
    plt.title('Temperature of the object over time with conduction')
    plt.grid(True)
    plt.show()

    return T-273

# テスト関数の実行
print(thermal_transit())
end_time = time.time()
elapsed_time = end_time - start_time
print(f"実行時間: {elapsed_time} 秒")"""
