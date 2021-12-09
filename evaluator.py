import subnet_values as sbv

# swt = 0
# pc = 1

# ip_address = "192.168.1.56"
# subnet_mask = "255.255.255.224"
# def_gateway = "192.168.1.32"

# switch_default_gateway = "192.168.1.32"
# switch_cidr_notation = 27
#192.168.1.32/27

def subnet_values(ip, cidr):
    if cidr < 8:
        result = sbv.networkClassZero(ip, cidr)
    elif cidr >= 8 and cidr <= 15:
        result = sbv.networkClassA(ip, cidr)
    elif cidr >= 16 and cidr <= 23:
        result = sbv.networkClassB(ip, cidr)
    elif cidr >= 24 and cidr <= 32:
        result = sbv.networkClassC(ip, cidr)
    elif cidr == 32:
        result = sbv.networkclass32(ip, cidr)

    return result

def ip_check(ip, defip, brdip):
    ip = list(int(i) for i in ip.split('.'))
    # print(ip)
    defip = list(int(i) for i in defip.split('.'))
    # print(defip)
    brdip = list(int(i) for i in brdip.split('.'))
    # print(brdip)
    if((ip[0] >= defip[0] and ip[0] <= brdip[0]) and (ip[1] >= defip[1] and ip[1] <= brdip[1]) and (ip[2] >= defip[2] and ip[2] <= brdip[2]) and (ip[3] >= defip[3] and ip[3] <= brdip[3])):
        return True
    else:
        return False

def evaluate_pc(swt,pc, ip, subnet, def_gate, sw_def, sw_cidr):
    switch_value = subnet_values(sw_def, sw_cidr)
    error_list = []
    if not ip_check(ip, switch_value["Default Gateway IP"], switch_value["Broadcast IP"]):
        error_list.append("IP Address in not in Valid Subnet Range")
    if def_gate != switch_value["Default Gateway IP"]:
        error_list.append("Default Gateway IP is Incorrect")
    if subnet != switch_value["Subnet Mask"]:
        error_list.append("Subnet Mask is Incorrect")
    if (ip_check(ip, switch_value["Default Gateway IP"], switch_value["Broadcast IP"]) and (def_gate == switch_value["Default Gateway IP"]) and (subnet == switch_value["Subnet Mask"])):
        error_list.append("OK")
    # print([swt, pc, error_list])
    return {
        "pc": [swt,pc,error_list]
        }

def evaluate_switch(swt, sw_def, sw_cidr):
    switch_value = subnet_values(sw_def, sw_cidr)
    error_list = []
    if sw_def != switch_value["Default Gateway IP"]:
        error_list.append("Switch Default Gateway IP is Incorrect")
    else:
        error_list.append("OK")
    # print([swt,error_list])
    return {
        "switch": [swt,error_list]
    }

# evaluate_pc(swt,pc,ip_address,subnet_mask,def_gateway,switch_default_gateway,switch_cidr_notation)
# evaluate_switch(swt,switch_default_gateway,switch_cidr_notation)

# def return_error(swt,pc,ip_address, subnet_mask, def_gateway, switch_default_gateway, switch_cidr_notation):
#     pc_error = [swt,pc,evaluate_pc(ip_address, subnet_mask, def_gateway, switch_default_gateway, switch_cidr_notation)]
#     # print(result_values)
#     sw_error = [swt,evaluate_switch(switch_default_gateway, switch_cidr_notation)]
#     # print(result_values)
#     return {
#         "switch_error": sw_error,
#         "pc_error": pc_error
#     }


