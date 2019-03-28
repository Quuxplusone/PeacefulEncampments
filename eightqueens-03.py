"""
...C....
.G......
......O.
..B.....
.....Y..
.......P
....M...
R.......
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "cyan",
      "maxInvariant": 0.106
    },
    {
      "minInvariant": 0.106,
      "color": "green",
      "maxInvariant": 0.218
    },
    {
      "minInvariant": 0.218,
      "color": "orange",
      "maxInvariant": 0.356
    },
    {
      "minInvariant": 0.356,
      "color": "blue",
      "maxInvariant": 0.501
    },
    {
      "minInvariant": 0.501,
      "color": "yellow",
      "maxInvariant": 0.619
    },
    {
      "minInvariant": 0.775,
      "color": "magenta",
      "maxInvariant": 0.885
    },
    {
      "minInvariant": 0.885,
      "color": "red",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "green",
      "maxInvariant": 0.426
    },
    {
      "minInvariant": 0.426,
      "color": "cyan",
      "maxInvariant": 0.634
    },
    {
      "minInvariant": 0.634,
      "color": "blue",
      "maxInvariant": 0.891
    },
    {
      "minInvariant": 0.891,
      "color": "red",
      "maxInvariant": 1.053
    },
    {
      "minInvariant": 1.053,
      "color": "orange",
      "maxInvariant": 1.180
    },
    {
      "minInvariant": 1.180,
      "color": "yellow",
      "maxInvariant": 1.362
    },
    {
      "minInvariant": 1.362,
      "color": "magenta",
      "maxInvariant": 1.524
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "orange",
      "maxInvariant": -0.478
    },
    {
      "minInvariant": -0.478,
      "color": "cyan",
      "maxInvariant": -0.341
    },
    {
      "minInvariant": -0.210,
      "color": "yellow",
      "maxInvariant": -0.074
    },
    {
      "minInvariant": -0.074,
      "color": "green",
      "maxInvariant": 0.058
    },
    {
      "minInvariant": 0.058,
      "color": "blue",
      "maxInvariant": 0.156
    },
    {
      "minInvariant": 0.156,
      "color": "magenta",
      "maxInvariant": 0.631
    },
    {
      "minInvariant": 0.631,
      "color": "red",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.110
    },
    {
      "minInvariant": 0.110,
      "color": "green",
      "maxInvariant": 0.242
    },
    {
      "minInvariant": 0.242,
      "color": "blue",
      "maxInvariant": 0.386
    },
    {
      "minInvariant": 0.386,
      "color": "cyan",
      "maxInvariant": 0.527
    },
    {
      "minInvariant": 0.527,
      "color": "magenta",
      "maxInvariant": 0.647
    },
    {
      "minInvariant": 0.647,
      "color": "yellow",
      "maxInvariant": 0.774
    },
    {
      "minInvariant": 0.774,
      "color": "orange",
      "maxInvariant": 0.902
    }
  ]
}
"""

import json
import urllib

json.encoder.FLOAT_REPR = lambda f: ("%.3f" % f)

print urllib.quote(json.dumps(json.loads(x)))

print json.dumps(json.loads(urllib.unquote(
"""
"""
)), indent=2)
