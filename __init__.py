# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HexUtilsQGis
                                 A QGIS plugin
 Tool-kit for HexASCII rasters
                             -------------------
        begin                : 2017-03-21
        copyright            : (C) 2017 by Luís Moreira de Sousa
        email                : luis.de.sousa@protonmail.ch
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load HexUtilsQGis class from file HexUtilsQGis.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from hex_utils_qgis import HexUtilsQGis
    return HexUtilsQGis(iface)
