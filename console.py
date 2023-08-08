#!/usr/bin/python3
"""Defines the HBnB console"""
import cmd

class HBNBCommand(cmd.Cmd):
    """It defines HBnB command interplater
    Attributes:
        prompt (str): The command prompt
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Enter quit command to exit program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
