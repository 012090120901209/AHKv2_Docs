# ControlSend / ControlSendText

Sends simulated keystrokes or text to a window or control.

``` Syntax
ControlSend Keys , Control, WinTitle, WinText, ExcludeTitle, ExcludeText
ControlSendText Keys , Control, WinTitle, WinText, ExcludeTitle, ExcludeText
```

## Parameters {#Parameters}

Keys

:   Type: [String](../Concepts.htm#strings)

    The sequence of keys to send (see the [Send](Send.htm) function for
    details). The rate at which characters are sent is determined by
    [SetKeyDelay](SetKeyDelay.htm).

    Unlike the [Send](Send.htm) function, mouse clicks cannot be sent by
    ControlSend. Use [ControlClick](ControlClick.htm) for that.

Control

:   Type: [String](../Concepts.htm#strings),
    [Integer](../Concepts.htm#numbers) or
    [Object](../Concepts.htm#objects)

    If omitted, the keystrokes will be sent directly to the target
    window instead of one of its controls (see [Automating
    Winamp](../misc/Winamp.htm) for an example). Otherwise, specify the
    control\'s ClassNN, text or HWND, or an object with a `Hwnd`
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

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the window or
control could not be found.

## Remarks {#Remarks}

ControlSendText sends the individual characters of the *Keys* parameter
without translating `{Enter}` to [Enter]{.kbd}, `^c` to
[Ctrl]{.kbd}+[C]{.kbd}, etc. For details, see [Text
mode](Send.htm#SendText). It is also valid to use [{Raw}](Send.htm#Raw)
or [{Text}](Send.htm#Text) with ControlSend.

If the *Control* parameter is omitted, this function will attempt to
send directly to the target window by sending to its topmost control
(which is often the correct one) or the window itself if there are no
controls. This is useful if a window does not appear to have any
controls at all, or just for the convenience of not having to worry
about which control to send to.

By default, modifier keystrokes (Ctrl, Alt, Shift, and Win) are sent as
they normally would be by the Send function. This allows command prompt
and other console windows to properly detect uppercase letters, control
characters, etc. It may also improve reliability in other ways.

However, in some cases these modifier events may interfere with the
active window, especially if the user is actively typing during a
ControlSend or if [Alt]{.kbd} is being sent (since [Alt]{.kbd} activates
the active window\'s menu bar). This can be avoided by explicitly
sending modifier up and down events as in this example:

    ControlSend "{Alt down}f{Alt up}", "Edit1", "Untitled - Notepad"

The method above also allows the sending of modifier keystrokes (Ctrl,
Alt, Shift, and Win) while the workstation is locked (protected by logon
prompt).

[BlockInput](BlockInput.htm) should be avoided when using ControlSend
against a console window such as command prompt. This is because it
might prevent capitalization and modifier keys such as [Ctrl]{.kbd} from
working properly.

The value of [SetKeyDelay](SetKeyDelay.htm) determines the speed at
which keys are sent. If the target window does not receive the
keystrokes reliably, try increasing the press duration via the second
parameter of [SetKeyDelay](SetKeyDelay.htm) as in these examples:

    SetKeyDelay 10, 10
    SetKeyDelay 0, 10
    SetKeyDelay -1, 0

If the target control is an Edit control (or something similar), the
following are usually more reliable and faster than ControlSend:

    EditPaste("This text will be inserted at the caret position.", ControlName, WinTitle)

    ControlSetText("This text will entirely replace any current text.", ControlName, WinTitle)

ControlSend is generally not capable of manipulating a window\'s menu
bar. To work around this, use [MenuSelect](MenuSelect.htm). If that is
not possible due to the nature of the menu bar, you could try to
discover the message that corresponds to the desired menu item by
following the [SendMessage Tutorial](../misc/SendMessage.htm).

## Related {#Related}

[SetKeyDelay](SetKeyDelay.htm), [Escape sequences (e.g.
\`n)](../misc/EscapeChar.htm) , [Control functions](Control.htm),
[Send](Send.htm), [Automating Winamp](../misc/Winamp.htm)

## Examples {#Examples}

::: {#ExNotepad .ex}
[](#ExNotepad){.ex_number} Opens Notepad minimized and send it some
text. This example may fail on Windows 11 or later, as it requires the
classic version of Notepad.

    Run "Notepad",, "Min", &PID  ; Run Notepad minimized.
    WinWait "ahk_pid " PID  ; Wait for it to appear.
    ; Send the text to the inactive Notepad edit control.
    ; The third parameter is omitted so the last found window is used.
    ControlSend "This is a line of text in the notepad window.{Enter}", "Edit1"
    ControlSendText "Notice that {Enter} is not sent as an Enter keystroke with ControlSendText.", "Edit1"

    Msgbox "Press OK to activate the window to see the result."
    WinActivate "ahk_pid " PID  ; Show the result.
:::

::: {#ExCmd .ex}
[](#ExCmd){.ex_number} Opens the command prompt and sent it some text.
This example may fail on Windows 11 or later, as it requires the classic
version of the command prompt.

    SetTitleMatchMode 2
    Run A_ComSpec,,, &PID  ; Run command prompt.
    WinWait "ahk_pid " PID  ; Wait for it to appear.
    ControlSend "ipconfig{Enter}",, "cmd.exe"  ; Send directly to the command prompt window.
:::

::: {#ExGUI .ex}
[](#ExGUI){.ex_number} Creates a [GUI](Gui.htm) with an edit control and
sent it some text.

    MyGui := Gui()
    MyGui.Add("Edit", "r10 w500")
    MyGui.Show()
    ControlSend "This is a line of text in the edit control.{Enter}", "Edit1", MyGui
    ControlSendText "Notice that {Enter} is not sent as an Enter keystroke with ControlSendText.", "Edit1", MyGui
:::
