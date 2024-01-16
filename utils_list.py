psutil_list = ['AF_LINn', 'AIX',  'BSD', 'CONN_CLOSE', 
                'CONN_CLOSE_WAIT', 'CONN_CLOSING', 'CONN_ESTABLISHED', 
                'CONN_FIN_WAIT1', 'CONN_FIN_WAIT2', 'CONN_LAST_ACK', 
                'CONN_LISTEN', 'CONN_NONE', 'CONN_SYN_RECV', 'CONN_SYN_SENT', 
                'CONN_TIME_WAIT', 'Error', 'FREEBSD', 'IOPRIO_CLASS_BE', 
                'IOPRIO_CLASS_IDLE', 'IOPRIO_CLASS_NONE', 'IOPRIO_CLASS_RT', 
                'LINUX', 'MACOS', 'NETBSD', 'NIC_DUPLEX_FULL', 'NIC_DUPLEX_HALF',
                'NIC_DUPLEX_UNKNOWN', 'NoSuchProcess', 'OPENBSD', 'OSX', 'POSIX', 
                'POWER_TIME_UNKNOWN', 'POWER_TIME_UNLIMITED', 'PROCFS_PATH',  
                'PermissionError', 'Popen', 'Process', 'ProcessLookupError',  
                'RLIMIT_AS', 'RLIMIT_CORE', 'RLIMIT_CPU', 'RLIMIT_DATA', 
                'RLIMIT_FSIZE', 'RLIMIT_LOCKS', 'RLIMIT_MEMLOCK', 
                'RLIMIT_MSGQUEUE', 'RLIMIT_NICE', 'RLIMIT_NOFILE',  
                'RLIMIT_NPROC', 'RLIMIT_RSS', 'RLIMIT_RTPRIO', 'RLIMIT_RTTIME',  
                'RLIMIT_SIGPENDING', 'RLIMIT_STACK', 'RLIM_INFINITY', 'STATUS_DEAD',  
                'STATUS_DISK_SLEEP', 'STATUS_IDLE', 'STATUS_LOCKED', 'STATUS_PARKED',  
                'STATUS_RUNNING', 'STATUS_SLEEPING', 'STATUS_STOPPED',  
                'STATUS_TRACING_STOP', 'STATUS_WAITING', 'STATUS_WAKING',   
                'STATUS_ZOMBIE', 'SUNOS', 'TimeoutExpired', 'WINDOWS', 'ZombieProcess',                  '_LOWEST_PID', '_PY3', '_SENTINEL', '_SubprocessTimeoutExpired',
             '_TOTAL_PHYMEM', '__all__', '__author__', '__builtins__',  
                '__cached__', '__doc__', '__file__', '__loader__', '__name__',  
                '__package__', '__path__', '__spec__', '__version__',  
                '_as_dict_attrnames', '_assert_pid_not_reused', '_common',  
                '_compat', '_cpu_busy_time', '_cpu_times_deltas', '_cpu_tot_time',  
                '_last_cpu_times', '_last_cpu_times_2', '_last_per_cpu_times',  
                '_last_per_cpu_times_2', '_pmap', '_ppid_map', '_pprint_secs',  
                '_pslinux', '_psplatform', '_psposix', '_psutil_linux',  
                '_psutil_posix', '_set_debug', '_timer', '_wrap_numbers',  
                'boot_time', 'collections', 'contextlib', 'cpu_count', 'cpu_freq',  
                'cpu_percent', 'cpu_stats', 'cpu_times', 'cpu_times_percent',  
                'datetime', 'disk_io_counters', 'disk_partitions', 'disk_usage',  
                'functools', 'getloadavg', 'long', 'net_connections', 'net_if_addrs',  
                'net_if_stats', 'net_io_counters', 'os', 'pid_exists', 'pids',  
                'process_iter', 'pwd', 'sensors_battery', 'sensors_fans',  
                'sensors_temperatures', 'signal', 'subprocess', 'swap_memory',  
                'sys', 'test', 'threading', 'time', 'users', 'version_info',  
                'virtual_memory', 'wait_procs']

with open ('/home/tony/projects/python/sys_monitor/sys_monitor.out', 'w') as utils:
    for i in psutil_list:
        utils.write(i)
        utils.write('\n')
        
    utils.close()
    

    