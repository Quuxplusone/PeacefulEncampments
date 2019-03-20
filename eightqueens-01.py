"""
...C....
......O.
..B.....
.......P
.G......
....M...
R.......
.....Y..
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "cyan",
      "maxInvariant": 0.104
    },
    {
      "minInvariant": 0.104,
      "color": "orange",
      "maxInvariant": 0.227
    },
    {
      "minInvariant": 0.227,
      "color": "blue",
      "maxInvariant": 0.379
    },
    {
      "minInvariant": 0.500,
      "color": "green",
      "maxInvariant": 0.569
    },
    {
      "minInvariant": 0.569,
      "color": "magenta",
      "maxInvariant": 0.737
    },
    {
      "minInvariant": 0.737,
      "color": "red",
      "maxInvariant": 0.892
    },
    {
      "minInvariant": 0.892,
      "color": "yellow",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "cyan",
      "maxInvariant": 0.649
    },
    {
      "minInvariant": 0.649,
      "color": "blue",
      "maxInvariant": 0.715
    },
    {
      "minInvariant": 0.715,
      "color": "green",
      "maxInvariant": 0.857
    },
    {
      "minInvariant": 0.857,
      "color": "red",
      "maxInvariant": 0.898
    },
    {
      "minInvariant": 0.898,
      "color": "orange",
      "maxInvariant": 1.102
    },
    {
      "minInvariant": 1.102,
      "color": "magenta",
      "maxInvariant": 1.288
    },
    {
      "minInvariant": 1.466,
      "color": "yellow",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "orange",
      "maxInvariant": -0.588
    },
    {
      "minInvariant": -0.588,
      "color": "cyan",
      "maxInvariant": -0.446
    },
    {
      "minInvariant": -0.275,
      "color": "blue",
      "maxInvariant": 0
    },
    {
      "minInvariant": 0,
      "color": "magenta",
      "maxInvariant": 0.177
    },
    {
      "minInvariant": 0.177,
      "color": "green",
      "maxInvariant": 0.299
    },
    {
      "minInvariant": 0.299,
      "color": "yellow",
      "maxInvariant": 0.536
    },
    {
      "minInvariant": 0.536,
      "color": "red",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.186
    },
    {
      "minInvariant": 0.186,
      "color": "green",
      "maxInvariant": 0.338
    },
    {
      "minInvariant": 0.338,
      "color": "blue",
      "maxInvariant": 0.450
    },
    {
      "minInvariant": 0.450,
      "color": "cyan",
      "maxInvariant": 0.553
    },
    {
      "minInvariant": 0.553,
      "color": "magenta",
      "maxInvariant": 0.594
    },
    {
      "minInvariant": 0.594,
      "color": "yellow",
      "maxInvariant": 0.701
    },
    {
      "minInvariant": 0.701,
      "color": "orange",
      "maxInvariant": 0.822
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
