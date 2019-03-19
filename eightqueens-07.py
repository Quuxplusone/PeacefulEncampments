"""
....M...
......O.
...C....
R.......
..B.....
.......P
.....Y..
.G......
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "magenta",
      "maxInvariant": 0.113
    },
    {
      "minInvariant": 0.113,
      "color": "orange",
      "maxInvariant": 0.257
    },
    {
      "minInvariant": 0.257,
      "color": "cyan",
      "maxInvariant": 0.361
    },
    {
      "minInvariant": 0.361,
      "color": "red",
      "maxInvariant": 0.501
    },
    {
      "minInvariant": 0.501,
      "color": "blue",
      "maxInvariant": 0.618
    },
    {
      "minInvariant": 0.743,
      "color": "yellow",
      "maxInvariant": 0.858
    },
    {
      "minInvariant": 0.858,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.554
    },
    {
      "minInvariant": 0.554,
      "color": "magenta",
      "maxInvariant": 0.694
    },
    {
      "minInvariant": 0.694,
      "color": "cyan",
      "maxInvariant": 0.833
    },
    {
      "minInvariant": 0.833,
      "color": "blue",
      "maxInvariant": 0.983
    },
    {
      "minInvariant": 0.983,
      "color": "orange",
      "maxInvariant": 1.110
    },
    {
      "minInvariant": 1.110,
      "color": "green",
      "maxInvariant": 1.339
    },
    {
      "minInvariant": 1.339,
      "color": "yellow",
      "maxInvariant": 1.539
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "orange",
      "maxInvariant": -0.588
    },
    {
      "minInvariant": -0.588,
      "color": "magenta",
      "maxInvariant": -0.389
    },
    {
      "minInvariant": -0.218,
      "color": "cyan",
      "maxInvariant": 0
    },
    {
      "minInvariant": 0,
      "color": "yellow",
      "maxInvariant": 0.164
    },
    {
      "minInvariant": 0.164,
      "color": "blue",
      "maxInvariant": 0.331
    },
    {
      "minInvariant": 0.331,
      "color": "red",
      "maxInvariant": 0.546
    },
    {
      "minInvariant": 0.546,
      "color": "green",
      "maxInvariant": 0.987
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.097
    },
    {
      "minInvariant": 0.097,
      "color": "green",
      "maxInvariant": 0.254
    },
    {
      "minInvariant": 0.254,
      "color": "blue",
      "maxInvariant": 0.383
    },
    {
      "minInvariant": 0.383,
      "color": "cyan",
      "maxInvariant": 0.506
    },
    {
      "minInvariant": 0.506,
      "color": "magenta",
      "maxInvariant": 0.617
    },
    {
      "minInvariant": 0.617,
      "color": "yellow",
      "maxInvariant": 0.783
    },
    {
      "minInvariant": 0.783,
      "color": "orange",
      "maxInvariant": 0.903
    }
  ]
}
"""

import json
import urllib
print urllib.quote(json.dumps(json.loads(x)))

json.encoder.FLOAT_REPR = lambda f: ("%.3f" % f)

print json.dumps(json.loads(urllib.unquote(
"""
"""
)), indent=2)
