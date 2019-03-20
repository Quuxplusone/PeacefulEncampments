"""
...C....
......O.
..B.....
.......P
.G......
....M...
R.......
.....Y..
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "cyan",
      "maxInvariant": 0.097
    },
    {
      "minInvariant": 0.097,
      "color": "orange",
      "maxInvariant": 0.219
    },
    {
      "minInvariant": 0.219,
      "color": "blue",
      "maxInvariant": 0.382
    },
    {
      "minInvariant": 0.500,
      "color": "green",
      "maxInvariant": 0.569
    },
    {
      "minInvariant": 0.569,
      "color": "magenta",
      "maxInvariant": 0.756
    },
    {
      "minInvariant": 0.756,
      "color": "red",
      "maxInvariant": 0.894
    },
    {
      "minInvariant": 0.894,
      "color": "yellow",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "cyan",
      "maxInvariant": 0.645
    },
    {
      "minInvariant": 0.645,
      "color": "blue",
      "maxInvariant": 0.713
    },
    {
      "minInvariant": 0.713,
      "color": "green",
      "maxInvariant": 0.851
    },
    {
      "minInvariant": 0.851,
      "color": "red",
      "maxInvariant": 0.899
    },
    {
      "minInvariant": 0.899,
      "color": "orange",
      "maxInvariant": 1.102
    },
    {
      "minInvariant": 1.102,
      "color": "magenta",
      "maxInvariant": 1.293
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
      "maxInvariant": -0.594
    },
    {
      "minInvariant": -0.594,
      "color": "cyan",
      "maxInvariant": -0.448
    },
    {
      "minInvariant": -0.276,
      "color": "blue",
      "maxInvariant": 0
    },
    {
      "minInvariant": 0,
      "color": "magenta",
      "maxInvariant": 0.185
    },
    {
      "minInvariant": 0.185,
      "color": "green",
      "maxInvariant": 0.303
    },
    {
      "minInvariant": 0.303,
      "color": "yellow",
      "maxInvariant": 0.617
    },
    {
      "minInvariant": 0.617,
      "color": "red",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.186
    },
    {
      "minInvariant": 0.186,
      "color": "green",
      "maxInvariant": 0.333
    },
    {
      "minInvariant": 0.333,
      "color": "blue",
      "maxInvariant": 0.440
    },
    {
      "minInvariant": 0.440,
      "color": "cyan",
      "maxInvariant": 0.553
    },
    {
      "minInvariant": 0.553,
      "color": "magenta",
      "maxInvariant": 0.590
    },
    {
      "minInvariant": 0.590,
      "color": "yellow",
      "maxInvariant": 0.696
    },
    {
      "minInvariant": 0.696,
      "color": "orange",
      "maxInvariant": 0.825
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
