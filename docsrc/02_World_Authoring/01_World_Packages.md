Driftwood 2D operates on World Packages -- zip files or directories containing game data. These are stored in the engine's data path and loaded at runtime. A given Game World may be made up of several World Packages, but at least one is necessary for the engine to run.

[TOC]

## Contents

Let's take a look at the kinds of data files one might expect to find inside a World Package.

### Init Script and Event Scripts

Event Scripts are written in Python 3, and direct the engine to perform actions by utilizing its scripting API. Without at least one event script, the engine will initialize but won't do anything. Every world must include at least one World Package containing the Init Script, "init.py", which is run first when the engine starts. Event Scripts are generally named with a ".py" extension.

### Tile and Sprite Sheets

These are png images containing a collection of tiles or sprite frames. They are generally named with a ".png" extension.

### Entity Descriptors

These are JSON files, optionally templated with Jinja2, which describe the characteristics of an entity which may be inserted into the game world. They are generally named with a ".json" extension.

### Widget Trees

These are JSON files, optionally templated with Jinja2, which describe a widget or group of widgets which can be inserted on screen. Like entity descriptors, they are generally named with a ".json" extension.

### Sound Effects and Music

These are audio files containing sound effects or music, which the engine can play. Possible formats are mp3, ogg, or flac, and they are named with the corresponding standard file extension.

### Lightmaps

These are greyscale png images which describe the shape and intensity of a light, which may be colorized and inserted into an area. They are generally named with a ".png" extension.

### Tilemaps

These are JSON files generated by the Tiled Map Editor, which describe a game area. They are generally named with a ".json" extension.

### TMX Sheets

These are JSON files generated by the Tiled Map Editor, which describe options for loading a tilemap. They are generally named with a ".json" extension.

## Notes

World Packages may contain subdirectories, and it is generally a good idea to use them to organize data when there is a large number of files. It may also be advisable to use multi-part file extensions so that files of the same filetype can be discerned by data type. For example, a tilemap file may be named "mymap.tilemap.json" so it is not mistaken for an entity descriptor.