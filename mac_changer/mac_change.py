import subprocess
import optparse
import re

def get_arg():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="change the interface address")
    parser.add_option("-m", "--mac", dest="new_mac", help="change the mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please enter interface see --help for more")
    if not options.new_mac:
        parser.error("[-] please enter new mac see --help for more")
    return options

def mac_changer(interface, new_mac):
    print("[+] change the mac " + str(interface) + " to " + str(new_mac))
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def mac_read(interface):
        result = subprocess.check_output(["ifconfig", interface])
        result_regex = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result)
        if result_regex:
            return result_regex.group(0)
        else:
            print("[-] no mac address found")


options = get_arg()
current_mac = mac_read(options.interface)
print("current mac" + str(current_mac))

mac_changer(options.interface, options.new_mac)
current_mac = mac_read(options.interface)
if current_mac == options.new_mac:
    print("[+] mac was changed successfully to " + current_mac)
else:
    print("[-] mac was not changed")