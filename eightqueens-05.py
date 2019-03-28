"""
..B.....
.....Y..
.......P
R.......
...C....
......O.
....M...
.G......
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "blue",
      "maxInvariant": 0.120
    },
    {
      "minInvariant": 0.120,
      "color": "yellow",
      "maxInvariant": 0.246
    },
    {
      "minInvariant": 0.401,
      "color": "red",
      "maxInvariant": 0.532
    },
    {
      "minInvariant": 0.532,
      "color": "cyan",
      "maxInvariant": 0.661
    },
    {
      "minInvariant": 0.661,
      "color": "orange",
      "maxInvariant": 0.782
    },
    {
      "minInvariant": 0.782,
      "color": "magenta",
      "maxInvariant": 0.897
    },
    {
      "minInvariant": 0.897,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "blue",
      "maxInvariant": 0.449
    },
    {
      "minInvariant": 0.449,
      "color": "red",
      "maxInvariant": 0.664
    },
    {
      "minInvariant": 0.664,
      "color": "yellow",
      "maxInvariant": 0.928
    },
    {
      "minInvariant": 0.928,
      "color": "cyan",
      "maxInvariant": 1.084
    },
    {
      "minInvariant": 1.084,
      "color": "green",
      "maxInvariant": 1.199
    },
    {
      "minInvariant": 1.320,
      "color": "magenta",
      "maxInvariant": 1.503
    },
    {
      "minInvariant": 1.503,
      "color": "orange",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -0.541,
      "color": "yellow",
      "maxInvariant": -0.370
    },
    {
      "minInvariant": -0.370,
      "color": "blue",
      "maxInvariant": -0.174
    },
    {
      "minInvariant": -0.174,
      "color": "orange",
      "maxInvariant": 0.026
    },
    {
      "minInvariant": 0.026,
      "color": "cyan",
      "maxInvariant": 0.217
    },
    {
      "minInvariant": 0.217,
      "color": "magenta",
      "maxInvariant": 0.366
    },
    {
      "minInvariant": 0.366,
      "color": "red",
      "maxInvariant": 0.553
    },
    {
      "minInvariant": 0.553,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.117
    },
    {
      "minInvariant": 0.117,
      "color": "green",
      "maxInvariant": 0.271
    },
    {
      "minInvariant": 0.271,
      "color": "blue",
      "maxInvariant": 0.371
    },
    {
      "minInvariant": 0.371,
      "color": "cyan",
      "maxInvariant": 0.500
    },
    {
      "minInvariant": 0.500,
      "color": "magenta",
      "maxInvariant": 0.616
    },
    {
      "minInvariant": 0.616,
      "color": "yellow",
      "maxInvariant": 0.729
    },
    {
      "minInvariant": 0.729,
      "color": "orange",
      "maxInvariant": 0.883
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
