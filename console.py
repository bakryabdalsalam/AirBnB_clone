#!/usr/bin/python3

"""Command interpeter."""
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """Class that handles the commands for AirBnB project."""

    prompt = "(hbnb) "
    classes = ["BaseModel"]
    all_objects = models.storage.all()

    def do_EOF(self, line):
        """Exits the command interpeter."""
        return True

    def do_quit(self, line):
        """Exits the command interpeter."""
        return True

    def emptyline(self):
        """Do nothing when empty line is entered."""
        pass

    def get_instance(self, name, ins_id):
        """Gets the object by the class name and id."""
        key = f"{name}.{ins_id}"
        instance = self.all_objects.get(key, None)
        return instance

    def check_line(self, line, count):
        """Checks the arguments passed with the command."""
        args = line.split()
        length = len(args)
        if length == 0:
            print("** class name missing **")
            return False
        else:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return False
            if count == 1:
                return True
            if length == 1:
                print("** instance id missing **")
                return False
            else:
                instance = self.get_instance(args[0], args[1])
                if instance is not None:
                    return True
                else:
                    print("** no instance found **")
                    return False

    def do_create(self, line):
        """Creates a new instance."""
        if self.check_line(line, 1):
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, line):
        """Shows information about created instance by id."""
        args = line.split()
        if self.check_line(line, 2):
            instance = self.get_instance(args[0], args[1])
            print(instance)

    def do_all(self, line):
        """Prints all objects with the class name provided."""
        args = line.split()
        if self.check_line(line, 1):
            objects = [str(v) for k, v in self.all_objects.items()
                       if k.startswith(args[0])]
            print(objects)

    def do_destroy(self, line):
        """Deletes an instance based on class name and id."""
        if self.check_line(line, 2):
            args = line.split()
            key = f"{args[0]}.{args[1]}"
            self.all_objects.pop(key)
            models.storage.save()

    def do_update(self, line):
        """Updates instance by class name and id
        by adding or updating instances.
        """
        if self.check_line(line, 2):
            args = line.split()
            length = len(args)
            if length == 2:
                print("** attribute name missing **")
            elif length == 3:
                print("** value missing **")
            else:
                instance = self.get_instance(args[0], args[1])
                name = args[2]
                value = args[3]
                if value.startswith('"'):
                    value = value[1:-1]
                if hasattr(instance, name):
                    attr_type = type(getattr(instance, name))
                    setattr(instance, name, attr_type(value))
                else:
                    setattr(instance, name, value)
                instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()