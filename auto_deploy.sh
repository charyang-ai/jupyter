cd ~
sudo apt update
sudo apt install docker -y;
mkdir models
rm -rf jupyter
git clone https://github.com/charyang-ai/jupyter.git
cd jupyter
pip install -r requirements.txt
docker pull rocm/vllm:instinct_main
python3 pyDocker.py
