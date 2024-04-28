# Automation Script for Cisco Network Devices
This Python script automates the process of pushing and pulling commands to Cisco network devices such as routers, switches, and Firewall ASAs. It utilizes the **Netmiko library for SSH** connections and supports configuration management across multiple devices.

## Usage
- **Input Credentials:** The script prompts the user to enter their username, password, and enable the password (if applicable).
- **Configuration Files:** It reads configuration commands from **configuration.txt** and IP addresses from **IPs.txt**.
- **Device Connection:** It establishes SSH connections to each device using the provided credentials.
- **Configuration Deployment:** The script sends the configuration commands to each device using **Netmiko's send_config_set** method.
- **Logging:** Session logs are saved to **output.txt** for debugging purposes.
- **Error Handling:** In case of connection failures, the script logs the error message and continues with the next device.


## Compatibility
### Tested on:
- **Cisco IOS devices** :
Routers, switches, and Firewall ASAs

## Instructions
1. Clone the repository or download the script files.
2. Modify configuration.txt with your desired configuration commands.
3. Update IPs.txt with the IP addresses of your Cisco devices.
4. Run the script and follow the prompts to input your credentials.


## Notes
- Ensure that Netmiko and its dependencies are installed (pip install netmiko).
- Use this script responsibly and in accordance with your organization's network policies.
- Feel free to contribute or provide feedback to improve the script's functionality.
