import psutil

print(psutil.cpu_count())

print(psutil.cpu_percent(percpu=True))

print(psutil.disk_usage('/'))

print(psutil.sensors_battery())