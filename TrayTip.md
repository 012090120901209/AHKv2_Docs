# TrayTip

Shows a balloon message window or, on Windows 10 and later, a toast
notification near the [tray icon](../Program.htm#tray-icon).

``` Syntax
TrayTip Text, Title, Options
```

## Parameters {#Parameters}

Text

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, the text will be entirely omitted from the
    traytip, making it vertically shorter. Otherwise, specify the
    message to display. Only the first 255 characters will be displayed.

    Carriage return (\`r) or linefeed (\`n) may be used to create
    multiple lines of text. For example: `` Line1`nLine2 ``.

    If *Text* is long, it can be broken up into several shorter lines by
    means of a [continuation section](../Scripts.htm#continuation),
    which might improve readability and maintainability.

Title

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, the title line will be entirely omitted from
    the traytip, making it vertically shorter. Otherwise, specify the
    title of the traytip. Only the first 63 characters will be
    displayed.

Options

:   Type: [String](../Concepts.htm#strings) or
    [Integer](../Concepts.htm#numbers)

    If blank or omitted, it defaults to 0. Otherwise, specify either an
    integer value (a combination by addition or bitwise-OR) or a string
    of zero or more case-insensitive options separated by at least one
    space or tab. One or more numeric options may also be included in
    the string.

      Function                              Dec   Hex    String
      ------------------------------------- ----- ------ ---------
      No icon                               0     0x0    N/A
      Info icon                             1     0x1    `Iconi`
      Warning icon                          2     0x2    `Icon!`
      Error icon                            3     0x3    `Iconx`
      [Tray icon](TraySetIcon.htm)          4     0x4    N/A
      Do not play the notification sound.   16    0x10   `Mute`
      Use the large version of the icon.    32    0x20   N/A

    The icon is also not shown by the traytip if it lacks a title (this
    does not apply to the toast notifications on Windows 10 and later).

    On Windows 10 and later, the small tray icon is generally displayed
    even if the \"tray icon\" option (4) is omitted, and specifying this
    option may cause the program\'s name to be shown in the
    notification.

## Hiding the Traytip {#Hiding_the_Traytip}

To hide the traytip, omit all parameters (or at least the *Text* and
*Title* parameters). For example:

    TrayTip

To hide the traytip on Windows 10, temporarily remove the [tray
icon](../Program.htm#tray-icon) (which not always work, according to at
least one report). For example:

    TrayTip "#1", "This is TrayTip #1"
    Sleep 3000   ; Let it display for 3 seconds.
    HideTrayTip
    TrayTip "#2", "This is the second notification."
    Sleep 3000

    ; Copy this function into your script to use it.
    HideTrayTip() {
        TrayTip  ; Attempt to hide it the normal way.
        if SubStr(A_OSVersion,1,3) = "10." {
            A_IconHidden := true
            Sleep 200  ; It may be necessary to adjust this sleep.
            A_IconHidden := false
        }
    }

## Remarks {#Remarks}

On Windows 10, a traytip window usually looks like this:

![TrayTip](../static/dlg_traytip.png)

**Windows 10 and later** replace all balloon windows with toast
notifications by default (this can be overridden via group policy).
Calling TrayTip multiple times will usually cause multiple notifications
to be placed in a \"queue\" instead of each notification replacing the
last.

TrayTip has no effect if the script lacks a [tray
icon](../Program.htm#tray-icon) (via [#NoTrayIcon](_NoTrayIcon.htm) or
[`A_IconHidden`](../Variables.htm#IconHidden)` := true`). TrayTip also
has no effect if the following REG_DWORD value exists and has been set
to 0:

    HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced >> EnableBalloonTips

On a related note, there is a tooltip displayed whenever the user hovers
the mouse over the script\'s [tray icon](../Program.htm#tray-icon). The
contents of this tooltip can be changed via:
[`A_IconTip`](../Variables.htm#IconTip)` := "My New Text"`.

## Related {#Related}

[ToolTip](ToolTip.htm), [SetTimer](SetTimer.htm), [Menu
object](Menu.htm), [MsgBox](MsgBox.htm), [InputBox](InputBox.htm),
[FileSelect](FileSelect.htm), [DirSelect](DirSelect.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Shows a multiline balloon message or toast
notification for 20 seconds near the [tray
icon](../Program.htm#tray-icon) without playing the notification sound.
It also has a title and contains an info icon.

    TrayTip "Multiline`nText", "My Title", "Iconi Mute"
:::

::: {#ExDisplayTime .ex}
[](#ExDisplayTime){.ex_number} Provides a more precise control over the
display time without having to use Sleep (which would stop the current
thread).

    TrayTip "This will be displayed for 5 seconds.", "Timed traytip"
    SetTimer () => TrayTip(), -5000

The following does the same, but allows you to replace the HideTrayTip
function definition with the one defined [above](#Hide) for Windows 10.

    TrayTip "This will be displayed for 5 seconds.", "Timed traytip"
    SetTimer HideTrayTip, -5000

    HideTrayTip() {
        TrayTip
    }
:::

::: {#ExPermanent .ex}
[](#ExPermanent){.ex_number} Permanently displays a traytip by
refreshing it periodically via timer. Note that this probably won\'t
work well on Windows 10 and later for [reasons described
above](#Windows10).

    SetTimer RefreshTrayTip, 1000
    RefreshTrayTip  ; Call it once to get it started right away.

    RefreshTrayTip()
    {
        TrayTip "This is a more permanent traytip.", "Refreshed traytip", "Mute"
    }
:::
