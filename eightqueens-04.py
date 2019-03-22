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
      "maxInvariant": 0.063
    },
    {
      "minInvariant": 0.063,
      "color": "yellow",
      "maxInvariant": 0.151
    },
    {
      "minInvariant": 0.368,
      "color": "blue",
      "maxInvariant": 0.578
    },
    {
      "minInvariant": 0.578,
      "color": "red",
      "maxInvariant": 0.782
    },
    {
      "minInvariant": 0.782,
      "color": "orange",
      "maxInvariant": 0.841
    },
    {
      "minInvariant": 0.841,
      "color": "magenta",
      "maxInvariant": 0.926
    },
    {
      "minInvariant": 0.926,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "cyan",
      "maxInvariant": 0.540
    },
    {
      "minInvariant": 0.540,
      "color": "yellow",
      "maxInvariant": 0.714
    },
    {
      "minInvariant": 0.714,
      "color": "blue",
      "maxInvariant": 0.822
    },
    {
      "minInvariant": 0.822,
      "color": "red",
      "maxInvariant": 0.960
    },
    {
      "minInvariant": 1.098,
      "color": "green",
      "maxInvariant": 1.279
    },
    {
      "minInvariant": 1.279,
      "color": "magenta",
      "maxInvariant": 1.453
    },
    {
      "minInvariant": 1.453,
      "color": "orange",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -0.571,
      "color": "yellow",
      "maxInvariant": -0.410
    },
    {
      "minInvariant": -0.410,
      "color": "cyan",
      "maxInvariant": -0.160
    },
    {
      "minInvariant": -0.160,
      "color": "orange",
      "maxInvariant": 0.096
    },
    {
      "minInvariant": 0.096,
      "color": "blue",
      "maxInvariant": 0.304
    },
    {
      "minInvariant": 0.304,
      "color": "magenta",
      "maxInvariant": 0.494
    },
    {
      "minInvariant": 0.494,
      "color": "red",
      "maxInvariant": 0.700
    },
    {
      "minInvariant": 0.700,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.160
    },
    {
      "minInvariant": 0.160,
      "color": "green",
      "maxInvariant": 0.261
    },
    {
      "minInvariant": 0.261,
      "color": "blue",
      "maxInvariant": 0.326
    },
    {
      "minInvariant": 0.326,
      "color": "cyan",
      "maxInvariant": 0.442
    },
    {
      "minInvariant": 0.442,
      "color": "magenta",
      "maxInvariant": 0.521
    },
    {
      "minInvariant": 0.521,
      "color": "yellow",
      "maxInvariant": 0.669
    },
    {
      "minInvariant": 0.669,
      "color": "orange",
      "maxInvariant": 0.831
    }
  ]
}
"""

def blow_up(j, factor):
    def inc(mn, mx):
        def f(elt):
            avg = (mn + mx) / 2.0
            elt["minInvariant"] = (elt["minInvariant"] - avg) * factor + avg
            elt["minInvariant"] = max(mn, elt["minInvariant"])
            elt["maxInvariant"] = (elt["maxInvariant"] - avg) * factor + avg
            elt["maxInvariant"] = min(mx, elt["maxInvariant"])
            return elt
        return f
    j["h"] = map(inc(0,1), j["h"])
    j["v"] = map(inc(0,1), j["v"])
    j["s"] = map(inc(0,2), j["s"])
    j["b"] = map(inc(-1,1), j["b"])
    return j

import json
import urllib

json.encoder.FLOAT_REPR = lambda f: ("%.3f" % f)

print urllib.quote(json.dumps(json.loads(x)))

print json.dumps(json.loads(urllib.unquote(
"""
"""
)), indent=2)
