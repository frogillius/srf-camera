# setup
sudo apt update
sudo apt install python3-pip
pip3 install torch torchvision torchaudio
pip3 install opencv-python pandas requests
pip3 install matplotlib  # Optional, for visualization

# prep
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip3 install -r requirements.txt
