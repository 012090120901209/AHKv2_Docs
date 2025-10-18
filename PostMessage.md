# PostMessage

Places a message in the message queue of a window or control.

``` Syntax
PostMessage MsgNumber , wParam, lParam, Control, WinTitle, WinText, ExcludeTitle, ExcludeText
```

## Parameters {#Parameters}

MsgNumber

:   Type: [Integer](../Concepts.htm#numbers)

    The message number to send. See the [message
    list](../misc/SendMessageList.htm) to determine the number.

wParam, lParam

:   Type: [Integer](../Concepts.htm#numbers)

    If either is omitted, 0 will be sent. Otherwise, specify the first
    and second component of the message.

    Each parameter must be an [integer](../Concepts.htm#numbers).

    If AutoHotkey or the target window is 32-bit, only the parameter\'s
    low 32 bits are used; that is, values are truncated if outside the
    range -2147483648 to 2147483647 (-0x80000000 to 0x7FFFFFFF) for
    signed values, or 0 to 4294967295 (0xFFFFFFFF) for unsigned values.
    If AutoHotkey and the target window are both 64-bit, any integer
    value [supported by AutoHotkey](../Concepts.htm#pure-numbers) can be
    used.

Control

:   Type: [String](../Concepts.htm#strings),
    [Integer](../Concepts.htm#numbers) or
    [Object](../Concepts.htm#objects)

    If omitted, the message will be posted directly to the target window
    rather than one of its controls. Otherwise, specify the control\'s
    ClassNN, text or HWND, or an object with a `Hwnd` property. For
    details, see [The Control Parameter](Control.htm#Parameter).

    If this parameter specifies a HWND (as an integer or object), it is
    not required to be the HWND of a control (child window). That is, it
    can also be the HWND of a top-level window.

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

An [OSError](Error.htm#OSError) is thrown if the message could not be
posted. For example, if the target window is running at a higher
integrity level than the script (i.e. it is running as admin while the
script is not), messages may be blocked.

## Remarks {#Remarks}

This function should be used with caution because sending a message to
the wrong window (or sending an invalid message) might cause unexpected
behavior or even crash the target application. This is because most
applications are not designed to expect certain types of messages from
external sources.

PostMessage places the message in the message queue associated with the
target window and does not wait for acknowledgement or reply. By
contrast, [SendMessage](SendMessage.htm) waits for the target window to
process the message, up until the timeout period expires.

Unlike [SendMessage](SendMessage.htm), PostMessage usually only sends
basic numeric values, not pointers to structures or strings.

To send a message to all windows in the system, including those that are
hidden or disabled, specify `0xFFFF` for *WinTitle* (0xFFFF is
HWND_BROADCAST). This technique should be used only for messages
intended to be broadcast.

To have a script receive a message, use [OnMessage](OnMessage.htm).

See the [Message Tutorial](../misc/SendMessage.htm) for an introduction
to using this function.

## Related {#Related}

[SendMessage](SendMessage.htm), [Message
List](../misc/SendMessageList.htm), [Message
Tutorial](../misc/SendMessage.htm), [OnMessage](OnMessage.htm),
[Automating Winamp](../misc/Winamp.htm), [DllCall](DllCall.htm),
[ControlSend](ControlSend.htm), [MenuSelect](MenuSelect.htm)

## Examples {#Examples}

::: {#ExSwitchKeybLang .ex}
[](#ExSwitchKeybLang){.ex_number} Switches the active window\'s keyboard
layout/language to English (US).

    PostMessage 0x0050, 0, 0x4090409,, "A"  ; 0x0050 is WM_INPUTLANGCHANGEREQUEST.
:::
