#!/usr/bin/python3

"""
The console module - command line interpreter
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class for command line interpreter
    """
    prompt = "(hbnb) "

    class_list = ["BaseModel",  "User"]

    def emptyline(self):
        """Empty line"""
        pass

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        End of File Method
        """
        return True

    def do_create(self, line):
        """
        Creates a new instance of BaseModel and prints the id
        """
        if not line:
            print("** class name missing **")
        elif line not in self.class_list:
            print("** class doesn't exist **")
        else:
            new = eval(line)()
            new.save()
            print(new.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        """
        line_list = line.split()

        if not line:
            print("** class name missing **")
        elif line_list[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(line_list) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(line_list[0], line_list[1])
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        line_list = line.split()

        if not line:
            print("** class name missing **")
        elif line_list[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(line_list) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(line_list[0], line_list[1])
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                del (storage.all()[key])
                storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        """
        if line:
            if line not in self.class_list:
                print("** class doesn't exist **")
            else:
                all_list = []
                for val in storage.all().values():
                    if type(val).__name__ == line:
                        all_list.append(str(val))
                print(all_list)
        else:
            all_list = []
            for key, val in storage.all().items():
                all_list.append(str(val))
            print(all_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        """
        line_list = line.split()

        if not line:
            print("** class name missing **")
        elif line_list[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(line_list) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(line_list[0], line_list[1])
            if key not in storage.all().keys():
                print("** no instance found **")

            elif len(line_list) == 2:
                print("** attribute name missing **")
            elif len(line_list) == 3:
                print("** value missing **")
            else:
                pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
