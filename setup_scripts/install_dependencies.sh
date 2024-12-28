# Setup script for use on debian
echo '### setup basic linux requirements (apt) ###'
apt update
apt-get install python3 python3-venv unzip curl postgresql-client libpq-dev -y --fix-missing

# Setup Python venv
echo '### setup Python venv ###'
python3 -m venv .venv
./.venv/bin/python3 -m pip install -r requirements.txt
