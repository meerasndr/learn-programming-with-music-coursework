"""
start.py
~~~~~~~~

This script is the main entry point. This will be
executed whenever the run button is pressed, after
saving the code in the editor as main.py.

This executes the main.py after adding all the variables
and functions defined in the music.py to the executing
environment.
"""

import music

# Execute the code in main.py with all the functions
# defined in music.py predefined
code = open("main.py").read()
env = dict(music.__dict__)
exec(code, env)