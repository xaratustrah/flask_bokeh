#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Flask plot test

based on:
http://hplgit.github.io/web4sciapps/doc/web/index.html
"""

from numpy import exp, cos, linspace
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool

TOOLS = "resize,crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select,hover"

hover = HoverTool(
    tooltips=[
        ("index", "$index"),
        ("(x,y)", "($x, $y)"),
        ("desc", "@desc"),
    ]
)


def damped_vibrations(t, A, b, w):
    return A * exp(-b * t) * cos(w * t)


def compute(A, b, w, T, resolution=500):
    """Return filename of plot of the damped_vibration function."""
    t = linspace(0, T, resolution + 1)
    u = damped_vibrations(t, A, b, w)

    plot = figure(tools=TOOLS)
    plot.line(t, u)
    return components(plot)


if __name__ == '__main__':
    print(compute(1, 0.1, 1, 20))
