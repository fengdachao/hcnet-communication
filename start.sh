echo 'start python service'

python3 ./v1.py
curl remote-server:3001/

echo 'end python service'
