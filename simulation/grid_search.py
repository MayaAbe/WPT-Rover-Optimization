import evaluate

def grid_search(evaluate_rover, distance_range=(10, 1010), charge_speed_range=(10, 100),
                capacity_range=(10, 1010), emissivity_range=(0, 1), increments=(200, 50, 200, 0.5)):
    
    min_time = float('inf')
    best_params = None
    best_initial_param = None


    for distance in range(distance_range[0], distance_range[1] + 1, increments[0]):
        for charge_speed in range(charge_speed_range[0], charge_speed_range[1] + 1, increments[1]):
            for capacity in range(capacity_range[0], capacity_range[1] + 1, increments[2]):
                for emissivity in [i/100 for i in range(int(emissivity_range[0]*100), int(emissivity_range[1]*100) + 1, int(increments[3]*100))]:
                    
                    time, _, _, flag, initial_param = evaluate_rover(distance, charge_speed, capacity, emissivity)
                    
                    if flag == 0 and time < min_time:
                        min_time = time
                        best_params = (distance, charge_speed, capacity, emissivity)
                        best_initial_param = initial_param
                        
    return best_params, best_initial_param

# For testing purpose, let's define a dummy evaluate_rover function
"""
def dummy_evaluate_rover(DISTANCE, CHARGE_SPEED, T_CAPASITY, EMISSIVITY):
    TIME = DISTANCE / CHARGE_SPEED + T_CAPASITY * EMISSIVITY
    SUPPLY_POWER = None
    N_STATION = None
    FLAG = None
    INITIAL_PARAM = (DISTANCE, CHARGE_SPEED, T_CAPASITY, EMISSIVITY)
    return TIME, SUPPLY_POWER, N_STATION, FLAG, INITIAL_PARAM
"""
    
# Testing the grid_search function with the dummy function
print(grid_search(evaluate.evaluate_rover))