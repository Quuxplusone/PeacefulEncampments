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
      "minInvariant": 0.119,
      "color": "magenta",
      "maxInvariant": 0.225
    }, 
    {
      "minInvariant": 0.225,
      "color": "red",
      "maxInvariant": 0.398
    },
    {
      "minInvariant": 0.398,
      "color": "yellow",
      "maxInvariant": 0.559
    },
    {
      "minInvariant": 0.559,
      "color": "green",
      "maxInvariant": 0.700
    },
    {
      "minInvariant": 0.700,
      "color": "cyan",
      "maxInvariant": 0.864
    },
    {
      "minInvariant": 0.864,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "s": [
    {
      "minInvariant": 0.251,
      "color": "red",
      "maxInvariant": 0.633
    },
    {
      "minInvariant": 0.633,
      "color": "magenta",
      "maxInvariant": 0.847
    },
    {
      "minInvariant": 0.847,
      "color": "green",
      "maxInvariant": 1.072
    },
    {
      "minInvariant": 1.072,
      "color": "yellow",
      "maxInvariant": 1.312
    },
    {
      "minInvariant": 1.312,
      "color": "blue",
      "maxInvariant": 1.515
    },
    {
      "minInvariant": 1.515,
      "color": "cyan",
      "maxInvariant": 2
    }
  ],
  "b": [
    {
      "minInvariant": -1,
      "color": "magenta",
      "maxInvariant": -0.353
    },
    {
      "minInvariant": -0.353,
      "color": "yellow",
      "maxInvariant": -0.198
    },
    {
      "minInvariant": -0.198,
      "color": "cyan",
      "maxInvariant": -0.100
    },
    {
      "minInvariant": 0.091,
      "color": "red",
      "maxInvariant": 0.241
    },
    {
      "minInvariant": 0.241,
      "color": "green",
      "maxInvariant": 0.428
    },
    {
      "minInvariant": 0.428,
      "color": "blue",
      "maxInvariant": 1
    }
  ],
  "v": [
    {
      "minInvariant": 0.125,
      "color": "red",
      "maxInvariant": 0.243
    },
    {
      "minInvariant": 0.243,
      "color": "green",
      "maxInvariant": 0.359
    },
    {
      "minInvariant": 0.359,
      "color": "blue",
      "maxInvariant": 0.512
    },
    {
      "minInvariant": 0.512,
      "color": "magenta",
      "maxInvariant": 0.680
    },
    {
      "minInvariant": 0.680,
      "color": "yellow",
      "maxInvariant": 0.799
    },
    {
      "minInvariant": 0.799,
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

import json
import urllib
print urllib.quote(json.dumps(json.loads(x)))

json.encoder.FLOAT_REPR = lambda f: ("%.3f" % f)

print json.dumps(json.loads(urllib.unquote(
"""
%7B%22v%22%3A%5B%7B%22minInvariant%22%3A0.125%2C%22maxInvariant%22%3A0.243%2C%22color%22%3A%22red%22%7D%2C%7B%22minInvariant%22%3A0.243%2C%22maxInvariant%22%3A0.359%2C%22color%22%3A%22green%22%7D%2C%7B%22minInvariant%22%3A0.359%2C%22maxInvariant%22%3A0.512%2C%22color%22%3A%22blue%22%7D%2C%7B%22minInvariant%22%3A0.512%2C%22maxInvariant%22%3A0.68%2C%22color%22%3A%22magenta%22%7D%2C%7B%22minInvariant%22%3A0.68%2C%22maxInvariant%22%3A0.799%2C%22color%22%3A%22yellow%22%7D%2C%7B%22minInvariant%22%3A0.799%2C%22maxInvariant%22%3A1%2C%22color%22%3A%22cyan%22%7D%5D%2C%22h%22%3A%5B%7B%22minInvariant%22%3A0.119%2C%22maxInvariant%22%3A0.225%2C%22color%22%3A%22magenta%22%7D%2C%7B%22minInvariant%22%3A0.225%2C%22maxInvariant%22%3A0.398%2C%22color%22%3A%22red%22%7D%2C%7B%22minInvariant%22%3A0.398%2C%22maxInvariant%22%3A0.559%2C%22color%22%3A%22yellow%22%7D%2C%7B%22minInvariant%22%3A0.559%2C%22maxInvariant%22%3A0.7%2C%22color%22%3A%22green%22%7D%2C%7B%22minInvariant%22%3A0.7%2C%22maxInvariant%22%3A0.864%2C%22color%22%3A%22cyan%22%7D%2C%7B%22minInvariant%22%3A0.864%2C%22maxInvariant%22%3A1%2C%22color%22%3A%22blue%22%7D%5D%2C%22s%22%3A%5B%7B%22minInvariant%22%3A0.251%2C%22maxInvariant%22%3A0.633%2C%22color%22%3A%22red%22%7D%2C%7B%22minInvariant%22%3A0.633%2C%22maxInvariant%22%3A0.847%2C%22color%22%3A%22magenta%22%7D%2C%7B%22minInvariant%22%3A0.847%2C%22maxInvariant%22%3A1.0719999999999998%2C%22color%22%3A%22green%22%7D%2C%7B%22minInvariant%22%3A1.0719999999999998%2C%22maxInvariant%22%3A1.3120000000000005%2C%22color%22%3A%22yellow%22%7D%2C%7B%22minInvariant%22%3A1.3120000000000005%2C%22maxInvariant%22%3A1.5150000000000001%2C%22color%22%3A%22blue%22%7D%2C%7B%22minInvariant%22%3A1.5150000000000001%2C%22maxInvariant%22%3A2%2C%22color%22%3A%22cyan%22%7D%5D%2C%22b%22%3A%5B%7B%22minInvariant%22%3A-1%2C%22maxInvariant%22%3A-0.353%2C%22color%22%3A%22magenta%22%7D%2C%7B%22minInvariant%22%3A-0.353%2C%22maxInvariant%22%3A-0.198%2C%22color%22%3A%22yellow%22%7D%2C%7B%22minInvariant%22%3A-0.198%2C%22maxInvariant%22%3A-0.10000000000000002%2C%22color%22%3A%22cyan%22%7D%2C%7B%22minInvariant%22%3A0.091%2C%22maxInvariant%22%3A0.241%2C%22color%22%3A%22red%22%7D%2C%7B%22minInvariant%22%3A0.241%2C%22maxInvariant%22%3A0.428%2C%22color%22%3A%22green%22%7D%2C%7B%22minInvariant%22%3A0.428%2C%22maxInvariant%22%3A1%2C%22color%22%3A%22blue%22%7D%5D%7D
"""
)), indent=2)
