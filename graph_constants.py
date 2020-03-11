import numpy as np

#https://stackoverflow.com/questions/6343330/importing-a-long-list-of-constants-to-a-python-file

#Setting defaults for testing purposes
DEFAULT_RAW_START = 200
DEFAULT_RAW_END = 320
DEFAULT_THROW_START = 0.5
DEFAULT_THROW_END = .70
DEFAULT_CATCH = 2.1
DEFAULT_THROW_START_IDX = 28
DEFAULT_THROW_END_IDX = 38
DEFAULT_CATCH_IDX = 108

class graph_vals:
    def __init__(self, d, t):
        my_dist = int(d)
        my_trial = int(t)
        if my_dist == 4:
            self.ANGLE = 20 * np.pi / 180
            if my_trial == 1:
                self.R_START = 100
                self.R_END = 168
                self.T_START_IDX = 10
                self.T_END_IDX = 31
                self.C_IDX = 67
            elif my_trial == 2:
                self.R_START = 60
                self.R_END = 127
                self.T_START_IDX = 18
                self.T_END_IDX = 26
                self.C_IDX = 66
            elif my_trial == 3:
                print("WARNING bad data: shorted out - Alex throw?")
                self.R_START = 0
                self.R_END = 127
                self.T_START_IDX = 18
                self.T_END_IDX = 26
                self.C_IDX = 66
            elif my_trial == 4:
                self.R_START = 43
                self.R_END = 110
                self.T_START_IDX = 8
                self.T_END_IDX = 27
                self.C_IDX = 66
        if my_dist == 8:
            self.ANGLE = 20 * np.pi / 180
            if my_trial == 1:
                self.R_START = 71
                self.R_END = 140
                self.T_START_IDX = 8
                self.T_END_IDX = 23
                self.C_IDX = 68
            elif my_trial == 2:
                print("WARNING weird data: no spin")
                self.R_START = 100
                self.R_END = 168
                self.T_START_IDX = 10
                self.T_END_IDX = 21
                self.C_IDX = 67
            elif my_trial == 3:
                self.R_START = 55
                self.R_END = 129
                self.T_START_IDX = 9
                self.T_END_IDX = 28
                self.C_IDX = 73
            elif my_trial == 4: 
                self.R_START = 80
                self.R_END = 151
                self.T_START_IDX = 12
                self.T_END_IDX = 24
                self.C_IDX = 70
        if my_dist == 12:
            self.ANGLE = 40 * np.pi / 180
            if my_trial == 1:
                print("WARNING bad data: ball not thrown")
                self.R_START = 0
                self.R_END = 800
                self.T_START_IDX = 23
                self.T_END_IDX = 36
                self.C_IDX = 68
            elif my_trial == 2:
                self.R_START = 75
                self.R_END = 140
                self.T_START_IDX = 10
                self.T_END_IDX = 24
                self.C_IDX = 64
            elif my_trial == 3:
                print("WARNING bad data: throw data missing")
                self.R_START = 104
                self.R_END = 188
                self.T_START_IDX = 20
                self.T_END_IDX = 28
                self.C_IDX = 83
            elif my_trial == 4:
                print("WARNING bad data: ball not thrown")
                self.R_START = 0
                self.R_END =350
                self.T_START_IDX = 8
                self.T_END_IDX = 27
                self.C_IDX = 66
        if my_dist == 16:
            self.ANGLE = 40 * np.pi / 180
            if my_trial == 1:
                print("WARNING bad data: gaps in acceleration data")
                print("Try: 16 m trial 4")
                self.R_START = 412
                self.R_END = 484
                self.T_START_IDX = 23
                self.T_END_IDX = 36
                self.C_IDX = 68
            elif my_trial == 2:
                print("WARNING bad data: gaps in acceleration data")
                print("Try: 16 m trial 4")
                self.R_START = 120
                self.R_END = 216
                self.T_START_IDX = 23
                self.T_END_IDX = 36
                self.C_IDX = 68
            elif my_trial == 3:
                print("WARNING weird data: radial acceleration non-exponential decay")
                print("Try: 16 m trial 4")
                self.R_START = 260
                self.R_END = 370
                self.T_START_IDX = 23
                self.T_END_IDX = 36
                self.C_IDX = 40
            elif my_trial == 4:
                self.R_START = 135
                self.R_END = 231
                self.T_START_IDX = 8
                self.T_END_IDX = 24
                self.C_IDX = 95
            elif my_trial == 5:
                self.R_START = 150
                self.R_END = 245
                self.T_START_IDX = 13
                self.T_END_IDX = 31
                self.C_IDX = 94
        if my_dist == 20:
            self.ANGLE = 45 * np.pi / 180
            if my_trial == 1:
                self.R_START = 210
                self.R_END = 324
                self.T_START_IDX = 23
                self.T_END_IDX = 35
                self.C_IDX = 113
            elif my_trial == 2:
                self.R_START = 210
                self.R_END = 308
                self.T_START_IDX = 18
                self.T_END_IDX = 27
                self.C_IDX = 97
    
    def get_raw_start(self):
        return self.R_START
        
    def get_raw_end(self):
        return self.R_END
    
    def get_throw_start_idx(self):
        return self.T_START_IDX
    
    def get_throw_end_idx(self):
        return self.T_END_IDX
    
    def get_catch_idx(self):
        return self.C_IDX
    
    def get_max_accel(self):
        return self.MAX_ACCEL
    
    def get_angle(self):
        return self.ANGLE
        
