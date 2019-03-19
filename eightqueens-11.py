"""
...C....
......O.
R.......
.......P
....M...
.G......
.....Y..
..B.....
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "cyan",
      "maxInvariant": 0.101
    },
    {
      "minInvariant": 0.101,
      "color": "orange",
      "maxInvariant": 0.242
    },
    {
      "minInvariant": 0.242,
      "color": "red",
      "maxInvariant": 0.356
    },
    {
      "minInvariant": 0.473,
      "color": "magenta",
      "maxInvariant": 0.581
    },
    {
      "minInvariant": 0.581,
      "color": "green",
      "maxInvariant": 0.728
    },
    {
      "minInvariant": 0.728,
      "color": "yellow",
      "maxInvariant": 0.905
    },
    {
      "minInvariant": 0.905,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.400
    },
    {
      "minInvariant": 0.400,
      "color": "cyan",
      "maxInvariant": 0.659
    },
    {
      "minInvariant": 0.659,
      "color": "green",
      "maxInvariant": 0.897
    },
    {
      "minInvariant": 0.897,
      "color": "orange",
      "maxInvariant": 1.044
    },
    {
      "minInvariant": 1.044,
      "color": "magenta",
      "maxInvariant": 1.160
    },
    {
      "minInvariant": 1.160,
      "color": "blue",
      "maxInvariant": 1.291
    },
    {
      "minInvariant": 1.470,
      "color": "yellow",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "orange",
      "maxInvariant": -0.562
    },
    {
      "minInvariant": -0.410,
      "color": "cyan",
      "maxInvariant": -0.183
    },
    {
      "minInvariant": -0.183,
      "color": "magenta",
      "maxInvariant": 0.020
    },
    {
      "minInvariant": 0.020,
      "color": "yellow",
      "maxInvariant": 0.138
    },
    {
      "minInvariant": 0.138,
      "color": "red",
      "maxInvariant": 0.325
    },
    {
      "minInvariant": 0.325,
      "color": "green",
      "maxInvariant": 0.534
    },
    {
      "minInvariant": 0.534,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.130
    },
    {
      "minInvariant": 0.130,
      "color": "green",
      "maxInvariant": 0.218
    },
    {
      "minInvariant": 0.218,
      "color": "blue",
      "maxInvariant": 0.339
    },
    {
      "minInvariant": 0.339,
      "color": "cyan",
      "maxInvariant": 0.500
    },
    {
      "minInvariant": 0.500,
      "color": "magenta",
      "maxInvariant": 0.661
    },
    {
      "minInvariant": 0.661,
      "color": "yellow",
      "maxInvariant": 0.782
    },
    {
      "minInvariant": 0.782,
      "color": "orange",
      "maxInvariant": 0.870
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
