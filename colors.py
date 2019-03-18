
colors = {
    'red': '#e6194b',
    'green': '#3cb44b',
    'blue': '#4363d8',
    'magenta': '#f032e6',
    'cyan': '#42d4f4',
    'yellow': '#ffe119',
    'orange': '#f58231',
    'purple': '#911eb4',
    'gray': '#a9a9a9',
    'lime': '#bfef45',
    'navy': '#000075',
    'lavender': '#e6beff',
    'black': '#000000',
    'brown': '#9a6324',
    'mint': '#aaffc3',
    'pink': '#fabebe',
    'teal': '#469990',
    'beige': '#fffac8',
    'maroon': '#800000',
    'olive': '#808000',
    'apricot': '#ffd8b1',
    'white': '#ffffff',
}

def unpackof(color):
    return (
        (color >> 16) & 0xff,
        (color >> 8) & 0xff,
        (color >> 0) & 0xff,
    )

def packof(r, g, b):
    r = int(round(r))
    g = int(round(g))
    b = int(round(b))
    r = 0 if r < 0 else 255 if r > 255 else r
    g = 0 if g < 0 else 255 if g > 255 else g
    b = 0 if b < 0 else 255 if b > 255 else b
    return (
        (r << 16) |
        (g << 8) |
        (b << 0)
    )

def grayness_of(r, g, b):
    return 0.2989*r + 0.5870*g + 0.1140*b

def desaturate(r, g, b, factor):
    gray = grayness_of(r, g, b)
    r = factor * gray + (1.0 - factor) * r
    g = factor * gray + (1.0 - factor) * g
    b = factor * gray + (1.0 - factor) * b
    r = 0 if r < 0 else 255 if r > 255 else r
    g = 0 if g < 0 else 255 if g > 255 else g
    b = 0 if b < 0 else 255 if b > 255 else b
    return r, g, b

def blacken(r, g, b, factor):
    r = factor * 0 + (1.0 - factor) * r
    g = factor * 0 + (1.0 - factor) * g
    b = factor * 0 + (1.0 - factor) * b
    return r, g, b

def whiten(r, g, b, factor):
    r = factor * 255 + (1.0 - factor) * r
    g = factor * 255 + (1.0 - factor) * g
    b = factor * 255 + (1.0 - factor) * b
    return r, g, b

def stripefillof(color):
    # This is the thing that used to be e.g. "F0D0D0" for red. Stripe fill (0.25).
    r, g, b = unpackof(color)
    r, g, b = whiten(r, g, b, 0.75)
    return packof(r, g, b)

def handlefillof(color):
    # This is the thing that used to be e.g. "F00000" for red. Handle fill (0.5), and stripe stroke (0.25), and encampment stroke (1).
    r, g, b = unpackof(color)
    r, g, b = desaturate(r, g, b, -0.25)
    return packof(r, g, b)

def stripestrokeof(color):
    return handlefillof(color)

def encampmentstrokeof(color):
    if color == 0xe6194b:
        return 0xff0000
    if color == 0x3cb44b:
        return 0x008000
    return handlefillof(color)

def handlestrokeof(color):
    # This is the thing that used to be e.g. "C00000" for red. Handle stroke (0.8).
    r, g, b = unpackof(color)
    r, g, b = desaturate(r, g, b, -0.25)
    r, g, b = blacken(r, g, b, 0.25)
    return packof(r, g, b)

def encampmentfillof(color):
    # This is the thing that used to be e.g. "F04040" for red. Encampment fill (1).
    return color

if __name__ == '__main__':
    for name, colorhex in colors.iteritems():
        color = int(colorhex[1:], 16)
        print '  .demo .%s { fill:#%06x; stroke:#%06x; stroke-width:2px; vector-effect:non-scaling-stroke; opacity:0.25; }' % (
            name, stripefillof(color), stripestrokeof(color)
        )

    for name, colorhex in colors.iteritems():
        color = int(colorhex[1:], 16)
        print '  .demo .%s_encampment { fill:#%06x; stroke:#%06x; stroke-width:4px; vector-effect:non-scaling-stroke; opacity:1; }' % (
            name, encampmentfillof(color), encampmentstrokeof(color)
        )

    for name, colorhex in colors.iteritems():
        color = int(colorhex[1:], 16)
        print '  .demo .%s_handle { fill:#%06x; stroke:#%06x; stroke-width:2px; vector-effect:non-scaling-stroke; fill-opacity:0.5; stroke-opacity:0.8; }' % (
            name, handlefillof(color), handlestrokeof(color)
        )
