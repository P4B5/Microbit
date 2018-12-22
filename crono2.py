from microbit import*

zero = "99999:99999"
one = "00000:99999"
two = "90999:99909"
three = "90909:99999"
four = "99900:09999"
five = "99909:90999"
six = "99999:90999"
seven = "90900:99999"
eight = "99099:99099"
nine = "99900:99999"

fonts = (zero, one, two, three, four, five, six, seven, eight, nine)  

minutes = 59   #declaration of the acumulator variables
hours = 99
seconds = 59

while True:
    
    #conditions of progression of the clock
    
    time=seconds  
    
    if seconds==0:
        seconds=59
        minutes = minutes - 1
        for index in range (5):            #this loop is to avoid that a number appear at the left when the seconds restart
            display.set_pixel(0,index, 0) 
            display.set_pixel(1, index, 0)
    
    if minutes==0:
        minutes=59
        hours = hours - 1
        for index in range (5):             
            display.set_pixel(0,index, 0) 
            display.set_pixel(1, index, 0)
            
    if hours==0:
        hours=99
        for index in range (5):            
            display.set_pixel(1, index, 0)
            display.set_pixel(1, index, 0)
    
    #buttons 
    
    if button_a.is_pressed():   #if we push button a we show the hours at the display
        time=hours
        
    if button_b.is_pressed():   #if we push button b we show the minutes at the display
        time=minutes
    

    #seconds acumularor (main program)
    
    seconds=seconds-1  
    
    #calculation of ten & units digits
    
    digR = int(time % 10)   #number of the right  (units)
    digL = int(time / 10)   #number of the left   (ten)
    
    numR = fonts[digR]          #isolate the list of the strings of the number at the right(units)   
    numR = numR.split(':')      #separate of each string in a list of two strings
    
    numL = fonts[digL]          #isolate the list of the strings of the number at the left(ten)  
    numL = numL.split(':')
    
    
    #print the numbers in the display
    
    #unit numbers
    
    for index, item in enumerate(numR[0]):   
        
        b=int(item)
        display.set_pixel(3, index, b)
    
    for index2, item2 in enumerate(numR[1]):
        
        b=int(item2)
        display.set_pixel(4, index2, b)
    
    #ten numbers
    
    
            
                    #condition to show the ten numbers
    for index, item in enumerate(numL[0]):
                
        b=int(item)
        display.set_pixel(0, index, b)
                
    for index2, item2 in enumerate(numL[1]):
             
        b=int(item2)
        display.set_pixel(1, index2, b)
    
    sleep(1000)    #the loop will repeat each 1000 miliseconds = 1seg