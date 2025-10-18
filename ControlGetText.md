# ControlGetText

Retrieves text from a control.

``` Syntax
Text := ControlGetText(Control , WinTitle, WinText, ExcludeTitle, ExcludeText)
```

## Parameters {#Parameters}

Control

:   Type: [String](../Concepts.htm#strings),
    [Integer](../Concepts.htm#numbers) or
    [Object](../Concepts.htm#objects)

    The control\'s ClassNN, text or HWND, or an object with a `Hwnd`
    property. For details, see [The Control
    Parameter](Control.htm#Parameter).

WinTitle, WinText, ExcludeTitle, ExcludeText

:   Type: [String](../Concepts.htm#strings),
    [Integer](../Concepts.htm#numbers) or
    [Object](../Concepts.htm#objects)

    If each of these is blank or omitted, the [Last Found
    Window](../misc/WinTitle.htm#LastFoundWindow) will be used.
    Otherwise, specify for *WinTitle* a [window title or other
    criteria](../misc/WinTitle.htm) to identify the target window and/or
    for *WinText* a substring from a single text element of the target
    window (as revealed by the included Window Spy utility).

    *ExcludeTitle* and *ExcludeText* can be used to exclude one or more
    windows by their title or text. Their specification is similar to
    *WinTitle* and *WinText*, except that *ExcludeTitle* does not
    recognize any criteria other than the window title.

    Window titles and text are case-sensitive. By default, hidden
    windows are not detected and hidden text elements are detected,
    unless changed with [DetectHiddenWindows](DetectHiddenWindows.htm)
    and [DetectHiddenText](DetectHiddenText.htm); however, when using
    [pure HWNDs](../misc/WinTitle.htm#ahk_id), hidden windows are always
    detected regardless of DetectHiddenWindows. By default, a window
    title can contain *WinTitle* or *ExcludeTitle* anywhere inside it to
    be a match, unless changed with
    [SetTitleMatchMode](SetTitleMatchMode.htm).

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the text of the specified control.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the window or
control could not be found.

## Remarks {#Remarks}

**Note:** To retrieve text from a ListView, ListBox, or ComboBox, use
[ListViewGetContent](ListViewGetContent.htm) or
[ControlGetItems](ControlGetItems.htm) instead.

If the retrieved text appears to be truncated (incomplete), it may be
necessary to retrieve the text by sending the WM_GETTEXT message via
[SendMessage](SendMessage.htm) instead. This is because some
applications do not respond properly to the WM_GETTEXTLENGTH message,
which causes AutoHotkey to make the return value too small to fit all
the text.

This function might use a large amount of RAM if the target control
(e.g. an editor with a large document open) contains a large quantity of
text. However, a variable\'s memory can be freed after use by assigning
it to nothing, i.e. `Text := ""`.

Text retrieved from most control types uses carriage return and linefeed
(\`r\`n) rather than a solitary linefeed (\`n) to mark the end of each
line.

It is not necessary to do `SetTitleMatchMode "Slow"` because
ControlGetText always retrieves the text using the slow mode (since it
works on a broader range of control types).

To retrieve an array of all controls in a window, use
[WinGetControls](WinGetControls.htm) or
[WinGetControlsHwnd](WinGetControlsHwnd.htm).

## Related {#Related}

[ControlSetText](ControlSetText.htm), [WinGetText](WinGetText.htm),
[Control functions](Control.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Retrieves the current text from Notepad\'s edit
control and stores it in `Text`{.variable}. This example may fail on
Windows 11 or later, as it requires the classic version of Notepad.

    Text := ControlGetText("Edit1", "Untitled -")
:::

::: {#ExMainWin .ex}
[](#ExMainWin){.ex_number} Retrieves and reports the current text from
the [main window](../Program.htm#main-window)\'s edit control.

    ListVars
    WinWaitActive "ahk_class AutoHotkey"
    MsgBox ControlGetText("Edit1") ; Use the window found above.
:::
