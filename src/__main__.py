###################################
## Driftwood 2D Game Dev. Suite  ##
## __main__.py                   ##
## Copyright 2014 PariahSoft LLC ##
###################################

## **********
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to
## deal in the Software without restriction, including without limitation the
## rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
## sell copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
##
## The above copyright notice and this permission notice shall be included in
## all copies or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
## FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
## IN THE SOFTWARE.
## **********

import signal
import sys
from sdl2 import *
import sdl2.ext as sdl2ext

VCUR = sys.version_info
VREQ = [3, 3, 3]

# We have to do this here before we start pulling in nonexistent imports.
if __name__ == "__main__":
    print("Driftwood 2D\nStarting up...")

    # Check Python version.
    if VCUR[0] < VREQ[0] or VCUR[1] < VREQ[1] or VCUR[2] < VREQ[2]:
        print("[0] FATAL: python >= {0}.{1}.{2} required, found python {3}.{4}.{5}".format(VREQ[0], VREQ[1], VREQ[2],
                                                                                           VCUR[0], VCUR[1], VCUR[2]))
        sys.exit(1)

import config
import log
import database
import filetype
import tick
import path
import cache
import resource
import input
import window
import entity
import area
import script


class Driftwood:
    """The top-level base class

    This class contains the top level manager class instances and the mainloop. The instance of this class is
    passed to scripts as an API reference.
    """

    def __init__(self):
        """Base class initializer.

        Initialize base class and manager classes. Manager classes and their methods form the Driftwood Scripting API.

        Attributes:
            config: ConfigManager instance.
            log: LogManager instance.
            database: DatabaseManager instance.
            filetype: Shortcut to filetype module.
            tick: TickManager instance.
            path: PathManager instance.
            cache: CacheManager instance.
            resource: ResourceManager instance.
            input: InputManager instance.
            window: WindowManager instance.
            entity: EntityManager instance.
            area: AreaManager instance.
            script: ScriptManager instance.

            running: Whether the mainloop should continue running. Set false to kill the engine.
        """
        self.config = config.ConfigManager(self)
        self.log = log.LogManager(self)
        self.database = database.DatabaseManager(self)
        self.filetype = filetype
        self.tick = tick.TickManager(self)
        self.path = path.PathManager(self)
        self.cache = cache.CacheManager(self)
        self.resource = resource.ResourceManager(self)
        self.input = input.InputManager(self)
        self.window = window.WindowManager(self)
        self.entity = entity.EntityManager(self)
        self.area = area.AreaManager(self)
        self.script = script.ScriptManager(self)

        # filetype API cleanup
        setattr(self.filetype, "renderer_ATTR", self.window.renderer)

        self.running = False

    def run(self):
        """Perform startup procedures and enter the mainloop.
        """
        # Only run if not already running.
        if not self.running:
            self.running = True

            # Execute the init function of the init script if present.
            if not self.path["init.py"]:
                self.log.log("WARNING", "Driftwood", "init.py missing, nothing will happen")
            else:
                self.script.call("init.py", "init")

            # This is the mainloop.
            while self.running:
                # Process SDL events.
                sdlevents = sdl2ext.get_events()
                for event in sdlevents:
                    if event.type == SDL_QUIT:
                        # Stop running.
                        self.running = False

                    elif event.type == SDL_KEYDOWN:
                        # Pass a keydown to the Input Manager.
                        self.input.key_down(event.key.keysym.sym)

                    elif event.type == SDL_KEYUP:
                        # Pass a keyup to the Input Manager.
                        self.input.key_up(event.key.keysym.sym)

                self.tick.tick()  # Process tick callbacks.

            print("Shutting down...")
            return 0


if __name__ == "__main__":
    # Set up the entry point.
    entry = Driftwood()

    # Make sure scripts have access to the base class.
    import builtins
    builtins.Driftwood = entry

    # Handle shutting down gracefully on INT and TERM signals.
    def sigint_handler(signum, frame):
        entry.running = False
    signal.signal(signal.SIGINT, sigint_handler)
    signal.signal(signal.SIGTERM, sigint_handler)

    # Run Driftwood and exit with its return code.
    sys.exit(entry.run())
