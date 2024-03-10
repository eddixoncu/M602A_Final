from m602.EmissionsCalculator import EmissionsCalculator


calculator = EmissionsCalculator()
emission = calculator.calculate_energy_emissions(12,2,3, )
print(f"Energy usage emission : {emission}")

print("END")

