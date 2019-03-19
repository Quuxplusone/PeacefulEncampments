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
      "maxInvariant": 0.088
    },
    {
      "minInvariant": 0.088,
      "color": "yellow",
      "maxInvariant": 0.187
    },
    {
      "minInvariant": 0.350,
      "color": "blue",
      "maxInvariant": 0.590
    },
    {
      "minInvariant": 0.590,
      "color": "red",
      "maxInvariant": 0.734
    },
    {
      "minInvariant": 0.734,
      "color": "orange",
      "maxInvariant": 0.784
    },
    {
      "minInvariant": 0.784,
      "color": "magenta",
      "maxInvariant": 0.892
    },
    {
      "minInvariant": 0.892,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "cyan",
      "maxInvariant": 0.632
    },
    {
      "minInvariant": 0.632,
      "color": "yellow",
      "maxInvariant": 0.775
    },
    {
      "minInvariant": 0.775,
      "color": "blue",
      "maxInvariant": 0.854
    },
    {
      "minInvariant": 0.854,
      "color": "red",
      "maxInvariant": 1.053
    },
    {
      "minInvariant": 1.186,
      "color": "green",
      "maxInvariant": 1.302
    },
    {
      "minInvariant": 1.302,
      "color": "magenta",
      "maxInvariant": 1.473
    },
    {
      "minInvariant": 1.473,
      "color": "orange",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -0.577,
      "color": "yellow",
      "maxInvariant": -0.428
    },
    {
      "minInvariant": -0.428,
      "color": "cyan",
      "maxInvariant": -0.246
    },
    {
      "minInvariant": -0.246,
      "color": "orange",
      "maxInvariant": 0.002
    },
    {
      "minInvariant": 0.002,
      "color": "blue",
      "maxInvariant": 0.230
    },
    {
      "minInvariant": 0.230,
      "color": "magenta",
      "maxInvariant": 0.373
    },
    {
      "minInvariant": 0.373,
      "color": "red",
      "maxInvariant": 0.594
    },
    {
      "minInvariant": 0.594,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.234
    },
    {
      "minInvariant": 0.234,
      "color": "green",
      "maxInvariant": 0.311
    },
    {
      "minInvariant": 0.311,
      "color": "blue",
      "maxInvariant": 0.393
    },
    {
      "minInvariant": 0.393,
      "color": "cyan",
      "maxInvariant": 0.485
    },
    {
      "minInvariant": 0.485,
      "color": "magenta",
      "maxInvariant": 0.555
    },
    {
      "minInvariant": 0.555,
      "color": "yellow",
      "maxInvariant": 0.720
    },
    {
      "minInvariant": 0.720,
      "color": "orange",
      "maxInvariant": 0.885
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
