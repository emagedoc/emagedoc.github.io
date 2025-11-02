#!/usr/bin/env python3
import json
import os
import pathlib
import shutil
import sys
from jinja2 import Environment, FileSystemLoader, select_autoescape

from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flaskext.markdown import Markdown

# Configuration
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FREEZER_RELATIVE_URLS = True
FREEZER_DESTINATION = 'build'
FREEZER_STATIC_IGNORE = ['*.git*']
FREEZER_BASE_URL = None
FREEZER_IGNORE_MIMETYPE_WARNINGS = True

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)
markdown_manager = Markdown(app, extensions=['fenced_code'], output_format='html5',)

pages_insights = [page for page in list(pages) if page.path.startswith('insights/')]
pages_arenas = [page for page in list(pages) if page.path.startswith('arenas/')]

# Routes
@app.route('/')
def index():
    with open('data/leaderboards.json') as leaderboards:
        return render_template('index.html', leaderboards=json.load(leaderboards))

@app.route('/<path:path>/')
def page(path):
    return render_template('page.html', page=pages.get_or_404(path))

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/insights')
def insights():
    return render_template('insights.html', pages=pages_insights)

@app.route('/arenas')
def arenas():
    return render_template('arenas.html', pages=pages_arenas)

@app.errorhandler(404)
def page_not_found(path):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@freezer.register_generator
def static():
    # This will yield all static files for freezing
    for dirpath, dirnames, filenames in os.walk('static'):
        for filename in filenames:
            rel_dir = os.path.relpath(dirpath, 'static')
            rel_file = os.path.join(rel_dir, filename) if rel_dir != '.' else filename
            yield {'filename': rel_file}


if __name__ == "__main__":
    print(pages)
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        port = int(os.environ.get('PORT', 5001))
        app.run(host='0.0.0.0', port=port)
