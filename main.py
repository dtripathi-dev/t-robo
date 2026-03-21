from typing import Callable, Any, cast
from commands import CmdOutput, CMD_REGISTRY, CmdWithArgs, PlaceCmdArgs, CmdArgs
from robo import RoboSim

def read_input(fn: Callable[[str], str]) -> str:
    return fn('Enter your command ')

def write_instructions(fn: Callable[[str], None]) -> None:
    return fn('''
You can enter one of the below commands. Note that all other commands will be ignored until a valid PLACE command is seen:
    PLACE X, Y -> to place robot on the Grid
    MOVE -> to move robot one cell in front of it
    LEFT -> to rotate the robot towards left without moving the robot
    RIGHT -> to rotate the robot towards right without moving the robot
    REPORT -> to report the current location and direction of the robot     
''')

def write_output(out: CmdOutput, fn: Callable[[str], None]):
    fn(str(out))

def write_error(out: Any, fn: Callable[[str], None]):
    fn(str(out))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    sim = RoboSim()

    while True:

        write_instructions(print)
        input_cmd = read_input(input).strip()

        if len(input_cmd) == 0:
            print('Please enter a valid command.')
            continue

        normalized_cmd = input_cmd.upper()
        print(f'Command entered: {normalized_cmd}')

        cmd_code, *cmd_raw_args = normalized_cmd.split()

        if cmd_code == 'EXIT':
            break

        print(f'Command received: {cmd_code}, {cmd_raw_args}')

        try:

            if cmd_code not in CMD_REGISTRY.keys():
                raise ValueError('Command not identified.')

            cmd = CMD_REGISTRY[cmd_code]

            if isinstance(cmd, CmdWithArgs):
                raw = cmd_raw_args[0] if cmd_raw_args else ''
                parsed_args = cmd.parse(raw)
                print(f'Parsed args: {parsed_args}')
                if cmd.code == 'PLACE':
                    output = cast(CmdWithArgs[PlaceCmdArgs], cmd).execute(sim, cast(PlaceCmdArgs, parsed_args))
                else:
                    output = cast(CmdWithArgs[CmdArgs], cmd).execute(sim, cast(CmdArgs, parsed_args))
            else:
                output = cmd.execute(sim)

            write_output(output, print)

        except ValueError as e:
            write_error(e, print)
