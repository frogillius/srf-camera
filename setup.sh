# setup
sudo apt update
sudo apt install python3-pip libgtk2.0-dev pkg-install
pip3 install torch torchvision torchaudio
pip3 install opencv-python pandas requests serial pyserial
pip3 install matplotlib  # Optional, for visualization

# prep
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip3 install -r requirements.txt

