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
from PyQt4.QtGui import QMessageBox

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'dialogue_new.ui'))


class DialogueNew(QtGui.QDialog, FORM_CLASS):
    
    SOURCES = ["ASCII squared raster", "CSV file", "Python function"]
    
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
        
        
    def sourceChanged(self, i):
        
        if(self.comboBoxSource.currentText() == self.SOURCES[0]):
            self.labelPathSource.setEnabled(True)
            self.filePathSource.setEnabled(True)
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
            self.pythonModule.setEnabled(False)
            self.pythonFunction.setEnabled(False)
            self.labelPythonModule.setEnabled(False)
            self.labelPythonFunction.setEnabled(False)
            
        elif(self.comboBoxSource.currentText() == self.SOURCES[1]):
            self.labelPathSource.setEnabled(True)
            self.filePathSource.setEnabled(True)
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
            self.pythonModule.setEnabled(False)
            self.pythonFunction.setEnabled(False)
            self.labelPythonModule.setEnabled(False)
            self.labelPythonFunction.setEnabled(False)
            
        elif(self.comboBoxSource.currentText() == self.SOURCES[2]):
            self.labelPathSource.setEnabled(False)
            self.filePathSource.setEnabled(False)
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
            self.pythonModule.setEnabled(True)
            self.pythonFunction.setEnabled(True)            
            self.labelPythonModule.setEnabled(True)
            self.labelPythonFunction.setEnabled(True)
        
        else:
            return
     
    def showMessage(self, msg):
                  
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("This is a message box")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("MessageBox demo")
        msg.setDetailedText(msg)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.msgbtn)
    
        retval = msg.exec_()
        print "value of pressed message box button:", retval
        
    def msgbtn(self, i):
        print "Button pressed is:",i.text()
        
        
        
        
        