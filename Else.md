# Else

Specifies one or more [statements](../Concepts.htm#statement) to execute
if the associated statement\'s body did not execute.

``` Syntax
Else Statement
```

``` Syntax
Else
{
    Statements
}
```

## Remarks {#Remarks}

Every use of *Else* must belong to (be associated with) an [If](If.htm),
[Catch](Catch.htm), [For](For.htm), [Loop](Loop.htm) or
[While](While.htm) statement above it. An *Else* always belongs to the
nearest applicable unclaimed statement above it unless a
[block](Block.htm) is used to change that behavior. The condition for an
*Else* statement executing depends on the associated statement:

-   [If expression](If.htm): The expression evaluated to false.
-   [For](For.htm), [Loop](Loop.htm) (any kind), [While](While.htm): The
    loop had zero iterations.
-   [Loop Read](LoopRead.htm): As above, but the presence of *Else* also
    prevents an error from being thrown if the file or path is not
    found. Therefore, *Else* executes if the file is empty or does not
    exist.
-   [Try](Try.htm)\...[Catch](Catch.htm): No exception was thrown within
    the *Try* block.

An *Else* can be followed immediately by any other single
[statement](../Concepts.htm#statement) on the same line. This is most
often used for \"else if\" ladders (see examples at the bottom).

If an *Else* owns more than one line, those lines must be enclosed in
braces (to create a [block](Block.htm)). However, if only one line
belongs to an *Else*, the braces are optional. For example:

    if (count > 0)  ; No braces are required around the next line because it's only a single line.
        MsgBox "Press OK to begin the process."
    else  ; Braces must be used around the section below because it consists of more than one line.
    {
        WinClose "Untitled - Notepad"
        MsgBox "There are no items present."
    }

The [One True Brace (OTB) style](Block.htm#otb) may optionally be used
around an *Else*. For example:

    if IsDone {
        ; ...
    } else if (x < y) {
        ; ...
    } else {
        ; ...
    }

## Related {#Related}

[Blocks](Block.htm), [If](If.htm), [Control Flow
Statements](../Language.htm#control-flow)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Common usage of an *Else* statement. This
example is executed as follows:

1.  If Notepad exists:
    1.  Activate it
    2.  Send the string \"This is a test.\" followed by [Enter]{.kbd}.
2.  Otherwise (that is, if Notepad does not exist):
    1.  Activate another window
    2.  Left-click at the coordinates 100, 200

<!-- -->

    if WinExist("Untitled - Notepad")
    {
        WinActivate
        Send "This is a test.{Enter}"
    }
    else
    {
        WinActivate "Some Other Window"
        MouseClick "Left", 100, 200
    }
:::

::: {#ExOtherUsages .ex}
[](#ExOtherUsages){.ex_number} Demonstrates different styles of how the
*Else* statement can be used too.

    if (x = 1)
        firstFunction()
    else if (x = 2) ; "else if" style
        secondFunction()
    else if x = 3
    {
        thirdFunction()
        Sleep 1
    }
    else defaultFunction()  ; i.e. Any single statement can be on the same line with an Else.
:::

::: {#ExLoop .ex}
[](#ExLoop){.ex_number} Executes some code if a loop had zero
iterations.

    ; Show File/Internet Explorer windows/tabs.
    for window in ComObject("Shell.Application").Windows
        MsgBox "Window #" A_Index ": " window.LocationName
    else
        MsgBox "No shell windows found."
:::
