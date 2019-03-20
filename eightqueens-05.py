"""
..B.....
.....Y..
.......P
R.......
...C....
......O.
....M...
.G......
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "blue",
      "maxInvariant": 0.105
    },
    {
      "minInvariant": 0.105,
      "color": "yellow",
      "maxInvariant": 0.231
    },
    {
      "minInvariant": 0.376,
      "color": "red",
      "maxInvariant": 0.507
    },
    {
      "minInvariant": 0.507,
      "color": "cyan",
      "maxInvariant": 0.640
    },
    {
      "minInvariant": 0.640,
      "color": "orange",
      "maxInvariant": 0.778
    },
    {
      "minInvariant": 0.778,
      "color": "magenta",
      "maxInvariant": 0.891
    },
    {
      "minInvariant": 0.891,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "blue",
      "maxInvariant": 0.433
    },
    {
      "minInvariant": 0.433,
      "color": "red",
      "maxInvariant": 0.653
    },
    {
      "minInvariant": 0.653,
      "color": "yellow",
      "maxInvariant": 0.941
    },
    {
      "minInvariant": 0.941,
      "color": "cyan",
      "maxInvariant": 1.077
    },
    {
      "minInvariant": 1.077,
      "color": "green",
      "maxInvariant": 1.188
    },
    {
      "minInvariant": 1.343,
      "color": "magenta",
      "maxInvariant": 1.524
    },
    {
      "minInvariant": 1.524,
      "color": "orange",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -0.579,
      "color": "yellow",
      "maxInvariant": -0.412
    },
    {
      "minInvariant": -0.412,
      "color": "blue",
      "maxInvariant": -0.206
    },
    {
      "minInvariant": -0.206,
      "color": "orange",
      "maxInvariant": 0
    },
    {
      "minInvariant": 0,
      "color": "cyan",
      "maxInvariant": 0.185
    },
    {
      "minInvariant": 0.185,
      "color": "magenta",
      "maxInvariant": 0.330
    },
    {
      "minInvariant": 0.330,
      "color": "red",
      "maxInvariant": 0.536
    },
    {
      "minInvariant": 0.536,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.109
    },
    {
      "minInvariant": 0.109,
      "color": "green",
      "maxInvariant": 0.257
    },
    {
      "minInvariant": 0.257,
      "color": "blue",
      "maxInvariant": 0.393
    },
    {
      "minInvariant": 0.393,
      "color": "cyan",
      "maxInvariant": 0.521
    },
    {
      "minInvariant": 0.521,
      "color": "magenta",
      "maxInvariant": 0.642
    },
    {
      "minInvariant": 0.642,
      "color": "yellow",
      "maxInvariant": 0.757
    },
    {
      "minInvariant": 0.757,
      "color": "orange",
      "maxInvariant": 0.904
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
