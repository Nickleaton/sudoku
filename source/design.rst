Design
======

Design decisions are documented here.

I want to make it that to add a new puzzle type or constraint, that its easy to do. You don't want to
be modifying lots of different files.  Ideally you should be able to write a class or classes that
can be placed in a plugin directory, and that is sufficient.

Class Registry
--------------

Each constraint class inherits from Item. Item implements a class registry. When the class, not instance,  is created
it registers itself.

In the src.utils.load_modules file there is a function, load_modules, that loads all the modules in the
plugin directory. It's also used to load all the core modules.

Top Level Classes
-----------------

Board
~~~~~
There is a Board class. This implements boards. Here the size of the board, the number of rows and columns.
The set of digits allowed is also specified here.

Command
~~~~~~~

Commands follow the gang of four idea of a command. Something that does a little bit of work, and
can be composed together.

There's a registry for commands. To see the structure of the commands, there is a script called
generate_command_pydot.py that creates a graph of the commands.

Glyphs
~~~~~~

All images are created using SVG. To draw the svg of the board and solution, glyphs are used. They are separated
out from constraints. It's not a one to one relationship. For example there are many line like constraints, Renban,
German whispers, ... and it doesn't need different glyphs for each, just the colour changing.

HTML
~~~~

There are templates for generating answers, and these are in the HTML directory, and are jinja2 templates

Constraint
~~~~~~~~~~

Parsers
~~~~~~~


Tokens
~~~~~~

Utils
~~~~~
