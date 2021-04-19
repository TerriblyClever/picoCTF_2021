nice_netcat_string= [112, 105, 99, 111, 67, 84, 70, 123, 103, 48, 48, 100, 95, 107, 49, 116, 116, 121, 33, 95, 110, 49, 99, 51, 95, 107, 49, 116, 116, 121, 33, 95, 53, 102, 98, 53, 101, 53, 49, 100, 125, 10] 
shop_challenge_string= [112, 105, 99, 111, 67, 84, 70, 123, 98, 52, 100, 95, 98, 114, 111, 103, 114, 97, 109, 109, 101, 114, 95, 98, 56, 100, 55, 50, 55, 49, 102, 125]

"""
flag = ""
for number in shop_challenge_string:
   flag += chr(number)
"""

flag = ""
for number in nice_netcat_string:
   flag += chr(number)

print(flag)