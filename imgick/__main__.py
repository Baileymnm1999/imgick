import sys
import argparse
import imgick.commands as commands

if __name__ == '__main__':
    # parse args
    parser = argparse.ArgumentParser(
        description='Create and edit imgick projects from the commandline',
        usage='imgick <command> [<args>]')

    parser.add_argument('command', help='Subcommand to run')
    # parse_args defaults to [1:] for args, but you need to
    # exclude the rest of the args too, or validation will fail
    args = parser.parse_args(sys.argv[1:2])
    if not hasattr(commands, args.command):
        print
        'Unrecognized command'
        parser.print_help()
        exit(1)
    # use dispatch pattern to invoke method with same name
    getattr(commands, args.command)(sys.argv[2:])
