import json
from time import sleep

def sendmsg(msgtype, **cmd):
  """Sends a message to the frontend.

  The frontend will receive the specified message whenever
  this function is called. The frontend can decide to some
  action on each of these messages.
  """
  msg = dict(msgtype=msgtype, cmd=cmd)
  print("--MSG--", json.dumps(msg))

def play(note):
  sendmsg("music", function="play", note=note)