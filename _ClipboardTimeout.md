# #ClipboardTimeout

Changes how long the script keeps trying to access the clipboard when
the first attempt fails.

``` Syntax
#ClipboardTimeout Milliseconds
```

## Parameters {#Parameters}

Milliseconds

:   Type: [Integer](../Concepts.htm#numbers)

    The length of the interval in milliseconds. Specify -1 to have it
    keep trying indefinitely. Specify 0 to have it try only once.

## Remarks {#Remarks}

If this directive is unspecified in the script, it will behave as though
set to 1000 (milliseconds).

Some applications keep the clipboard open for long periods of time,
perhaps to write or read large amounts of data. In such cases,
increasing this setting causes the script to wait longer before giving
up and displaying an error message.

This settings applies to all [clipboard](A_Clipboard.htm) operations,
the simplest of which are the following examples: `Var := A_Clipboard`
and `A_Clipboard := "New Text"`.

Whenever the script is waiting for the clipboard to become available,
new [threads](../misc/Threads.htm) [cannot]{.underline} be launched and
[timers](SetTimer.htm) will not run. However, if the user presses a
[hotkey](../Hotkeys.htm), selects a [custom menu item](Menu.htm), or
performs a [GUI action](Gui.htm) such as pressing a button, that event
will be buffered until later; in other words, its subroutine will be
performed after the clipboard finally becomes available.

This directive does [not]{.underline} cause the reading of clipboard
data to be reattempted if the first attempt fails.

Like other directives, #ClipboardTimeout cannot be executed
conditionally.

## Related {#Related}

[A_Clipboard](A_Clipboard.htm), [Thread](Thread.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Causes the script to wait 2 seconds instead of
1 second before giving up accessing the clipboard and displaying an
error message.

    #ClipboardTimeout 2000
:::
