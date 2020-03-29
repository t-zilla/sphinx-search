import subprocess
import time

start_time = time.time()

processes = [subprocess.Popen(['/usr/local/bin/python', '/scripts/test.py']) for _ in range(1, 10)]
exit_codes = [p.wait() for p in processes]

print("--- %s seconds ---" % (time.time() - start_time))