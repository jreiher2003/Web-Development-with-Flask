"""`appengine_config` gets loaded when starting a new application instance."""
import sys
import os.path
# add `lib` subdirectory to `sys.path`, so our `main` module can load
# third-party libraries. as in Virtualenv 
sys.path.insert(0, os.path.join(os.path.dirname('_'), 'venv/Lib/site-packages'))

