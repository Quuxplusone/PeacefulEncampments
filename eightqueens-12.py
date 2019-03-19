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
      "maxInvariant": 0.076
    },
    {
      "minInvariant": 0.076,
      "color": "cyan",
      "maxInvariant": 0.187
    },
    {
      "minInvariant": 0.187,
      "color": "orange",
      "maxInvariant": 0.293
    },
    {
      "minInvariant": 0.293,
      "color": "red",
      "maxInvariant": 0.5
    },
    {
      "minInvariant": 0.707,
      "color": "green",
      "maxInvariant": 0.816
    },
    {
      "minInvariant": 0.816,
      "color": "magenta",
      "maxInvariant": 0.926
    },
    {
      "minInvariant": 0.926,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.5
    },
    {
      "minInvariant": 0.5,
      "color": "cyan",
      "maxInvariant": 0.661
    },
    {
      "minInvariant": 0.661,
      "color": "yellow",
      "maxInvariant": 0.817
    },
    {
      "minInvariant": 0.817,
      "color": "green",
      "maxInvariant": 1
    },
    {
      "minInvariant": 1,
      "color": "orange",
      "maxInvariant": 1.183
    },
    {
      "minInvariant": 1.183,
      "color": "blue",
      "maxInvariant": 1.343
    },
    {
      "minInvariant": 1.343,
      "color": "magenta",
      "maxInvariant": 1.497
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "yellow",
      "maxInvariant": -0.619
    },
    {
      "minInvariant": -0.619,
      "color": "orange",
      "maxInvariant": -0.453
    },
    {
      "minInvariant": -0.453,
      "color": "cyan",
      "maxInvariant": -0.289
    },
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.289
    },
    {
      "minInvariant": 0.289,
      "color": "magenta",
      "maxInvariant": 0.453
    },
    {
      "minInvariant": 0.453,
      "color": "green",
      "maxInvariant": 0.619
    },
    {
      "minInvariant": 0.619,
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
      "maxInvariant": 0.232
    },
    {
      "minInvariant": 0.232,
      "color": "blue",
      "maxInvariant": 0.373
    },
    {
      "minInvariant": 0.373,
      "color": "cyan",
      "maxInvariant": 0.5
    },
    {
      "minInvariant": 0.5,
      "color": "magenta",
      "maxInvariant": 0.627
    },
    {
      "minInvariant": 0.627,
      "color": "yellow",
      "maxInvariant": 0.768
    },
    {
      "minInvariant": 0.768,
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
