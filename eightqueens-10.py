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
      "maxInvariant": 0.091
    },
    {
      "minInvariant": 0.091,
      "color": "green",
      "maxInvariant": 0.229
    },
    {
      "minInvariant": 0.229,
      "color": "orange",
      "maxInvariant": 0.382
    },
    {
      "minInvariant": 0.382,
      "color": "red",
      "maxInvariant": 0.482
    },
    {
      "minInvariant": 0.482,
      "color": "cyan",
      "maxInvariant": 0.618
    },
    {
      "minInvariant": 0.737,
      "color": "magenta",
      "maxInvariant": 0.870
    },
    {
      "minInvariant": 0.870,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "green",
      "maxInvariant": 0.420
    },
    {
      "minInvariant": 0.420,
      "color": "red",
      "maxInvariant": 0.602
    },
    {
      "minInvariant": 0.602,
      "color": "yellow",
      "maxInvariant": 0.843
    },
    {
      "minInvariant": 0.843,
      "color": "cyan",
      "maxInvariant": 1.048
    },
    {
      "minInvariant": 1.048,
      "color": "orange",
      "maxInvariant": 1.184
    },
    {
      "minInvariant": 1.184,
      "color": "blue",
      "maxInvariant": 1.297
    },
    {
      "minInvariant": 1.297,
      "color": "magenta",
      "maxInvariant": 1.523
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "yellow",
      "maxInvariant": -0.565
    },
    {
      "minInvariant": -0.565,
      "color": "orange",
      "maxInvariant": -0.339
    },
    {
      "minInvariant": -0.182,
      "color": "green",
      "maxInvariant": 0.013
    },
    {
      "minInvariant": 0.013,
      "color": "cyan",
      "maxInvariant": 0.160
    },
    {
      "minInvariant": 0.160,
      "color": "magenta",
      "maxInvariant": 0.301
    },
    {
      "minInvariant": 0.301,
      "color": "red",
      "maxInvariant": 0.502
    },
    {
      "minInvariant": 0.502,
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
      "maxInvariant": 0.249
    },
    {
      "minInvariant": 0.249,
      "color": "blue",
      "maxInvariant": 0.371
    },
    {
      "minInvariant": 0.371,
      "color": "cyan",
      "maxInvariant": 0.501
    },
    {
      "minInvariant": 0.501,
      "color": "magenta",
      "maxInvariant": 0.622
    },
    {
      "minInvariant": 0.622,
      "color": "yellow",
      "maxInvariant": 0.749
    },
    {
      "minInvariant": 0.749,
      "color": "orange",
      "maxInvariant": 0.881
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
