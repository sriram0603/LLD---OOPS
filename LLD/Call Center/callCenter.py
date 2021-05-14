from enum import Enum

class Rank(Enum):
    OPERATOR = 0
    SUPERVISOR = 1
    DIRECTOR = 2

class CallState(Enum):
    ACTIVE = 0
    INPROGRESS = 1
    COMPLETED = 2

class Call:
    def __init__(self,rank):
        self.state = CallState.ACTIVE
        self.employee = None
        self.rank = rank

class Employee:
    def __init__(self,Emp_id,rank,call: Call):
        self.id = Emp_id
        self.rank = rank
        self.call = call
        
    def take_call(self):
        self.call.state = CallState.INPROGRESS
        self.call.employee = self.id
    
    def complete_call(self):
        self.call.state = CallState.COMPLETED
        self.call = None
    
    def escalateCall(self):
        self.