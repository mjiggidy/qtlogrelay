
import logging, sys
from PySide6 import QtCore, QtWidgets
from qtlogrelay import QtLogRelayHandler

MESSAGE_DURATION_MSEC:int = 500
"""How long to display the last log message (msecs)"""

class DemoWindow(QtWidgets.QWidget):
	"""Window to demonstrate basic `QtLogRelayHandler` signal usage"""

	def __init__(self):

		super().__init__()

		self.setLayout(QtWidgets.QVBoxLayout())

		# Create a QPushButton that emits a typical python `logging.LogRecord`
		self.btn_log = QtWidgets.QPushButton("Do Me A Log")
		self.btn_log.clicked.connect(lambda: logging.getLogger(__name__).info("Button clicked"))
		self.layout().addWidget(self.btn_log)
		
		# Create a label to show the latest log message
		self.lbl_lastevent = QtWidgets.QLabel()
		self.lbl_lastevent.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
		self.layout().addWidget(self.lbl_lastevent)

		# Create a timer to clear the last log message
		self.timer_clear_lbl = QtCore.QTimer(interval=MESSAGE_DURATION_MSEC)
		self.timer_clear_lbl.timeout.connect(self.lbl_lastevent.clear)
		
		# Add a `QtLogRelayHandler` to this module's logger
		self.qtloghandler = QtLogRelayHandler()
		logging.getLogger(__name__).addHandler(self.qtloghandler)

		# Now we can connect to that handler's signal to show it in the label
		self.qtloghandler.logEventReceived.connect(
			self.showLoggedEventMessage,
			QtCore.Qt.ConnectionType.QueuedConnection
		)

	@QtCore.Slot(logging.LogRecord)
	def showLoggedEventMessage(self, record:logging.LogRecord):
		"""Briefly show the log message in the label"""

		self.lbl_lastevent.setText(record.getMessage())
		self.timer_clear_lbl.start()

def main() -> int:

	logging.basicConfig(level=logging.NOTSET)

	app = QtWidgets.QApplication()
	
	wnd_main = DemoWindow()
	wnd_main.show()
	
	return app.exec()

if __name__ == "__main__":
	sys.exit(main())