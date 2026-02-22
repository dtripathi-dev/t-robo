def read_input() -> str:
    return input('Enter your command ')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while True:
        input_cmd = read_input()

        if len(input_cmd) == 0:
            print('Please enter a valid command.')
            continue

        normalized_cmd = input_cmd.strip().upper()
        print(f'Command entered: {normalized_cmd}')

        cmd_code, *cmd_raw_args = normalized_cmd.split()

        if cmd_code == 'EXIT':
            break

        print(f'Command recieved: {cmd_code}, {cmd_raw_args}')
