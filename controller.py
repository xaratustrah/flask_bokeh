#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Flask plot test

based on:
http://hplgit.github.io/web4sciapps/doc/web/index.html
"""
from model import InputForm
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from compute import compute
from bokeh.resources import INLINE

app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)

    if request.method == 'POST' and form.validate():
        plot_script, plot_div = compute(form.A.data, form.b.data,
                                        form.w.data, form.T.data)
    else:
        plot_script, plot_div = compute(1, 0.1, 1, 20)

    return render_template('view_bootstrap.html',
                           form=form,
                           plot_script=plot_script,
                           plot_div=plot_div,
                           )


if __name__ == '__main__':
    app.run(debug=True)
