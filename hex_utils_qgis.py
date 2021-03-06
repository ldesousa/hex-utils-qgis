# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HexUtilsQGis
                                 A QGIS plugin
 Tool-kit for HexASCII rasters
                              -------------------
        begin                : 2017-03-21
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Luís Moreira de Sousa
        email                : luis.de.sousa@protonmail.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon, QFileDialog, QPushButton, QColor
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from dialogue_load import DialogueLoad
from dialogue_new import DialogueNew
import os.path

from qgis.gui import QgsMessageBar 
from qgis.core import QgsRendererRangeV2, QgsGraduatedSymbolRendererV2, QgsFillSymbolV2
from hex_utils.hasc import HASC


class HexUtilsQGis:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'HexUtilsQGis_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)


        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Hexagonal Rasters')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'HexUtilsQGis')
        self.toolbar.setObjectName(u'HexUtilsQGis')
        
       

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('HexUtilsQGis', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)
        
        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/HexUtilsQGis/icons/Load.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Load HexASCII raster'),
            callback=self.run,
            parent=self.iface.mainWindow())
        
        # Create the dialog (after translation) and keep reference
        self.dlg = DialogueLoad()
        # Activate file search button
        self.dlg.lineEdit.clear()
        self.dlg.pushButton.clicked.connect(self.select_file)
        
        self.add_action(
            ':/plugins/HexUtilsQGis/icons/New.png',
            text=self.tr(u'Create new HexASCII raster'),
            callback=self.runNew,
            parent=self.iface.mainWindow())

        # Create New dialogue
        self.dlgNew = DialogueNew()
        

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Hexagonal Rasters'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar


    def run(self):
        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            fileName = self.dlg.lineEdit.text()
            
            # Load the HexASCII file
            hexASCII = HASC()
            try:
                hexASCII.loadFromFile(fileName)
                hexASCII.saveAsGML(fileName + ".gml")
            except (ValueError, IOError) as ex:
                self.iface.messageBar().pushMessage(
                     "Error", "Failed to load the raster %s: %s" % (fileName, ex), 
                     level=QgsMessageBar.CRITICAL)

            # Add HexASCII to the layer heap    
            vector = fileName.split("/")
            layerName = vector[len(vector)-1]
            layerName = layerName.split(".")[0]
            layer = self.iface.addVectorLayer(fileName + ".gml", layerName, "ogr")
            if not layer:
                self.iface.messageBar().pushMessage(
                     "Error", "Failed to add raster to the layer heap", 
                     level=QgsMessageBar.CRITICAL)    

            self.createChoropleth(layer, hexASCII.min, hexASCII.max)


    def runNew(self):
        """Run method that performs all the real work"""
        # Show the dialog and set the interface instance
        # Dialogue interaction is handed by the class itself
        self.dlgNew.show()
        self.dlgNew.iface = self.iface 
                

    def createChoropleth(self, layer, min, max, num_classes = 10):
        
        myTargetField = HASC().valueField 
        myRangeList = []
        myOpacity = 1
        
        step = (max - min) / num_classes
        col_step = 256 / (num_classes - 1)
        
        for i in range(num_classes):
            label = str(min + step * i) + " - " + str(min + step * (i + 1))
            hex_level = hex(int(col_step * i)).split('x')[1]
            if (len(hex_level) < 2):
                hex_level = "0" + hex_level
            colour = "#" + hex_level + hex_level + hex_level 
            symbol = QgsFillSymbolV2.createSimple(
                {'color': colour, 
                 'color_border': colour,
                 'width_border':'0'})
            symbol.setAlpha(myOpacity)
            myRangeList.append(QgsRendererRangeV2(min + step * i, min + step * (i + 1), symbol, label))

        renderer = QgsGraduatedSymbolRendererV2('', myRangeList)
        renderer.setMode(QgsGraduatedSymbolRendererV2.EqualInterval)
        renderer.setClassAttribute(myTargetField)
        layer.setRendererV2(renderer)

        
    def select_file(self):
        fileName = QFileDialog.getOpenFileName(self.dlg, "Select file ","", '*.hasc');
        self.dlg.lineEdit.setText(fileName)
