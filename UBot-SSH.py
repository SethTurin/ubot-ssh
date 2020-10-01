import os
import math
import re
import shutil
import subprocess as sp
import random
import sys
from System.IO import Directory, Path


# cmd = [SSH_BIN, '-l', user, host, command]

################################################################################
################################# CONFIG #######################################
################################################################################


system = "Windows"
try:
    if sys.argv[1] == 'OSX':
        system = 'OSX'
except IndexError:
    pass

BASE_PATH = os.getcwd()
# CLIPS_PATH = os.path.join(BASE_PATH, 'test_clips')
TEMP_PATH = os.getenv('TEMP')
DETACHED_PROCESS = 0x00000008
if system == 'OSX':
    SSH_BIN = 'ssh'
else:
    ssh_path = os.path.join(os.getenv('SYSTEMROOT'), "System32", "OpenSSH")
    SSH_BIN = os.path.join(ssh_path, 'ssh.exe')
LOGLEVEL = 'warning'

################################################################################
################################## UTILS #######################################
################################################################################


def _subprocess_call(cmd, name="command"):
    """ Executes subprocess command."""


    popen_params = { "stderr": sp.PIPE,
                     "creationflags": DETACHED_PROCESS }

    try:
        process = sp.Popen(cmd, **popen_params)
        err = process.communicate()[1]
    except OSError as err:
        print "OSError: %s" % err
        raise
    except TypeError as err:
        print "TypeError: %s" % err
        raise

    if process.returncode:
        print err
        raise StandardError 
    else:
        # TODO should output be printed on success?
        print err
        print "Successfully executed %s" % name

    del process

    return err




################################################################################
################################## commands ####################################
################################################################################


def sshcommand(host, user, command):

    cmd = [SSH_BIN,
            '-l', user,
            host,
            command
            ]
    _subprocess_call(cmd, 'sshcommand')

