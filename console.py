#!/usr/bin/python3

"""
The console module - command line interpreter
"""

import cmd
import os


class HBNBCommand(cmd.Cmd):
    """
    Class for command line interpreter
    """
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("To quit the interpreter cleanly")

    def do_EOF(self, line):
        """
        End of File Method
        """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
