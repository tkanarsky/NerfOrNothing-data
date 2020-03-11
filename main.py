import numpy as np
import argparse
import matplotlib.pyplot as plt
import graph_constants

#Constants
FOOTBALL_RADIUS = 0.025 #from AccelHandler.h

#Parse Argments
parser = argparse.ArgumentParser()
parser.add_argument("distance", help="distance Nerf Ball was thrown, acceptable values are 4, 8, 12, 16, 20")
parser.add_argument("trial", help="trial number at that distance, range [1,5] but dependent on available datasets")
parser.add_argument("-e", "--exact", help="will not truncate decimals of output", action="store_true")
parser.add_argument("-s", "--script", help="outputs in csv format angular velocity, distance traveled and supresses creation of graph and some text output", action="store_true")
args = parser.parse_args()
path = args.distance + "m_" + args.trial + ".csv"

#Read specified CSV file
raw = np.loadtxt(path, skiprows=1, delimiter=',')

#Get graphing parameters
gp = graph_constants.graph_vals(args.distance, args.trial)
if not args.script:
    print("Graphing " + args.distance + "m Throw #" + args.trial + "...")
raw_start = gp.get_raw_start()
raw_end = gp.get_raw_end()
throw_start_idx = gp.get_throw_start_idx()
throw_end_idx = gp.get_throw_end_idx()
catch_idx = gp.get_catch_idx()

#Trims data on both ends, raw = rows of .csv that correspond to trial
raw = raw[raw_start:raw_end]

#Reads time
x_axis = raw[:, 0]
time_axis = (x_axis - x_axis[0]) / 1000.

#Sets additional graphing variables
throw_start = time_axis[throw_start_idx]
throw_end = time_axis[throw_end_idx] #.70
catch = time_axis[catch_idx] #2.1

#Radial Acceleration Readings
radial_x_raw = raw[:, 1]
radial_y_raw = raw[:, 2]
radial_z_raw = raw[:, 3]

#Axial Acceleration Readings
axial_x_raw = raw[:, 4]
axial_y_raw = raw[:, 5]
axial_z_raw = raw[:, 6]

#Calculate Magnitude of Accelerations
axial_mag = np.sqrt(np.abs(radial_x_raw**2 + radial_y_raw**2 + radial_z_raw**2))
radial_mag = np.sqrt(np.abs(axial_x_raw**2 + axial_y_raw**2 + axial_z_raw**2))

#Set max graph height
max_graph_height = np.max(axial_mag) + (np.max(axial_mag)/10)

#Graphs acceleration data
index_axis = np.linspace(0, len(time_axis), len(time_axis))
plt.scatter(time_axis, axial_mag, color="blue", label="Magnitude of Radial Acceleration")
plt.scatter(time_axis, radial_mag, color='red', label="Magnitude of Axial Acceleration")

#Marks start of throw, end of throw, and catch
plt.vlines(throw_start, 0, max_graph_height, color='green', label='Throw Start')
plt.vlines(throw_end, 0, max_graph_height, color='orange', label='Release')
plt.vlines(catch, 0, max_graph_height, color='purple', label='Catch')

#Prints (old) distance traveled (need to update)
#print(np.trapz(axial_mag[throw_start_idx:throw_end_idx], time_axis[throw_start_idx:throw_end_idx]) * (time_axis[catch_idx]-time_axis[throw_end_idx]))

#Calculate average angular velocity
linear_velocity = np.sqrt(np.abs(FOOTBALL_RADIUS * radial_mag[throw_start_idx:throw_end_idx]))
angular_velocity = linear_velocity / FOOTBALL_RADIUS
avg_angular_velocity = np.average(angular_velocity)

#Calculate distance traveled
integrated_accel = np.trapz(axial_mag[throw_start_idx:throw_end_idx] - 9.8, time_axis[throw_start_idx:throw_end_idx])
velocity = integrated_accel * np.cos(gp.get_angle())
delta_time = time_axis[catch_idx] - time_axis[throw_end_idx]
distance_traveled = velocity * delta_time

#Print data, format based on command line arguments
if args.script:
    if args.exact:
        print(str(avg_angular_velocity) + "," + str(distance_traveled))
    else:
        print("{:.3f},{:.3f}".format(avg_angular_velocity, distance_traveled))
else:
    if args.exact:
        print("Average Angular Velocity = " + str(avg_angular_velocity) + " radians/s")
        print("Distance Traveled = " + str(distance_traveled) + "m")
    else:
        print("Average Angular Velocity = {:.3f} radians/s".format(avg_angular_velocity))
        print("Distance Traveled = {:.3f} m".format(distance_traveled))


#Labels graph and adds legend
if not args.script:
    plt.title("Acceleration of " + args.distance + "m Throw")
    plt.ylabel("Acceleration (m/s^2)")
    plt.xlabel("Time (s)")
    plt.legend(loc="upper right")
    plt.show()
