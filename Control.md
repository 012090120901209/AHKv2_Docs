# Control Functions

Functions for retrieving information about a control or for performing
various operations on a control. Click on a function name for details.

  ------------------------------------------------------------------------------------
  Function                                         Description
  ------------------------------------------------ -----------------------------------
  [ControlAddItem](ControlAddItem.htm)             Adds the specified string as a new
                                                   entry at the bottom of a ListBox or
                                                   ComboBox.

  [ControlChooseIndex](ControlChooseIndex.htm)     Sets the selection in a ListBox,
                                                   ComboBox or Tab control to be the
                                                   Nth item.

  [ControlChooseString](ControlChooseString.htm)   Sets the selection in a ListBox or
                                                   ComboBox to be the first entry
                                                   whose leading part matches the
                                                   specified string.

  [ControlClick](ControlClick.htm)                 Sends a mouse button or mouse wheel
                                                   event to a control.

  [ControlDeleteItem](ControlDeleteItem.htm)       Deletes the specified entry number
                                                   from a ListBox or ComboBox.

  [ControlFindItem](ControlFindItem.htm)           Returns the entry number of a
                                                   ListBox or ComboBox that is a
                                                   complete match for the specified
                                                   string.

  [ControlFocus](ControlFocus.htm)                 Sets input focus to a given control
                                                   on a window.

  [ControlGetChecked](ControlGetChecked.htm)       Returns a non-zero value if the
                                                   checkbox or radio button is
                                                   checked.

  [ControlGetChoice](ControlGetChoice.htm)         Returns the name of the currently
                                                   selected entry in a ListBox or
                                                   ComboBox.

  [ControlGetClassNN](ControlGetClassNN.htm)       Returns the ClassNN (class name and
                                                   sequence number) of the specified
                                                   control.

  [ControlGetEnabled](ControlGetEnabled.htm)       Returns a non-zero value if the
                                                   specified control is enabled.

  [ControlGetFocus](ControlGetFocus.htm)           Retrieves which control of the
                                                   target window has keyboard focus,
                                                   if any.

  [ControlGetHwnd](ControlGetHwnd.htm)             Returns the unique ID number of the
                                                   specified control.

  [ControlGetIndex](ControlGetIndex.htm)           Returns the index of the currently
                                                   selected entry or tab in a ListBox,
                                                   ComboBox or Tab control.

  [ControlGetItems](ControlGetItems.htm)           Returns an array of items/rows from
                                                   a ListBox, ComboBox, or
                                                   DropDownList.

  [ControlGetPos](ControlGetPos.htm)               Retrieves the position and size of
                                                   a control.

  [ControlGetStyle\                                Returns an integer representing the
  ControlGetExStyle](ControlGetStyle.htm)          style or extended style of the
                                                   specified control.

  [ControlGetText](ControlGetText.htm)             Retrieves text from a control.

  [ControlGetVisible](ControlGetVisible.htm)       Returns a non-zero value if the
                                                   specified control is visible.

  [ControlHide](ControlHide.htm)                   Hides the specified control.

  [ControlHideDropDown](ControlHideDropDown.htm)   Hides the drop-down list of a
                                                   ComboBox control.

  [ControlMove](ControlMove.htm)                   Moves or resizes a control.

  [ControlSend\                                    Sends simulated keystrokes or text
  ControlSendText](ControlSend.htm)                to a window or control.

  [ControlSetChecked](ControlSetChecked.htm)       Turns on (checks) or turns off
                                                   (unchecks) a checkbox or radio
                                                   button.

  [ControlSetEnabled](ControlSetEnabled.htm)       Enables or disables the specified
                                                   control.

  [ControlSetStyle\                                Changes the style or extended style
  ControlSetExStyle](ControlSetStyle.htm)          of the specified control,
                                                   respectively.

  [ControlSetText](ControlSetText.htm)             Changes the text of a control.

  [ControlShow](ControlShow.htm)                   Shows the specified control if it
                                                   was previously hidden.

  [ControlShowDropDown](ControlShowDropDown.htm)   Shows the drop-down list of a
                                                   ComboBox control.

  [EditGetCurrentCol](EditGetCurrentCol.htm)       Returns the column number in an
                                                   Edit control where the caret (text
                                                   insertion point) resides.

  [EditGetCurrentLine](EditGetCurrentLine.htm)     Returns the line number in an Edit
                                                   control where the caret (text
                                                   insert point) resides.

  [EditGetLine](EditGetLine.htm)                   Returns the text of the specified
                                                   line in an Edit control.

  [EditGetLineCount](EditGetLineCount.htm)         Returns the number of lines in an
                                                   Edit control.

  [EditGetSelectedText](EditGetSelectedText.htm)   Returns the selected text in an
                                                   Edit control.

  [EditPaste](EditPaste.htm)                       Pastes the specified string at the
                                                   caret (text insertion point) in an
                                                   Edit control.

  [ListViewGetContent](ListViewGetContent.htm)     Returns a list of items/rows from a
                                                   ListView.
  ------------------------------------------------------------------------------------

