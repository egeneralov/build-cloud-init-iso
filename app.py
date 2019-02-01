import os

from tempfile import mkdtemp, mkstemp
from flask import Flask, request, abort


app = Flask(__name__)


class cd:
  def __init__(self, newPath):
    self.newPath = os.path.expanduser(newPath)

  def __enter__(self):
    self.savedPath = os.getcwd()
    os.chdir(self.newPath)

  def __exit__(self, etype, value, traceback):
    os.chdir(self.savedPath)


@app.route('/', methods=['POST'])
def hello():
  return '{"ok": true}'


@app.route('/', methods=['POST'])
def template_uploaded():
  [ print(i) for i in request.files ]
  
  for key in ['user-data', 'meta-data']:
    if key not in request.files:
      abort(400)
  
  tmp = mkdtemp()
  iso = mkstemp()[1]
  
  for key in ['user-data', 'meta-data']:
    with open('{}/{}'.format(tmp,key), 'w+') as f:
      f.write(request.files[key].stream.read().decode())

  with cd(tmp):
    code = os.system(
      'genisoimage -output {} -volid cidata -joliet -rock user-data meta-data'.format(iso)
    )
  
  if code != 0:
    abort(500)
  
  
  with open(iso, 'rb') as f:
    return f.read()



if __name__ == '__main__':
  app.run(
    port = os.environ('PORT'),
    host = '0.0.0.0',
    debug = True
  )
