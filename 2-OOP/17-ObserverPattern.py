class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, obs):
        self._observers.append(obs)

    def notify(self, message):
        for obs in self._observers:
            obs.update(message)

class Observer:
    def update(self, message):
        print("Received:", message)
