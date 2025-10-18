# GuiCtrlFromHwnd

Retrieves the [GuiControl object](GuiControl.htm) of a GUI control
associated with the specified window handle.

``` Syntax
GuiControlObj := GuiCtrlFromHwnd(Hwnd)
```

## Parameters {#Parameters}

Hwnd

:   Type: [Integer](../Concepts.htm#numbers)

    The window handle (HWND) of a GUI control, or a child window of such
    a control (e.g. the Edit control of a ComboBox). The control must
    have been created by the current script via [Gui.Add](Gui.htm#Add).

## Return Value {#Return_Value}

Type: [Object](../Concepts.htm#objects) or [String
(empty)](../Concepts.htm#nothing)

This function returns the [GuiControl object](GuiControl.htm) associated
with the specified HWND, or an empty string if there isn\'t one or the
HWND is invalid.

## Remarks {#Remarks}

For example, a HWND of a GUI control can be retrieved via
[GuiControl.Hwnd](GuiControl.htm#Hwnd), [MouseGetPos](MouseGetPos.htm)
or [OnMessage](OnMessage.htm).

## Related {#Related}

[Gui()](Gui.htm#Call), [Gui object](Gui.htm), [GuiControl
object](GuiControl.htm), [GuiFromHwnd](GuiFromHwnd.htm), [Control
Types](GuiControls.htm), [ListView](ListView.htm),
[TreeView](TreeView.htm), [Menu object](Menu.htm), [Control
functions](Control.htm), [MsgBox](MsgBox.htm),
[FileSelect](FileSelect.htm), [DirSelect](DirSelect.htm)

## Examples {#Examples}

See the [ToolTip example](Gui.htm#ExToolTip) on the Gui object page.
