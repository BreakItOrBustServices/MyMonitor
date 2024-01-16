# sys_monitor.py
import psutil
import time


while True:
    # CPU usage
    number_cpus = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent(interval=1)

    # Memory usage
    mem = psutil.virtual_memory()
    mem_total = mem.total
    mem_used = mem.used
    mem_percent = mem.percent

    # Disk usage
    disk = psutil.disk_usage('/')
    disk_total = disk.total
    disk_used = disk.used
    disk_percent = disk.percent

    # Network activity
    net_io = psutil.net_io_counters(pernic=True)
    net_bytes_sent = net_io(net_bytes_sent)
    net_bytes_recv = net_io(net_bytes_recv)
    print("CPU Quantity: ", number_cpus)
    print("CPU Percentage: ", cpu_percent)
    print("Memory: ", mem_used, "MB / ", mem_total, "MB ", mem_percent)
    print("Disk: ", disk_used,", MB / ",disk_total," MB" ,disk_percent)
    print("Network: Sent: ", net_bytes_sent, "MB, Received: ", net_bytes_recv, "MB")

    time.sleep(5)
