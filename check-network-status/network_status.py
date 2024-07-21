import asyncio
import ping3
import datetime

async def ping_host(hostname):
    try:
        response_time = ping3.ping(hostname, timeout=1)
        if response_time is None:
            return None
        else:
            return response_time * 1000
    except:
        return None

async def log_network_status(hostname):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    log_file = f'network_status-{timestamp}.log'

    sent_packets = 0
    received_packets = 0

    try:
        with open(log_file, 'a') as log:
            while True:
                sent_packets += 1
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                response_time = await ping_host(hostname)
                if response_time is None:
                    status = "Request timed out"
                else:
                    status = f"Response time: {response_time:.2f} ms"
                    received_packets += 1

                log_entry = f'{sent_packets} - {current_time} - {status}'
                print(log_entry)
                log.write(log_entry + '\n')

                await asyncio.sleep(1)  # 1초마다 핑 체크
    except (KeyboardInterrupt, asyncio.exceptions.CancelledError):
        print("\nTerminating the program.")
    finally:
        lost_packets = sent_packets - received_packets
        loss_percentage = (lost_packets / sent_packets) * 100 if sent_packets > 0 else 0
        summary = (f"Summary:\n"
                   f"Sent: {sent_packets}, Received: {received_packets}, Lost: {lost_packets}, "
                   f"Loss: {loss_percentage:.2f}%")
        print(summary)
        with open(log_file, 'a') as log:
            log.write(summary + '\n')

if __name__ == "__main__":
    hostname = '168.126.63.1'  # KT DNS 서버
    asyncio.run(log_network_status(hostname))

