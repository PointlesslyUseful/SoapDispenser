Dataset of Creative Senz3D hand acquisitions used in:
A. Memo, L. Minto, P. Zanuttigh, "Exploiting Silhouette Descriptors and Synthetic Data for Hand Gesture Recognition", STAG: Smart Tools & Apps for Graphics, 2015.

Department of Information Engineering - University of Padova (Italy)

____________________________

Files and directories structure:

-       ./acquisitions/:

        Contains the acquisitions with this structure: 
        Ss/Gg/ where 1<=s<=4 is the subject and 1<=g<=11 is the gesture.

-       ./acquisitions/Ss/Gg/:

        r-depth.bin: Senz3D depth map raw (320 x 240 short 16 bit).
        r-conf.bin: Senz3D confidence map raw (320 x 240 short 16 bit).
        r-color.png: Senz3D color map (640 x 480).
        where 1<r=<=30 is the number of repetition.

-       ./senz3d_calibration.txt: 

        Senz3D intrinsic parameters.
        fx: The focal length along the x axis, expressed in pixel units.
        fy: The focal length along the y axis, expressed in pixel units.
        cx: The central point along the x axis, expressed in pixel units.
        cy: The central point along the y axis, expressed in pixel units.
        k1: The first radial distortion coefficient.
        k2: The second radial distortion coefficient.
        k3: The third radial distortion coefficient.
        p1: The first tangential distortion coefficient.
        p2: The second tangential distortion coefficient.
____________________________

For additional information please write an e-mail to lttm@dei.unipd.it
