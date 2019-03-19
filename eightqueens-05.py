"""
..B.....
.....Y..
.......P
R.......
...C....
......O.
....M...
.G......
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "blue",
      "maxInvariant": 0.088
    },
    {
      "minInvariant": 0.088,
      "color": "yellow",
      "maxInvariant": 0.230
    },
    {
      "minInvariant": 0.378,
      "color": "red",
      "maxInvariant": 0.496
    },
    {
      "minInvariant": 0.496,
      "color": "cyan",
      "maxInvariant": 0.622
    },
    {
      "minInvariant": 0.622,
      "color": "orange",
      "maxInvariant": 0.774
    },
    {
      "minInvariant": 0.774,
      "color": "magenta",
      "maxInvariant": 0.893
    },
    {
      "minInvariant": 0.893,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "blue",
      "maxInvariant": 0.440
    },
    {
      "minInvariant": 0.440,
      "color": "red",
      "maxInvariant": 0.662
    },
    {
      "minInvariant": 0.662,
      "color": "yellow",
      "maxInvariant": 0.922
    },
    {
      "minInvariant": 0.922,
      "color": "cyan",
      "maxInvariant": 1.069
    },
    {
      "minInvariant": 1.069,
      "color": "green",
      "maxInvariant": 1.181
    },
    {
      "minInvariant": 1.338,
      "color": "magenta",
      "maxInvariant": 1.524
    },
    {
      "minInvariant": 1.524,
      "color": "orange",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -0.585,
      "color": "yellow",
      "maxInvariant": -0.418
    },
    {
      "minInvariant": -0.418,
      "color": "blue",
      "maxInvariant": -0.211
    },
    {
      "minInvariant": -0.211,
      "color": "orange",
      "maxInvariant": -0.003
    },
    {
      "minInvariant": -0.003,
      "color": "cyan",
      "maxInvariant": 0.184
    },
    {
      "minInvariant": 0.184,
      "color": "magenta",
      "maxInvariant": 0.315
    },
    {
      "minInvariant": 0.315,
      "color": "red",
      "maxInvariant": 0.530
    },
    {
      "minInvariant": 0.530,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.118
    },
    {
      "minInvariant": 0.118,
      "color": "green",
      "maxInvariant": 0.266
    },
    {
      "minInvariant": 0.266,
      "color": "blue",
      "maxInvariant": 0.410
    },
    {
      "minInvariant": 0.410,
      "color": "cyan",
      "maxInvariant": 0.521
    },
    {
      "minInvariant": 0.521,
      "color": "magenta",
      "maxInvariant": 0.643
    },
    {
      "minInvariant": 0.643,
      "color": "yellow",
      "maxInvariant": 0.759
    },
    {
      "minInvariant": 0.759,
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
