"""
....M...
.G......
...C....
......O.
..B.....
.......P
.....Y..
R.......
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "magenta",
      "maxInvariant": 0.096
    },
    {
      "minInvariant": 0.096,
      "color": "green",
      "maxInvariant": 0.260
    },
    {
      "minInvariant": 0.260,
      "color": "cyan",
      "maxInvariant": 0.337
    },
    {
      "minInvariant": 0.337,
      "color": "orange",
      "maxInvariant": 0.478
    },
    {
      "minInvariant": 0.621,
      "color": "blue",
      "maxInvariant": 0.756
    },
    {
      "minInvariant": 0.756,
      "color": "yellow",
      "maxInvariant": 0.914
    },
    {
      "minInvariant": 0.914,
      "color": "red",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "green",
      "maxInvariant": 0.547
    },
    {
      "minInvariant": 0.547,
      "color": "magenta",
      "maxInvariant": 0.719
    },
    {
      "minInvariant": 0.719,
      "color": "cyan",
      "maxInvariant": 0.898
    },
    {
      "minInvariant": 0.898,
      "color": "blue",
      "maxInvariant": 1.027
    },
    {
      "minInvariant": 1.027,
      "color": "red",
      "maxInvariant": 1.132
    },
    {
      "minInvariant": 1.132,
      "color": "orange",
      "maxInvariant": 1.344
    },
    {
      "minInvariant": 1.552,
      "color": "yellow",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "magenta",
      "maxInvariant": -0.519
    },
    {
      "minInvariant": -0.519,
      "color": "orange",
      "maxInvariant": -0.392
    },
    {
      "minInvariant": -0.253,
      "color": "cyan",
      "maxInvariant": -0.102
    },
    {
      "minInvariant": -0.102,
      "color": "green",
      "maxInvariant": 0
    },
    {
      "minInvariant": 0,
      "color": "yellow",
      "maxInvariant": 0.214
    },
    {
      "minInvariant": 0.214,
      "color": "blue",
      "maxInvariant": 0.611
    },
    {
      "minInvariant": 0.611,
      "color": "red",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.189
    },
    {
      "minInvariant": 0.189,
      "color": "green",
      "maxInvariant": 0.275
    },
    {
      "minInvariant": 0.275,
      "color": "blue",
      "maxInvariant": 0.407
    },
    {
      "minInvariant": 0.407,
      "color": "cyan",
      "maxInvariant": 0.553
    },
    {
      "minInvariant": 0.553,
      "color": "magenta",
      "maxInvariant": 0.679
    },
    {
      "minInvariant": 0.679,
      "color": "yellow",
      "maxInvariant": 0.777
    },
    {
      "minInvariant": 0.777,
      "color": "orange",
      "maxInvariant": 0.870
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
