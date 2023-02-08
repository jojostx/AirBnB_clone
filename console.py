#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def help_help(self):
        """ Prints help command description """
        print("Provides description of a given command")

    def emptyline(self):
        """do nothing when empty line"""
        pass

    def do_quit(self, line):
        """ Quit command to exit the command interpreter """
        return True

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
