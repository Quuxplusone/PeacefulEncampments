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
      "maxInvariant": 0.234
    },
    {
      "minInvariant": 0.234,
      "color": "orange",
      "maxInvariant": 0.383
    },
    {
      "minInvariant": 0.383,
      "color": "red",
      "maxInvariant": 0.484
    },
    {
      "minInvariant": 0.484,
      "color": "cyan",
      "maxInvariant": 0.617
    },
    {
      "minInvariant": 0.734,
      "color": "magenta",
      "maxInvariant": 0.872
    },
    {
      "minInvariant": 0.872,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "green",
      "maxInvariant": 0.439
    },
    {
      "minInvariant": 0.439,
      "color": "red",
      "maxInvariant": 0.625
    },
    {
      "minInvariant": 0.625,
      "color": "yellow",
      "maxInvariant": 0.857
    },
    {
      "minInvariant": 0.857,
      "color": "cyan",
      "maxInvariant": 1.054
    },
    {
      "minInvariant": 1.054,
      "color": "orange",
      "maxInvariant": 1.189
    },
    {
      "minInvariant": 1.189,
      "color": "blue",
      "maxInvariant": 1.306
    },
    {
      "minInvariant": 1.306,
      "color": "magenta",
      "maxInvariant": 1.500
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "yellow",
      "maxInvariant": -0.582
    },
    {
      "minInvariant": -0.582,
      "color": "orange",
      "maxInvariant": -0.349
    },
    {
      "minInvariant": -0.171,
      "color": "green",
      "maxInvariant": 0
    },
    {
      "minInvariant": 0,
      "color": "cyan",
      "maxInvariant": 0.156
    },
    {
      "minInvariant": 0.156,
      "color": "magenta",
      "maxInvariant": 0.299
    },
    {
      "minInvariant": 0.299,
      "color": "red",
      "maxInvariant": 0.486
    },
    {
      "minInvariant": 0.486,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.144
    },
    {
      "minInvariant": 0.144,
      "color": "green",
      "maxInvariant": 0.259
    },
    {
      "minInvariant": 0.259,
      "color": "blue",
      "maxInvariant": 0.381
    },
    {
      "minInvariant": 0.381,
      "color": "cyan",
      "maxInvariant": 0.514
    },
    {
      "minInvariant": 0.514,
      "color": "magenta",
      "maxInvariant": 0.629
    },
    {
      "minInvariant": 0.629,
      "color": "yellow",
      "maxInvariant": 0.762
    },
    {
      "minInvariant": 0.762,
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
