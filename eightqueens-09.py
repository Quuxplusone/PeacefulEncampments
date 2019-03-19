"""
..B.....
.....Y..
...C....
R.......
.......P
....M...
......O.
.G......
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "blue",
      "maxInvariant": 0.094
    },
    {
      "minInvariant": 0.094,
      "color": "yellow",
      "maxInvariant": 0.240
    },
    {
      "minInvariant": 0.240,
      "color": "cyan",
      "maxInvariant": 0.356
    },
    {
      "minInvariant": 0.356,
      "color": "red",
      "maxInvariant": 0.474
    },
    {
      "minInvariant": 0.609,
      "color": "magenta",
      "maxInvariant": 0.760
    },
    {
      "minInvariant": 0.760,
      "color": "orange",
      "maxInvariant": 0.866
    },
    {
      "minInvariant": 0.866,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "blue",
      "maxInvariant": 0.396
    },
    {
      "minInvariant": 0.396,
      "color": "red",
      "maxInvariant": 0.589
    },
    {
      "minInvariant": 0.589,
      "color": "cyan",
      "maxInvariant": 0.826
    },
    {
      "minInvariant": 0.826,
      "color": "yellow",
      "maxInvariant": 0.967
    },
    {
      "minInvariant": 0.967,
      "color": "green",
      "maxInvariant": 1.115
    },
    {
      "minInvariant": 1.115,
      "color": "magenta",
      "maxInvariant": 1.323
    },
    {
      "minInvariant": 1.558,
      "color": "orange",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "yellow",
      "maxInvariant": -0.478
    },
    {
      "minInvariant": -0.345,
      "color": "blue",
      "maxInvariant": -0.178
    },
    {
      "minInvariant": -0.178,
      "color": "cyan",
      "maxInvariant": -0.068
    },
    {
      "minInvariant": -0.068,
      "color": "orange",
      "maxInvariant": 0.090
    },
    {
      "minInvariant": 0.090,
      "color": "magenta",
      "maxInvariant": 0.264
    },
    {
      "minInvariant": 0.264,
      "color": "red",
      "maxInvariant": 0.545
    },
    {
      "minInvariant": 0.545,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.096
    },
    {
      "minInvariant": 0.096,
      "color": "green",
      "maxInvariant": 0.204
    },
    {
      "minInvariant": 0.204,
      "color": "blue",
      "maxInvariant": 0.358
    },
    {
      "minInvariant": 0.358,
      "color": "cyan",
      "maxInvariant": 0.506
    },
    {
      "minInvariant": 0.506,
      "color": "magenta",
      "maxInvariant": 0.642
    },
    {
      "minInvariant": 0.642,
      "color": "yellow",
      "maxInvariant": 0.766
    },
    {
      "minInvariant": 0.766,
      "color": "orange",
      "maxInvariant": 0.886
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
