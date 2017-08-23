import subprocess
import tempfile

query="panera"
with tempfile.TemporaryFile() as tempf:
    cmd = ['search']
    cmd.append(query)
    proc = subprocess.Popen(cmd, stdout=tempf)
    proc.wait()
    tempf.seek(0)
    print tempf.read()
