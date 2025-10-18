# GuiFromHwnd

Retrieves the [Gui object](Gui.htm) of a GUI window associated with the
specified window handle.

``` Syntax
GuiObj := GuiFromHwnd(Hwnd , RecurseParent)
```

## Parameters {#Parameters}

Hwnd

:   Type: [Integer](../Concepts.htm#numbers)

    The window handle (HWND) of a GUI window previously created by the
    script, or if *RecurseParent* is true, any child window of a GUI
    window created by the script.

RecurseParent

:   Type: [Boolean](../Concepts.htm#boolean)

    If this parameter is true and *Hwnd* identifies a child window which
    is not a GUI, the function searches for and retrieves its closest
    parent window which is a GUI. Otherwise, the function returns an
    empty string if *Hwnd* does not directly identify a GUI window.

## Return Value {#Return_Value}

Type: [Object](../Concepts.htm#objects) or [String
(empty)](../Concepts.htm#nothing)

This function returns the [Gui object](Gui.htm) associated with the
specified HWND, or an empty string if there isn\'t one or the HWND is
invalid.

## Remarks {#Remarks}

For example, the HWND of a GUI window may be passed to an
[OnMessage](OnMessage.htm) function, or can be retrieved via
[Gui.Hwnd](Gui.htm#Hwnd), [WinExist](WinExist.htm) or some other method.

## Related {#Related}

[Gui()](Gui.htm#Call), [Gui object](Gui.htm), [GuiControl
object](GuiControl.htm), [GuiCtrlFromHwnd](GuiCtrlFromHwnd.htm),
[Control Types](GuiControls.htm), [ListView](ListView.htm),
[TreeView](TreeView.htm), [Menu object](Menu.htm), [Control
functions](Control.htm), [MsgBox](MsgBox.htm),
[FileSelect](FileSelect.htm), [DirSelect](DirSelect.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Retrieves the Gui object by using the HWND of
the GUI window just created and reports its title.

    MyGui := Gui(, "Title of Window")
    MyGui.Add("Text",, "Some text to display.")
    MyGui.Show()

    MsgBox(GuiFromHwnd(MyGui.Hwnd).Title)
:::
