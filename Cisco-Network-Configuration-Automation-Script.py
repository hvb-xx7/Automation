# Automation Script for Cisco Network Devices
# Date: 23-04-2024
# Author: Hichem belguendouz
# Github : https://github.com/hvb-xx7/Automation
# Tested on: All Cisco Network devices such routers, switches, Firewall ASAs .


from netmiko import ConnectHandler
import getpass


username = input("Enter your username: ") # Prompt to enter the UserName
password = getpass.getpass("Enter your password: ") # Prompt to enter the Password
enable_password = getpass.getpass("Enter your enable password (if applicable): ")  # Prompt for the enable password

#Read the Configuration from the file
with open('configuration.txt') as f:
    commands_list = f.read().splitlines()

 
# Read The  IP Addresses
with open('IPs.txt') as f:
    devices_list = f.read().splitlines()

    
    
for ip_address in devices_list:
    print('Connecting to device:', ip_address)
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address,
        'username': username,
        'password': password,
        'secret': enable_password,  # Add the enable password to the device dictionary
        'global_delay_factor': 2,  # Add a delay between commands
        'session_log': 'output.txt',  # Enable session logging for debugging
    }

    try:
    # Establishes a connection to a network device using the ConnectHandler class from the Netmiko library.
        net_connect = ConnectHandler(**ios_device)
        
    # Enter privileged mode 
        net_connect.enable()
     # send_config_set is a method provided by Netmiko to send a list of configuration commands (commands_list) to the device.
        output = net_connect.send_config_set(commands_list)
     # print  the response received from the device 
        print(output)
     # closes the connection to the network device
        net_connect.disconnect()
        
    except Exception as e:
    # print an error message if there was  connection failure
        print(f"Failed to connect to {ip_address}: {str(e)}")