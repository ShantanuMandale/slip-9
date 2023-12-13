def water_jug_problem(capacity_jug1, capacity_jug2, target):
    jug1 = 0
    jug2 = 0

    while jug2 != target:
        if jug2 == 0:
            jug2 = capacity_jug2
            print(f"Fill the {capacity_jug2}-gallon jug")

        pour = min(jug2, capacity_jug1 - jug1)
        jug2 -= pour
        jug1 += pour
        print(f"Pour {pour} gallons from {capacity_jug2}-gallon jug to {capacity_jug1}-gallon jug")

        if jug2 == target:
            break

        if jug1 == capacity_jug1:
            jug1 = 0
            print(f"Empty the {capacity_jug1}-gallon jug")

        pour = min(jug2, capacity_jug1 - jug1)
        jug2 -= pour
        jug1 += pour
        print(f"Pour {pour} gallons from {capacity_jug2}-gallon jug to {capacity_jug1}-gallon jug")

    print("\nTarget achieved! Final state:")
    print(f"{capacity_jug1}-gallon jug: {jug1} gallons")
    print(f"{capacity_jug2}-gallon jug: {jug2} gallons")

if __name__ == "__main__":
    capacity_jug1 = 5
    capacity_jug2 = 7
    target = 4

    print(f"Solving the Water Jug Problem to achieve {target} gallons in the 7-gallon jug:")
water_jug_problem(capacity_jug1, capacity_jug2, target)

