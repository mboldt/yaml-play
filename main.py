import pprint
import yaml

doc = '''---
shared: &anchor
  from_shared: foo

consumer1: *anchor
  # This errors:
  # from_consumer1: bar

consumer2:
  <<: *anchor
  from_consumer2: baz
'''

pyobj = yaml.load(doc)
pprint.pprint(pyobj)
