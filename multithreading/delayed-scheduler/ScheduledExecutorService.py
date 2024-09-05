import threading
import time
from queue import PriorityQueue
from concurrent.futures import Future


class ScheduledExecutorService:
    def __init__(self, pool_size):
        self.pool_size = pool_size
        self.tasks = PriorityQueue()
        self.stop_event = threading.Event()
        self.workers = [threading.Thread(target=self._worker) for _ in range(pool_size)]
        for worker in self.workers:
            worker.start()

    def _worker(self):
        while not self.stop_event.is_set():
            try:
                execute_at, task, future = self.tasks.get(timeout=1)
                current_time = time.time()
                if current_time < execute_at:
                    time.sleep(execute_at - current_time)
                result = task()
                future.set_result(result)
            except Exception as e:
                if future:
                    future.set_exception(e)

    def schedule(self, func, delay, *args, **kwargs):
        future = Future()
        execute_at = time.time() + delay
        task = lambda: func(*args, **kwargs)
        self.tasks.put((execute_at, task, future))
        return future

    def schedule_at_fixed_rate(self, func, initial_delay, period, *args, **kwargs):
        def repeating_task():
            while not self.stop_event.is_set():
                start_time = time.time()
                func(*args, **kwargs)
                elapsed_time = time.time() - start_time
                sleep_time = max(0, period - elapsed_time)
                time.sleep(sleep_time)

        future = Future()
        execute_at = time.time() + initial_delay
        task = repeating_task
        self.tasks.put((execute_at, task, future))
        return future

    def shutdown(self):
        self.stop_event.set()
        for worker in self.workers:
            worker.join()
