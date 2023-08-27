import sys
import os

if len(sys.argv) < 2:
  sys.exit()

path = sys.argv[1]
basename = os.path.basename(path)

with open(path,"rb") as mapfile:
  content = mapfile.read()
#NUL P K ETX EOT
offset = content.find(b'\x00\x50\x4b\x03\x04') + 1
if offset == 0:
  print("couldn't find packed content.")
  input()
  sys.exit()

newfile = f"{path}/../" + basename.replace(".bsp",".zip")
print(f"writing output to {newfile}")

with open(newfile,"wb") as output:
  output.write(content[offset:])
