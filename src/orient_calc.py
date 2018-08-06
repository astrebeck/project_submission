class track_obj():
    """docstring for ClassName."""
    def __init__(self):
        #Object IDs
        self.Label = "Unlabeled Object"
        
        #overall orientation
        self.inplane_rot = None
        self.orbit_rot = None
        self.center_a = None
        self.width_a = None
        self.height_a = None

        #gear icon position
        self.center_g = None
        self.width_g = None
        self.height_g = None

        #db icon position
        self.center_d = None
        self.width_d = None
        self.height_d = None

        #calculate the inplane orientation of the tacked object
        def get_inplane(self):
            #use angles between center point of db and gear
            pass

        #calculate the out of plane orientation of the tracked object
        def get_outplane(self):
            #for y axis rotation use distance between gear and db
            pass

        #get the current scale of the current tracked object
        def get_scale(self):
            #use box areas expected vs actual for a given angle/rotation
            pass



        