
import os, sys
from argparse import ArgumentParser

from paver.tasks import main, Environment, _group_by_module

from pin import command
from pin.util import get_project_root

class PinPaverCommand(command.PinBaseCommandDelegator):
    '''
    Commands inside your pavement file.
    '''
    command = 'paver'

    @classmethod
    def get_subcommands(cls):
        cwd = os.getcwd()
        root = get_project_root(cwd)
        try:
            sys.path.append(root)
            mod = __import__('pavement')
            env = Environment(mod)
            tasks = env.get_tasks()
            maxlen, tasklist = _group_by_module(tasks)
            for name, group in tasklist:
                if name == 'pavement':
                    return dict((t.shortname, t) for t in group)
        except ImportError:
            return dict()

    def setup_parser(self, parser):
        parser.add_argument('paverargs', nargs='*')

    def execute(self):
        if self.root:
            os.chdir(self.root)
            print "echo %s" % self.options.paverargs
            main(self.options.paverargs)
            return True

command.register(PinPaverCommand)
