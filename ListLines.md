# ListLines

Enables or disables line logging or displays the script lines most
recently executed.

``` Syntax
ListLines Mode
```

## Parameters {#Parameters}

Mode

:   Type: [Integer (boolean)](../Concepts.htm#boolean)

    If omitted, the history of lines most recently executed is shown.
    Otherwise, specify one of the following numbers, which affects only
    the behavior of the [current thread](../misc/Threads.htm) as
    follows:

    **1** (true): Include subsequently-executed lines in the history.

    **0** (false): Omit subsequently-executed lines from the history.

## Return Value {#Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

This function returns the previous setting; either 0 (false) or 1
(true).

## Remarks {#Remarks}

If ListLines is not used to affect line logging, the default setting is
1 (true).

`ListLines` (with no parameter) is equivalent to selecting the
\"View-\>Lines most recently executed\" menu item in the [main
window](../Program.htm#main-window). It can help [debug a
script](../Scripts.htm#debug).

`ListLines False` and `ListLines True` can be used to selectively omit
some lines from the history, which can help prevent the history from
filling up too quickly (such as in a loop with many fast iterations).
The line which called ListLines is also removed from the line history,
to prevent clutter. Additionally, performance may be reduced by a few
percent while line logging is enabled.

When the ListLines mode is changed, the current line (generally the one
that called ListLines or assigned to A_ListLines) is omitted from the
line history.

Every newly launched [thread](../misc/Threads.htm) (such as a
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timed](SetTimer.htm) subroutine) starts off fresh with the default
setting for this function. That default may be changed by using this
function during [script startup](../Scripts.htm#auto).

The built-in variable **A_ListLines** contains 1 if ListLines is enabled
and 0 otherwise.

On a related note, the built-in variables
[A_LineNumber](../Variables.htm#LineNumber) and
[A_LineFile](../Variables.htm#LineFile) contain the currently executing
line number and the file name to which it belongs.

## Related {#Related}

[KeyHistory](KeyHistory.htm), [ListHotkeys](ListHotkeys.htm),
[ListVars](ListVars.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Enables and disables line logging for specific
lines and then displays the result.

    x := "This line is logged"
    ListLines False
    x := "This line is not logged"
    ListLines True
    ListLines
    MsgBox
:::
