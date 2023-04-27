# Ping and Traceroute Script

This Python script pings a list of IP addresses every 5 seconds and performs a traceroute to display the path to each IP. 
The output is shown in a table format with a timestamp, IP address, status (OK, Timeout, or Error), and the path.

## Prerequisites

- Python 3.6 or later
- pip (included with most Python installations)

## Setting up the environment

1. **Create a virtual environment**: To create a virtual environment, open a terminal or command prompt, navigate to the project directory, and run the following command:

```
    python -m venv venv
```
2. **Activate the virtual environment**: Activate the virtual environment using the appropriate command for your platform:

- Windows:
```
    venv\Scripts\activate
```
- macOS \ Linux:
```
    source venv/bin/activate
```
When the virtual environment is activated, you should see the environment name in your command prompt, like this: (venv).

3. **Install requirements**: While the virtual environment is activated, install the required dependencies using the following command:

```
    pip install -r requirements.txt
```

## Running the script

To run the script, simply execute the following command while your virtual environment is activated:

```
    python ping.py
```
The script will run indefinitely, pinging the specified IP addresses and displaying the traceroute results every 5 seconds. To stop the script, press Ctrl+C.


## Customising the IP addresses

To ping and traceroute different IP addresses, modify the ip_addresses list in the ping.py script with your desired IP addresses. For example:

```
    ip_addresses = ["8.8.4.4", "8.8.8.8"]
```