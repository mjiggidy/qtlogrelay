import logging
from PySide6 import QtCore

class QtLogRelayHandler(logging.Handler):
	"""
	A python `logging` handler to emit a Qt signal when a new event is logged.
	"""

	class _RelaySignals(QtCore.QObject):
		"""QtObject for relay signals"""

		logEventReceived = QtCore.Signal(logging.LogRecord)
		"""A new log record has been received"""


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self._signals = self._RelaySignals()
		self.logEventReceived = self._signals.logEventReceived
		"""A new log record has been received"""
	
	def emit(self, record:logging.LogRecord):
		"""Do a log real nice"""

		self.logEventReceived.emit(record)

		# NOTE: Investigate queued connection when connecting to slot:
		# self.logEventReceived.connect(slot, QtCore.Qt.QueuedConnection)