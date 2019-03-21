"""
O......
....M..
.R.....
.....Y.
..G....
......C
...B...
"""

x = """
{
  "h": [
    {
      "minInvariant": 0.128,
      "color": "magenta",
      "maxInvariant": 0.255
    }, 
    {
      "minInvariant": 0.255,
      "color": "red",
      "maxInvariant": 0.411
    },
    {
      "minInvariant": 0.411,
      "color": "yellow",
      "maxInvariant": 0.565
    },
    {
      "minInvariant": 0.565,
      "color": "green",
      "maxInvariant": 0.724
    },
    {
      "minInvariant": 0.724,
      "color": "cyan",
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
      "minInvariant": 0.275,
      "color": "red",
      "maxInvariant": 0.660
    },
    {
      "minInvariant": 0.660,
      "color": "magenta",
      "maxInvariant": 0.876
    },
    {
      "minInvariant": 0.876,
      "color": "green",
      "maxInvariant": 1.103
    },
    {
      "minInvariant": 1.103,
      "color": "yellow",
      "maxInvariant": 1.334
    },
    {
      "minInvariant": 1.334,
      "color": "blue",
      "maxInvariant": 1.549
    },
    {
      "minInvariant": 1.549,
      "color": "cyan",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "magenta",
      "maxInvariant": -0.349
    },
    {
      "minInvariant": -0.349,
      "color": "yellow",
      "maxInvariant": -0.201
    },
    {
      "minInvariant": -0.201,
      "color": "cyan",
      "maxInvariant": -0.083
    },
    {
      "minInvariant": 0.060,
      "color": "red",
      "maxInvariant": 0.223
    },
    {
      "minInvariant": 0.223,
      "color": "green",
      "maxInvariant": 0.410
    },
    {
      "minInvariant": 0.410,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0.147,
      "color": "red",
      "maxInvariant": 0.258
    },
    {
      "minInvariant": 0.258,
      "color": "green",
      "maxInvariant": 0.370
    },
    {
      "minInvariant": 0.370,
      "color": "blue",
      "maxInvariant": 0.542
    },
    {
      "minInvariant": 0.542,
      "color": "magenta",
      "maxInvariant": 0.690
    },
    {
      "minInvariant": 0.690,
      "color": "yellow",
      "maxInvariant": 0.844
    },
    {
      "minInvariant": 0.844,
      "color": "cyan",
      "maxInvariant": 1
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

def shift_downright(j, factor):
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
    j["h"] = map(inc(0,1), j["h"])
    return j

import json
import urllib

json.encoder.FLOAT_REPR = lambda f: ("%.3f" % f)

print urllib.quote(json.dumps(shift_right(json.loads(x), 0.01)))

print json.dumps(json.loads(urllib.unquote(
"""
"""
)), indent=2)
