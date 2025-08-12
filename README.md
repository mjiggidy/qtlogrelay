qtlogrelay
==========

`qtlogrelay` is a python module for the `QtLogRelayHandler` class.

`QtLogRelayHandler` is a `logging.Handler` which relays logged events from python's `logging` module 
to a PySide6 application via a `QtCore.Signal`.

Basic Usage
-----------

Create an instance of `QtLogRelayHandler` and install it as a log handler for your python logger.  
Then connect the `QtLogRelayHandler.logEventReceived` signal to an appropriate slot to do what you need to do in your PySide6 application.

```python
# Add a `QtLogRelayHandler` to this module's logger

qtloghandler = QtLogRelayHandler()
logging.getLogger(__name__).addHandler(qtloghandler)

# Now we can connect to that handler's signal to do stuff with the `logging.LogRecord` object

qtloghandler.logEventReceived.connect(
    processLogRecord,
    QtCore.Qt.ConnectionType.QueuedConnection
)
```

See `examples/basic.py` for a functioning example.
