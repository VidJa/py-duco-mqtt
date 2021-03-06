from ducobox import DucoboxClient
from serial import Serial
from time import sleep
import logging

log = logging.getLogger(__name__)


class DucoboxSerialClient(DucoboxClient):

    def __init__(self, config):
        log.info("Initializing Duco serial client")
        super(DucoboxSerialClient, self).__init__(config)
        self._device = config["device"]
        self._baudrate = config["baudrate"]
        self.inter_char_delay = 0.001
        self.c = None

    def open(self):
        self.c = Serial(
            port=self._device,
            baudrate=self._baudrate,
            timeout=0.1)

    def close(self):
        self.c.close()

    def write(self, data):
        for d in data:
            self.c.write(d)
            self.c.flush()
            sleep(self.inter_char_delay)


    def read(self, timeout):
        if self.c.timeout != timeout:
            self.c.timeout = timeout
        return self.c.read(128)
