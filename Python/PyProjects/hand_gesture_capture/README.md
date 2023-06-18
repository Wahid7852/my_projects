Python: (3.8.5)
  Anaconda Distribution: To download click [here](https://www.anaconda.com/products/individual).
  conda create --name gest python=3.8.5
  conda activate gest
  pip install -r requirements.txt
  conda install PyAudio pywin32
  pip install opencv-python==4.5.5.64
  set protocol_buffers_python_implementation=python
  python Gesture_Controller.py
