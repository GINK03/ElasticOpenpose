import os
import sys
import glob
import math
import json
import pickle

POSE_COCO_BODY_PARTS =  {
  0 : "Nose",
  1 : "Neck",
  2 : "RShoulder",
  3 : "RElbow",
  4 : "RWrist",
  5 : "LShoulder",
  6 : "LElbow",
  7 : "LWrist",
  8 : "RHip",
  9 : "RKnee",
  10: "RAnkle",
  11: "LHip",
  12: "LKnee",
  13: "LAnkle",
  14: "REye",
  15: "LEye",
  16: "REar",
  17: "LEar",
  18: "Bkg"
}


def step1():
  n_d = {}

  """ reocer data from json """
  for name in sorted(glob.glob("../openpose/json/*.json")):
    o   = json.loads(open(name).read())
    mvs = o["people"] 
    for e, mv in enumerate(mvs):
      """ please insert merge algorithm """
      if n_d.get(e) is None:
        n_d[e] = []
      ps = mv["body_parts"]
      # print( ps )
      shot = {}
      for i in range(19):
        print(i,POSE_COCO_BODY_PARTS[i], ps[3*i:3*i+3] )
        shot[ POSE_COCO_BODY_PARTS[i] ] = ps[3*i:3*i+3]
      n_d[e].append( shot )

      
      print( shot )
  open("n_d.pkl", "wb").write( pickle.dumps(n_d) )

if __name__ == '__main__':
  if '--step1' in sys.argv:
    step1()
    
