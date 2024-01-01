import wave, contextlib, math, time
import speech_recognition as sr
from moviepy.editor import AudioFileClip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
class Ui_MainWindow(object):
    """Main window GUI."""

    def __init__(self):
        """Initialisation function."""
        self.mp4_file_name = ""
        self.output_file = ""
        self.audio_file = "speech.wav"

    def setupUi(self, MainWindow):
        # Main window
        MainWindow.setObjectName("Extract Text from Video")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 161, 41))
        # Selected video file label
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.selected_video_label = QtWidgets.QLabel(self.centralwidget)
        self.selected_video_label.setGeometry(QtCore.QRect(230, 20, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.selected_video_label.setFont(font)
        self.selected_video_label.setFrameShape(QtWidgets.QFrame.Box)
        self.selected_video_label.setText("")
        self.selected_video_label.setObjectName("selected_video_label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 90, 161, 41))
        # Transcribed text box
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.transcribed_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.transcribed_text.setGeometry(QtCore.QRect(230, 320, 381, 431))
        self.transcribed_text.setObjectName("transcribed_text")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 280, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.transcribe_button = QtWidgets.QPushButton(self.centralwidget)
        self.transcribe_button.setEnabled(False)
        self.transcribe_button.setGeometry(QtCore.QRect(230, 150, 221, 81))
        # Transcribe button
        font = QtGui.QFont()
        font.setPointSize(14)
        self.transcribe_button.setFont(font)
        self.transcribe_button.setObjectName("transcribe_button")
        self.transcribe_button.clicked.connect(self.process_and_transcribe_audio)
        # progeress bar
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setGeometry(QtCore.QRect(230, 250, 381, 23))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.message_label = QtWidgets.QLabel(self.centralwidget)
        self.message_label.setGeometry(QtCore.QRect(0, 760, 651, 21))
        # Message label (for errors and warnings)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.message_label.setFont(font)
        self.message_label.setFrameShape(QtWidgets.QFrame.Box)
        self.message_label.setText("")
        self.message_label.setObjectName("message_label")
        self.output_file_name = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.output_file_name.setGeometry(QtCore.QRect(230, 90, 371, 41))
        # Output file name
        font = QtGui.QFont()
        font.setPointSize(14)
        self.output_file_name.setFont(font)
        self.output_file_name.setObjectName("output_file_name")
        # Menubar options
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_mp4_video_recording = QtWidgets.QAction(MainWindow)
        self.actionOpen_mp4_video_recording.setObjectName("actionOpen_mp4_video_recording")
        self.actionOpen_mp4_video_recording.triggered.connect(self.open_audio_file)
        self.actionAbout_vid2text = QtWidgets.QAction(MainWindow)
        self.actionAbout_vid2text.setObjectName("actionAbout_vid2text")
        self.actionAbout_vid2text.triggered.connect(self.show_about)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.triggered.connect(self.new_project)
        self.menuFile.addAction(self.actionOpen_mp4_video_recording)
        self.menuFile.addAction(self.actionNew)
        self.menuAbout.addAction(self.actionAbout_vid2text)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Extract Text from Video", "Extract Text from Video"))
        self.label.setText(_translate("MainWindow", "Selected video file:"))
        self.label_3.setText(_translate("MainWindow", "Output file name:"))
        self.label_5.setText(_translate("MainWindow", "Transcribed text:"))
        self.transcribe_button.setText(_translate("MainWindow", "Transcribe"))
        self.output_file_name.setPlaceholderText(_translate("MainWindow", "interview1.txt"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionOpen_mp4_video_recording.setText(_translate("MainWindow", "Open mp4 video recording"))
        self.actionAbout_vid2text.setText(_translate("MainWindow", "About the project"))
        self.actionNew.setText(_translate("MainWindow", "New"))

    def open_audio_file(self):
        file_name = QFileDialog.getOpenFileName()
        if file_name[0][-3:] == "mp4":
            self.transcribe_button.setEnabled(True)
            self.mp4_file_name = file_name[0]
            self.message_label.setText("")
            self.selected_video_label.setText(file_name[0])
        else:
            self.message_label.setText("Please select an *.mp4 file")
    
    def convert_mp4_to_wav(self):
        self.message_label.setText("Converting mp4 to audio (*.wav)...")
        self.convert_thread = convertVideoToAudioThread(self.mp4_file_name, self.audio_file)
        self.convert_thread.finished.connect(self.finished_converting)
        self.convert_thread.start()
    
    def get_audio_duration(self, audio_file):
        with contextlib.closing(wave.open(audio_file,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            return duration
    
    def transcribe_audio(self, audio_file):
        total_duration = self.get_audio_duration(audio_file) / 10
        total_duration = math.ceil(total_duration)
        self.td = total_duration
        if len(self.output_file_name.toPlainText()) > 0:
            self.output_file = self.output_file_name.toPlainText()
        else:
            self.output_file = "my_speech_file.txt"
        # Use thread to process in the background and avoid freezing the GUI
        self.thread = transcriptionThread(total_duration, audio_file, self.output_file)
        self.thread.finished.connect(self.finished_transcribing)
        self.thread.change_value.connect(self.set_progress_value)
        self.thread.start()
    
    def finished_converting(self):
        self.message_label.setText("Transcribing file...")
        self.transcribe_audio(self.audio_file)
    
    def finished_transcribing(self):
        self.progress_bar.setValue(100)
        self.transcribe_button.setEnabled(True)
        self.message_label.setText("")
        self.update_text_output()
    
    def set_progress_value(self, val):
        increment = int(math.floor(100*(float(val)/self.td)))
        self.progress_bar.setValue(increment)
    
    def process_and_transcribe_audio(self):
        self.transcribe_button.setEnabled(False)
        self.message_label.setText("Converting mp4 to audio (*.wav)...")
        self.convert_mp4_to_wav()
    
    def update_text_output(self):
        f = open(self.output_file, "r")
        self.transcribed_text.setText(f.read())
        f.close()
    
    def new_project(self):
        self.message_label.setText("")
        self.transcribed_text.setText("")
        self.selected_video_label.setText("")
        self.output_file_name.document().setPlainText("")
        self.progress_bar.setValue(0)

    def show_about(self):
        msg = QMessageBox()
        msg.setWindowTitle("About the project")
        msg.setText(" Created to extract text from videos.")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

class convertVideoToAudioThread(QThread):
    def __init__(self, mp4_file_name, audio_file):
        QThread.__init__(self)
        self.mp4_file_name = mp4_file_name
        self.audio_file = audio_file

    def __del__(self):
        self.wait()

    def run(self):
        audio_clip = AudioFileClip(self.mp4_file_name)
        audio_clip.write_audiofile(self.audio_file)

class transcriptionThread(QThread):
    change_value = pyqtSignal(int)
    def __init__(self, total_duration, audio_file, output_file):
        QThread.__init__(self)
        self.total_duration = total_duration
        self.audio_file = audio_file
        self.output_file = output_file

    def __del__(self):
        self.wait()

    def run(self):
        r = sr.Recognizer()
        for i in range(0, self.total_duration):
            try:
                with sr.AudioFile(self.audio_file) as source:
                    audio = r.record(source, offset=i*10, duration=10)
                    f = open(self.output_file, "a")
                    f.write(r.recognize_google(audio))
                    f.write(" ")
                self.change_value.emit(i)
            except:
                print("Unknown word detected...")
                continue
            f.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())