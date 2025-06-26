import os
import threading
import time


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class FileManager(metaclass=Singleton):

    def __init__(self, name_file, path_to_file):
        # File output
        self.name_file = name_file
        current_path = os.getcwd()
        self.path_to_file = path_to_file
        self.f = None

    def open(self):
        self.f = open(self.path_to_file, "w+")
        self.f.write("Log output for " + self.name_file)

    def write(self, to_write):
        self.f.write(f"{to_write}")

    def close(self):
        self.f.close()

    def log(msg):
        thread_name = threading.current_thread().name
        print(f"{thread_name}: {msg}")
