import json
from multiprocessing import Pool
from multiprocessing import cpu_count
import time
import sys
import subprocess
import socket


url = 'http://127.0.0.1:5000'


@app.route('/<int:seed>', methods=['POST', 'GET'])
def show_seed(seed):
    if request.method == 'POST':
        #requests.post(url, data=json.dumps({"num":100}))
		theproc = subprocess.Popen([sys.executable, "stress_cpu.py"])
		theproc.communicate()
    else:
        return socket.gethostname()


if __name__ == '__main__':
   app.run(debug = True)