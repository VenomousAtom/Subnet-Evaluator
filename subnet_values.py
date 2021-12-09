# For Finding all the Different Values from Subnetting According to Provided Data

# cidrA = 9
# ipA = "91.18.7.6"
# cidrB = 17
# ipB = "129.35.67.46"
# cidrC = 25
# ipC = "192.168.67.46"

def networkClassZero(ip, cidr):
    # print("INPUT:", ip , "/", cidr)
    # print("IP Address:", ip, "\n")
    ip_addr = ip.split('.')
    sub_mask_bin = ['0', '00000000', '00000000', '00000000']
    temp = []
    subnetting_address = cidr % 8
    for i in range(8):
        if (i+1) <= subnetting_address:
            temp.append('1')
        else:
            temp.append('0')
    # print("temp:", temp)
    tempo_bin = ''.join(temp)
    # print("Tempo_bin:", tempo_bin)
    sub_mask_bin[0] = tempo_bin
    subnet_mask_bin = '.'.join(sub_mask_bin)
    # print("--> sub_mask_bin[0]:", sub_mask_bin[1], " --> subnet_mask_bin:", subnet_mask_bin)
    sub_mask_str = []
    for subs in sub_mask_bin:
        sub_mask_str.append(int(subs, 2))
    sub_mask_dec = []
    for subs in sub_mask_str:
        sub_mask_dec.append(str(subs))
    subnet_mask_dec = '.'.join(sub_mask_dec)
    # print("--> sub_mask_dec[0]:", sub_mask_dec[1], " --> subnet_mask_dec:", subnet_mask_dec, "\n")
    power = 8 - subnetting_address
    magic_number = 2 ** power
    # print("-- magic_number:", magic_number, "--")
    subnet_ranges = []
    for i in range(255):
        network_address = magic_number * i
        broadcast_address = (magic_number * (i+1)) - 1
        if broadcast_address <= 255:
            # print(">> network_address:", ip_addr[0] + "." + str(network_address) + ".0.0", "   >> [USABLE HOST RANGE] :", ip_addr[0] + "." + str(
            #     network_address) + ".0.1", "-", ip_addr[0] + "." + str(broadcast_address) + ".255.254", "   >> broadcast_address:", ip_addr[0] + "." + str(broadcast_address) + ".255.255")
            subnet_ranges.append([str(network_address) + ".0.0.0", str(network_address) +
                                  ".0.0.1",  str(broadcast_address) + ".255.255.254",  str(broadcast_address) + ".255.255.255"])

            if int(ip_addr[0]) >= network_address:
                if int(ip_addr[0]) <= broadcast_address and int(ip_addr[1]) <= 255 and int(ip_addr[2]) <= 255 and int(ip_addr[3]) <= 255:
                    net_ad = str(network_address) + ".0.0.0"
                    broad_ad = str(broadcast_address) + ".255.255.255"
                    ad_ran = str(network_address) + ".0.0.1" + " - " + str(broadcast_address) + ".255.255.254"
        else:
            break
    # print("\nEntered IP", ip, "in \n>> network_address:", net_ad, "   >> [USABLE HOST RANGE] :", ad_ran, "   >> broadcast_address:", broad_ad)
    # print(subnet_ranges)
    values = {
        "IP Address": ip,
        "Default Gateway IP": net_ad,
        "Host IP Range": ad_ran,
        "Broadcast IP": broad_ad,
        "Subnet Mask Binary": subnet_mask_bin,
        "Subnet Mask": subnet_mask_dec,
        "Cidr": cidr,
        "Subnet Ranges": subnet_ranges,
        "IP Network Class": ""
    }
    return values

