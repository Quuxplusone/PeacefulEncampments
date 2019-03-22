"""
.....Y..
.G......
......O.
R.......
...C....
.......P
....M...
..B.....
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "yellow",
      "maxInvariant": 0.093
    },
    {
      "minInvariant": 0.093,
      "color": "green",
      "maxInvariant": 0.218
    },
    {
      "minInvariant": 0.218,
      "color": "orange",
      "maxInvariant": 0.391
    },
    {
      "minInvariant": 0.391,
      "color": "red",
      "maxInvariant": 0.488
    },
    {
      "minInvariant": 0.488,
      "color": "cyan",
      "maxInvariant": 0.605
    },
    {
      "minInvariant": 0.751,
      "color": "magenta",
      "maxInvariant": 0.885
    },
    {
      "minInvariant": 0.885,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "green",
      "maxInvariant": 0.436
    },
    {
      "minInvariant": 0.436,
      "color": "red",
      "maxInvariant": 0.652
    },
    {
      "minInvariant": 0.652,
      "color": "yellow",
      "maxInvariant": 0.893
    },
    {
      "minInvariant": 0.893,
      "color": "cyan",
      "maxInvariant": 1.082
    },
    {
      "minInvariant": 1.082,
      "color": "orange",
      "maxInvariant": 1.228
    },
    {
      "minInvariant": 1.228,
      "color": "blue",
      "maxInvariant": 1.361
    },
    {
      "minInvariant": 1.361,
      "color": "magenta",
      "maxInvariant": 1.556
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "yellow",
      "maxInvariant": -0.622
    },
    {
      "minInvariant": -0.622,
      "color": "orange",
      "maxInvariant": -0.407
    },
    {
      "minInvariant": -0.185,
      "color": "green",
      "maxInvariant": -0.004
    },
    {
      "minInvariant": -0.004,
      "color": "cyan",
      "maxInvariant": 0.150
    },
    {
      "minInvariant": 0.150,
      "color": "magenta",
      "maxInvariant": 0.300
    },
    {
      "minInvariant": 0.300,
      "color": "red",
      "maxInvariant": 0.487
    },
    {
      "minInvariant": 0.487,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.145
    },
    {
      "minInvariant": 0.145,
      "color": "green",
      "maxInvariant": 0.274
    },
    {
      "minInvariant": 0.274,
      "color": "blue",
      "maxInvariant": 0.403
    },
    {
      "minInvariant": 0.403,
      "color": "cyan",
      "maxInvariant": 0.542
    },
    {
      "minInvariant": 0.542,
      "color": "magenta",
      "maxInvariant": 0.670
    },
    {
      "minInvariant": 0.670,
      "color": "yellow",
      "maxInvariant": 0.805
    },
    {
      "minInvariant": 0.805,
      "color": "orange",
      "maxInvariant": 0.915
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
