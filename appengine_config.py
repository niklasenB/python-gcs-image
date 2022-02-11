"""Add the lib directory to the path, so you can use libraries."""
# appengine_config.py
from google.appengine.ext import vendor


import sys
import os.path
#sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

# Add any libraries install in the "lib" folder.
vendor.add('lib')