import psutil

def system_health():
    user_cpu = int(input('enter CPU threshold value:'))
    user_memory = int(input('enter memory threshold value:'))
    user_disk = int(input('enter disk threshold value:'))

    current_cpu = psutil.cpu_percent(interval=1)
    current_memory = psutil.virtual_memory().percent
    current_disk = psutil.disk_usage('C:\\').percent

    print('current cpu usage: ', current_cpu, '%')
    print('current memory usage: ', current_memory, '%')
    print('current disk usage: ', current_disk, '%')

    # Check CPU usage
    if current_cpu > user_cpu:
        print('CPU usage is high')
    else:
        print('CPU usage is normal')

    # Check Memory usage
    if current_memory > user_memory:
        print('Memory usage is high')
    else:
        print('Memory usage is normal')

    #check Disk usage
    if current_disk > user_disk:
        print('Disk usage is high')
    else:
        print('Disk usage is normal')

system_health()