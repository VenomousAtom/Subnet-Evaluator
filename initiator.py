def initiate(pc_lim): #[2,3,4]
    li = []
    sw_li = []

    for switch in range(len(pc_lim)):
        li.append(' ')
        sw_li.append(' ')
        # print(li)

    for switch in range(len(pc_lim)):
        temp = []
        for details in range(2):
            temp.append(' ')
            sw_li[switch] = temp

    for switch in range(len(pc_lim)):
        temp = []
        for pc in range(pc_lim[switch]):
            temp.append(' ')
            li[switch] = temp
            # print(li)

    for switch in range(len(pc_lim)):
        for pc in range(pc_lim[switch]):
            temp = []
            for details in range(3):
                temp.append(' ')
                li[switch][pc] = temp
                # print(li)

    return {
        "switch":sw_li,
        "pc":li
        }

# PC : li[switch][pc][value number]
# SWITCH: sw_li[switch][value number]