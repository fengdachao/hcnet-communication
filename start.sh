#!/bin/bash

cd /home/vfes/hcnet-communication/
gnome-terminal --window-with-profile=hold-window -- python3 /home/vfes/hcnet-communication/v1.py
#python3 v1.py
# i=1;  
# for (( ; ; ))  
# do  
# python3 v1.py
# sleep 2
# echo Current Number: $((i++))  
# done

# function check_ipaddr
# {
#   # Here we look for an IP(v4|v6) address when doing ip addr
#   # Note we're filtering out 127.0.0.1 and ::1/128 which are the "localhost" ip addresses
#   # I'm also removing fe80: which is the "link local" prefix

#   ip addr | \
#   grep -v 127.0.0.1 | \
#   grep -v '::1/128' | \
#   grep -v 'inet6 fe80:' | \
#   grep -E "inet [[:digit:]]+\.[[:digit:]]+\.[[:digit:]]+\.[[:digit:]]+|inet6" | \
#   wc -l
# }
# function check_google
# {
#   netcat -z -w 5 8.8.8.8 53 && echo 1 || echo 0
# }

# until [ `check_ipaddr` -gt 7 ]; do
#   sleep 2
# done



# until [ `check_google` -eq 1 ]; do
#   sleep 2
# done

# echo running python3
# python3 v1.py
