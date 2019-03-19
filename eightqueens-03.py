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
      "maxInvariant": 0.110
    },
    {
      "minInvariant": 0.110,
      "color": "green",
      "maxInvariant": 0.220
    },
    {
      "minInvariant": 0.220,
      "color": "orange",
      "maxInvariant": 0.355
    },
    {
      "minInvariant": 0.355,
      "color": "blue",
      "maxInvariant": 0.492
    },
    {
      "minInvariant": 0.492,
      "color": "yellow",
      "maxInvariant": 0.626
    },
    {
      "minInvariant": 0.776,
      "color": "magenta",
      "maxInvariant": 0.885
    },
    {
      "minInvariant": 0.885,
      "color": "red",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "green",
      "maxInvariant": 0.428
    },
    {
      "minInvariant": 0.428,
      "color": "cyan",
      "maxInvariant": 0.637
    },
    {
      "minInvariant": 0.637,
      "color": "blue",
      "maxInvariant": 0.886
    },
    {
      "minInvariant": 0.886,
      "color": "red",
      "maxInvariant": 1.046
    },
    {
      "minInvariant": 1.046,
      "color": "orange",
      "maxInvariant": 1.179
    },
    {
      "minInvariant": 1.179,
      "color": "yellow",
      "maxInvariant": 1.353
    },
    {
      "minInvariant": 1.353,
      "color": "magenta",
      "maxInvariant": 1.528
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "orange",
      "maxInvariant": -0.475
    },
    {
      "minInvariant": -0.475,
      "color": "cyan",
      "maxInvariant": -0.339
    },
    {
      "minInvariant": -0.211,
      "color": "yellow",
      "maxInvariant": -0.077
    },
    {
      "minInvariant": -0.077,
      "color": "green",
      "maxInvariant": 0.074
    },
    {
      "minInvariant": 0.074,
      "color": "blue",
      "maxInvariant": 0.175
    },
    {
      "minInvariant": 0.175,
      "color": "magenta",
      "maxInvariant": 0.629
    },
    {
      "minInvariant": 0.629,
      "color": "red",
      "maxInvariant": 1
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
      "maxInvariant": 0.232
    },
    {
      "minInvariant": 0.232,
      "color": "blue",
      "maxInvariant": 0.394
    },
    {
      "minInvariant": 0.394,
      "color": "cyan",
      "maxInvariant": 0.523
    },
    {
      "minInvariant": 0.523,
      "color": "magenta",
      "maxInvariant": 0.646
    },
    {
      "minInvariant": 0.646,
      "color": "yellow",
      "maxInvariant": 0.768
    },
    {
      "minInvariant": 0.768,
      "color": "orange",
      "maxInvariant": 0.894
    }
  ]
}
"""

import json
import urllib
print urllib.quote(json.dumps(json.loads(x)))

print json.dumps(json.loads(urllib.unquote(
"""
"""
)), indent=2)
