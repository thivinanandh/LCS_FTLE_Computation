# %%
import numpy as np
import matplotlib.pyplot as plt

h = 0.5
xmin = 0;
xmax = 2;
ymin = 0 ;
ymax = 1;

X = np.arange(xmin,xmax+h,h)
Y = np.arange(ymin,ymax+h,h)
## create Grid
gridX,gridY = np.meshgrid(X,Y)

Sol_x = np.arange(1,len(X)*len(Y)+1,1).reshape((len(Y),len(X)))
Sol_y = np.arange(1,len(X)*len(Y)+1,1).reshape((len(Y),len(X)))

# %%
#### INterpolation for Velocity 
## Consider the object to be a Meshed grid. 
## NOrmalise all the position of the mesh points to be between [0,xmax] and [0,ymax]
## based on the current position of point , identify the Cell ( or bounding box ) of the point
##          -- This can be done by computing delta =  currPOsition % h ;
##          -- the other four points can be computed by (currX - delta) , (currY - delta ) // Left bottom
##          -- The index of these 4 arrays can be found by using normal indexing formulas. 
##           -- After identifying the indices, a linear interpolation can be applied to get the value at those points.



def interpolateSolution(currentX, CurrentY):
    global Sol_x, Sol_y,h,xmin,xmax,ymin,ymax;
    diffX = currentX % h;
    diffY = CurrentY % h;
    print("Difx : ", diffX, "Diffy : ", diffY)
    pointLT = (currentX - diffX , CurrentY + diffY)
    pointLB = (currentX - diffX, CurrentY - diffY)
    pointRT = (currentX + diffX , CurrentY + diffY)
    pointRB = (currentX + diffX , CurrentY - diffY)

    if(abs(diffX < 1e-6) and abs(diffY) < 1e-6): ## a point 
        return Sol_x[int(currentX - xmin)/h,int(CurrentY - ymin)/h  ] ,Sol_y[int(currentX - xmin)/h,int(CurrentY - ymin)/h  ] ;
    elif(abs(diffX < 1e-6) ):   ## Edge 
        a = Sol_x[]

    ## Identify the Coordinates of this point 
    loc_LT = (int(np.floor((pointLT[0] -    xmin )/h)) , int(np.floor((pointLT[1] -    ymin )/h)) )
    loc_LB = (int(np.floor((pointLB[0] -    xmin )/h)) , int(np.floor((pointLB[1] -    ymin )/h)) )
    loc_RT = (int(np.floor((pointRT[0] -    xmin )/h)) , int(np.floor((pointRT[1] -    ymin )/h)) )
    loc_RB = (int(np.floor((pointRB[0] -    xmin )/h)) , int(np.floor((pointRB[1] -    ymin )/h)) )

    print(pointLT , " , " , pointLB , " , " , pointRT , " , ", pointRB)
    print(loc_LT , " , " , loc_LB , " , " , loc_RT , " , ", loc_RB)
    ### get the values at these co-ordinates 
    Val_LT_x = (Sol_x[loc_LT[1],loc_LT[0]]);
    Val_LB_x = (Sol_x[loc_LB[1],loc_LB[0]]);
    Val_RT_x = (Sol_x[loc_RT[1],loc_RT[0]]);
    Val_RB_x = (Sol_x[loc_RB[1],loc_RB[0]]);

    Val_LT_y = (Sol_y[loc_LT[1],loc_LT[0]]);
    Val_LB_y = (Sol_y[loc_LB[1],loc_LB[0]]);
    Val_RT_y = (Sol_y[loc_RT[1],loc_RT[0]]);
    Val_RB_y = (Sol_y[loc_RB[1],loc_RB[0]]);

    ##Compute average of all points
    avg_x = Val_LT_x + Val_LB_x + Val_RT_x + Val_RB_x;
    avg_y =  Val_LT_y + Val_LB_y + Val_RT_y + Val_RB_y;

    avg_x /= 4;
    avg_y /= 4;

    return avg_x,avg_y


# %%
interpolateSolution(0,0.25)

# %%
