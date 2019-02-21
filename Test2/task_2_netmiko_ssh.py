from netmiko import ConnectHandler
from pprint import pprint

"""
ssh_connect() function establishes ssh connection.
Inputs are:
device_info : a dictionary with minimum parameters - ip, username, password, type of the device.
              compatible devices are listed under CLASS_MAPPER keys in the following link(https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py)
command : show command to be captured

Output is returned as a string
"""
def ssh_connect(device_info, command):

    ssh_connection = ConnectHandler(**device_info)

    interface_cli = ssh_connection.send_command(command)

    pprint(interface_cli)

    return interface_cli


"""
write_device_logs() function writes a string into a text file.
Inputs are:
log_file_name : string will be written to the text file named log_file_name
string : string to be written in the text file

Output: text file will be created in the same location where the python script is executed
"""
def write_device_logs(log_file_name, string):
    f = open(log_file_name, "w")
    f.write(string)
    f.close()


"""
When you execute a Python script, it is treated as the main and its __name__ attribute is set to "__main__".
If you import this script as a module in another script, the __name__ is set to the name of the script/module.
"""
if __name__ == "__main__":
    ### inputs ###
    device_info = {"device_type": "cisco_xe",
                   "host": "198.18.134.11",
                   "username": "admin",
                   "password": "C1sco12345"}

    command = "show ip interface brief"

    log_file_name = "device_logs.txt"

    ### function call to establish ssh connection and return the output as a string
    interface_cli = ssh_connect(device_info, command)

    ### function call to write the output string into a text file
    write_device_logs(log_file_name, interface_cli)
