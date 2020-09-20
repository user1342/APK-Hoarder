import datetime
import subprocess as sp
import json
import os
import re
import time


def clean_terminal_response(byte_to_clean):
    """
    Used to clean a response. Primarily decodes a byte to string and removes uncesseary new line characters
    :param byte_to_clean:
    :return: a string without newline characters.
    """
    return byte_to_clean.decode().replace("\r","").replace("\n","")

def run_command(command):
    """
    Runs a command provided as a string with subprocess.popen.
    :param command: a string representation of a shell command
    :return: a list of the result of the provided command
    """
    proc = sp.Popen(command, shell = True, stdin=sp.PIPE, stdout=sp.PIPE)
    lines = proc.stdout.readlines()
    print("Run command: '{}'".format(command))
    if lines is not None and len(lines) > 0:
        print("\tResult: '{}...".format(lines[0]))
    else:
        print("No response from command")
    return lines

def is_adb_available():
    """
    Runs a simple adb command to check if a device is connected via adb.
    :return: True if a device is connected via adb
    """
    adb_available = True

    result = run_command("adb get-state")
    if result is None or result == "error: no devices/emulators found":
        adb_available = False


    return adb_available



def get_list_of_device_packages():
    """
    Runs a series of commands to identify which application packages are installed on a device.
    :return: a list of the installed packages
    """
    packages = run_command("adb shell pm list packages")

    iterator = 0
    for package in packages:
        packages[iterator] = clean_terminal_response(package)
        iterator = iterator + 1

    return packages

def get_paths(list_of_packages):
    """
    Identifies the apk path of for a list of packages
    :param list_of_packages: a list of packages
    :return: a list of APK locations relating to the provided package names
    """
    list_of_paths = []

    for package in list_of_packages:
        package = package.replace("package:","")
        paths = run_command("adb shell pm path {}".format(package))

        for path in paths:
            path = clean_terminal_response(path)
            path = path.replace("package:", "")
            list_of_paths.append(path)

    return list_of_paths

def get_tasking():
    """
    A function which iterates over the commands listed in the tasking file and returns them as a list of commands.
    :return: A list of commands to be performed.
    """
    tasking_file_name = 'tasking.json'
    if os.path.isfile((tasking_file_name)):
        with open(tasking_file_name) as json_file:
            data = json.load(json_file)
            tasking = data["tasks"]
    else:
        raise Exception("Tasking JSON file not provided at '{}'".format(os.path.join(os.getcwd(),tasking_file_name)))

    return tasking


# Checks if a device is connected via adb
if is_adb_available():

    paths_to_review = get_paths(get_list_of_device_packages())

    # Loops through all application packages on the device and in turn their apk paths
    for application_path in paths_to_review:
        # Performs each command in the tasking file replacing the keywords
        application_name = re.search("([^\/]*$)",application_path).group(0)
        for command in get_tasking():
            # Replace keywords if used
            command = command.replace("<applications_path>",application_path)
            command = command.replace("<applications_name>",application_name)
            run_command(command)
            time.sleep(0.5)

    print("Finished - '{}' packages reviewed.".format(len(paths_to_review)))

else:
    raise Exception("ADB is not available. Please connect a device.")