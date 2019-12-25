# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Agriculture Composite", pos = wx.DefaultPosition, size = wx.Size( 828,275 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bandFile = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Band File" ), wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.swir = wx.StaticText( bandFile.GetStaticBox(), wx.ID_ANY, u"SWIR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.swir.Wrap( -1 )
		bSizer4.Add( self.swir, 0, wx.ALL, 5 )
		
		self.colon = wx.StaticText( bandFile.GetStaticBox(), wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.colon.Wrap( -1 )
		bSizer4.Add( self.colon, 0, wx.ALL, 5 )
		
		self.m_filePicker1 = wx.FilePickerCtrl( bandFile.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer4.Add( self.m_filePicker1, 1, wx.ALL, 5 )
		
		
		bandFile.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.nir  = wx.StaticText( bandFile.GetStaticBox(), wx.ID_ANY, u"NIR  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nir .Wrap( -1 )
		bSizer5.Add( self.nir , 0, wx.ALL, 5 )
		
		self.colon = wx.StaticText( bandFile.GetStaticBox(), wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.colon.Wrap( -1 )
		bSizer5.Add( self.colon, 0, wx.ALL, 5 )
		
		self.m_filePicker2 = wx.FilePickerCtrl( bandFile.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer5.Add( self.m_filePicker2, 1, wx.ALL, 5 )
		
		
		bandFile.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.blue = wx.StaticText( bandFile.GetStaticBox(), wx.ID_ANY, u"Blue ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.blue.Wrap( -1 )
		bSizer6.Add( self.blue, 0, wx.ALL, 5 )
		
		self.colon = wx.StaticText( bandFile.GetStaticBox(), wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.colon.Wrap( -1 )
		bSizer6.Add( self.colon, 0, wx.ALL, 5 )
		
		self.m_filePicker3 = wx.FilePickerCtrl( bandFile.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer6.Add( self.m_filePicker3, 1, wx.ALL, 5 )
		
		
		bandFile.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.mtl = wx.StaticText( bandFile.GetStaticBox(), wx.ID_ANY, u"MTL ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mtl.Wrap( -1 )
		bSizer9.Add( self.mtl, 0, wx.ALL, 5 )
		
		self.colon = wx.StaticText( bandFile.GetStaticBox(), wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.colon.Wrap( -1 )
		bSizer9.Add( self.colon, 0, wx.ALL, 5 )
		
		self.m_filePicker4 = wx.FilePickerCtrl( bandFile.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer9.Add( self.m_filePicker4, 1, wx.ALL, 5 )
		
		
		bandFile.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( bandFile, 1, wx.EXPAND, 5 )
		
		crop = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Crop" ), wx.HORIZONTAL )
		
		upperLeft = wx.StaticBoxSizer( wx.StaticBox( crop.GetStaticBox(), wx.ID_ANY, u"Upper Left" ), wx.VERTICAL )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ULLatitude = wx.StaticText( upperLeft.GetStaticBox(), wx.ID_ANY, u"Latitude   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ULLatitude.Wrap( -1 )
		bSizer11.Add( self.ULLatitude, 0, wx.ALL, 5 )
		
		self.colon = wx.StaticText( upperLeft.GetStaticBox(), wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.colon.Wrap( -1 )
		bSizer11.Add( self.colon, 0, wx.ALL, 5 )
		
		self.latStartText = wx.TextCtrl( upperLeft.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.latStartText, 0, wx.ALL, 5 )
		
		
		bSizer10.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ULLongitude = wx.StaticText( upperLeft.GetStaticBox(), wx.ID_ANY, u"Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ULLongitude.Wrap( -1 )
		bSizer12.Add( self.ULLongitude, 0, wx.ALL, 5 )
		
		self.colon = wx.StaticText( upperLeft.GetStaticBox(), wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.colon.Wrap( -1 )
		bSizer12.Add( self.colon, 0, wx.ALL, 5 )
		
		self.lonStartText = wx.TextCtrl( upperLeft.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.lonStartText, 0, wx.ALL, 5 )
		
		
		bSizer10.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		
		upperLeft.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		
		crop.Add( upperLeft, 1, wx.EXPAND, 5 )
		
		lowerRight = wx.StaticBoxSizer( wx.StaticBox( crop.GetStaticBox(), wx.ID_ANY, u"Lower Right" ), wx.VERTICAL )
		
		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ULLatitude1 = wx.StaticText( lowerRight.GetStaticBox(), wx.ID_ANY, u"Latitude   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ULLatitude1.Wrap( -1 )
		bSizer111.Add( self.ULLatitude1, 0, wx.ALL, 5 )
		
		self.colon1 = wx.StaticText( lowerRight.GetStaticBox(), wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.colon1.Wrap( -1 )
		bSizer111.Add( self.colon1, 0, wx.ALL, 5 )
		
		self.latEndText = wx.TextCtrl( lowerRight.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.latEndText, 0, wx.ALL, 5 )
		
		
		lowerRight.Add( bSizer111, 1, wx.EXPAND, 5 )
		
		bSizer121 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ULLongitude1 = wx.StaticText( lowerRight.GetStaticBox(), wx.ID_ANY, u"Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ULLongitude1.Wrap( -1 )
		bSizer121.Add( self.ULLongitude1, 0, wx.ALL, 5 )
		
		self.colon2 = wx.StaticText( lowerRight.GetStaticBox(), wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.colon2.Wrap( -1 )
		bSizer121.Add( self.colon2, 0, wx.ALL, 5 )
		
		self.lonEndText = wx.TextCtrl( lowerRight.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer121.Add( self.lonEndText, 0, wx.ALL, 5 )
		
		
		lowerRight.Add( bSizer121, 1, wx.EXPAND, 5 )
		
		
		crop.Add( lowerRight, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( crop, 1, wx.EXPAND, 5 )
		
		processing = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Processing" ), wx.VERTICAL )
		
		self.cropButton = wx.Button( processing.GetStaticBox(), wx.ID_ANY, u"Crop", wx.DefaultPosition, wx.DefaultSize, 0 )
		processing.Add( self.cropButton, 0, wx.ALL, 5 )
		
		self.reflectanceButton = wx.Button( processing.GetStaticBox(), wx.ID_ANY, u"Reflectance", wx.DefaultPosition, wx.DefaultSize, 0 )
		processing.Add( self.reflectanceButton, 0, wx.ALL, 5 )
		
		self.compositeButton = wx.Button( processing.GetStaticBox(), wx.ID_ANY, u"Composite", wx.DefaultPosition, wx.DefaultSize, 0 )
		processing.Add( self.compositeButton, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( processing, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.showButton = wx.Button( self, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.showButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.saveButton = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.saveButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.onSwirFileChanged )
		self.m_filePicker2.Bind( wx.EVT_FILEPICKER_CHANGED, self.onNirFileChanged )
		self.m_filePicker3.Bind( wx.EVT_FILEPICKER_CHANGED, self.onBlueFileChanged )
		self.m_filePicker4.Bind( wx.EVT_FILEPICKER_CHANGED, self.onMtlFileChanged )
		self.cropButton.Bind( wx.EVT_BUTTON, self.onCropButtonClick )
		self.reflectanceButton.Bind( wx.EVT_BUTTON, self.onReflectanceButtonClick )
		self.compositeButton.Bind( wx.EVT_BUTTON, self.onCompositeButtonClick )
		self.showButton.Bind( wx.EVT_BUTTON, self.onShowButtonClick )
		self.saveButton.Bind( wx.EVT_BUTTON, self.onSaveButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onSwirFileChanged( self, event ):
		event.Skip()
	
	def onNirFileChanged( self, event ):
		event.Skip()
	
	def onBlueFileChanged( self, event ):
		event.Skip()
	
	def onMtlFileChanged( self, event ):
		event.Skip()
	
	def onCropButtonClick( self, event ):
		event.Skip()
	
	def onReflectanceButtonClick( self, event ):
		event.Skip()
	
	def onCompositeButtonClick( self, event ):
		event.Skip()
	
	def onShowButtonClick( self, event ):
		event.Skip()
	
	def onSaveButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class ShowFrame
###########################################################################

class ShowFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Hasil", pos = wx.DefaultPosition, size = wx.Size( 613,358 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.imageHolder = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"baliAgriculture2.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.imageHolder, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.closeButton = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.closeButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.closeButton.Bind( wx.EVT_BUTTON, self.onCloseButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onCloseButtonClick( self, event ):
		event.Skip()
	

