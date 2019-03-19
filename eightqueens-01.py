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
      "maxInvariant": 0.079
    },
    {
      "minInvariant": 0.079,
      "color": "orange",
      "maxInvariant": 0.190
    },
    {
      "minInvariant": 0.190,
      "color": "blue",
      "maxInvariant": 0.304
    },
    {
      "minInvariant": 0.5,
      "color": "green",
      "maxInvariant": 0.641
    },
    {
      "minInvariant": 0.641,
      "color": "magenta",
      "maxInvariant": 0.78
    },
    {
      "minInvariant": 0.78,
      "color": "red",
      "maxInvariant": 0.896
    },
    {
      "minInvariant": 0.896,
      "color": "yellow",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "cyan",
      "maxInvariant": 0.612
    },
    {
      "minInvariant": 0.612,
      "color": "blue",
      "maxInvariant": 0.682
    },
    {
      "minInvariant": 0.682,
      "color": "green",
      "maxInvariant": 0.837
    },
    {
      "minInvariant": 0.837,
      "color": "red",
      "maxInvariant": 0.895
    },
    {
      "minInvariant": 0.895,
      "color": "orange",
      "maxInvariant": 1.191
    },
    {
      "minInvariant": 1.191,
      "color": "magenta",
      "maxInvariant": 1.317
    },
    {
      "minInvariant": 1.456,
      "color": "yellow",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "orange",
      "maxInvariant": -0.573
    },
    {
      "minInvariant": -0.573,
      "color": "cyan",
      "maxInvariant": -0.45
    },
    {
      "minInvariant": -0.271,
      "color": "blue",
      "maxInvariant": 0
    },
    {
      "minInvariant": 0,
      "color": "magenta",
      "maxInvariant": 0.213
    },
    {
      "minInvariant": 0.213,
      "color": "green",
      "maxInvariant": 0.313
    },
    {
      "minInvariant": 0.313,
      "color": "yellow",
      "maxInvariant": 0.627
    },
    {
      "minInvariant": 0.627,
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
      "maxInvariant": 0.299
    },
    {
      "minInvariant": 0.299,
      "color": "blue",
      "maxInvariant": 0.410
    },
    {
      "minInvariant": 0.410,
      "color": "cyan",
      "maxInvariant": 0.547
    },
    {
      "minInvariant": 0.547,
      "color": "magenta",
      "maxInvariant": 0.59
    },
    {
      "minInvariant": 0.59,
      "color": "yellow",
      "maxInvariant": 0.701
    },
    {
      "minInvariant": 0.701,
      "color": "orange",
      "maxInvariant": 0.814
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
