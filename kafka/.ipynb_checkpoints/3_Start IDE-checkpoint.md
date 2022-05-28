# Jupyter Lab - Python IDE

Prerequsites:
- Started deploy-server

export WORKDIR='/root/PySpark/workspace/3_Kafka'
cd $WORKDIR

#########################################################################################
# 1. (deploy-server) Create python venv with dependencies
#########################################################################################

sudo apt-get install -y python3-venv python3-pip
python3 -m venv venv --copies
source venv/bin/activate

cat <<EOF | tee requirements.txt
jupyterlab
kafka-python
psycopg2
EOF

pip install --upgrade pip
pip install -r requirements.txt 


#########################################################################################
# 2. (deploy-server) Start jupyter lab
#########################################################################################

jupyter lab


#########################################################################################
# 3. (PC) Open jupyter lab
#########################################################################################

## Forward a port in vscode
8888

or 
Ctrl + Shift + P, type "Forward a port"

## Open webbrowser
http://localhost:8888/xxxx