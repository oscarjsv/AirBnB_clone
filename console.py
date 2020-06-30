#!/usr/bin/python3
"""module for task 6
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """class HBNB Command"""
    prompt = '(hbnb)'

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True
    def do_EOF(self, line):
        """EQF command to exit the program\n"""
        return True

    def emptyline(self):
        pass
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()