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
      "maxInvariant": 0.095
    },
    {
      "minInvariant": 0.095,
      "color": "green",
      "maxInvariant": 0.232
    },
    {
      "minInvariant": 0.232,
      "color": "orange",
      "maxInvariant": 0.367
    },
    {
      "minInvariant": 0.367,
      "color": "red",
      "maxInvariant": 0.467
    },
    {
      "minInvariant": 0.467,
      "color": "cyan",
      "maxInvariant": 0.593
    },
    {
      "minInvariant": 0.725,
      "color": "magenta",
      "maxInvariant": 0.875
    },
    {
      "minInvariant": 0.875,
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
      "maxInvariant": 0.580
    },
    {
      "minInvariant": 0.580,
      "color": "yellow",
      "maxInvariant": 0.833
    },
    {
      "minInvariant": 0.833,
      "color": "cyan",
      "maxInvariant": 1.028
    },
    {
      "minInvariant": 1.028,
      "color": "orange",
      "maxInvariant": 1.176
    },
    {
      "minInvariant": 1.176,
      "color": "blue",
      "maxInvariant": 1.297
    },
    {
      "minInvariant": 1.297,
      "color": "magenta",
      "maxInvariant": 1.524
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "yellow",
      "maxInvariant": -0.558
    },
    {
      "minInvariant": -0.558,
      "color": "orange",
      "maxInvariant": -0.346
    },
    {
      "minInvariant": -0.176,
      "color": "green",
      "maxInvariant": 0.022
    },
    {
      "minInvariant": 0.022,
      "color": "cyan",
      "maxInvariant": 0.151
    },
    {
      "minInvariant": 0.151,
      "color": "magenta",
      "maxInvariant": 0.280
    },
    {
      "minInvariant": 0.280,
      "color": "red",
      "maxInvariant": 0.512
    },
    {
      "minInvariant": 0.512,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.134
    },
    {
      "minInvariant": 0.134,
      "color": "green",
      "maxInvariant": 0.245
    },
    {
      "minInvariant": 0.245,
      "color": "blue",
      "maxInvariant": 0.359
    },
    {
      "minInvariant": 0.359,
      "color": "cyan",
      "maxInvariant": 0.503
    },
    {
      "minInvariant": 0.503,
      "color": "magenta",
      "maxInvariant": 0.627
    },
    {
      "minInvariant": 0.627,
      "color": "yellow",
      "maxInvariant": 0.742
    },
    {
      "minInvariant": 0.742,
      "color": "orange",
      "maxInvariant": 0.866
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
