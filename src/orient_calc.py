from math import sqrt,atan,degrees

class track_obj():
    """docstring for ClassName."""
    def __init__(self):
        #Object IDs
        self.Label = "Unlabeled Object"
        
        #overall orientation
        self.inplane_rot = None
        self.orbit_rot = None
        self.center = None
        self.dims = None
        self.confidence = None

        #gear icon position
        self.center_g = None
        self.dims_g = None

        #db icon position
        self.center_d = None
        self.dims_d = None

        #calculate the inplane orientation of the tacked object
    def get_inplane(self):
        #use angles between center point of db and gear
        if(self.center_g and self.center_d):
            x_diff = self.center_d[0] - self.center_g[0]
            y_diff = self.center_g[1] - self.center_d[1]
        # distance = sqrt((x_diff**2) + (y_diff**2))

            if(not x_diff):
                if(y_diff < 0): self.inplane_rot = 180
                else: self.inplane_rot = 0
                
            else:
                if(round(degrees(atan(y_diff/x_diff)),2) < 0):
                    self.inplane_rot = round(-90 - degrees(atan(y_diff/x_diff)),2)
                elif(round(degrees(atan(y_diff/x_diff)),2) > 0):
                    self.inplane_rot = round(90 -degrees(atan(y_diff/x_diff)),2)
                # self.inplane_rot = 90 - round(self.inplane_rot,2)

        else: return -1

        

    #calculate the out of plane orientation of the tracked object
    def get_outplane(self):
        #for y axis rotation use distance between gear and db
        pass

    #get the scale of the current tracked object
    def get_scale(self):
        #use box areas expected vs actual for a given angle/rotation
        pass


def in_main_obj(main_obj,child_obj):
    """
    helper function to detect if the child_obj is part of the main_obj

    """
    #get bounding box dims for the main box
    main_left = main_obj.center[0] - (main_obj.dims[0]/2)
    main_right = main_obj.center[0] + (main_obj.dims[0]/2)
    main_top = main_obj.center[1] + (main_obj.dims[1]/2)
    main_bottom = main_obj.center[1] - (main_obj.dims[1]/2)

    #get bools for child object positions
    in_left = (child_obj[0] > main_left)
    in_right = (child_obj[0] < main_right)
    in_top = (child_obj[1] < main_top)
    in_bottom = (child_obj[1] > main_bottom)

    # print('\n\n++++++++++++')
    # print(in_left)
    # print(in_right)
    # print(in_top)
    # print(in_bottom)

    #see if child object is in the main object
    if(in_left and in_right and in_top and in_bottom): return 1
    else: return 0




        