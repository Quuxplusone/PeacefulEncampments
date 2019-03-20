"""
.....Y..
.G......
......O.
R.......
...C....
.......P
....M...
..B.....
"""

x = """
{
  "h": [
    {
      "minInvariant": 0,
      "color": "yellow",
      "maxInvariant": 0.094
    },
    {
      "minInvariant": 0.094,
      "color": "green",
      "maxInvariant": 0.222
    },
    {
      "minInvariant": 0.222,
      "color": "orange",
      "maxInvariant": 0.387
    },
    {
      "minInvariant": 0.387,
      "color": "red",
      "maxInvariant": 0.481
    },
    {
      "minInvariant": 0.481,
      "color": "cyan",
      "maxInvariant": 0.591
    },
    {
      "minInvariant": 0.756,
      "color": "magenta",
      "maxInvariant": 0.884
    },
    {
      "minInvariant": 0.884,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "green",
      "maxInvariant": 0.454
    },
    {
      "minInvariant": 0.454,
      "color": "red",
      "maxInvariant": 0.674
    },
    {
      "minInvariant": 0.674,
      "color": "yellow",
      "maxInvariant": 0.893
    },
    {
      "minInvariant": 0.893,
      "color": "cyan",
      "maxInvariant": 1.087
    },
    {
      "minInvariant": 1.087,
      "color": "orange",
      "maxInvariant": 1.236
    },
    {
      "minInvariant": 1.236,
      "color": "blue",
      "maxInvariant": 1.367
    },
    {
      "minInvariant": 1.367,
      "color": "magenta",
      "maxInvariant": 1.559
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "yellow",
      "maxInvariant": -0.627
    },
    {
      "minInvariant": -0.627,
      "color": "orange",
      "maxInvariant": -0.408
    },
    {
      "minInvariant": -0.183,
      "color": "green",
      "maxInvariant": -0.018
    },
    {
      "minInvariant": -0.018,
      "color": "cyan",
      "maxInvariant": 0.133
    },
    {
      "minInvariant": 0.133,
      "color": "magenta",
      "maxInvariant": 0.276
    },
    {
      "minInvariant": 0.276,
      "color": "red",
      "maxInvariant": 0.478
    },
    {
      "minInvariant": 0.478,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.157
    },
    {
      "minInvariant": 0.157,
      "color": "green",
      "maxInvariant": 0.284
    },
    {
      "minInvariant": 0.284,
      "color": "blue",
      "maxInvariant": 0.411
    },
    {
      "minInvariant": 0.411,
      "color": "cyan",
      "maxInvariant": 0.549
    },
    {
      "minInvariant": 0.549,
      "color": "magenta",
      "maxInvariant": 0.679
    },
    {
      "minInvariant": 0.679,
      "color": "yellow",
      "maxInvariant": 0.811
    },
    {
      "minInvariant": 0.811,
      "color": "orange",
      "maxInvariant": 0.916
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
print urllib.quote(json.dumps(json.loads(x)))

json.encoder.FLOAT_REPR = lambda f: ("%.3f" % f)

print json.dumps(json.loads(urllib.unquote(
"""
"""
)), indent=2)
