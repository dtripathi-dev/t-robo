from transport import CliTransport
from commands import registry
from robo import RoboSim
from command_adaptor import RoboSimCommandAdaptor

def get_instructions() -> str:
    return '''
You can enter one of the below commands. Note that all other commands will be ignored until a valid PLACE command is seen:
    PLACE X, Y -> to place robot on the Grid
    MOVE -> to move robot one cell in front of it
    LEFT -> to rotate the robot towards left without moving the robot
    RIGHT -> to rotate the robot towards right without moving the robot
    REPORT -> to report the current location and direction of the robot     
'''

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    transport = CliTransport('Enter a new command:\n')
    sim = RoboSim()
    RoboSimCommandAdaptor.configure(sim, registry, print)

    while True:

        transport.write(get_instructions())
        input_cmd = transport.read().strip().upper()

        if len(input_cmd) == 0:
            print('Please enter a valid command.')
            continue

        if input_cmd == 'EXIT':
            break

        try:
            RoboSimCommandAdaptor.process_command(input_cmd)
        except ValueError as e:
            transport.write(str(e))
