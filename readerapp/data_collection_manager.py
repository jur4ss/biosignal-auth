from emg_driver.emg_shield import EMGShieldController
from emg_driver.data_collection import DataCollectionThread

class DataCollectionManager(object):
    def __init__(self, settings):
        self.thread = None
        self.controller = None
        self.current_token = None
        self.settings = settings

    def start_collection(self, values, interpreted_values, token):
        self.__delete_thread()
        self.controller = EMGShieldController()
        self.current_token = token
        self.thread = DataCollectionThread(self.controller, values, interpreted_values, self.settings)
        self.thread.daemon = True
        self.thread.start()

    def stop_collection(self):
        self.controller = None
        self.__delete_thread()
        token = self.current_token
        self.current_token = None
        return token

    def __delete_thread(self):
        if self.thread is None:
            return
        self.thread.stop()
        self.thread.join()
        self.thread = None
