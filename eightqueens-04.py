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
      "maxInvariant": 0.074
    },
    {
      "minInvariant": 0.074,
      "color": "yellow",
      "maxInvariant": 0.161
    },
    {
      "minInvariant": 0.355,
      "color": "blue",
      "maxInvariant": 0.592
    },
    {
      "minInvariant": 0.592,
      "color": "red",
      "maxInvariant": 0.745
    },
    {
      "minInvariant": 0.745,
      "color": "orange",
      "maxInvariant": 0.791
    },
    {
      "minInvariant": 0.791,
      "color": "magenta",
      "maxInvariant": 0.904
    },
    {
      "minInvariant": 0.904,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0,
      "color": "cyan",
      "maxInvariant": 0.531
    },
    {
      "minInvariant": 0.531,
      "color": "yellow",
      "maxInvariant": 0.715
    },
    {
      "minInvariant": 0.715,
      "color": "blue",
      "maxInvariant": 0.803
    },
    {
      "minInvariant": 0.803,
      "color": "red",
      "maxInvariant": 0.938
    },
    {
      "minInvariant": 1.122,
      "color": "green",
      "maxInvariant": 1.248
    },
    {
      "minInvariant": 1.248,
      "color": "magenta",
      "maxInvariant": 1.406
    },
    {
      "minInvariant": 1.406,
      "color": "orange",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -0.552,
      "color": "yellow",
      "maxInvariant": -0.398
    },
    {
      "minInvariant": -0.398,
      "color": "cyan",
      "maxInvariant": -0.196
    },
    {
      "minInvariant": -0.196,
      "color": "orange",
      "maxInvariant": 0.072
    },
    {
      "minInvariant": 0.072,
      "color": "blue",
      "maxInvariant": 0.288
    },
    {
      "minInvariant": 0.288,
      "color": "magenta",
      "maxInvariant": 0.448
    },
    {
      "minInvariant": 0.448,
      "color": "red",
      "maxInvariant": 0.645
    },
    {
      "minInvariant": 0.645,
      "color": "green",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0,
      "color": "red",
      "maxInvariant": 0.178
    },
    {
      "minInvariant": 0.178,
      "color": "green",
      "maxInvariant": 0.257
    },
    {
      "minInvariant": 0.257,
      "color": "blue",
      "maxInvariant": 0.336
    },
    {
      "minInvariant": 0.336,
      "color": "cyan",
      "maxInvariant": 0.437
    },
    {
      "minInvariant": 0.437,
      "color": "magenta",
      "maxInvariant": 0.500
    },
    {
      "minInvariant": 0.500,
      "color": "yellow",
      "maxInvariant": 0.634
    },
    {
      "minInvariant": 0.634,
      "color": "orange",
      "maxInvariant": 0.843
    }
  ]
}
"""

def shift_left(j, factor):
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
    j["v"] = map(dec(0,1), j["v"])
    j["s"] = map(dec(0,2), j["s"])
    j["b"] = map(inc(-1,1), j["b"])
    return j

import json
import urllib
print urllib.quote(json.dumps(json.loads(x)))

json.encoder.FLOAT_REPR = lambda f: ("%.3f" % f)

print json.dumps(json.loads(urllib.unquote(
"""
"""
)), indent=2)
