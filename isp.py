import numpy as np
import matplotlib.pyplot as plt
import math

heights = np.linspace(0, 28000, 1000)
atms = np.linspace(100000, 0, 1000)

standard_gravity_value = 9.80665
mass_flow_rate_value = 197
exit_velocity_value = 2200
standard_atmospheric_pressure_value = 101325
exit_pressure_value = standard_atmospheric_pressure_value * 1.5
nozzle_area_value = 0.9

L = 0.00976
Cp = 1004.685
T0 = 288.16
M = 0.0289697
R0 = 8.31446

def ambient_air_pressure(height, atmospheric_value):
    return atmospheric_value * (1 - standard_gravity_value * height / (Cp * T0)) ** (Cp * M / R0)


def engine_thrust(mass_flow_rate, exit_velocity, exit_pressure, nozzle_area, height, atmospheric_value):
    return mass_flow_rate * exit_velocity + (exit_pressure - ambient_air_pressure(height, atmospheric_value)) * nozzle_area


def specific_impulse(standard_gravity, mass_flow_rate, exit_velocity, exit_pressure, nozzle_area, height, atmospheric_value):
    return engine_thrust(mass_flow_rate, exit_velocity, exit_pressure, nozzle_area, height,atmospheric_value) / (
                standard_gravity * mass_flow_rate)


def specific_impulse_merlin(height, atmospheric_value, mass):
    return specific_impulse(standard_gravity_value, mass, exit_velocity_value, exit_pressure_value,
                            nozzle_area_value, height, atmospheric_value)

values = []

for i in range(len(atms)):
  values.append(specific_impulse_merlin(heights[i], atms[i]*1.5, mass_flow_rate_value))


h1 = 0
h2 = 28000

print("Impulse in", h1, "meters:", specific_impulse_merlin(h1, standard_atmospheric_pressure_value*1.5, mass_flow_rate_value))
print("Impulse in", h2, "meters:", specific_impulse_merlin(h2, 0, mass_flow_rate_value))

fig, ax = plt.subplots()
line, = ax.plot(heights, values)
ax.set_xlabel('Height [m]')
ax.set_ylabel('Specific Impulse [s]')

plt.show()