def networkClassA(ip, cidr):
    # print("INPUT:", ip , "/", cidr)
    # print("IP Address:", ip, "\n")
    ip_addr = ip.split('.')
    sub_mask_bin = ['11111111', '00000000', '00000000', '00000000']
    temp = []
    subnetting_address = cidr % 8
    for i in range(8):
        if (i+1) <= subnetting_address:
            temp.append('1')
        else:
            temp.append('0')
    # print("temp:", temp)
    tempo_bin = ''.join(temp)
    # print("Tempo_bin:", tempo_bin)
    sub_mask_bin[1] = tempo_bin
    subnet_mask_bin = '.'.join(sub_mask_bin)
    # print("--> sub_mask_bin[0]:", sub_mask_bin[1], " --> subnet_mask_bin:", subnet_mask_bin)
    sub_mask_str = []
    for subs in sub_mask_bin:
        sub_mask_str.append(int(subs, 2))
    sub_mask_dec = []
    for subs in sub_mask_str:
        sub_mask_dec.append(str(subs))
    subnet_mask_dec = '.'.join(sub_mask_dec)
    # print("--> sub_mask_dec[0]:", sub_mask_dec[1], " --> subnet_mask_dec:", subnet_mask_dec, "\n")
    power = 8 - subnetting_address
    magic_number = 2 ** power
    # print("-- magic_number:", magic_number, "--")
    subnet_ranges = []
    for i in range(255):
        network_address = magic_number * i
        broadcast_address = (magic_number * (i+1)) -1
        if broadcast_address <= 255:
            # print(">> network_address:", ip_addr[0] + "." + str(network_address) + ".0.0", "   >> [USABLE HOST RANGE] :", ip_addr[0] + "." + str(
            #     network_address) + ".0.1", "-", ip_addr[0] + "." + str(broadcast_address) + ".255.254", "   >> broadcast_address:", ip_addr[0] + "." + str(broadcast_address) + ".255.255")
            subnet_ranges.append([ip_addr[0] + "." + str(network_address) + ".0.0", ip_addr[0] + "." + str(network_address) +
                                ".0.1", ip_addr[0] + "." + str(broadcast_address) + ".255.254", ip_addr[0] + "." + str(broadcast_address) + ".255.255"])
            
            if int(ip_addr[1]) >= network_address:
                if int(ip_addr[1]) <= broadcast_address and int(ip_addr[2]) <= 255  and int(ip_addr[3]) <= 255:
                    net_ad = ip_addr[0] + "." + str(network_address) + ".0.0"
                    broad_ad = ip_addr[0] + "." + str(broadcast_address) + ".255.255"
                    ad_ran = ip_addr[0] + "." + str(network_address) + ".0.1" + " - " + ip_addr[0] + "." + str(broadcast_address) + ".255.254"
        else:
            break
    # print("\nEntered IP", ip, "in \n>> network_address:", net_ad, "   >> [USABLE HOST RANGE] :", ad_ran, "   >> broadcast_address:", broad_ad)
    # print(subnet_ranges)
    values = {
        "IP Address": ip,
        "Default Gateway IP": net_ad,
        "Default Gateway IP": net_ad,
        "Default Gateway IP": net_ad,
        "Host IP Range": ad_ran,
        "Broadcast IP": broad_ad,
        "Subnet Mask Binary": subnet_mask_bin,
        "Subnet Mask": subnet_mask_dec,
        "Cidr": cidr,
        "Subnet Ranges": subnet_ranges,
        "IP Network Class": "A"
    }
    return values

