"""
...C....
R.......
....M...
.......P
.....Y..
..B.....
......O.
.G......
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "cyan",
      "maxInvariant": 0.126
    },
    {
      "minInvariant": 0.126,
      "color": "red",
      "maxInvariant": 0.256
    },
    {
      "minInvariant": 0.256,
      "color": "magenta",
      "maxInvariant": 0.377
    },
    {
      "minInvariant": 0.520,
      "color": "yellow",
      "maxInvariant": 0.637
    },
    {
      "minInvariant": 0.637,
      "color": "blue",
      "maxInvariant": 0.769
    },
    {
      "minInvariant": 0.769,
      "color": "orange",
      "maxInvariant": 0.879
    },
    {
      "minInvariant": 0.879,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.365
    },
    {
      "minInvariant": 0.365,
      "color": "cyan",
      "maxInvariant": 0.680
    },
    {
      "minInvariant": 0.680,
      "color": "magenta",
      "maxInvariant": 0.943
    },
    {
      "minInvariant": 0.943,
      "color": "blue",
      "maxInvariant": 1.055
    },
    {
      "minInvariant": 1.055,
      "color": "green",
      "maxInvariant": 1.164
    },
    {
      "minInvariant": 1.164,
      "color": "yellow",
      "maxInvariant": 1.342
    },
    {
      "minInvariant": 1.519,
      "color": "orange",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -0.430,
      "color": "cyan",
      "maxInvariant": -0.306
    },
    {
      "minInvariant": -0.306,
      "color": "magenta",
      "maxInvariant": -0.171
    },
    {
      "minInvariant": -0.171,
      "color": "yellow",
      "maxInvariant": -0.032
    },
    {
      "minInvariant": -0.032,
      "color": "orange",
      "maxInvariant": 0.087
    },
    {
      "minInvariant": 0.087,
      "color": "red",
      "maxInvariant": 0.267
    },
    {
      "minInvariant": 0.267,
      "color": "blue",
      "maxInvariant": 0.601
    },
    {
      "minInvariant": 0.601,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.100
    },
    {
      "minInvariant": 0.100,
      "color": "green",
      "maxInvariant": 0.239
    },
    {
      "minInvariant": 0.239,
      "color": "blue",
      "maxInvariant": 0.363
    },
    {
      "minInvariant": 0.363,
      "color": "cyan",
      "maxInvariant": 0.480
    },
    {
      "minInvariant": 0.480,
      "color": "magenta",
      "maxInvariant": 0.607
    },
    {
      "minInvariant": 0.607,
      "color": "yellow",
      "maxInvariant": 0.741
    },
    {
      "minInvariant": 0.741,
      "color": "orange",
      "maxInvariant": 0.891
    }
  ]
}
"""

import json
import urllib

json.encoder.FLOAT_REPR = lambda f: ("%.3f" % f)

print urllib.quote(json.dumps(json.loads(x)))

print json.dumps(json.loads(urllib.unquote(
"""
"""
)), indent=2)
