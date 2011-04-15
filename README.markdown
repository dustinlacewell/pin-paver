pin-paver
=======

pin-paver provides 'project-wide' access to commands inside your pavement.py file. pin-paver will list your paver commands in the **pin help** command.

    $pin help
    usage: pin [-v]

    optional arguments:
      -v, --version  show program's version number and exit

    Available commands for /home/dlacewell/dev/pmcs:
    destroy  - Destroy and unregister the project from pin.
    go       - Teleport to a specific project.
    help     -  This help information. 
    init     - Initialize pin in the current directory. 
    paver    --------------------------------------------------------------------------
             Commands inside your pavement file.
             test  - A test command that does nothing.


### Commands

* **pin paver [paver args]** : Execute any commands inside your pavement.py file