def networkClassB(ip, cidr):
    # print("INPUT:", ip, "/", cidr)
    # print("IP Address:", ip, "\n")
    ip_addr = ip.split('.')
    sub_mask_bin = ['11111111', '11111111', '00000000', '00000000']
    temp = []
    subnetting_address = cidr % 8
    for i in range(8):
        if (i+1) <= subnetting_address:
            temp.append('1')
        else:
            temp.append('0')
    # print("temp:", temp)
    tempo_bin = ''.join(temp)
    # print("Tempo_bin:", tempo_bin)
    sub_mask_bin[2] = tempo_bin
    subnet_mask_bin = '.'.join(sub_mask_bin)
    # print("--> sub_mask_bin[0]:", sub_mask_bin[2],
    #     " --> subnet_mask_bin:", subnet_mask_bin)

    sub_mask_str = []
    for subs in sub_mask_bin:
        sub_mask_str.append(int(subs, 2))
    sub_mask_dec = []
    for subs in sub_mask_str:
        sub_mask_dec.append(str(subs))

    subnet_mask_dec = '.'.join(sub_mask_dec)
    # print("--> sub_mask_dec[0]:", sub_mask_dec[2],
    #     " --> subnet_mask_dec:", subnet_mask_dec, "\n")

    power = 8 - subnetting_address
    magic_number = 2 ** power
    # print("-- magic_number:", magic_number, "--")
    subnet_ranges = []
    for i in range(255):
        network_address = magic_number * i
        broadcast_address = (magic_number * (i+1)) - 1
        if broadcast_address <= 255:
            # print(">> network_address:", ip_addr[0] + "." + ip_addr[1] + "." + str(network_address) + ".0", "   >> [USABLE HOST RANGE] :", ip_addr[0] + "." + ip_addr[1] + "." + str(
            #     network_address) + ".1", "-", ip_addr[0] + "." + ip_addr[1] + "." + str(broadcast_address) + ".254", "   >> broadcast_address:", ip_addr[0] + "." + ip_addr[1] + "." + str(broadcast_address) + ".255")
            subnet_ranges.append([ip_addr[0] + "." + ip_addr[1] + "." + str(network_address) + ".0", ip_addr[0] + "." + ip_addr[1] + "." + str(network_address) +
                                ".1", ip_addr[0] + "." + ip_addr[1] + "." + str(broadcast_address) + ".254", ip_addr[0] + "." + ip_addr[1] + "." + str(broadcast_address) + ".255"])

            if int(ip_addr[2]) >= network_address:
                if int(ip_addr[2]) <= broadcast_address and int(ip_addr[3]) <= 255:
                    net_ad = ip_addr[0] + "." + ip_addr[1] + \
                        "." + str(network_address) + ".0"
                    broad_ad = ip_addr[0] + "." + ip_addr[1] + "." + \
                        str(broadcast_address) + ".255"
                    ad_ran = ip_addr[0] + "." + ip_addr[1] + "." + str(network_address) + ".1" + \
                        " - " + ip_addr[0] + "." + ip_addr[1] + "." + str(broadcast_address) + ".254"
        else:
            break

    # print("\nEntered IP", ip, "in \n>> network_address:", net_ad,
    #     "   >> [USABLE HOST RANGE] :", ad_ran, "   >> broadcast_address:", broad_ad)
    # print(subnet_ranges)
    values = {
        "IP Address": ip,
        "Default Gateway IP": net_ad,
        "Host IP Range": ad_ran,
        "Broadcast IP": broad_ad,
        "Subnet Mask Binary": subnet_mask_bin,
        "Subnet Mask": subnet_mask_dec,
        "Cidr": cidr,
        "Subnet Ranges": subnet_ranges,
        "IP Network Class": "B"
    }
    return values

