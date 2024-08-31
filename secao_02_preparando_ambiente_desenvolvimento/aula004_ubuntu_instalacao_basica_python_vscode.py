# Instalar os pacotes abaixo: 
# (https://gist.github.com/luizomf/688c8a48fe007829c120818138ac2317)

"""
sudo apt update -y
sudo apt upgrade -y
sudo apt install git curl build-essential -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update -y
sudo apt install gcc make default-libmysqlclient-dev libssl-dev -y
sudo apt install python3.10-full python3.10-dev -y
sudo apt install python3.10-venv -y
sudo apt install -y zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
sudo apt update -y
sudo apt upgrade -y
"""


# Criar ambiente virtual dentro da pasta do projeto:

"""
python3 -m venv venv (2º 'venv' é o: nome-ambiente-virtual)
source venv/bin/activate
python -m pip install pip --upgrade (Atualiza o 'pip' do python. Instalador de pacotes do python)
deactivate (Fecha o ambiente virtual)
"""


# Testandoo python:

# .venv/bin/activate
# python arquivo.py
 
print(1 + 1)