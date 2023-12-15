# STORING THE EVENTS 
    
eventStorage = {} 

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


# CREATING NEW EVENTS AND TASKS
        
## create a new event function
        
def newEvent(title, day, startTime, endTime, description, people, completion, section):
    key = title
    value = Event(title, day, startTime, endTime, description, people, completion, section)
    eventStorage[key] = value
        
## create a new task function
    
def newTask(title, completion, section):
    key = title
    value = Event(title, completion, section)
    eventStorage[key] = value
        
# DEFINING FUNCTIONS TO BE ENACTED ON EVENTS AND TASKS

## change title
    
## change day
    
## change start time

## change end time

## change people 
    
## mark completed

## add people
    
## change section
    
## delete event
    
# COLOR CHANGING FUNCTIONS
