import time
from math import log, atan, sqrt 

start_time = time.time()

def thermal_transit(
        passed_time=1000,
        emissivity_rover=0.655,
        C=1000,
        Q_in=100,
        T_initial=300,  
        T_env=100,     
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

    F_ij = log(((1+x**2)*(1+y**2))/(1+x**2+y**2)) + \
                  x**2*log((x**2 * (1+x**2+y**2))/((1+x**2)*(x**2+y**2))) + \
                  y**2*log((y**2 * (1+x**2+y**2))/((1+y**2)*(x**2+y**2))) + \
                  4*x*atan(1/x) + 4*y*atan(1/y) - 4*sqrt(x**2+y**2)*atan(1/sqrt(x**2+y**2))

    R1 = emissivity_rover * S_top
    R2 = emissivity_rover * emissivity_regolith * S_side
    R3 = emissivity_rover * emissivity_regolith * S_bottom * F_ij

    time_below_273 = 0
    dT_when_below_273 = 0

    while time <= passed_time:
        Q_radiation = (R1+R2+R3) * sigma * (T**4 - T_env**4)
        R_leg = d / (k * A)
        R_T = 0.07
        R_tire = 0.1 / (0.22 * 0.0003)
        Q_conduction = (T - T_env) / (R_leg + R_T + R_tire)
        
        Q_out = Q_radiation + Q_conduction
        
        dT = (Q_in - Q_out) * dt / C
        T += dT
        time += dt

        if T < 273 and time_below_273 == 0:
            time_below_273 = passed_time - time
            dT_when_below_273 = dT/dt

    heating_consumption = time_below_273 * dT_when_below_273

    return T-273, heating_consumption

# 今回は使わなかったが，物質の熱容量の温度変化を考慮すれば必要
def t_change(T_initial, Q_in, time_in, T_conductance):
    dt = 0.1
    T_increace = 0
    for _ in range(int(time_in/dt)):
        delta_T = Q_in * dt / T_conductance(T)
        T_increace += delta_T
    return T_increace

def C_linear(T, C0=1000, alpha=1):
    return C0 + alpha * T

if __name__ == "__main__":
    thermal_transit()