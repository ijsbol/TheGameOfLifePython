# The Game of Life
 The Game of Life but programmed in Python

## How to use the interactive editor.
Install the requirements using `pip install -r requirements.txt` (or `python -m pip install -r requirements.txt`)

Launch the interactive editor using `python interactive-editor.py`.

Click the squares you wish to make alive / kill (click once to make alive (white) click again to kill (black))

To start the simulation, press the `space` key, to stop the simulation / edit it, press the `tab` key.

![img](https://i.imgur.com/csVOmRi.gif)

## How to run via python files.
Download the files and run `python visual-editor.py` or `python manual-editor.py` in your terminal.

## How to edit
You can either (painfully) edit `manual-editor.py`, or, alternatively, use the `visual-editor.py` file and edit the `STARTING_GENERATION` variable where you can visually change the starting generation.

## Example
![img](https://i.imgur.com/D93VuKk.gif)

## Emojis don't display in my terminal!
First of all, get a better terminal, second, you can disable the emojis by going to `life/__init__.py` and changing `FANCY_MODE` from `True` to `False`. Here you can also change the overall look of the game.

## Extra debug information
Parse the following into `life.Board()` as kwargs for debug features;
|kwarg|Explanation|
|--|--|
|`debug=True`|Enables debug features.|
|`display_as_numbers=True`|Displays cells as the number of alive cells surrounding them.|
|`advanced_number_display=True`|Displays cells as the number of alive cells surrounding them as well as provides information on the cells current alive/dead state.|
|`label_axis=True`|Will label the x & y axis - this breaks for x/y values <10.|
|`wrapping=True`|Will allow the board to act as an infinte plane.|
|`random_start=True`|Allows the board to be initialised with a random layout.|