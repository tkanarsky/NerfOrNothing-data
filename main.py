import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter


path = "data/20meters/124705.csv"

raw = np.loadtxt(path, skiprows=1, delimiter=',')

raw = raw[200:320]
throw_start = 0.5
throw_end = .70
catch = 2.1

throw_start_idx = 28
throw_end_idx = 38
catch_idx = 108

# raw = raw[400:500, :]
x_axis = raw[:, 0]
time_axis = (x_axis - x_axis[0]) / 1000.

radial_x_raw = raw[:, 1]
# radial_x_raw = savgol_filter(radial_x_raw, 21, 3)
radial_y_raw = raw[:, 2]
# radial_y_raw = savgol_filter(radial_y_raw, 21, 3)
radial_z_raw = raw[:, 3]
# radial_z_raw = savgol_filter(radial_z_raw, 21, 3)


axial_x_raw = raw[:, 4]
# axial_x_raw = savgol_filter(axial_x_raw, 21, 3)
axial_y_raw = raw[:, 5]
# axial_y_raw = savgol_filter(axial_y_raw, 21, 3)
axial_z_raw = raw[:, 6]
# axial_z_raw = savgol_filter(axial_z_raw, 21, 3)

axial_mag = np.sqrt(np.abs(radial_x_raw**2 + radial_y_raw**2 + radial_z_raw**2 - (9.8*np.cos(np.pi/4))**2))
radial_mag = np.sqrt(np.abs(axial_x_raw**2 + axial_y_raw**2 + axial_z_raw**2 - (9.8*np.cos(np.pi/4))**2))

# axial_mag -= 9.81
# radial_mag -= 9.81*np.cos(np.pi/4)

print(np.trapz(axial_mag[throw_start_idx:throw_end_idx], time_axis[throw_start_idx:throw_end_idx]) * (time_axis[catch_idx]-time_axis[throw_end_idx]))

index_axis = np.linspace(0, len(time_axis), len(time_axis))
plt.scatter(time_axis, axial_mag, color="blue", label="Radial Accelerometer")
plt.scatter(time_axis, radial_mag, color='red', label="Axial Accelerometer")

# plt.scatter(time_axis, axial_z_raw, color='green')
plt.vlines(throw_start, 0, 200, color='green', label='Throw Start')
plt.vlines(throw_end, 0, 200, color='orange', label='Release')
plt.vlines(catch, 0, 200, color='purple', label='Catch')
plt.ylabel("Acceleration (m/s^2)")
plt.xlabel("Time (s)")
plt.legend(loc="upper right")
plt.show()
