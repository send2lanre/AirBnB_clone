#!/usr/bin/python3
"""This code houses our CLI loop"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """CLI Class"""
    prompt: '(hbnb)'
    class_handles = {
            'BaseModel': BaseModel, 'User': User, 'City': City,
            'Place': Place, 'Amenity': Amenity,
            'Review': Review, 'State': State}

    def do_quit(self, arg):
        """quit method"""
        exit()

    def do_EOF(self, arg):
        """exit method"""
        print('')
        exit()

    def emptyline(self):
        """override default empty line"""
        pass

    def do_create(self, arg):
        """creates an instance of the
        base class
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg:
            args = arg.split()
            if len(args) == 1:
                if arg in self.class_handles.keys():
                    new = self.class_handles[arg]()
                    new.save()
                    print(new.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, arg):
        """shows a particular instance
        of a class based on id
        """
        if len(arg) == 0:
            print(" **class name missing **")
            return
        if arg:
            args = arg.split()
            if args[0] not in self.class_handles.keys():
                print("** class doesn't exist **")
                return
            elif len(args) > 1:
                key_id = args[0] + '.' + args[1]
                if key_id in storage.all():
                    print(storage.all()[key_id])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")

    def do_destroy(self, arg):
        """deletes an instance of the
        base class based on the id
        """
        args = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.class_handles:
            print("class doesn't exist")
            return
        elif len(args) > 1:
            key_id = args[0] + '.' + args[1]
            if key_id in storage.all():
                storage.all().pop(key_id)
                storage.save()
            else:
                print("** no instance found **")
                return
        else:
            print("** instance id missing **")

    def do_all(self, arg):
        """prints all instances
        irrespective of class name
        """
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
        elif arg not in self.class_handles:
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in storage.all().items() if arg in b])

    def do_update(self, arg):
        """updates an instance based on
        class name and id
        """
        args = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in self.class_handles:
            print("class doesn't exist")
            return
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) > 1:
            key_id = args[0] + '.' + args[1]
            if key_id in storage.all():
                if len(args) > 2:
                    if len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(
                                storage.all()[key_id],
                                arg[2], arg[3][1:-1])
                        storage.all()[key_id].save()
                else:
                    print("** attribute name missing **")
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
