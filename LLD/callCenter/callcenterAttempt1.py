from abc import ABCMeta , abstractmethod
from enum import Enum

class Rank(Enum):
    OPERATOR = 0
    SUPERVISOR = 1

class CallState(Enum):
    QUEUED = 0
    IN_PROGRESS = 1
    COMPLETED = 2


class Employee(metaclass=ABCMeta):
    
    def __init__(self , employee_id , name , rank , call_center):
        self.employee_id = employee_id
        self.name = name
        self.rank = rank
        self.call = None
        self.call_center = call_center
    
    def take_call(self , call):
        self.call = call
        self.call.employee = self
        self.call.state = CallState.IN_PROGRESS
        self.unregister()
    
    def end_call(self):
        self.call.state = CallState.COMPLETED
        self.call = None
        self.register()
    
    @abstractmethod
    def escalate_call(self):
        pass
    
    def register(self):
        if self.rank == Rank.OPERATOR:
            self.call_center.register_operator(self)
        else:
            self.call_center.register_supervisor(self)
    
    def unregister(self):
        if self.rank == Rank.OPERATOR:
            self.call_center.unregister_operator(self)
        else:
            self.call_center.unregister_supervisor(self)


class Operator(Employee):
    def __init__(self , employee_id, name, call_center):
        super().__init__(employee_id,name,Rank.OPERATOR, call_center)
    
    def escalate_call(self):
        if self.call:
            self.call.rank = Rank.SUPERVISOR
            self.call.state = CallState.QUEUED
            self.call_center.dispatch_call(self.call)
            self.call = None
            self.register()
    
        
    

class Supervisor(Employee):
    def __init__(self , employee_id, name,call_center):
        super().__init__(employee_id,name,Rank.SUPERVISOR , call_center)
    
    def escalate_call(self):
        raise NotImplemented('Supervisors must be able to handle any call')
        
        
class Call(object):
    
    def __init__(self):
        self.state = CallState.QUEUED
        self.employee = None
        self.rank = Rank.OPERATOR



class CallCenter(object):
    
    def __init__(self):
        self.operators = set()
        self.supervisors = set()
        self.operatorQueue = []
        self.supervisorQueue = []
    
    def register_operator(self,operator):
        self.operators.add(operator)
        self._dequeue_call(Rank.OPERATOR)
    
    def register_supervisor(self,supervisor):
        self.supervisors.add(supervisor)
        self._dequeue_call(Rank.SUPERVISOR)
    
    def unregister_operator(self , operator):
        self.operators.remove(operator)
    
    def unregister_supervisor(self , supervisor):
        self.supervisors.remove(supervisor)
    
    def _enqueue_call(self , call , rank):
        if rank == Rank.OPERATOR:
            self.operatorQueue.append(call)
        else:
            self.supervisorQueue.append(call)
    
    def _dequeue_call(self,rank):
        if rank == Rank.OPERATOR:
            if len(self.operatorQueue):
                self.dispatch_call(self.operatorQueue.pop(0))
        else:
            if len(self.supervisorQueue):
                self.dispatch_call(self.supervisorQueue.pop(0))
            
    
    def dispatch_call(self,call):
        if call.rank == Rank.OPERATOR:
            if not self._dispatch(call , self.operators):
                self._enqueue_call(call , Rank.OPERATOR)
        else:
            if not self._dispatch(call , self.supervisors):
                self._enqueue_call(call, Rank.SUPERVISOR)
    
    def _dispatch(self,call,employees):
        for employee in employees:
            if employee.call is None:
                employee.take_call(call)
                return True
        return False