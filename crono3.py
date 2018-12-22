from microbit import*

zero = "99999:99999"
one = "00000:90000"
two = "00000:99000"
three = "00000:99900"
four = "00000:99990"
five = "00000:99999"
six = "99999:90000"
seven = "99999:99000"
eight = "99999:99900"
nine = "99999:99990"

fonts = (zero, one, two, three, four, five, six, seven, eight, nine)  

minutes = 0   #declaration of the acumulator variables
hours = 0
seconds = 0

while True:
    
    #conditions of progression of the clock
    
    time=seconds  
    
    if seconds==60:
        seconds=0
        minutes = minutes + 1
        for index in range (5):            #this loop is to avoid that a number appear at the left when the seconds restart
            display.set_pixel(0,index, 0) 
            display.set_pixel(1, index, 0)
    
    if minutes==60:
        minutes=0
        hours = hours + 1
        for index in range (5):             
            display.set_pixel(0,index, 0) 
            display.set_pixel(1, index, 0)
            
    if hours==99:
        hours=0
        for index in range (5):            
            display.set_pixel(1, index, 0)
            display.set_pixel(1, index, 0)
    
    #buttons 
    
    if button_a.is_pressed():   #if we push button a we show the hours at the display
        time=hours
        
    if button_b.is_pressed():   #if we push button b we show the minutes at the display
        time=minutes
    

    #seconds acumularor (main program)
    
    seconds=seconds+1  
    
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
    
    if digL<1:                               #condition to not show a zero at the left
       for index in range (5):
            display.set_pixel(0,index, 0) 
            display.set_pixel(1, index, 0)
            
    elif digL>=1 and digL<=5:                 #condition to show the ten numbers
        for index, item in enumerate(numL[0]):
                
            b=int(item)
            display.set_pixel(0, index, b)
                
        for index2, item2 in enumerate(numL[1]):
             
            b=int(item2)
            display.set_pixel(1, index2, b)
    
    sleep(1000)    #the loop will repeat each 1000 miliseconds = 1seg