import os
from gears.compressors import ExecCompressor


class UglifyJSCompressor(ExecCompressor):

    executable = os.path.join(os.path.dirname(__file__), 'node_modules/uglify-js/bin/uglifyjs')
    params = []
