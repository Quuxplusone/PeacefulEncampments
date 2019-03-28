"""
....M...
......O.
...C....
R.......
..B.....
.......P
.....Y..
.G......
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "magenta",
      "maxInvariant": 0.119
    },
    {
      "minInvariant": 0.119,
      "color": "orange",
      "maxInvariant": 0.248
    },
    {
      "minInvariant": 0.248,
      "color": "cyan",
      "maxInvariant": 0.356
    },
    {
      "minInvariant": 0.356,
      "color": "red",
      "maxInvariant": 0.484
    },
    {
      "minInvariant": 0.484,
      "color": "blue",
      "maxInvariant": 0.600
    },
    {
      "minInvariant": 0.726,
      "color": "yellow",
      "maxInvariant": 0.836
    },
    {
      "minInvariant": 0.836,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.537
    },
    {
      "minInvariant": 0.537,
      "color": "magenta",
      "maxInvariant": 0.664
    },
    {
      "minInvariant": 0.664,
      "color": "cyan",
      "maxInvariant": 0.807
    },
    {
      "minInvariant": 0.807,
      "color": "blue",
      "maxInvariant": 0.957
    },
    {
      "minInvariant": 0.957,
      "color": "orange",
      "maxInvariant": 1.122
    },
    {
      "minInvariant": 1.122,
      "color": "green",
      "maxInvariant": 1.318
    },
    {
      "minInvariant": 1.318,
      "color": "yellow",
      "maxInvariant": 1.526
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "orange",
      "maxInvariant": -0.617
    },
    {
      "minInvariant": -0.617,
      "color": "magenta",
      "maxInvariant": -0.398
    },
    {
      "minInvariant": -0.227,
      "color": "cyan",
      "maxInvariant": -0.036
    },
    {
      "minInvariant": -0.036,
      "color": "yellow",
      "maxInvariant": 0.139
    },
    {
      "minInvariant": 0.139,
      "color": "blue",
      "maxInvariant": 0.309
    },
    {
      "minInvariant": 0.309,
      "color": "red",
      "maxInvariant": 0.542
    },
    {
      "minInvariant": 0.542,
      "color": "green",
      "maxInvariant": 0.965
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.117
    },
    {
      "minInvariant": 0.117,
      "color": "green",
      "maxInvariant": 0.268
    },
    {
      "minInvariant": 0.268,
      "color": "blue",
      "maxInvariant": 0.383
    },
    {
      "minInvariant": 0.383,
      "color": "cyan",
      "maxInvariant": 0.500
    },
    {
      "minInvariant": 0.500,
      "color": "magenta",
      "maxInvariant": 0.617
    },
    {
      "minInvariant": 0.617,
      "color": "yellow",
      "maxInvariant": 0.783
    },
    {
      "minInvariant": 0.783,
      "color": "orange",
      "maxInvariant": 0.906
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
