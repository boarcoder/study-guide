"""
Interface with satellite.

Limitations:
- Slow connection
- Unavailable frequently
- Requests sent may take long latency return.

Handle all cases. See `sensor_data_model.py`
"""

from enum import Enum
from time import sleep
from tokenize import Token
import requests
from sensor_data_model import SensorData
from datetime import datetime

ex_get_sensor_data = """
{
    "id": 1,
    "frequency": 20,
    "status": "ACTIVE",
    "measurement": 20.105,
}
"""

ex_post_sensor_data = """
{
    "frequency": 10
}
"""

BASE_URL = "http://localhost:8000"
DEFAULT_TIMEOUT_SECONDS = 5


class SensorGetCode(Enum):
    SUCCESS = 200
    NOT_FOUND = 404


class SensorPostCode(Enum):
    SUCCESS = 200
    INVALID_OR_NO_FREQ = 400
    NOT_ENOUGH_RESOURCES = 500


def get_all_sensor():
    requests.get(f"{BASE_URL}/sensor-ids")


def get_sensor(id: int, timeout_sec=DEFAULT_TIMEOUT_SECONDS):
    url = f"{BASE_URL}/sensors/{id}"
    try:
        res = requests.get(url, timeout=timeout_sec)
    except requests.exceptions.Timeout:
        print("The request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    if res.status_code == SensorGetCode.NOT_FOUND.value:
        return None
    if res.status_code == SensorGetCode.SUCCESS.value:
        return SensorData.model_valididate(res.json())


def post_sensor(timeout_sec=DEFAULT_TIMEOUT_SECONDS):
    url = f"{BASE_URL}/sensors/{id}"
    try:
        res = requests.get(url, timeout=timeout_sec)
    except requests.exceptions.Timeout:
        print("The request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    if res.status_code == SensorPostCode.INVALID_OR_NO_FREQ.value:
        return None
    if res.status_code == SensorPostCode.NOT_ENOUGH_RESOURCES.value:
        return None
    if res.status_code == SensorPostCode.SUCCESS.value:
        return SensorData.model_valididate(res.json())
    return None


# 1. The service is stable. Create a sensor.
post_sensor()


# 2. The service is stable. Get 10 unique measurements for a sensor id.
# 3. The service is unstable now, try to add retry method and throw corresponding error code
class TokenBucket:
    def __init__(self, token_max=100, token_per_min=10):
        self.token_bucket = token_max
        self.token_max = token_max
        self.token_per_min = token_per_min
        self.last_update_time = datetime.now()

    def check_limit(self):
        tokens = self.update_bucket()
        if tokens > 0:
            tokens -= 1
            return True
        return False

    def update_bucket(self):
        time_delta = datetime.now() - self.last_update_time
        self.last_update_time = datetime.now()
        self.token_bucket = max(self.token_max, time_delta.total_seconds / 60)
        return self.token_bucket


client_rate_limiter = TokenBucket()
measurement_list = []
fail_list = []
max_retry_time_sec = 1000
retry_limit = 100
timeout_sec = max_retry_time_sec / retry_limit
retry_ct = 0
while len(measurement_list) < 10 and retry_ct < retry_limit:
    max_exponent = 3
    for i in range(1, max_exponent):
        if client_rate_limiter.check_limit():
            res = get_sensor(1, timeout_sec**i)
            if not res:
                retry_ct += 1
        else:
            print("waiting for client side rate limit to retry")
            sleep(1)
