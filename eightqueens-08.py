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
      "maxInvariant": 0.140
    },
    {
      "minInvariant": 0.140,
      "color": "red",
      "maxInvariant": 0.250
    },
    {
      "minInvariant": 0.250,
      "color": "magenta",
      "maxInvariant": 0.352
    },
    {
      "minInvariant": 0.486,
      "color": "yellow",
      "maxInvariant": 0.605
    },
    {
      "minInvariant": 0.605,
      "color": "blue",
      "maxInvariant": 0.750
    },
    {
      "minInvariant": 0.750,
      "color": "orange",
      "maxInvariant": 0.839
    },
    {
      "minInvariant": 0.839,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.374
    },
    {
      "minInvariant": 0.374,
      "color": "cyan",
      "maxInvariant": 0.691
    },
    {
      "minInvariant": 0.691,
      "color": "magenta",
      "maxInvariant": 0.938
    },
    {
      "minInvariant": 0.938,
      "color": "blue",
      "maxInvariant": 1.029
    },
    {
      "minInvariant": 1.029,
      "color": "green",
      "maxInvariant": 1.113
    },
    {
      "minInvariant": 1.113,
      "color": "yellow",
      "maxInvariant": 1.317
    },
    {
      "minInvariant": 1.520,
      "color": "orange",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -0.458,
      "color": "cyan",
      "maxInvariant": -0.335
    },
    {
      "minInvariant": -0.335,
      "color": "magenta",
      "maxInvariant": -0.199
    },
    {
      "minInvariant": -0.199,
      "color": "yellow",
      "maxInvariant": -0.082
    },
    {
      "minInvariant": -0.082,
      "color": "orange",
      "maxInvariant": 0.078
    },
    {
      "minInvariant": 0.078,
      "color": "red",
      "maxInvariant": 0.248
    },
    {
      "minInvariant": 0.248,
      "color": "blue",
      "maxInvariant": 0.526
    },
    {
      "minInvariant": 0.526,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.102
    },
    {
      "minInvariant": 0.102,
      "color": "green",
      "maxInvariant": 0.243
    },
    {
      "minInvariant": 0.243,
      "color": "blue",
      "maxInvariant": 0.378
    },
    {
      "minInvariant": 0.378,
      "color": "cyan",
      "maxInvariant": 0.489
    },
    {
      "minInvariant": 0.489,
      "color": "magenta",
      "maxInvariant": 0.622
    },
    {
      "minInvariant": 0.622,
      "color": "yellow",
      "maxInvariant": 0.757
    },
    {
      "minInvariant": 0.757,
      "color": "orange",
      "maxInvariant": 0.901
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
