# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
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

		s_main = wx.BoxSizer( wx.VERTICAL )

		self.title = wx.StaticText( self, wx.ID_ANY, u"Marquette Visualization Lab Cave Control", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.title.Wrap( -1 )

		self.title.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Corbel" ) )

		s_main.Add( self.title, 0, wx.ALIGN_CENTER|wx.TOP, 5 )

		s_body = wx.BoxSizer( wx.HORIZONTAL )

		s_left = wx.BoxSizer( wx.VERTICAL )

		s_proj = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Projectors" ), wx.VERTICAL )

		s_grid1 = wx.GridSizer( 0, 2, 5, 0 )

		self.t_ppower = wx.StaticText( s_proj.GetStaticBox(), wx.ID_ANY, u"Projector Power", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.t_ppower.Wrap( -1 )

		s_grid1.Add( self.t_ppower, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.c_ppower = wx.ToggleButton( s_proj.GetStaticBox(), wx.ID_ANY, u"OFF", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.c_ppower.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		s_grid1.Add( self.c_ppower, 0, wx.EXPAND, 5 )

		self.t_shutters = wx.StaticText( s_proj.GetStaticBox(), wx.ID_ANY, u"All Shutters", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.t_shutters.Wrap( -1 )

		s_grid1.Add( self.t_shutters, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.c_shutters = wx.ToggleButton( s_proj.GetStaticBox(), wx.ID_ANY, u"OPEN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.c_shutters.SetValue( True )
		self.c_shutters.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		s_grid1.Add( self.c_shutters, 0, wx.EXPAND, 5 )

		self.t_powerpoint = wx.StaticText( s_proj.GetStaticBox(), wx.ID_ANY, u"Side/Floor Shutters", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.t_powerpoint.Wrap( -1 )

		s_grid1.Add( self.t_powerpoint, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.c_floor = wx.ToggleButton( s_proj.GetStaticBox(), wx.ID_ANY, u"AUTO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.c_floor.SetValue( True )
		self.c_floor.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		s_grid1.Add( self.c_floor, 0, wx.EXPAND, 5 )

		self.t_stereo = wx.StaticText( s_proj.GetStaticBox(), wx.ID_ANY, u"Stereoscopy (3D Mode)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.t_stereo.Wrap( -1 )

		s_grid1.Add( self.t_stereo, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.c_stereo = wx.ToggleButton( s_proj.GetStaticBox(), wx.ID_ANY, u"OFF", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.c_stereo.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.c_stereo.Enable( False )

		s_grid1.Add( self.c_stereo, 0, wx.EXPAND, 5 )


		s_proj.Add( s_grid1, 1, wx.EXPAND, 5 )


		s_left.Add( s_proj, 4, wx.EXPAND, 5 )

		s_audio = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Audio" ), wx.VERTICAL )

		s_grid2 = wx.GridSizer( 0, 2, 5, 0 )

		self.t_audio = wx.StaticText( s_audio.GetStaticBox(), wx.ID_ANY, u"Power", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.t_audio.Wrap( -1 )

		s_grid2.Add( self.t_audio, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.c_audio = wx.ToggleButton( s_audio.GetStaticBox(), wx.ID_ANY, u"OFF", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.c_audio.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		s_grid2.Add( self.c_audio, 0, wx.EXPAND, 5 )

		self.t_volume = wx.StaticText( s_audio.GetStaticBox(), wx.ID_ANY, u"Volume", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.t_volume.Wrap( -1 )

		s_grid2.Add( self.t_volume, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.c_volume = wx.Slider( s_audio.GetStaticBox(), wx.ID_ANY, 50, 0, 99, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
		s_grid2.Add( self.c_volume, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		s_audio.Add( s_grid2, 1, wx.EXPAND, 5 )


		s_left.Add( s_audio, 2, wx.EXPAND, 5 )


		s_body.Add( s_left, 2, wx.ALL|wx.EXPAND, 5 )

		s_right = wx.BoxSizer( wx.VERTICAL )

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
		s_right.Add( self.grid, 0, wx.EXPAND|wx.TOP, 9 )


		s_right.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.b_refresh = wx.Button( self, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.b_refresh.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		s_right.Add( self.b_refresh, 0, wx.EXPAND, 5 )


		s_body.Add( s_right, 1, wx.ALL|wx.EXPAND, 5 )


		s_main.Add( s_body, 1, wx.EXPAND, 0 )


		self.SetSizer( s_main )
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
		self.b_refresh.Bind( wx.EVT_BUTTON, self.refreshStatus )

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

	def refreshStatus( self, event ):
		event.Skip()


