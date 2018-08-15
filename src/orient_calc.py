from math import sqrt,atan,degrees

class track_obj():
    """docstring for ClassName."""
    def __init__(self):
        #Object IDs
        self.Label = "Unlabeled Object"

        #object labels
        self.boxes = []
        self.db_box = []
        self.gear_box = []

        #static variables
        self.scale_1 = 153
        self.op_rot_size_x = 75
        self.op_rot_size_y = 55
        
        #overall orientation
        self.inplane_rot = 0
        self.op_rot = ()
        self.top_left = ()
        self.center = ()
        self.dims = ()
        self.confidence = 0
        self.scale = 0

        #gear icon position
        self.center_g = ()
        self.dims_g = ()

        #db icon position
        self.center_d = ()
        self.dims_d = ()

        #calculate the inplane orientation of the detected object
    def get_inplane(self):
        #use angles between top_left point of db and gear
        if(self.center_g and self.center_d):
            x_diff = self.center_d[0] - self.center_g[0]
            y_diff = self.center_g[1] - self.center_d[1]

            if(not x_diff):
                if(y_diff < 0): self.inplane_rot = 180
                else: self.inplane_rot = 0
                
            else:
                if(round(degrees(atan(y_diff/x_diff)),2) < 0):
                    self.inplane_rot = round(-90 - degrees(atan(y_diff/x_diff)),2)
                elif(round(degrees(atan(y_diff/x_diff)),2) > 0):
                    self.inplane_rot = round(90 -degrees(atan(y_diff/x_diff)),2)


        else: return -1

    #calculate the out of plane orientation of the tracked object
    def get_outplane(self):
        
        if(self.dims_g and self.scale):
            screen_rot_x = 90 - ((self.dims_g[1] / (self.op_rot_size_x * self.scale)) * 90)
            screen_rot_y = 90 - ((self.dims_g[0] / (self.op_rot_size_y * self.scale)) * 90)
            self.op_rot = (round(screen_rot_x,2),round(screen_rot_y,2))
        
    #get the scale of the current tracked object
    def get_scale(self):
        #use box areas expected vs actual for a given angle/rotation
        self.scale = round(sqrt(self.dims[0]**2 + self.dims[1]**2) / self.scale_1,2)


    #valid capture?
    def valid(self):
        if(self.center_g and self.center_d and self.dims_g and self.dims_d): 
            
            self.boxes.append(('0 '+ str(self.center[0]/512) + ' ' + str(self.center[1]/512) + ' ' + str(self.dims[0]/512) + ' ' + str(self.dims[1]/512)))
            self.db_box.append(('1 ' + str(self.center_g[0]/512) + ' ' + str(self.center_g[1]/512) + ' ' + str(self.dims_g[0]/512) + ' ' + str(self.dims_g[1]/512)))
            self.gear_box.append(('2 ' + str(self.center_d[0]/512) + ' ' + str(self.center_d[1]/512) + ' ' + str(self.dims_d[0]/512) + ' ' + str(self.dims_d[1]/512))) 
            return 1
        else: return 0 


def in_main_obj(main_obj,child_obj):
    """
    helper function to detect if the child_obj is part of the main_obj

    """
    #get bounding box dims for the main box
    main_left = main_obj.top_left[0] - (main_obj.dims[0]/2)
    main_right = main_obj.top_left[0] + (main_obj.dims[0]/2)
    main_top = main_obj.top_left[1] + (main_obj.dims[1]/2)
    main_bottom = main_obj.top_left[1] - (main_obj.dims[1]/2)

    #get bools for child object positions
    in_left = (child_obj[0] > main_left)
    in_right = (child_obj[0] < main_right)
    in_top = (child_obj[1] < main_top)
    in_bottom = (child_obj[1] > main_bottom)

    #see if child object is in the main object
    if(in_left and in_right and in_top and in_bottom): return 1
    else: return 0




        