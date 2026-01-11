#!/usr/bin/python3
"""Module for the HBNB command interpreter."""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone."""
    prompt = '(hbnb) '
    __classes = {
        "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
    }

    def do_create(self, arg):
        """Creates a new instance and saves it."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints string representation of an instance."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representations of instances."""
        args = shlex.split(arg)
        obj_list = []
        if len(args) > 0:
            if args[0] not in self.__classes:
                print("** class doesn't exist **")
                return
            for key, obj in storage.all().items():
                if key.startswith(args[0]):
                    obj_list.append(str(obj))
        else:
            for obj in storage.all().values():
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance attribute."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        obj = storage.all()[key]
        attr_name = args[2]
        attr_val = args[3]

        # Handle type casting for int and float
        try:
            if hasattr(obj, attr_name):
                type_hint = type(getattr(obj, attr_name))
                setattr(obj, attr_name, type_hint(attr_val))
            else:
                setattr(obj, attr_name, attr_val)
        except (ValueError, TypeError):
            setattr(obj, attr_name, attr_val)
        obj.save()

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
