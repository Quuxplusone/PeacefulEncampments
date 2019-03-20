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
      "maxInvariant": 0.103
    },
    {
      "minInvariant": 0.103,
      "color": "orange",
      "maxInvariant": 0.228
    },
    {
      "minInvariant": 0.228,
      "color": "red",
      "maxInvariant": 0.354
    },
    {
      "minInvariant": 0.474,
      "color": "magenta",
      "maxInvariant": 0.603
    },
    {
      "minInvariant": 0.603,
      "color": "green",
      "maxInvariant": 0.731
    },
    {
      "minInvariant": 0.731,
      "color": "yellow",
      "maxInvariant": 0.889
    },
    {
      "minInvariant": 0.889,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.401
    },
    {
      "minInvariant": 0.401,
      "color": "cyan",
      "maxInvariant": 0.655
    },
    {
      "minInvariant": 0.655,
      "color": "green",
      "maxInvariant": 0.901
    },
    {
      "minInvariant": 0.901,
      "color": "orange",
      "maxInvariant": 1.050
    },
    {
      "minInvariant": 1.050,
      "color": "magenta",
      "maxInvariant": 1.167
    },
    {
      "minInvariant": 1.167,
      "color": "blue",
      "maxInvariant": 1.291
    },
    {
      "minInvariant": 1.460,
      "color": "yellow",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "orange",
      "maxInvariant": -0.591
    },
    {
      "minInvariant": -0.424,
      "color": "cyan",
      "maxInvariant": -0.202
    },
    {
      "minInvariant": -0.202,
      "color": "magenta",
      "maxInvariant": 0.026
    },
    {
      "minInvariant": 0.026,
      "color": "yellow",
      "maxInvariant": 0.166
    },
    {
      "minInvariant": 0.166,
      "color": "red",
      "maxInvariant": 0.366
    },
    {
      "minInvariant": 0.366,
      "color": "green",
      "maxInvariant": 0.552
    },
    {
      "minInvariant": 0.552,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.114
    },
    {
      "minInvariant": 0.114,
      "color": "green",
      "maxInvariant": 0.227
    },
    {
      "minInvariant": 0.227,
      "color": "blue",
      "maxInvariant": 0.358
    },
    {
      "minInvariant": 0.358,
      "color": "cyan",
      "maxInvariant": 0.500
    },
    {
      "minInvariant": 0.500,
      "color": "magenta",
      "maxInvariant": 0.674
    },
    {
      "minInvariant": 0.674,
      "color": "yellow",
      "maxInvariant": 0.773
    },
    {
      "minInvariant": 0.773,
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
