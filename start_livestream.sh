#! /bin/sh
sudo service motion restart
sudo service motion start
python3 camera-livestream/webserver.py &
python camera-livestream/stepper_con.py 192.168.168.101 &
node camera-livestream/websocket-controls

#  xterm -title "python" -hold -e python.sh &
#  xterm -title "brower" -hold -e brower.sh