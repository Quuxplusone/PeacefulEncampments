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
      "maxInvariant": 0.108
    },
    {
      "minInvariant": 0.108,
      "color": "yellow",
      "maxInvariant": 0.225
    },
    {
      "minInvariant": 0.225,
      "color": "cyan",
      "maxInvariant": 0.377
    },
    {
      "minInvariant": 0.377,
      "color": "red",
      "maxInvariant": 0.494
    },
    {
      "minInvariant": 0.625,
      "color": "magenta",
      "maxInvariant": 0.760
    },
    {
      "minInvariant": 0.760,
      "color": "orange",
      "maxInvariant": 0.887
    },
    {
      "minInvariant": 0.887,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "blue",
      "maxInvariant": 0.413
    },
    {
      "minInvariant": 0.413,
      "color": "red",
      "maxInvariant": 0.573
    },
    {
      "minInvariant": 0.573,
      "color": "cyan",
      "maxInvariant": 0.817
    },
    {
      "minInvariant": 0.817,
      "color": "yellow",
      "maxInvariant": 1.007
    },
    {
      "minInvariant": 1.007,
      "color": "green",
      "maxInvariant": 1.167
    },
    {
      "minInvariant": 1.167,
      "color": "magenta",
      "maxInvariant": 1.363
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
      "maxInvariant": -0.474
    },
    {
      "minInvariant": -0.310,
      "color": "blue",
      "maxInvariant": -0.155
    },
    {
      "minInvariant": -0.155,
      "color": "cyan",
      "maxInvariant": -0.057
    },
    {
      "minInvariant": -0.057,
      "color": "orange",
      "maxInvariant": 0.089
    },
    {
      "minInvariant": 0.089,
      "color": "magenta",
      "maxInvariant": 0.253
    },
    {
      "minInvariant": 0.253,
      "color": "red",
      "maxInvariant": 0.550
    },
    {
      "minInvariant": 0.550,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.104
    },
    {
      "minInvariant": 0.104,
      "color": "green",
      "maxInvariant": 0.214
    },
    {
      "minInvariant": 0.214,
      "color": "blue",
      "maxInvariant": 0.337
    },
    {
      "minInvariant": 0.337,
      "color": "cyan",
      "maxInvariant": 0.507
    },
    {
      "minInvariant": 0.507,
      "color": "magenta",
      "maxInvariant": 0.635
    },
    {
      "minInvariant": 0.635,
      "color": "yellow",
      "maxInvariant": 0.771
    },
    {
      "minInvariant": 0.771,
      "color": "orange",
      "maxInvariant": 0.883
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
