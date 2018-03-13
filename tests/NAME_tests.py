from nose.tools import *
import NAME
print NAME
def setup():
  print "setup!"

def teardown():
  print "tear down!"

def test_basic():
  print "I RAN!"