## The *Control* Parameter {#Parameter}

Functions which operate on individual controls have a parameter named
*Control* which supports a few different ways to identify the control.
The *Control* parameter can be one of the following:

**ClassNN** ([String](../Concepts.htm#strings)): The ClassNN (classname
and instance number) of the control, which can be determined via Window
Spy. For example \"Edit1\" is the first control with classname \"Edit\".

**Text** ([String](../Concepts.htm#strings)): The control\'s text. The
matching behavior is determined by
[SetTitleMatchMode](SetTitleMatchMode.htm).

**HWND** ([Integer](../Concepts.htm#numbers)): The control\'s HWND,
which is typically retrieved via [ControlGetHwnd](ControlGetHwnd.htm),
[MouseGetPos](MouseGetPos.htm), or [DllCall](DllCall.htm). This also
works on hidden controls even when
[DetectHiddenWindows](DetectHiddenWindows.htm) is Off. Any subsequent
window parameters are ignored.

**Object:** An object of any type with a `Hwnd` property, such as a
[GuiControl](GuiControl.htm). A [PropertyError](Error.htm#PropertyError)
is thrown if the object has no `Hwnd` property, or
[TypeError](Error.htm#TypeError) if it does not return a pure integer.
Any subsequent window parameters are ignored.

**Omitted:** A few functions are able to operate on either a control or
a top-level window. Omitting the *Control* parameter causes the function
to use the target window (specified by
*[WinTitle](../misc/WinTitle.htm)*) instead of one of its controls. For
example, [ControlSend](ControlSend.htm) can send keyboard messages
directly to the window.

## Error Handling {#Error_Handling}

Typically one of the following errors may be thrown:

-   [TargetError](Error.htm#TargetError): The target window or control
    could not be found.
-   [Error](Error.htm) or [OSError](Error.htm#OSError): There was a
    problem carring out the function\'s purpose, such as retrieving a
    setting or applying a change.
-   [ValueError](Error.htm#ValueError) or
    [TypeError](Error.htm#TypeError): Invalid parameters were detected.

## Remarks {#Remarks}

To improve reliability, a delay is done automatically after each use of
a Control function that changes a control (except for
[ControlSetStyle](ControlSetStyle.htm) and
[ControlSetExStyle](ControlSetStyle.htm)). That delay can be changed via
[SetControlDelay](SetControlDelay.htm) or by assigning a value to
[A_ControlDelay](../Variables.htm#ControlDelay). For details, see
[SetControlDelay remarks](SetControlDelay.htm#Remarks).

To discover the ClassNN or HWND of the control that the mouse is
currently hovering over, use [MouseGetPos](MouseGetPos.htm).

To retrieve an array of all controls in a window, use
[WinGetControls](WinGetControls.htm) or
[WinGetControlsHwnd](WinGetControlsHwnd.htm).

## Related {#Related}

[SetControlDelay](SetControlDelay.htm), [Win functions](Win.htm),
[GuiControl object](GuiControl.htm) (for controls created by the script)
