# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
#import wx.xrc
import wx.grid

###########################################################################
## Class maingui
###########################################################################

class maingui ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CaveControl", pos = wx.DefaultPosition, size = wx.Size( 700,550 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		sizer1 = wx.BoxSizer( wx.VERTICAL )

		self.title = wx.StaticText( self, wx.ID_ANY, u"Marquette Visualization Lab Cave Control", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.title.Wrap( -1 )

		self.title.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Corbel" ) )

		sizer1.Add( self.title, 0, wx.ALIGN_CENTER|wx.TOP, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		sizer2 = wx.BoxSizer( wx.VERTICAL )

		sizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Projectors" ), wx.VERTICAL )

		sizer6 = wx.GridSizer( 0, 2, 5, 0 )

		self.t_ppower = wx.StaticText( sizer4.GetStaticBox(), wx.ID_ANY, u"Projector Power", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.t_ppower.Wrap( -1 )

		sizer6.Add( self.t_ppower, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.c_ppower = wx.ToggleButton( sizer4.GetStaticBox(), wx.ID_ANY, u"OFF", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.c_ppower.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		sizer6.Add( self.c_ppower, 0, wx.EXPAND, 5 )

		self.t_shutters = wx.StaticText( sizer4.GetStaticBox(), wx.ID_ANY, u"Projector Shutters", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.t_shutters.Wrap( -1 )

		sizer6.Add( self.t_shutters, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.c_shutters = wx.ToggleButton( sizer4.GetStaticBox(), wx.ID_ANY, u"OPEN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.c_shutters.SetValue( True )
		self.c_shutters.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		sizer6.Add( self.c_shutters, 0, wx.EXPAND, 5 )

		self.t_floor = wx.StaticText( sizer4.GetStaticBox(), wx.ID_ANY, u"Floor Projectors", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.t_floor.Wrap( -1 )

		sizer6.Add( self.t_floor, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.c_floor = wx.ToggleButton( sizer4.GetStaticBox(), wx.ID_ANY, u"AUTO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.c_floor.SetValue( True )
		self.c_floor.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		sizer6.Add( self.c_floor, 0, wx.EXPAND, 5 )

		self.t_stereo = wx.StaticText( sizer4.GetStaticBox(), wx.ID_ANY, u"Stereoscopy (3D Mode)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.t_stereo.Wrap( -1 )

		sizer6.Add( self.t_stereo, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.c_stereo = wx.ToggleButton( sizer4.GetStaticBox(), wx.ID_ANY, u"AUTO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.c_stereo.SetValue( True )
		self.c_stereo.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		sizer6.Add( self.c_stereo, 0, wx.EXPAND, 5 )


		sizer4.Add( sizer6, 1, wx.EXPAND, 5 )


		sizer2.Add( sizer4, 4, wx.EXPAND, 5 )

		sizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Audio" ), wx.VERTICAL )

		sizer7 = wx.GridSizer( 0, 2, 5, 0 )

		self.t_audio = wx.StaticText( sizer5.GetStaticBox(), wx.ID_ANY, u"Power", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.t_audio.Wrap( -1 )

		sizer7.Add( self.t_audio, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.c_audio = wx.ToggleButton( sizer5.GetStaticBox(), wx.ID_ANY, u"OFF", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.c_audio.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		sizer7.Add( self.c_audio, 0, wx.EXPAND, 5 )

		self.t_volume = wx.StaticText( sizer5.GetStaticBox(), wx.ID_ANY, u"Volume", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.t_volume.Wrap( -1 )

		sizer7.Add( self.t_volume, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.c_volume = wx.Slider( sizer5.GetStaticBox(), wx.ID_ANY, 50, 0, 99, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
		sizer7.Add( self.c_volume, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		sizer5.Add( sizer7, 1, wx.EXPAND, 5 )


		sizer2.Add( sizer5, 2, wx.EXPAND, 5 )


		bSizer4.Add( sizer2, 2, wx.ALL|wx.EXPAND, 5 )

		sizer3 = wx.BoxSizer( wx.VERTICAL )

		self.grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid.CreateGrid( 11, 1 )
		self.grid.EnableEditing( False )
		self.grid.EnableGridLines( True )
		self.grid.EnableDragGridSize( False )
		self.grid.SetMargins( 0, 0 )

		# Columns
		self.grid.SetColSize( 0, 210 )
		self.grid.EnableDragColMove( False )
		self.grid.EnableDragColSize( False )
		self.grid.SetColLabelValue( 0, u"Response" )
		self.grid.SetColLabelSize( 34 )
		self.grid.SetColLabelAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTER )

		# Rows
		self.grid.SetRowSize( 0, 36 )
		self.grid.SetRowSize( 1, 36 )
		self.grid.SetRowSize( 2, 36 )
		self.grid.SetRowSize( 3, 36 )
		self.grid.SetRowSize( 4, 36 )
		self.grid.SetRowSize( 5, 36 )
		self.grid.SetRowSize( 6, 36 )
		self.grid.SetRowSize( 7, 36 )
		self.grid.SetRowSize( 8, 36 )
		self.grid.SetRowSize( 9, 36 )
		self.grid.SetRowSize( 10, 36 )
		self.grid.EnableDragRowSize( False )
		self.grid.SetRowLabelValue( 0, u"1" )
		self.grid.SetRowLabelValue( 1, u"2" )
		self.grid.SetRowLabelValue( 2, u"3" )
		self.grid.SetRowLabelValue( 3, u"4" )
		self.grid.SetRowLabelValue( 4, u"5" )
		self.grid.SetRowLabelValue( 5, u"6" )
		self.grid.SetRowLabelValue( 6, u"7" )
		self.grid.SetRowLabelValue( 7, u"8" )
		self.grid.SetRowLabelValue( 8, u"9" )
		self.grid.SetRowLabelValue( 9, u"10" )
		self.grid.SetRowLabelValue( 10, u"A" )
		self.grid.SetRowLabelSize( 30 )
		self.grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTER )
		sizer3.Add( self.grid, 1, wx.EXPAND|wx.TOP, 10 )


		sizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( sizer3, 1, wx.ALL|wx.EXPAND, 5 )


		sizer1.Add( bSizer4, 1, wx.EXPAND, 0 )


		self.SetSizer( sizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.quit )
		self.c_ppower.Bind( wx.EVT_TOGGLEBUTTON, self.togglePower )
		self.c_shutters.Bind( wx.EVT_TOGGLEBUTTON, self.toggleShutters )
		self.c_floor.Bind( wx.EVT_TOGGLEBUTTON, self.toggleFloor )
		self.c_stereo.Bind( wx.EVT_TOGGLEBUTTON, self.toggleStereo )
		self.c_audio.Bind( wx.EVT_TOGGLEBUTTON, self.toggleAudio )
		self.c_volume.Bind( wx.EVT_SCROLL_CHANGED, self.updateVolume )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def quit( self, event ):
		event.Skip()

	def togglePower( self, event ):
		event.Skip()

	def toggleShutters( self, event ):
		event.Skip()

	def toggleFloor( self, event ):
		event.Skip()

	def toggleStereo( self, event ):
		event.Skip()

	def toggleAudio( self, event ):
		event.Skip()

	def updateVolume( self, event ):
		event.Skip()


