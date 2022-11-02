import subprocess
import sys
from prettytable import PrettyTable

ip_arg = input("Your IP (192.168.0.135): ")
ip_parts = ip_arg.split('.')
ip = ip_parts[0] +"." + ip_parts[1] + "." + ip_parts[2] + "."
start_from = input("Start From (2): ")
end_at = input("End At (20): ")
sudo_password = input("Your Sudo Password: (s3cUr3): ")
print("***************************")
print("Ip: " , ip_arg)
print("start_from: " , start_from)
print("end_at: " , end_at)
print("***************************")

result = []
result_table = PrettyTable(['IP', 'Mac'])

for i in range(int(start_from), int(end_at)+1):
    print("Trying: " + str(ip) + str(i))

    command = 'nmap -sU -p 161 -T4 ' + str(ip) + str(i)
    command = command.split()

    cmd1 = subprocess.Popen(['echo',sudo_password], stdout=subprocess.PIPE)
    cmd2 = subprocess.Popen(['sudo','-S'] + command, stdin=cmd1.stdout, stdout=subprocess.PIPE)

    output = cmd2.stdout.read().decode() 

    for line in output.splitlines():
        if "MAC Address" in line:
            only_mac = line.split("MAC Address:")[1]
            print("Mac Found: " + str(only_mac))
            current_ip = str(ip) + str(i)
            result_table.add_row([current_ip, only_mac])

print("\r\n")
print(result_table)
 