
import os, sys
from argparse import ArgumentParser

from paver.tasks import main

from pin import command

class PinPaverCommand(command.PinCommand):
    command = 'paver'

    def setup_parser(self, parser):
        parser.add_argument('paverargs', nargs='*')

    def execute(self, cwd, root):
        os.chdir(root)
        main(self.options.paverargs)

command.register(PinPaverCommand)
