import subprocess
from scapy.all import sniff, Raw


def get_interfaces():
    # Code phai viet lai de chay tren linux (fedora)
    result = subprocess.run(
        ["ip", "-o", "link", "show"], capture_output=True, text=True
    )
    output_lines = result.stdout.splitlines()
    interfaces = []
    for line in output_lines:
        parts = line.split(":")
        if len(parts) >= 2:
            iface = parts[1].strip()
            if iface != "lo":
                interfaces.append(iface)
    return interfaces


def packet_handler(packet):
    if packet.haslayer(Raw):
        print("Captured packet:")
        print(str(packet))


# Lay danh sach cac giao dien mang
interfaces = get_interfaces()
# In danh sach
print("Danh sach cac giao dien mang:")
for i, iface in enumerate(interfaces, start=1):
    print(f"{i}. {iface}")

# Lua chon giao dien mang tu mot nguoi dung
choice = int(input("Chon giao dien mang(nhap so): "))
selected_iface = interfaces[choice - 1]

# Bat goi tin tren giao dien mang duoc goi
sniff(iface=selected_iface, prn=packet_handler, filter="tcp")
