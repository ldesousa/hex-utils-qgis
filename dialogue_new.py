# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HexUtilsQGisDialog
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

import os

from PyQt4 import QtGui, uic
from PyQt4.QtGui import QMessageBox, QFileDialog
from qgis.gui import QgsMessageBar 

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'dialogue_new.ui'))


class DialogueNew(QtGui.QDialog, FORM_CLASS):
    
    SOURCES = ["ASCII squared raster", "CSV file", "Python function"]
    
    iface = None
    
    def __init__(self, parent=None):
        """Constructor."""
        super(DialogueNew, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        
        self.comboBoxSource.addItems(self.SOURCES)
        self.comboBoxSource.currentIndexChanged.connect(self.sourceChanged)
        
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        # Activate file search button
        self.pushButtonSource.clicked.connect(self.selectFileSource)
        
        
    def accept(self):
        
        self.checkOptions()
        
        
    def reject(self):
        
        self.done(0)
        
    
    def selectFileSource(self):
        
        extension = ""
        if(self.comboBoxSource.currentText() == self.SOURCES[0]):
            extension = '*.asc'
        elif(self.comboBoxSource.currentText() == self.SOURCES[1]):
            extension = '*.csv'
        elif(self.comboBoxSource.currentText() == self.SOURCES[2]):
            extension = '*.py'
        
        fileNameSource = QFileDialog.getOpenFileName(self, "Select file ","", extension);
        self.filePathSource.setText(fileNameSource)
        
        
    def sourceChanged(self, i):
        
        if(self.comboBoxSource.currentText() == self.SOURCES[0]):
            self.pushButtonSource.setEnabled(True)
            self.labelExtent.setEnabled(False)
            self.labelNorthingTop.setEnabled(False)
            self.labelNorthingBottom.setEnabled(False)
            self.labelEastingRight.setEnabled(False)
            self.labelEastingLeft.setEnabled(False)
            self.northingTop.setEnabled(False)
            self.northingBottom.setEnabled(False)
            self.eastingRight.setEnabled(False)
            self.eastingLeft.setEnabled(False)
            self.labelMethod.setEnabled(False)
            self.comboBoxMethod.setEnabled(False)
            self.pythonFunction.setEnabled(False)
            self.labelPythonFunction.setEnabled(False)
            
        elif(self.comboBoxSource.currentText() == self.SOURCES[1]):
            self.pushButtonSource.setEnabled(True)
            self.labelExtent.setEnabled(True)
            self.labelNorthingTop.setEnabled(True)
            self.labelNorthingBottom.setEnabled(True)
            self.labelEastingRight.setEnabled(True)
            self.labelEastingLeft.setEnabled(True)
            self.northingTop.setEnabled(True)
            self.northingBottom.setEnabled(True)
            self.eastingRight.setEnabled(True)
            self.eastingLeft.setEnabled(True)
            self.labelMethod.setEnabled(True)
            self.comboBoxMethod.setEnabled(True)
            self.pythonFunction.setEnabled(False)
            self.labelPythonFunction.setEnabled(False)
            
        elif(self.comboBoxSource.currentText() == self.SOURCES[2]):
            self.pushButtonSource.setEnabled(False)
            self.labelExtent.setEnabled(True)
            self.labelNorthingTop.setEnabled(True)
            self.labelNorthingBottom.setEnabled(True)
            self.labelEastingRight.setEnabled(True)
            self.labelEastingLeft.setEnabled(True)
            self.northingTop.setEnabled(True)
            self.northingBottom.setEnabled(True)
            self.eastingRight.setEnabled(True)
            self.eastingLeft.setEnabled(True)
            self.labelMethod.setEnabled(False)
            self.comboBoxMethod.setEnabled(False)
            self.pythonFunction.setEnabled(True)            
            self.labelPythonFunction.setEnabled(True)
        
        else:
            return
        
        
    def checkOptions(self):
        
        if(self.comboBoxSource.currentText() == ""):
            self.showErrorMessage("Please select a source type.")
            return False
        
        if(self.filePathNew.text() == None or self.filePathNew.text() == ""):
            self.showErrorMessage("Please provide an output file.")
            return False
        
        if(self.filePathSource.text() == None or self.filePathSource.text() == ""):
            self.showErrorMessage("Please select a source file.")
            return False

        if(self.comboBoxSource.currentText() != self.SOURCES[2]):
            if(self.northingTop.text() == None or self.northingTop.text() == "" or 
               self.northingBottom.text() == None or self.northingBottom.text() == "" or
               self.eastingRight.text() == None or self.eastingRight.text() == "" or
               self.eastingLeft.text() == None or self.eastingLeft.text() == ""):
                self.showErrorMessage("Extent is mandatory for this source type.")
                return False               
            if(self.pythonModule.text() == None or self.pythonModule.text() == ""):
                self.showErrorMessage("Please select a Python module.")
                return False
            if(self.pythonFunction.text() == None or self.pythonFunction.text() == ""):
                self.showErrorMessage("Please select a Python function in the module.")
                return False
            
        return True
     
     
    def showErrorMessage(self, mesg):
                  
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(mesg)
        msgBox.setWindowTitle("Unable to proceed")
        msgBox.exec_()

        
        
        
        
        