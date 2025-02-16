package org.example;

class Elevator {
    protected int currentFloor;
    protected IElevatorState state;

    public Elevator() {
        this.currentFloor = 0;
        this.state = new IdleState();
    }

    public void moveToFloor(int floor){
        // api to move the elevator to a specific floor
        if(floor > currentFloor){
            state = new MovingUpState();
        }
        else if (floor < currentFloor){
            state = new MovingDownState();
        }
        else {
            state = new IdleState();
        }
        state.handleRequest();
        currentFloor = floor;
    }
}

interface IElevatorState{
    void handleRequest();
}

class MovingUpState implements IElevatorState{

    @Override
    public void handleRequest() {
        // Move up
    }
}

class MovingDownState implements IElevatorState{

    @Override
    public void handleRequest() {
        // Move down
    }
}

class IdleState implements IElevatorState{

    @Override
    public void handleRequest() {
        // Idle
    }
}

interface IObserver{
    void update(int floor , String direction);
}

class FloorRequestPanel implements IObserver{

    @Override
    public void update(int floor, String direction) {

    }
}
