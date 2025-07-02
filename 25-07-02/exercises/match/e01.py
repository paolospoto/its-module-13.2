# Command interpreter
# RULES:
# Use match-case statements
# - Accept commands: "start", "stop", "exit"
# - Print appropriate messages for each command ("System started", "System stopped", "System exited")

command = input('Inset command: ')


match command:
    case 'start':
        print('System started')
    case 'stop':
        print('System stopped')
    case 'exit':
        print('System exited')
    case _:
        print('Command not valid')
