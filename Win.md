# Win Functions

Functions for retrieving information about one or more windows or for
performing various operations on a window. Click on a function name for
details.

  ----------------------------------------------------------------------------------
  Function                                       Description
  ---------------------------------------------- -----------------------------------
  [WinActivate](WinActivate.htm)                 Activates the specified window.

  [WinActivateBottom](WinActivateBottom.htm)     Same as
                                                 [WinActivate](WinActivate.htm)
                                                 except that it activates the
                                                 bottommost matching window rather
                                                 than the topmost.

  [WinActive](WinActive.htm)                     Checks if the specified window
                                                 exists and is currently active
                                                 (foremost).

  [WinClose](WinClose.htm)                       Closes the specified window.

  [WinExist](WinExist.htm)                       Checks if the specified window
                                                 exists.

  [WinGetClass](WinGetClass.htm)                 Retrieves the specified window\'s
                                                 class name.

  [WinGetClientPos](WinGetClientPos.htm)         Retrieves the position and size of
                                                 the specified window\'s client
                                                 area.

  [WinGetControls](WinGetControls.htm)           Returns an array of names
                                                 (ClassNNs) for all controls in the
                                                 specified window.

  [WinGetControlsHwnd](WinGetControlsHwnd.htm)   Returns an array of unique ID
                                                 numbers (HWNDs) for all controls in
                                                 the specified window.

  [WinGetCount](WinGetCount.htm)                 Returns the number of existing
                                                 windows that match the specified
                                                 criteria.

  [WinGetID](WinGetID.htm)                       Returns the unique ID number (HWND)
                                                 of the specified window.

  [WinGetIDLast](WinGetIDLast.htm)               Returns the unique ID number (HWND)
                                                 of the last/bottommost window if
                                                 there is more than one match.

  [WinGetList](WinGetList.htm)                   Returns an array of unique ID
                                                 numbers (HWNDs) for all existing
                                                 windows that match the specified
                                                 criteria.

  [WinGetMinMax](WinGetMinMax.htm)               Returns a non-zero number if the
                                                 specified window is maximized or
                                                 minimized.

  [WinGetPID](WinGetPID.htm)                     Returns the Process ID number (PID)
                                                 of the specified window.

  [WinGetPos](WinGetPos.htm)                     Retrieves the position and size of
                                                 the specified window.

  [WinGetProcessName](WinGetProcessName.htm)     Returns the name of the process
                                                 that owns the specified window.

  [WinGetProcessPath](WinGetProcessPath.htm)     Returns the full path and name of
                                                 the process that owns the specified
                                                 window.

  [WinGetStyle\                                  Returns the style or extended style
  WinGetExStyle](WinGetStyle.htm)                (respectively) of the specified
                                                 window.

  [WinGetText](WinGetText.htm)                   Retrieves the text from the
                                                 specified window.

  [WinGetTitle](WinGetTitle.htm)                 Retrieves the title of the
                                                 specified window.

  [WinGetTransColor](WinGetTransColor.htm)       Returns the color that is marked
                                                 transparent in the specified
                                                 window.

  [WinGetTransparent](WinGetTransparent.htm)     Returns the degree of transparency
                                                 of the specified window.

  [WinHide](WinHide.htm)                         Hides the specified window.

  [WinKill](WinKill.htm)                         Forces the specified window to
                                                 close.

  [WinMaximize](WinMaximize.htm)                 Enlarges the specified window to
                                                 its maximum size.

  [WinMinimize](WinMinimize.htm)                 Collapses the specified window into
                                                 a button on the task bar.

  [WinMinimizeAll\                               Minimizes or unminimizes all
  WinMinimizeAllUndo](WinMinimizeAll.htm)        windows.

  [WinMove](WinMove.htm)                         Changes the position and/or size of
                                                 the specified window.

  [WinMoveBottom](WinMoveBottom.htm)             Sends the specified window to the
                                                 bottom of stack; that is, beneath
                                                 all other windows.

  [WinMoveTop](WinMoveTop.htm)                   Brings the specified window to the
                                                 top of the stack without explicitly
                                                 activating it.

  [WinRedraw](WinRedraw.htm)                     Redraws the specified window.

  [WinRestore](WinRestore.htm)                   Unminimizes or unmaximizes the
                                                 specified window if it is minimized
                                                 or maximized.

  [WinSetAlwaysOnTop](WinSetAlwaysOnTop.htm)     Makes the specified window stay on
                                                 top of all other windows (except
                                                 other always-on-top windows).

  [WinSetEnabled](WinSetEnabled.htm)             Enables or disables the specified
                                                 window.

  [WinSetRegion](WinSetRegion.htm)               Changes the shape of the specified
                                                 window to be the specified
                                                 rectangle, ellipse, or polygon.

  [WinSetStyle\                                  Changes the style or extended style
  WinSetExStyle](WinSetStyle.htm)                of the specified window,
                                                 respectively.

  [WinSetTitle](WinSetTitle.htm)                 Changes the title of the specified
                                                 window.

  [WinSetTransColor](WinSetTransColor.htm)       Makes all pixels of the chosen
                                                 color invisible inside the
                                                 specified window.

  [WinSetTransparent](WinSetTransparent.htm)     Makes the specified window
                                                 semi-transparent.

  [WinShow](WinShow.htm)                         Unhides the specified window.

  [WinWait](WinWait.htm)                         Waits until the specified window
                                                 exists.

  [WinWaitActive\                                Waits until the specified window is
  WinWaitNotActive](WinWaitActive.htm)           active or not active.

  [WinWaitClose](WinWaitClose.htm)               Waits until no matching windows can
                                                 be found.
  ----------------------------------------------------------------------------------

## Remarks {#Remarks}

To discover the unique ID number of the window that the mouse is
currently hovering over, use [MouseGetPos](MouseGetPos.htm).

## Related {#Related}

[SetWinDelay](SetWinDelay.htm), [Control functions](Control.htm), [Gui
object](Gui.htm) (for windows created by the script)
