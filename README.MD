SpriteSheet Exporter
====================

SpriteSheet Exporter is a plugin that will generate a spritesheet arranged from bottom to top placement of layers and grouped by rows.

Let's try to look at this example document structure:

    Document
    + Row 4 Column 1 (Paint layer)
    + Row 3 Column 1 (Paint layer)
    + Row 2 Column 1 (Paint layer)
    + Row 1 Column 1 (Paint layer)
    

These layers are named according to placement. A single paint layer in the top level will be considered a single row and placed in column 1. As such they will all take up a row on their own.

Note: The layers are named for demonstration purposes, they can have any name.

  

Now let's look at this second example:

    Document
    v Row 3 (Group layer)
      + Column 2 (Paint layer)
      + Column 1 (Paint layer)
    v Row 2 (Group layer)
      + Column 3 (Paint layer)
      + Column 2 (Paint layer)
      + Column 1 (Paint layer)
    + Row 1 Column 1 (Paint layer)
    

These layers are also named according to placement. Layers inside a group layer will be arranged horizontally from left to right starting from the bottom layer.

  

Now let's look at this final example:

    Document
    v Row 1 (Group layer)
      v Column 2 (Group layer)
        + Head (Paint layer)
        + Body (Paint layer)
        + Arms (Paint layer)
        + Legs (Paint layer)
      > Column 1 (Group layer)
    

Group layers inside a top-level group layer will be flattened, and the flattened version of the second-level group layer will be the output of that column.
