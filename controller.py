#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Flask plot test

inspired by:
http://hplgit.github.io/web4sciapps/doc/web/index.html


"""
from model import InputForm
from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from compute import compute
from bokeh.resources import INLINE
import subprocess

app = Flask(__name__)
Bootstrap(app)


def run_cmd(cmd_string):
    try:
        p = subprocess.Popen(cmd_string.split(),
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        ok = p.wait()
        out, err = p.communicate()
    except FileNotFoundError:
        out = b''
        err = b''
        ok = True

    return ok, out, err


@app.route('/_get_date', methods=['GET', 'POST'])
def _get_date():
    ok, out, err = run_cmd('date')
    return jsonify(result=out.decode('utf-8'))


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)

    if request.method == 'POST' and form.validate():
        plot_script, plot_div = compute(form.A.data, form.b.data,
                                        form.w.data, form.T.data)
    else:
        plot_script, plot_div = compute(1, 0.1, 1, 20)

    return render_template('view.html',
                           form=form,
                           plot_script=plot_script,
                           plot_div=plot_div,
                           )


if __name__ == '__main__':
    app.run(debug=True)
