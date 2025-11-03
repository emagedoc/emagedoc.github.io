#!/usr/bin/env python3
import json
import os
import sys

from flask import Flask, render_template
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

pages_insights = [p for p in pages if p.path.startswith('insights/')]
pages_arenas = [p for p in pages if p.path.startswith('arenas/')]

# Routes
@app.route('/')
def index():
    with open('data/leaderboards.json') as leaderboards:
        return render_template('index.html', leaderboards=json.load(leaderboards))

@app.route('/<path:path>/')
def page(path):
    return render_template('page.html', page=pages.get_or_404(path))

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/team/')
def team():
    return render_template('team.html')

@app.route('/insights/')
def insights():
    return render_template('insights.html', pages=pages_insights)

@app.route('/insights/<path:path>/')
def insight(path):
    return render_template('page.html', page=pages.get_or_404('insights/' + path))

@app.route('/arenas/')
def arenas():
    return render_template('arenas.html', pages=pages_arenas)

@app.route('/arenas/<path:path>/')
def arena(path):
    return render_template('arena.html', page=pages.get_or_404('arenas/' + path))

@app.errorhandler(404)
def page_not_found(path):
    return render_template('404.html'), 404

# Freezer generators
@freezer.register_generator
def page():
    for p in pages:
        if not p.path.startswith(('insights/', 'arenas/')):
            yield {'path': p.path}

@freezer.register_generator
def insight():
    for p in pages_insights:
        yield {'path': p.path[9:]}  # Strip 'insights/' prefix

@freezer.register_generator
def arena():
    for p in pages_arenas:
        yield {'path': p.path[7:]}  # Strip 'arenas/' prefix

@freezer.register_generator
def static():
    for dirpath, dirnames, filenames in os.walk('static'):
        for filename in filenames:
            rel_dir = os.path.relpath(dirpath, 'static')
            rel_file = os.path.join(rel_dir, filename) if rel_dir != '.' else filename
            yield {'filename': rel_file}


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        port = int(os.environ.get('PORT', 5001))
        app.run(host='0.0.0.0', port=port)
