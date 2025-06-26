
class SimError:
    def __init__(self, motive, message):
        self.motive = motive
        self.message = message

    def get_motive(self):
        return self.motive

    def get_message(self):
        return self.message

    def set_motive(self, motive):
        self.motive = motive

    def set_message(self, message):
        self.message = message

