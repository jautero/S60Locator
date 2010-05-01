import simplejson
import gaeclient
import sys, os

try:
  gaeclient.api_url=os.environ["SBF_SERVER"]
except:
  pass

if __name__ == "__main__":
  buddy_name=None
  message=None
  if (len(sys.argv)==3):
    buddy_name="centre"
    lat=float(sys.argv[1])
    lon=float(sys.argv[2])
  if (len(sys.argv)>3):
    buddy_name=sys.argv[1]
    lat=float(sys.argv[2])
    lon=float(sys.argv[3])
    if (len(sys.argv)>4):
      message=" ".join(sys.argv[4:])
  if not buddy_name:
    print "Usage: %s [<name>] <latitude> <longitude> [<message> ...]" % sys.argv
    exit(1)
  position={"latitude":lat,"longitude":lon}
  if message:
    position["message"]=message
  data=gaeclient.update_position(buddy_name,simplejson.dumps(position))
  print data
