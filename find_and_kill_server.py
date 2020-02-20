import subprocess, signal, os


p = subprocess.Popen(['pgrep', '-l' , 'Python'], stdout=subprocess.PIPE)
out, err = p.communicate()

for line in out.splitlines():        
    line = bytes.decode(line)
    pid = int(line.split(None, 1)[0])
    os.kill(pid, signal.SIGKILL)