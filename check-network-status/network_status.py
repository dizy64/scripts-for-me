import datetime
import time

import ping3


def log_network_status(hostname, log_file):
    try:
        with open(log_file, "a") as log:
            while True:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                try:
                    response_time = ping3.ping(hostname, timeout=1)
                    if response_time is None:
                        status = "Request timed out"
                    else:
                        status = f"Response time: {response_time * 1000:.2f} ms"
                except Exception as e:
                    status = f"Error: {e}"

                log_entry = f"{timestamp} - {status}"
                print(log_entry)
                log.write(log_entry + "\n")

                time.sleep(1)
    except KeyboardInterrupt:
        print("\nTerminating the program.")
    finally:
        log.close()


if __name__ == "__main__":
    hostname = "168.126.63.1"
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    log_file = f"network_status-{timestamp}.log"

    log_network_status(hostname, log_file)
