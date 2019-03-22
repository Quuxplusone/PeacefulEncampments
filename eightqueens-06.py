"""
....M...
..B.....
.......P
...C....
......O.
R.......
.....Y..
.G......
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "magenta",
      "maxInvariant": 0.109
    },
    {
      "minInvariant": 0.109,
      "color": "blue",
      "maxInvariant": 0.215
    },
    {
      "minInvariant": 0.377,
      "color": "cyan",
      "maxInvariant": 0.500
    },
    {
      "minInvariant": 0.500,
      "color": "orange",
      "maxInvariant": 0.605
    },
    {
      "minInvariant": 0.605,
      "color": "red",
      "maxInvariant": 0.769
    },
    {
      "minInvariant": 0.769,
      "color": "yellow",
      "maxInvariant": 0.886
    },
    {
      "minInvariant": 0.886,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "blue",
      "maxInvariant": 0.500
    },
    {
      "minInvariant": 0.500,
      "color": "magenta",
      "maxInvariant": 0.642
    },
    {
      "minInvariant": 0.642,
      "color": "red",
      "maxInvariant": 0.783
    },
    {
      "minInvariant": 0.783,
      "color": "cyan",
      "maxInvariant": 0.972
    },
    {
      "minInvariant": 0.972,
      "color": "green",
      "maxInvariant": 1.173
    },
    {
      "minInvariant": 1.299,
      "color": "orange",
      "maxInvariant": 1.431
    },
    {
      "minInvariant": 1.431,
      "color": "yellow",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -0.573,
      "color": "magenta",
      "maxInvariant": -0.368
    },
    {
      "minInvariant": -0.368,
      "color": "orange",
      "maxInvariant": -0.175
    },
    {
      "minInvariant": -0.175,
      "color": "blue",
      "maxInvariant": -0.027
    },
    {
      "minInvariant": -0.027,
      "color": "cyan",
      "maxInvariant": 0.118
    },
    {
      "minInvariant": 0.118,
      "color": "yellow",
      "maxInvariant": 0.360
    },
    {
      "minInvariant": 0.360,
      "color": "red",
      "maxInvariant": 0.725
    },
    {
      "minInvariant": 0.725,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.095
    },
    {
      "minInvariant": 0.095,
      "color": "green",
      "maxInvariant": 0.200
    },
    {
      "minInvariant": 0.200,
      "color": "blue",
      "maxInvariant": 0.336
    },
    {
      "minInvariant": 0.336,
      "color": "cyan",
      "maxInvariant": 0.471
    },
    {
      "minInvariant": 0.471,
      "color": "magenta",
      "maxInvariant": 0.593
    },
    {
      "minInvariant": 0.593,
      "color": "yellow",
      "maxInvariant": 0.740
    },
    {
      "minInvariant": 0.740,
      "color": "orange",
      "maxInvariant": 0.888
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
