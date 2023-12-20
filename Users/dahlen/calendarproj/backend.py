# STORING THE EVENTS 
    
eventStorage = []

# DEFINING CLASSES

## event superclass defintion

class Event():
    def __init__(self, title, day, startTime, endTime, description, people, completion, section):
        self.title = title
        self.day = day
        self.startTime = startTime
        self.endTime = endTime
        self.description = description
        self.people = people
        self.completion = completion
        self.section = section

## task subclass definition
        
class Task(Event):
    def __init__(self, title, completion, section):
        self.title = title
        self.completion = completion
        self.section = section
    
    def changeTitle(self, title):
        self.title = title
    
    def changeDay(self, day):
        self.day = day
    
    def changeStartTIme(self, startTime):
        self.startTime = startTime
    
    def changeEndTime(self, endTime):
        self.endTime = endTime
    
    def changeDescription(self, description):
        self.description = description
    
    def changePeople(self, people):
        self.people = people

    def changeCompletion(self):
        self.completion = not self.completion
    
    def changeSection(self, section):
        self.section = section
    

def deleteEvent(Event):
    index = eventStorage.index(Event)
    eventStorage.pop(index)
    
# COLOR CHANGING FUNCTIONS
# ^ will need to be implemented after frontend and backend are implemented together