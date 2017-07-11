Utilities for Hexagonal ASCII grids
===============================================================================


Copyright
-------------------------------------------------------------------------------

Copyright (c) 2017 Luís Moreira de Sousa. All rights reserved. 
Any use of this software constitutes full acceptance of all terms of the 
document licence.

Project updates
-------------------------------------------------------------------------------

For the latest updates please consult 
[`hex-utils` project page](https://www.researchgate.net/project/HexUtils-software-tools-for-hexagonal-rasters) 
at ResearchGate.

New information is also posted on Twitter under the [#HexASCII](https://twitter.com/hashtag/HexASCII) tag.   

Description
-------------------------------------------------------------------------------

This project provides a user interface to the [hex-utils](https://github.com/ldesousa/hex-utils) 
toolkit for the creation and display of [HexASCII](https://github.com/ldesousa/HexAsciiBNF) 
rasters.

The functionalities present are:

 - Display an HexASCII raster in QGIS, with an automatically generated 
 choropleth.
 
 - Create a new HexASCII raster from the following sources:
   - Squared raster encoded with the ESRI ASCII grammar.
   - CSV file containing point samples, i.e. (x,y,z) data triplets.
   - Mathematical surface defined as a Python function. 


Installation Requirements
-------------------------------------------------------------------------------

To use this QGis plug-in the [hex-utils](https://pypi.python.org/pypi/hex-utils) 
Python library is required. It may be installed from PyPi:

`sudo pip install hex-utils`

Visit the [hex-utils](https://github.com/ldesousa/hex-utils) repository for 
other installation options.


Installing from the QGis plug-in repository
-------------------------------------------------------------------------------

Coming soon.

Installing from GitHub
-------------------------------------------------------------------------------

1. Switch into the QGis plug-in folder:

`cd ~/.qgis2/python/plugins/`

2. Clone the repository:

`git clone https://github.com/ldesousa/hex-utils-qgis.git`

Licence
-------------------------------------------------------------------------------

This suite of programmes is released under the [EUPL 1.2 licence](https://joinup.ec.europa.eu/community/eupl/og_page/introduction-eupl-licence). 
For full details please consult the LICENCE file.
