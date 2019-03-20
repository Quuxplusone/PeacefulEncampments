"""
...C....
......O.
R.......
.......P
....M...
.G......
.....Y..
..B.....
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "cyan",
      "maxInvariant": 0.102
    },
    {
      "minInvariant": 0.102,
      "color": "orange",
      "maxInvariant": 0.226
    },
    {
      "minInvariant": 0.226,
      "color": "red",
      "maxInvariant": 0.353
    },
    {
      "minInvariant": 0.483,
      "color": "magenta",
      "maxInvariant": 0.585
    },
    {
      "minInvariant": 0.585,
      "color": "green",
      "maxInvariant": 0.726
    },
    {
      "minInvariant": 0.726,
      "color": "yellow",
      "maxInvariant": 0.885
    },
    {
      "minInvariant": 0.885,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.410
    },
    {
      "minInvariant": 0.410,
      "color": "cyan",
      "maxInvariant": 0.654
    },
    {
      "minInvariant": 0.654,
      "color": "green",
      "maxInvariant": 0.888
    },
    {
      "minInvariant": 0.888,
      "color": "orange",
      "maxInvariant": 1.059
    },
    {
      "minInvariant": 1.059,
      "color": "magenta",
      "maxInvariant": 1.189
    },
    {
      "minInvariant": 1.189,
      "color": "blue",
      "maxInvariant": 1.299
    },
    {
      "minInvariant": 1.476,
      "color": "yellow",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "orange",
      "maxInvariant": -0.594
    },
    {
      "minInvariant": -0.435,
      "color": "cyan",
      "maxInvariant": -0.226
    },
    {
      "minInvariant": -0.226,
      "color": "magenta",
      "maxInvariant": 0.032
    },
    {
      "minInvariant": 0.032,
      "color": "yellow",
      "maxInvariant": 0.174
    },
    {
      "minInvariant": 0.174,
      "color": "red",
      "maxInvariant": 0.369
    },
    {
      "minInvariant": 0.369,
      "color": "green",
      "maxInvariant": 0.534
    },
    {
      "minInvariant": 0.534,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.110
    },
    {
      "minInvariant": 0.110,
      "color": "green",
      "maxInvariant": 0.223
    },
    {
      "minInvariant": 0.223,
      "color": "blue",
      "maxInvariant": 0.370
    },
    {
      "minInvariant": 0.370,
      "color": "cyan",
      "maxInvariant": 0.521
    },
    {
      "minInvariant": 0.521,
      "color": "magenta",
      "maxInvariant": 0.668
    },
    {
      "minInvariant": 0.668,
      "color": "yellow",
      "maxInvariant": 0.784
    },
    {
      "minInvariant": 0.784,
      "color": "orange",
      "maxInvariant": 0.890
    }
  ]
}
"""

def shift_right(j, factor):
    def inc(mn, mx):
        def f(elt):
            if elt["minInvariant"] != mn: elt["minInvariant"] += factor
            if elt["maxInvariant"] != mx: elt["maxInvariant"] += factor
            return elt
        return f
    def dec(mn, mx):
        def f(elt):
            if elt["minInvariant"] != mn: elt["minInvariant"] -= factor
            if elt["maxInvariant"] != mx: elt["maxInvariant"] -= factor
            return elt
        return f
    j["v"] = map(inc(0,1), j["v"])
    j["s"] = map(inc(0,2), j["s"])
    j["b"] = map(dec(-1,1), j["b"])
    return j

import json
import urllib

json.encoder.FLOAT_REPR = lambda f: ("%.3f" % f)

print urllib.quote(json.dumps(json.loads(x)))

print json.dumps(json.loads(urllib.unquote(
"""
"""
)), indent=2)
