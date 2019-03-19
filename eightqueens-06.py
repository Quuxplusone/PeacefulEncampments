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
      "maxInvariant": 0.090
    },
    {
      "minInvariant": 0.090,
      "color": "blue",
      "maxInvariant": 0.237
    },
    {
      "minInvariant": 0.367,
      "color": "cyan",
      "maxInvariant": 0.500
    },
    {
      "minInvariant": 0.500,
      "color": "orange",
      "maxInvariant": 0.614
    },
    {
      "minInvariant": 0.614,
      "color": "red",
      "maxInvariant": 0.769
    },
    {
      "minInvariant": 0.769,
      "color": "yellow",
      "maxInvariant": 0.913
    },
    {
      "minInvariant": 0.913,
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
      "maxInvariant": 0.692
    },
    {
      "minInvariant": 0.692,
      "color": "red",
      "maxInvariant": 0.858
    },
    {
      "minInvariant": 0.858,
      "color": "cyan",
      "maxInvariant": 1.037
    },
    {
      "minInvariant": 1.037,
      "color": "green",
      "maxInvariant": 1.191
    },
    {
      "minInvariant": 1.343,
      "color": "orange",
      "maxInvariant": 1.486
    },
    {
      "minInvariant": 1.486,
      "color": "yellow",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -0.595,
      "color": "magenta",
      "maxInvariant": -0.421
    },
    {
      "minInvariant": -0.421,
      "color": "orange",
      "maxInvariant": -0.235
    },
    {
      "minInvariant": -0.235,
      "color": "blue",
      "maxInvariant": -0.063
    },
    {
      "minInvariant": -0.063,
      "color": "cyan",
      "maxInvariant": 0.133
    },
    {
      "minInvariant": 0.133,
      "color": "yellow",
      "maxInvariant": 0.312
    },
    {
      "minInvariant": 0.312,
      "color": "red",
      "maxInvariant": 0.649
    },
    {
      "minInvariant": 0.649,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.126
    },
    {
      "minInvariant": 0.126,
      "color": "green",
      "maxInvariant": 0.257
    },
    {
      "minInvariant": 0.257,
      "color": "blue",
      "maxInvariant": 0.368
    },
    {
      "minInvariant": 0.368,
      "color": "cyan",
      "maxInvariant": 0.514
    },
    {
      "minInvariant": 0.514,
      "color": "magenta",
      "maxInvariant": 0.626
    },
    {
      "minInvariant": 0.626,
      "color": "yellow",
      "maxInvariant": 0.786
    },
    {
      "minInvariant": 0.786,
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
