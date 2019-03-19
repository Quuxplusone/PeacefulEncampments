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
      "maxInvariant": 0.105
    },
    {
      "minInvariant": 0.105,
      "color": "green",
      "maxInvariant": 0.221
    },
    {
      "minInvariant": 0.221,
      "color": "orange",
      "maxInvariant": 0.357
    },
    {
      "minInvariant": 0.357,
      "color": "blue",
      "maxInvariant": 0.486
    },
    {
      "minInvariant": 0.486,
      "color": "yellow",
      "maxInvariant": 0.626
    },
    {
      "minInvariant": 0.775,
      "color": "magenta",
      "maxInvariant": 0.883
    },
    {
      "minInvariant": 0.883,
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
      "maxInvariant": 0.643
    },
    {
      "minInvariant": 0.643,
      "color": "blue",
      "maxInvariant": 0.885
    },
    {
      "minInvariant": 0.885,
      "color": "red",
      "maxInvariant": 1.050
    },
    {
      "minInvariant": 1.050,
      "color": "orange",
      "maxInvariant": 1.184
    },
    {
      "minInvariant": 1.184,
      "color": "yellow",
      "maxInvariant": 1.355
    },
    {
      "minInvariant": 1.355,
      "color": "magenta",
      "maxInvariant": 1.529
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "orange",
      "maxInvariant": -0.476
    },
    {
      "minInvariant": -0.476,
      "color": "cyan",
      "maxInvariant": -0.338
    },
    {
      "minInvariant": -0.210,
      "color": "yellow",
      "maxInvariant": -0.074
    },
    {
      "minInvariant": -0.074,
      "color": "green",
      "maxInvariant": 0.050
    },
    {
      "minInvariant": 0.050,
      "color": "blue",
      "maxInvariant": 0.171
    },
    {
      "minInvariant": 0.171,
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
      "maxInvariant": 0.109
    },
    {
      "minInvariant": 0.109,
      "color": "green",
      "maxInvariant": 0.263
    },
    {
      "minInvariant": 0.263,
      "color": "blue",
      "maxInvariant": 0.383
    },
    {
      "minInvariant": 0.383,
      "color": "cyan",
      "maxInvariant": 0.524
    },
    {
      "minInvariant": 0.524,
      "color": "magenta",
      "maxInvariant": 0.649
    },
    {
      "minInvariant": 0.649,
      "color": "yellow",
      "maxInvariant": 0.773
    },
    {
      "minInvariant": 0.773,
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
