# Generic Ipsum: a generic dummy text generator #

Generates dummy text, based on two files: a themed file (the _generic_) and an ipsum file (the _ipsum_).
Also takes three other arguments:
* number of paragraphs: must be an integer, defaults to 5 if a value less than 1 is provided;
* uses ipsum: indicates if the dummy text generator should use or not the ipsum text. Must be one of True or False;
* comma chance: the ratio of commas in the text. Must range from 0 to 100.
