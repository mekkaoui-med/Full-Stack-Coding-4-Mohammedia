import random

# Use the fixed function
def get_random_temp(season):
    season = season.lower()
    match season:
        case "winter":
            temp_random = random.randint(-10, 16)
        case "spring":
            temp_random = random.randint(10, 24)
        case "summer":
            temp_random = random.randint(20, 32)
        case "autumn":
            temp_random = random.randint(15, 25)
        case _:
            temp_random = random.randint(-10, 40)
    return temp_random

# Test ranges for each season
season_ranges = {
    "winter": (-10, 16),
    "spring": (10, 24),
    "summer": (20, 32),
    "autumn": (15, 25),
}

# Run automated tests
for season, (low, high) in season_ranges.items():
    print(f"\nTesting season: {season}")
    for _ in range(10):  # test 10 random values
        temp = get_random_temp(season)
        if low <= temp <= high:
            result = "PASS"
        else:
            result = f"FAIL (got {temp})"
        print(f"Temp: {temp}, Test: {result}")

# Test invalid season
print("\nTesting invalid season input:")
for _ in range(5):
    temp = get_random_temp("rainy")
    if -10 <= temp <= 40:
        result = "PASS"
    else:
        result = f"FAIL (got {temp})"
    print(f"Temp: {temp}, Test: {result}")
