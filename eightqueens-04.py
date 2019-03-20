"""
...C....
.....Y..
.......P
..B.....
R.......
......O.
....M...
.G......
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "cyan",
      "maxInvariant": 0.085
    },
    {
      "minInvariant": 0.085,
      "color": "yellow",
      "maxInvariant": 0.185
    },
    {
      "minInvariant": 0.354,
      "color": "blue",
      "maxInvariant": 0.589
    },
    {
      "minInvariant": 0.589,
      "color": "red",
      "maxInvariant": 0.732
    },
    {
      "minInvariant": 0.732,
      "color": "orange",
      "maxInvariant": 0.785
    },
    {
      "minInvariant": 0.785,
      "color": "magenta",
      "maxInvariant": 0.893
    },
    {
      "minInvariant": 0.893,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "cyan",
      "maxInvariant": 0.636
    },
    {
      "minInvariant": 0.636,
      "color": "yellow",
      "maxInvariant": 0.774
    },
    {
      "minInvariant": 0.774,
      "color": "blue",
      "maxInvariant": 0.855
    },
    {
      "minInvariant": 0.855,
      "color": "red",
      "maxInvariant": 1.053
    },
    {
      "minInvariant": 1.183,
      "color": "green",
      "maxInvariant": 1.300
    },
    {
      "minInvariant": 1.300,
      "color": "magenta",
      "maxInvariant": 1.464
    },
    {
      "minInvariant": 1.464,
      "color": "orange",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -0.581,
      "color": "yellow",
      "maxInvariant": -0.434
    },
    {
      "minInvariant": -0.434,
      "color": "cyan",
      "maxInvariant": -0.243
    },
    {
      "minInvariant": -0.243,
      "color": "orange",
      "maxInvariant": 0
    },
    {
      "minInvariant": 0,
      "color": "blue",
      "maxInvariant": 0.234
    },
    {
      "minInvariant": 0.234,
      "color": "magenta",
      "maxInvariant": 0.387
    },
    {
      "minInvariant": 0.387,
      "color": "red",
      "maxInvariant": 0.581
    },
    {
      "minInvariant": 0.581,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.239
    },
    {
      "minInvariant": 0.239,
      "color": "green",
      "maxInvariant": 0.313
    },
    {
      "minInvariant": 0.313,
      "color": "blue",
      "maxInvariant": 0.394
    },
    {
      "minInvariant": 0.394,
      "color": "cyan",
      "maxInvariant": 0.487
    },
    {
      "minInvariant": 0.487,
      "color": "magenta",
      "maxInvariant": 0.553
    },
    {
      "minInvariant": 0.553,
      "color": "yellow",
      "maxInvariant": 0.721
    },
    {
      "minInvariant": 0.721,
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