def networkClassC(ip, cidr):
    # print("INPUT:", ip, "/", cidr)
    # print("IP Address:", ip, "\n")
    ip_addr = ip.split('.')
    sub_mask_bin = ['11111111', '11111111', '11111111', '00000000']
    temp = []
    subnetting_address = cidr % 8
    for i in range(8):
        if (i+1) <= subnetting_address:
            temp.append('1')
        else:
            temp.append('0')
    # print("temp:", temp)
    tempo_bin = ''.join(temp)
    # print("Tempo_bin:", tempo_bin)
    sub_mask_bin[3] = tempo_bin
    subnet_mask_bin = '.'.join(sub_mask_bin)
    # print("--> sub_mask_bin[0]:", sub_mask_bin[3],
    #     " --> subnet_mask_bin:", subnet_mask_bin)

    sub_mask_str = []
    for subs in sub_mask_bin:
        sub_mask_str.append(int(subs, 2))
    sub_mask_dec = []
    for subs in sub_mask_str:
        sub_mask_dec.append(str(subs))

    subnet_mask_dec = '.'.join(sub_mask_dec)
    # print("--> sub_mask_dec[0]:", sub_mask_dec[3],
    #     " --> subnet_mask_dec:", subnet_mask_dec, "\n")

    power = 8 - subnetting_address
    magic_number = 2 ** power
    # print("-- magic_number:", magic_number, "--")
    subnet_ranges = []
    for i in range(255):
        network_address = magic_number * i
        broadcast_address = (magic_number * (i+1)) - 1
        if broadcast_address <= 255:
            # print(">> network_address:", ip_addr[0] + "." + ip_addr[1] + "." + ip_addr[2] + "." + str(network_address), "   >> [USABLE HOST RANGE] :", ip_addr[0] + "." + ip_addr[1] + "." + ip_addr[2] + "." + str(
            #     network_address), "-", ip_addr[0] + "." + ip_addr[1] + "." + ip_addr[2] + "." + str(broadcast_address), "   >> broadcast_address:", ip_addr[0] + "." + ip_addr[1] + "." + ip_addr[2] + "." + str(broadcast_address))
            subnet_ranges.append([ip_addr[0] + "." + ip_addr[1] + "." + ip_addr[2] + "." + str(network_address), ip_addr[0] + "." + ip_addr[1] + "." + ip_addr[2] + "." + str(
                network_address + 1), ip_addr[0] + "." + ip_addr[1] + "." + ip_addr[2] + "." + str(broadcast_address - 1), ip_addr[0] + "." + ip_addr[1] + "." + ip_addr[2] + "." + str(broadcast_address)])

            if int(ip_addr[3]) >= network_address:
                if int(ip_addr[3]) <= broadcast_address:
                    net_ad = ip_addr[0] + "." + ip_addr[1] + "." + ip_addr[2] + "." + \
                        str(network_address)
                    broad_ad = ip_addr[0] + "." + ip_addr[1] + "." + ip_addr[2] + "." + \
                        str(broadcast_address)
                    ad_ran = ip_addr[0] + "." + ip_addr[1] + "." + ip_addr[2] + "." + str(network_address) + \
                        " - " + ip_addr[0] + "." + ip_addr[1] + "." + \
                        ip_addr[2] + "." + str(broadcast_address)
        else:
            break

    # print("\nEntered IP", ip, "in \n>> network_address:", net_ad,
    #     "   >> [USABLE HOST RANGE] :", ad_ran, "   >> broadcast_address:", broad_ad)
    # print(subnet_ranges)
    values = {
        "IP Address": ip,
        "Default Gateway IP": net_ad,
        "Host IP Range": ad_ran,
        "Broadcast IP": broad_ad,
        "Subnet Mask Binary": subnet_mask_bin,
        "Subnet Mask": subnet_mask_dec,
        "Cidr": cidr,
        "Subnet Ranges": subnet_ranges,
        "IP Network Class": "C"
    }
    return values

def networkclass32(ip, cidr):
    values = {
        "IP Address": ip,
        "Default Gateway IP": ip,
        "Host IP Range": "-",
        "Broadcast IP": ip,
        "Subnet Mask Binary": "11111111.11111111.11111111.11111111",
        "Subnet Mask": "255.255.255.255",
        "Cidr": cidr,
        "Subnet Ranges": ["-", "-", "-", "-"],
        "IP Network Class": "C"
    }
# print("\n")
# print(networkClassA(ipA, cidrA))
# print("\n")
# print(networkClassB(ipB, cidrB))
# print("\n")
# print(networkClassC(ipC, cidrC))

# ip_addr = input("Enter IP Address: ")
# ip = (ip_addr.split('.'))
# print(ip)
# ip_bin = []
# for vals in ip:
#     ip_bin.append(format(int(vals),'08b'))
# print(ip_bin)
# ip_bin_final = '.'.join(ip_bin)
# print(ip_bin_final)
# # print("Binary of number ",number," is: ",(format(number,'08b')))
