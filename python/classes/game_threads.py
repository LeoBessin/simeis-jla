import threading


class GameThread():
    def __init__(self):
        self.threads = []

    def start_threads(self):
        for thread in self.threads:
            thread.start()

    def add_thread(self, thread_dict):
        t = threading.Thread(target=thread_dict["target"], args=(thread_dict["delay"],))
        self.threads.append(t)
