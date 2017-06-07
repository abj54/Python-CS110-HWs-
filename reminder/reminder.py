## Anwesh Joshi
## reminder.py
## HW 6


from clock import * 
from calendar import *

import time


class Event:
    

    def __init__(self,date,time,Info):
        "this takes date, time and info which are strings"
        self.date=date
        self.time=time
        self.Info=Info
        self.setEvent(date,time,Info)
        self.eventlist=[]

            
    def setEvent(self,date,time,Info):
        """date has to be in format 12/12/12 and
        time in format 12:12 as seconds are ignored
        and year is 2016 if ignored as well. Info
        is a string"""
        try:
            D=[int(x) for x in self.date.split("/")]
            T=[int(x) for x in self.time.split(":")]
            if len(D)==2:
                D=D+[2016]
            self._calendar=Calendar(D[0],D[1],D[2])
            self._clock=Clock(T[0],T[1],0)
        except IndexError:
            print ("Wrong Format")
        except ValueError:
            print ("Wrong format")

    def hours(self):
        "getting hours"
        return self._clock.hours()
    def minutes(self):
        "getting minutes"
        return self._clock.minutes()
    def month(self):
        "getting month"
        return self._calendar.month()
    def year(self):
        "getting year"
        return self._calendar.year()
    def day(self):
        "getting day"
        return self._calendar.day()
            
       
        

    def __cmp__(self,other):
         """Comparing two events that return -1,0 and 1 if self is earlier,
equal and later than other event"""
         if self.year()<other.year():
             return -1
         elif self.year()>other.year():
             return 1
         else:
             if self.month()<other.month():
                 return -1
             if self.month()>other.month():
                 return 1
             else:
                 if self.day()<other.day():
                    return -1
                 if self.day()>other.day():
                    return 1
                 else:
                    if self.hours()>other.hours():
                        return 1
                    if self.hours()<other.hours():
                        return -1
                    else:
                        if self.minutes()<other.minutes():
                            return -1
                        if self.minutes()>self.minutes():
                            return 1
                        else:
                            return 0
    def __lt__(self,other):
        """these check for the earlier events"""
        return self.__cmp__(other)<0
    def __eq__(self,other):
        """these check for the same time events"""
        return self.__cmp__(other)==0
    def __gt__(self,other):
        """these check the later events"""
        return self.__cmp__(other)>0

    def __str__(self):
        """this is what the Class returns. Clock and Calenda and Info seperated
by commas"""
        return str(self._calendar)+","+str(self._clock)+","+self.Info
   
        



        
        
        
      

    
        
            
                
            
        
    


