"""
....M...
.G......
...C....
......O.
..B.....
.......P
.....Y..
R.......
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "magenta",
      "maxInvariant": 0.086
    },
    {
      "minInvariant": 0.086,
      "color": "green",
      "maxInvariant": 0.199
    },
    {
      "minInvariant": 0.199,
      "color": "cyan",
      "maxInvariant": 0.292
    },
    {
      "minInvariant": 0.292,
      "color": "orange",
      "maxInvariant": 0.416
    },
    {
      "minInvariant": 0.557,
      "color": "blue",
      "maxInvariant": 0.658
    },
    {
      "minInvariant": 0.768,
      "color": "yellow",
      "maxInvariant": 0.911
    },
    {
      "minInvariant": 0.911,
      "color": "red",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "green",
      "maxInvariant": 0.534
    },
    {
      "minInvariant": 0.534,
      "color": "magenta",
      "maxInvariant": 0.692
    },
    {
      "minInvariant": 0.692,
      "color": "cyan",
      "maxInvariant": 0.813
    },
    {
      "minInvariant": 0.813,
      "color": "blue",
      "maxInvariant": 0.946
    },
    {
      "minInvariant": 0.946,
      "color": "red",
      "maxInvariant": 1.047
    },
    {
      "minInvariant": 1.047,
      "color": "orange",
      "maxInvariant": 1.297
    },
    {
      "minInvariant": 1.486,
      "color": "yellow",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "magenta",
      "maxInvariant": -0.5
    },
    {
      "minInvariant": -0.5,
      "color": "orange",
      "maxInvariant": -0.412
    },
    {
      "minInvariant": -0.302,
      "color": "cyan",
      "maxInvariant": -0.108
    },
    {
      "minInvariant": -0.108,
      "color": "green",
      "maxInvariant": 0.059
    },
    {
      "minInvariant": 0.059,
      "color": "yellow",
      "maxInvariant": 0.255
    },
    {
      "minInvariant": 0.255,
      "color": "blue",
      "maxInvariant": 0.635
    },
    {
      "minInvariant": 0.635,
      "color": "red",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.167
    },
    {
      "minInvariant": 0.167,
      "color": "green",
      "maxInvariant": 0.245
    },
    {
      "minInvariant": 0.245,
      "color": "blue",
      "maxInvariant": 0.388
    },
    {
      "minInvariant": 0.388,
      "color": "cyan",
      "maxInvariant": 0.534
    },
    {
      "minInvariant": 0.534,
      "color": "magenta",
      "maxInvariant": 0.647
    },
    {
      "minInvariant": 0.647,
      "color": "yellow",
      "maxInvariant": 0.718
    },
    {
      "minInvariant": 0.718,
      "color": "orange",
      "maxInvariant": 0.841
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
