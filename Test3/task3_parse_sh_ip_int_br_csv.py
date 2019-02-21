import re
from pprint import pprint
import csv

## dictionary initialisation
interface_dict={}

## list initialisation
list_of_interface_dict=[]


## read a text file and returns a list where each element of a list is a line from the text file
def read_device_logs(log_file_name):
    f = open(log_file_name,"r")
    return f.readlines()## f.readlines() : reads until EOF(end of file), returns a list containing the lines


"""
function to parse "show ip interface brief" output text file
Returns a list of dictionaries, each dictionary pointing to an interface and its related info
"""
def parse_sh_ip_int_br(log_file_list):
    for line in log_file_list:
        line = re.sub("\s{2,}", " ", line)
        line = line.split(" ")

        if len(line)>5:
            interface=line[0]
            ip_address=line[1]
            protocol=line[5]
            ip=re.search(r"\d+.*",line[1]) ## regex to search for ip address in the given string
            if ip:
                interface_dict = {"Interface":interface, "IP Address":ip_address, "Protocol Status":protocol}
                list_of_interface_dict.append(interface_dict)

    #pprint(list_of_interface_dict)
    return list_of_interface_dict


"""
write a dictionary to a csv file
headers of csv file are the keys from the dictionary
cell values per row in the csv file are the values of the respective keys of each dictionary
"""
def write_to_csv(list_of_interface_dict, header, output_csv_file):

    with open(output_csv_file, mode='w', newline='\n') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        writer.writerows(list_of_interface_dict)



"""
When you execute a Python script, it is treated as the main and its __name__ attribute is set to "__main__".
If you import this script as a module in another script, the __name__ is set to the name of the script/module.
"""
if __name__ == "__main__":
    ## Inputs ##
    log_file_name = "device_logs.txt"

    ## Output ##
    output_csv_file = "interface_details.csv"

    ## Function Call to read text file and returns a list
    log_file_list = read_device_logs(log_file_name)

    ## function call to parse the device logs list
    list_of_interface_dict = parse_sh_ip_int_br(log_file_list)

    ## write to a csv file with the headers
    header = ['Interface', 'IP Address', 'Protocol Status']
    write_to_csv(list_of_interface_dict, header, output_csv_file)
