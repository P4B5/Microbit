
from microbit import*   

samples = []  #new list to store the values

SIZE=100
AVG_MAX_ELEMENTS=10
    
while True:
    
    acum_x=0   
    acum_y=0
    acum_z=0
    
    # coger nueva muestra
    val_x=accelerometer.get_x()  #X axis ~green~
    val_y=accelerometer.get_y()  #Y axis ~blue~
    val_z=accelerometer.get_z()  #Z axis ~orange~
    
    tup=(val_x, val_y, val_z)    #store each lecture of three elements in a tuple 

    # store the sample in the list samples
    
    if len(samples) == SIZE:   #lenght of the list samples must be less or equal than 'SIZE'
        samples.pop(0)
    samples.append(tup)
    
    
    #make the average
    
    if len (samples)>=AVG_MAX_ELEMENTS:  #elements inside the list must be more than "AVG_MAX_ELEMENTS" to do the average
        
        for i in range(-1, -11, -1):
            
            acum_x += samples[i][0]     
            acum_y += samples[i][1]
            acum_z += samples[i][2]
     
        avg_x = acum_x/AVG_MAX_ELEMENTS
        avg_y = acum_y/AVG_MAX_ELEMENTS
        avg_z = acum_z/AVG_MAX_ELEMENTS
       
        acum=(avg_x, avg_y, avg_z) 
        
        print(acum) #print the average on the plotter

    sleep(100)  
    