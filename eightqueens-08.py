"""
...C....
R.......
....M...
.......P
.....Y..
..B.....
......O.
.G......
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "cyan",
      "maxInvariant": 0.159
    },
    {
      "minInvariant": 0.159,
      "color": "red",
      "maxInvariant": 0.269
    },
    {
      "minInvariant": 0.269,
      "color": "magenta",
      "maxInvariant": 0.383
    },
    {
      "minInvariant": 0.509,
      "color": "yellow",
      "maxInvariant": 0.635
    },
    {
      "minInvariant": 0.635,
      "color": "blue",
      "maxInvariant": 0.770
    },
    {
      "minInvariant": 0.770,
      "color": "orange",
      "maxInvariant": 0.869
    },
    {
      "minInvariant": 0.869,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.375
    },
    {
      "minInvariant": 0.375,
      "color": "cyan",
      "maxInvariant": 0.728
    },
    {
      "minInvariant": 0.728,
      "color": "magenta",
      "maxInvariant": 0.952
    },
    {
      "minInvariant": 0.952,
      "color": "blue",
      "maxInvariant": 1.054
    },
    {
      "minInvariant": 1.054,
      "color": "green",
      "maxInvariant": 1.153
    },
    {
      "minInvariant": 1.153,
      "color": "yellow",
      "maxInvariant": 1.341
    },
    {
      "minInvariant": 1.527,
      "color": "orange",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -0.416,
      "color": "cyan",
      "maxInvariant": -0.313
    },
    {
      "minInvariant": -0.313,
      "color": "magenta",
      "maxInvariant": -0.166
    },
    {
      "minInvariant": -0.166,
      "color": "yellow",
      "maxInvariant": -0.045
    },
    {
      "minInvariant": -0.045,
      "color": "orange",
      "maxInvariant": 0.092
    },
    {
      "minInvariant": 0.092,
      "color": "red",
      "maxInvariant": 0.265
    },
    {
      "minInvariant": 0.265,
      "color": "blue",
      "maxInvariant": 0.544
    },
    {
      "minInvariant": 0.544,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.105
    },
    {
      "minInvariant": 0.105,
      "color": "green",
      "maxInvariant": 0.243
    },
    {
      "minInvariant": 0.243,
      "color": "blue",
      "maxInvariant": 0.372
    },
    {
      "minInvariant": 0.372,
      "color": "cyan",
      "maxInvariant": 0.488
    },
    {
      "minInvariant": 0.488,
      "color": "magenta",
      "maxInvariant": 0.610
    },
    {
      "minInvariant": 0.610,
      "color": "yellow",
      "maxInvariant": 0.749
    },
    {
      "minInvariant": 0.749,
      "color": "orange",
      "maxInvariant": 0.895
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
