"""
.....Y..
...C....
......O.
R.......
.......P
.G......
....M...
..B.....
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "yellow",
      "maxInvariant": 0.077
    },
    {
      "minInvariant": 0.077,
      "color": "cyan",
      "maxInvariant": 0.188
    },
    {
      "minInvariant": 0.188,
      "color": "orange",
      "maxInvariant": 0.293
    },
    {
      "minInvariant": 0.293,
      "color": "red",
      "maxInvariant": 0.500
    },
    {
      "minInvariant": 0.707,
      "color": "green",
      "maxInvariant": 0.813
    },
    {
      "minInvariant": 0.813,
      "color": "magenta",
      "maxInvariant": 0.924
    },
    {
      "minInvariant": 0.924,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.501
    },
    {
      "minInvariant": 0.501,
      "color": "cyan",
      "maxInvariant": 0.665
    },
    {
      "minInvariant": 0.665,
      "color": "yellow",
      "maxInvariant": 0.838
    },
    {
      "minInvariant": 0.838,
      "color": "green",
      "maxInvariant": 1
    },
    {
      "minInvariant": 1,
      "color": "orange",
      "maxInvariant": 1.162
    },
    {
      "minInvariant": 1.162,
      "color": "blue",
      "maxInvariant": 1.336
    },
    {
      "minInvariant": 1.336,
      "color": "magenta",
      "maxInvariant": 1.498
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "yellow",
      "maxInvariant": -0.623
    },
    {
      "minInvariant": -0.623,
      "color": "orange",
      "maxInvariant": -0.435
    },
    {
      "minInvariant": -0.435,
      "color": "cyan",
      "maxInvariant": -0.288
    },
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.288
    },
    {
      "minInvariant": 0.288,
      "color": "magenta",
      "maxInvariant": 0.435
    },
    {
      "minInvariant": 0.435,
      "color": "green",
      "maxInvariant": 0.623
    },
    {
      "minInvariant": 0.623,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.136
    },
    {
      "minInvariant": 0.136,
      "color": "green",
      "maxInvariant": 0.232
    },
    {
      "minInvariant": 0.232,
      "color": "blue",
      "maxInvariant": 0.372
    },
    {
      "minInvariant": 0.372,
      "color": "cyan",
      "maxInvariant": 0.500
    },
    {
      "minInvariant": 0.500,
      "color": "magenta",
      "maxInvariant": 0.628
    },
    {
      "minInvariant": 0.628,
      "color": "yellow",
      "maxInvariant": 0.768
    },
    {
      "minInvariant": 0.768,
      "color": "orange",
      "maxInvariant": 0.864
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
