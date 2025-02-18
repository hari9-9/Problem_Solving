from abc import ABCMeta, abstractmethod
from enum import Enum
from collections import deque


# ---------------- ENUMS ---------------- #

class Rank(Enum):
    OPERATOR = 0
    SUPERVISOR = 1

class CallState(Enum):
    QUEUED = 0
    IN_PROGRESS = 1
    COMPLETED = 2


# ---------------- CALL CLASS ---------------- #

class Call:
    """Represents an incoming call"""
    def __init__(self):
        self.state = CallState.QUEUED
        self.employee = None
        self.rank = Rank.OPERATOR


# ---------------- EMPLOYEE BASE CLASS ---------------- #

class Employee(metaclass=ABCMeta):
    """Abstract class for employees handling calls"""
    
    def __init__(self, employee_id, name, rank, employee_manager):
        self.employee_id = employee_id
        self.name = name
        self.rank = rank
        self.call = None
        self.employee_manager = employee_manager
        self.is_available = True  # ✅ Track availability

    def take_call(self, call):
        """Assigns a call to this employee"""
        if not self.is_available:
            raise Exception(f"{self.name} is already on a call!")

        self.call = call
        self.call.employee = self
        self.call.state = CallState.IN_PROGRESS
        self.is_available = False  # Mark unavailable
        self.employee_manager.unregister(self)

    def end_call(self):
        """Marks the call as completed and makes employee available"""
        if self.call:
            self.call.state = CallState.COMPLETED
            self.call = None
            self.is_available = True  # Mark available
            self.employee_manager.register(self)

    @abstractmethod
    def escalate_call(self):
        """Abstract method to handle escalation logic"""
        pass


# ---------------- OPERATOR & SUPERVISOR ---------------- #

class Operator(Employee):
    """Operator class that handles calls and can escalate"""

    def __init__(self, employee_id, name, employee_manager):
        super().__init__(employee_id, name, Rank.OPERATOR, employee_manager)

    def escalate_call(self):
        """Escalates the call to a supervisor if needed"""
        if self.call:
            self.call.rank = Rank.SUPERVISOR
            self.call.state = CallState.QUEUED
            self.employee_manager.dispatch_call(self.call)
            self.call = None
            self.employee_manager.register(self)


class Supervisor(Employee):
    """Supervisors handle escalated calls and cannot escalate further"""

    def __init__(self, employee_id, name, employee_manager):
        super().__init__(employee_id, name, Rank.SUPERVISOR, employee_manager)

    def escalate_call(self):
        """Supervisors must resolve the issue"""
        print(f"Supervisor {self.name} must handle the call.")


# ---------------- EMPLOYEE MANAGER ---------------- #

class EmployeeManager:
    """Manages registration, availability, and call dispatching"""

    def __init__(self):
        self.operators = set()
        self.supervisors = set()
        self.operator_queue = deque()
        self.supervisor_queue = deque()

    def register(self, employee):
        """Registers an available employee and assigns waiting calls"""
        if employee.rank == Rank.OPERATOR:
            self.operators.add(employee)
            self._dequeue_call(Rank.OPERATOR)
        else:
            self.supervisors.add(employee)
            self._dequeue_call(Rank.SUPERVISOR)

    def unregister(self, employee):
        """Unregisters an employee when they take a call"""
        if employee.rank == Rank.OPERATOR:
            self.operators.discard(employee)
        else:
            self.supervisors.discard(employee)

    def dispatch_call(self, call):
        """Attempts to assign a call to an available employee"""
        if call.rank == Rank.OPERATOR:
            if not self._dispatch(call, self.operators):
                print(f"No available operators. Call is added to queue.")
                self.operator_queue.append(call)
        else:
            if not self._dispatch(call, self.supervisors):
                print(f"No available supervisors. Call is added to queue.")
                self.supervisor_queue.append(call)

    def _dispatch(self, call, employees):
        """Finds an available employee to take the call"""
        for employee in employees:
            if employee.is_available:
                employee.take_call(call)
                return True
        return False

    def _dequeue_call(self, rank):
        """Assigns a call from the queue to an available employee"""
        if rank == Rank.SUPERVISOR and self.supervisor_queue:
            self.dispatch_call(self.supervisor_queue.popleft())
        elif rank == Rank.OPERATOR and self.operator_queue:
            self.dispatch_call(self.operator_queue.popleft())


# ---------------- CALL CENTER ---------------- #

class CallCenter:
    """Main call center class that handles call distribution"""

    def __init__(self):
        self.employee_manager = EmployeeManager()

    def hire_operator(self, employee_id, name):
        """Creates and registers a new operator"""
        operator = Operator(employee_id, name, self.employee_manager)
        self.employee_manager.register(operator)

    def hire_supervisor(self, employee_id, name):
        """Creates and registers a new supervisor"""
        supervisor = Supervisor(employee_id, name, self.employee_manager)
        self.employee_manager.register(supervisor)

    def receive_call(self):
        """Handles incoming calls"""
        new_call = Call()
        self.employee_manager.dispatch_call(new_call)
