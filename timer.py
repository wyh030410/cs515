import time

class TimerError(Exception):
    pass

class Timer:
    def __init__(self):
        self._total_time = 0.0
        self._start_time = None
        self._running = False

    def start(self):
        if self._running:
            raise TimerError("timer is already running")
        self._start_time = time.time()
        self._running = True

    def stop(self):
        if not self._running:
            raise TimerError("timer is not running")
        elapsed = time.time() - self._start_time
        self._total_time += elapsed
        self._running = False
        self._start_time = None

    def total(self):
        if self._running:
            return self._total_time + (time.time() - self._start_time)
        return self._total_time

    def reset(self):
        self._total_time = 0.0