class Reminder(Clock,Calendar):

    def __init__(self):
        """ Here i just create an object"""
        self.Eventlist=[]
        self.nowTime()
        
        
        
    def nowTime(self):
        """Here I obtain the current system time"""
        t=time.localtime()[0:5]
        self._nowcalendar=Calendar(t[1],t[2],t[0])
        self._nowclock=Clock(t[3],t[4],0)
    


    def __str__(self):
        return str(self._nowcalendar)+","+str(self._nowclock)

    def hours(self):
        """Hours from nowTime"""
        return self._nowclock.hours()
    def minutes(self):
        """Minutes from nowTime"""
        return self._nowclock.minutes()
    def month(self):
        """Month from nowTime"""
        return self._nowcalendar.month()
    def year(self):
        """Year from nowTime"""
        return self._nowcalendar.year()
    def day(self):
        """Day from nowTime"""
        return self._nowcalendar.day()
    def seconds(self):
        """Seconds from nowTime"""
        return self._nowclock.seconds()

    def tick(self):
        """Advances time one second and checks if the day is over """
        self._nowclock.tick()
        if self.hours()==0 and self.minutes()==0 and self.seconds()==0:
            self.advance()
    def tock(self):
        """Advances time one minute using tick """
        for s in range(60):
            self.tick()
    def tack(self):
        """Advances time one minute using tick """
        for s in range(3600):
            self.tick()
    def advance(self):
        """Increases the time by a day """
        self._nowcalendar.advance()

    def __cmp__(self,other):
        """Comparing two events that return -1,0 and 1 if self is earlier,
         equal and later than other event"""
        if self.year()<other.year():
            return -1
        elif self.year()>other.year():
            return 1
        else:
            if self.month()<other.month():
                return -1
            if self.month()>other.month():
                return 1
            else:
                if self.day()<other.day():
                   return -1
                if self.day()>other.day():
                   return 1
                else:
                    if self.hours()>other.hours():
                        return 1
                    if self.hours()<other.hours():
                        return -1
                    else:
                        if self.minutes()<other.minutes():
                            return -1
                        if self.minutes()>self.minutes():
                            return 1
                        else:
                            return 0
         
   
            

    def interact(self):
        """Interacting with user to setup a reminder for an Event"""
        try:
            w=open("init.txt",'r').read()
            w=w.split("\n")
            print "from init.txt"
            if len(w)>1:
                
                for j in range(len(w)-1):
                    line=w[j].split(",")
                    self.Event=Event(line[0],line[1],line[2])
                    
                    if self.__cmp__(self.Event)<0:
                        
                        print (self.Event)
                        self.Eventlist+=[str(self.Event)]
                        self.Eventlist.sort()
            
            else:
                print "No Events found"

        except IOError:
            print ("No init.txt file found")

        while True:
            line = raw_input(">")
            line=line.replace(" ","")
            try:
                command=line[0]
            

                if command=="q":
                     w=open("init.txt",'w')
                     for j in range(len(self.Eventlist)):
                         w.write(self.Eventlist[j])
                         w.write("\n")
                     print len(self.Eventlist),"events added in init.txt"
                     w.close()
                     break

                if command == '?':
                    print "Reminder Commands: \n\
    q       [for quit] \n\
    ?       [ask for help] \n\
    t       [print 'current' time]  \n\
    e , ,  [schedule event] \n\
    s      [search for event with all strings] \n\
    x       [delete found event] \n\
    p       [print scheduled events] \n\
    m    [advance time  minutes, one if no ] \n\
    h    [advance time  hours, one if no ] \n\
    d    [advance time  days, one if no ] \n\
      w   [write scheduled events to the named file.] \n\
    r   [read and schedule events from the named file.]"

                elif command=="t":
                    print (self)

                elif command=="s":
                  
                    Foundlist=[]
                    a=line[1:].replace(" ","")
                    b=a[2:-2]
                    search=[x for x in b]
                  
                    for l in range(len(self.Eventlist)):
                        r=0
                        a=self.Eventlist[l].split(",")
                        info=a[2].replace(" ","")
                        info=[x for x in info]
                      
                        for j in range(len(search)):
                            if search[j] in info:
                                r=r+1
                                info.remove(search[j])
                            else:
                                r=r+0
                        if len(search)==r:
                            Foundlist+=[self.Eventlist[l]]
                            
                            print (self.Eventlist[l])
                    if len(Foundlist)==0:
                        print ("NO results")
                    
                             
                elif command=="x":
                    try:
                        n=len(Foundlist)
                        if n!=0:
                            for x in range(n):
                                self.Eventlist.remove(Foundlist[x])
                            print n,'events deleted'
                        else:
                            print ("No events to remove")
                    except UnboundLocalError:
                        print ("Run 's' first")
                  

                elif command=="p":
                    if len(self.Eventlist)!=0:
                        for j in range(len(self.Eventlist)):
                            print (self.Eventlist[j])
                    else:
                        print ("No events to show")
                    
                      

                elif command=="m":
                    try:
                        if len(line)==1:
                            line=line+"1"
                        n=eval(line[1:])
                        
                        for s in range(n):
                            self.tock()
                       
                        print (self)

                        while len(self.Eventlist)!=0:
                           self.nowwEvent=self.Eventlist[0].split(",")
                           self.nowEvent=Event(self.nowwEvent[0],\
                                               self.nowwEvent[1],\
                                               self.nowwEvent[2])
                           if self.__cmp__(self.nowEvent)>=0:
                               print (self.nowEvent)
                               print ("*****Reminder*****")
                               self.Eventlist.remove(self.Eventlist[0])
                           else:
                               break
                    except NameError:
                        print"Wrong Format"      
                   

                elif command=="h":
                    try:
                        if len(line)==1:
                            line=line+"1"
                        n=eval(line[1:])

                        for s in range(n):
                            self.tack()
                            
                        print (self)
                        while len(self.Eventlist)!=0:
                           self.nowwEvent=self.Eventlist[0].split(",")
                           self.nowEvent=Event(self.nowwEvent[0],self.nowwEvent[1],\
                                               self.nowwEvent[2])
                           if self.__cmp__(self.nowEvent)>=0:
                               print (self.nowEvent)
                               print ("*****Reminder*****")
                               self.Eventlist.remove(self.Eventlist[0])
                           else:
                               break
                    
                    except NameError:
                        print "Wrong Format"

                elif command=="d":
                    try:
                        if len(line)==1:
                            line=line+"1"
                        n=eval(line[1:])
                        
                        for i in range(n):
                            self.advance()
                        print (self)
                          

                        while len(self.Eventlist)!=0:
                           self.nowwEvent=self.Eventlist[0].split(",")
                           self.nowEvent=Event(self.nowwEvent[0],self.nowwEvent[1],\
                                               self.nowwEvent[2])
                           if self.__cmp__(self.nowEvent)>=0:
                               print (self.nowEvent)
                               print ("*****Reminder*****")
                               self.Eventlist.remove(self.Eventlist[0])
                           else:
                               break
                        
                    except NameError:
                        print "Wrong format"
                            
                                               
                elif command=="w":
                    try:
                        f=line[1:]
                        w=open(f,'w')
                        for j in range(len(self.Eventlist)):
                            w.write(self.Eventlist[j])
                            w.write("\n")
                        print len(self.Eventlist),"events added in",f
                        w.close()
                    except IOError:
                        print "Invalid file"

                elif command=="r":
                    try:
                        self.Eventlist=[]
                        f=line[1:].replace(" ","")
                        w=open(f,'r').read()
                        w=w.split("\n")
                        for j in range(len(w)-1):
                          
                            line=w[j].split(",")
                            self.Event=Event(line[0],line[1],line[2])
                            if self.__cmp__(self.Event)<0:
                                print (self.Event)
                                self.Eventlist+=[str(self.Event)]
                                self.Eventlist.sort()
                        print (len(self.Eventlist)),"events added"
                    except IOError:
                        print "What file?"
                    except IndexError:
                        print "Wrong file"
                              
                      
                elif command=="e":
                   
                    line=line[1:].split(",")
                    try:
                        self.Event=Event(line[0],line[1],line[2])
                        if self.__cmp__(self.Event)>0:
                            print ("Event Date has passed")
                        elif self.__cmp__(self.Event)==0:
                            print ("EVENT is now")
                        else:
                            print (self.Event)
                            self.Eventlist+=[str(self.Event)]
                            self.Eventlist.sort()
                    except IndexError:
                      print ('Wrong Format')
                    except AttributeError:
                        print"Wrong Format"

                
                elif command not in  ["q","m","s","t","d","h","e","?","w",
                                      "r","p","x"]:
                     print "What command is that?"

               

            except IndexError:
                print"Enter Command Again"
            

                  
        
        




                
                
            
       
            




        
            
           
              
    
          
          
       
                      

    

    





