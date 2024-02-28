def calculate_expected_traffic_time(num_cars, avg_speed, distance):
    time_in_traffic = distance / max(avg_speed - (num_cars * 0.05), 1)
    return time_in_traffic

# Example usage:
num_cars = 20
avg_speed = 60
distance = 100
expected_time = calculate_expected_traffic_time(num_cars, avg_speed, distance)
print("Expected time in traffic:", expected_time)
