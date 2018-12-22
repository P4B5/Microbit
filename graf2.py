from microbit import*   

samples = []  #new list to store the values

SIZE=30 #only 30 elements
AVG_MAX_ELEMENTS=10
    
while True:
    
    acum_x=0   
    acum_y=0
    
    
    if button_a.was_pressed():
        s1=samples[-1]
        final=int(s1[0])
        display.show("{}".format(final))
        display.clear()  
        
    if button_b.was_pressed():
        s1=samples[-1]
        final=int(s1[1])
        display.show("{}".format(final))   
        display.clear() 
        
    # coger nueva muestra
    val_x=accelerometer.get_x()  #X axis ~green~
    val_y=accelerometer.get_y()  #Y axis ~blue~
    
    
    tup=(val_x, val_y)    #store each lecture of three elements in a tuple 

    # store the sample in the list samples
    
    if len(samples) == SIZE:   #lenght of the list samples must be less or equal than 'SIZE'
        samples.pop(0)
    samples.append(tup)
    
    
    #make the average
    
    if len (samples)>=SIZE:  #elements inside the list must be more than "AVG_MAX_ELEMENTS" to do the average
        
        for i in range(-1, -30, -1):
            
            acum_x += samples[i][0]     
            acum_y += samples[i][1]
            
     
        avg_x = acum_x/AVG_MAX_ELEMENTS
        avg_y = acum_y/AVG_MAX_ELEMENTS
        
       
        acum=(avg_x, avg_y) 
        
        print(acum) #print the average on the plotter

    sleep(100)  
    