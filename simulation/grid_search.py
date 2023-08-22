import evaluate
import time

start_time = time.time()


def grid_search(
    evaluate_rover,
    distance_range=(10, 1010),
    charge_speed_range=(10, 100),
    capacity_range=(10, 1010),
    emissivity_range=(0, 1),
    increments=(200, 50, 200, 0.5),
):
    # min_time = float('inf')
    # min_power = float('inf')
    min_number = float("inf")
    best_params = None
    best_initial_param = None

    total_iterations = (
        ((distance_range[1] - distance_range[0]) // increments[0] + 1)
        * ((charge_speed_range[1] - charge_speed_range[0]) // increments[1] + 1)
        * ((capacity_range[1] - capacity_range[0]) // increments[2] + 1)
        * (
            (int(emissivity_range[1] * 100) - int(emissivity_range[0] * 100))
            // int(increments[3] * 100)
            + 1
        )
    )

    current_iteration = 0

    for distance in range(distance_range[0], distance_range[1] + 1, increments[0]):
        for charge_speed in range(
            charge_speed_range[0], charge_speed_range[1] + 1, increments[1]
        ):
            for capacity in range(
                capacity_range[0], capacity_range[1] + 1, increments[2]
            ):
                for emissivity in [
                    i / 100
                    for i in range(
                        int(emissivity_range[0] * 100),
                        int(emissivity_range[1] * 100) + 1,
                        int(increments[3] * 100),
                    )
                ]:
                    time, power, number, flag, initial_param = evaluate_rover(
                        distance, charge_speed, capacity, emissivity
                    )

                    if flag == 0 and number < min_number:  # time/powerに書き換える
                        min_number = number  # time/powerに書き換える
                        best_params = (distance, charge_speed, capacity, emissivity)
                        best_initial_param = initial_param

                    current_iteration += 1
                    print(f"Current Iteration: {current_iteration}/{total_iterations}")
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

print(grid_search(evaluate.evaluate_rover))

end_time = time.time()
elapsed_time = end_time - start_time
print(f"実行時間: {elapsed_time} 秒")
