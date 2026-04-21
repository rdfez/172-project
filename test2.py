import ev3_dc as ev3

with ev3.EV3(protocol=ev3.BLUETOOTH, host='00:16:53:4E:C1:14') as my_robot:
    print(my_robot)