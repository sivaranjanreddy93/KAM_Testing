import threading
import ostart
import time


class SerialMonitor(threading.Thread):
    SYNC_BYTES = b'\x90\xeb'

    def __init__(self, device='/dev/ttyUSB0', baudrate=19200, timeout=5):
        print("Initializing Serial Monitor")
        self._running = False
        self._name = 'SerialMonitorThread-{}'.format(device)
        self._device = serial.Serial(device, baudrate=baudrate, timeout=timeout)
        self._write_lock = threading.Lock()

        super().__init__(name=self._name)

    def write(self, user_input, encode=False, terminator=None):
        print("Locking for CMD Write...")
        self._write_lock.acquire()
        tx = user_input + terminator if terminator else user_input
        print(f"Writing CMD to device: {tx}")
        self._device.write(tx.encode() if encode else tx)
        print("CMD Written...")
        self._write_lock.release()
        print("CMD Write Lock Released...")

    def stop(self):
        self._running = False
        print('stop thread: ' + threading.current_thread())
        self.join()

    def run(self):
        print('starting thread: ' + threading.current_thread())
        self._running = True
        try:
            while self._running:
                self._device.reset_input_buffer()
                self._device.read_until(self.SYNC_BYTES)
                ser_bytes = self._device.read(35)
                print(f'\r{ser_bytes}', end='', flush=True)
                time.sleep(0.25)
        finally:
            self._device.close()