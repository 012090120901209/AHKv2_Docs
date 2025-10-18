# ListVars

Displays the script\'s [variables](../Variables.htm): their names and
current contents.

``` Syntax
ListVars
```

## Remarks {#Remarks}

This function is equivalent to selecting the \"View-\>Variables\" menu
item in the [main window](../Program.htm#main-window). It can help
[debug a script](../Scripts.htm#debug).

For each variable in the list, the variable\'s name and contents are
shown, along with other information depending on what the variable
contains. Each item is terminated with a carriage return and newline
(`` `r`n ``), but may span multiple lines if the variable contains
`` `r`n ``.

List items may take the following forms (where words in *italics* are
placeholders):

``` no-highlight
VarName[Length of Capacity]: String
VarName: TypeName object {Info}
VarName: Number
```

*Capacity* is the variable\'s current [capacity](VarSetStrCapacity.htm).

*String* is the first 60 characters of the variable\'s string value.

*Info* depends on the type of object, but is currently very limited.

If ListVars is used inside a [function](../Functions.htm), the following
are listed:

-   [Local variables](../Functions.htm#Local), including variables of
    outer functions which are referenced by the current function.
-   [Static variables](../Functions.htm#static) for the current
    function. [Global variables](../Functions.htm#Global) declared
    inside the function are also listed in this section.
-   If the current function is nested inside another function, static
    variables of each outer function are also listed.
-   All [global variables](../Functions.htm#Global).

## Related {#Related}

[KeyHistory](KeyHistory.htm), [ListHotkeys](ListHotkeys.htm),
[ListLines](ListLines.htm)

The [DebugVars](https://github.com/Lexikos/DebugVars.ahk#debugvars)
script can be used to inspect and change the contents of variables and
objects.

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Displays information about the script\'s
variables.

    var1 := "foo"
    var2 := "bar"
    obj := []
    ListVars
    Pause
:::
