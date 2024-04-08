import platform
import psutil
import os
import socket
import time

def get_os_info():
    # OS Name and Version
    os_name = platform.system()
    os_version = platform.release()
    
    # Processor Information
    processor_info = platform.processor()
    
    # Memory (GB)
    memory_info = round(psutil.virtual_memory().total / (1024 ** 3), 2)
    
    # Available Disk Space (GB)
    disk_info = round(psutil.disk_usage('/').free / (1024 ** 3), 2)
    
    # Current User
    current_user = platform.node()
    
    # IP Address
    ip_address = socket.gethostbyname(socket.gethostname())
    
    # System Uptime (in seconds)
    uptime = round(time.time() - psutil.boot_time())
    
    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # Running Processes (PID, name, memory usage)
    processes = []
    for process in psutil.process_iter():
        try:
            pinfo = process.as_dict(attrs=['pid', 'name', 'memory_info'])
            processes.append(pinfo)
        except psutil.NoSuchProcess:
            pass
    
    # Disk Partitions (device name, mount point)
    disk_partitions = psutil.disk_partitions()
    
    # System Architecture
    system_architecture = platform.architecture()[0]
    
    # Environment Variables
    env_variables = os.environ
    
    return (os_name, os_version, processor_info, memory_info, disk_info, current_user,
            ip_address, uptime, cpu_usage, processes, disk_partitions, system_architecture, env_variables)

def main():
    os_name, os_version, processor_info, memory_info, disk_info, current_user, ip_address, uptime, cpu_usage, processes, disk_partitions, system_architecture, env_variables = get_os_info()
    
    print("OS Name:", os_name)
    print("OS Version:", os_version)
    print("Processor Information:", processor_info)
    print("Memory (GB):", memory_info)
    print("Available Disk Space (GB):", disk_info)
    print("Current User:", current_user)
    print("IP Address:", ip_address)
    print("System Uptime (seconds):", uptime)
    print("CPU Usage (%):", cpu_usage)
    print("Running Processes:")
    for process in processes:
        print(f"PID: {process['pid']}, Name: {process['name']}, Memory Usage: {process['memory_info'].rss / (1024 ** 2)} MB")
    print("Disk Partitions:")
    for partition in disk_partitions:
        print(f"Device: {partition.device}, Mount Point: {partition.mountpoint}")
    print("System Architecture:", system_architecture)
    print("Environment Variables:")
    for key, value in env_variables.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
