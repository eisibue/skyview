def SVF(x,cellsize=1):
    #Find Shape parameters
    z=len(x)
    w=int(np.sqrt(z))
    c =(int(w/2))
    x=x.reshape(w,w)
    print("length",z)
        #haha test
    #Calculate height difference
    Height = x-x[c,c]
    
    #Set minimum height difference
    Height = np.clip(Height,0,90) 
    
    #Calculate euclidian distances
    # Found on https://stackoverflow.com/questions/40820955/numpy-average-distance-from-array-center
    grid_x, grid_y = np.mgrid[0:x.shape[0], 0:x.shape[1]]
    #print(grid_x,grid_y)
    center = (c,c)
    grid_x = grid_x - center[0]
    grid_y = grid_y - center[1]

    Grid_distance = np.hypot(grid_x, grid_y)
    
    #Calculate Horizon angle
    Horizon_angle=np.arctan(Height/Grid_distance)
    
    Select_angle=np.nan_to_num(Horizon_angle)
    #Calculate Horizontal and Vetical Max Angle
    V1=Select_angle[:c,c]
    V2=Select_angle[c:,c]
    H1=Select_angle[c,:c]
    H2=Select_angle[c,c:]
    V1=V1.max()
    V2=V2.max()
    H1=H1.max()
    H2=H2.max()

    #Calculate Daigonal Max Angle
    Diag1=Select_angle.diagonal()
    Diag2=np.fliplr(Select_angle).diagonal()
    DR1=Diag1[:c]
    DR2=Diag1[c:]
    DL1=Diag2[:c]
    DL2=Diag2[c:]
    DR1=DR1.max()
    DR2=DR2.max()
    DL1=DL1.max()
    DL2=DL2.max()

    Max_Angle=([V1,V2,H1,H2,DR1,DR2,DL1,DL2])
    
    #Calculate Sin of angles
    SinYt= (np.sin(Max_Angle))
    SinYt=np.nan_to_num(SinYt)
    Smean=np.mean(SinYt)
    SinYt=np.ravel(SinYt)
    
    #Calculate SVF
    #z=np.ravel(x)
    nt=(len(SinYt))
    print(nt)
    print(sum(SinYt))
    SVF = 1 - (sum(SinYt)/nt)
    
    return SVF
