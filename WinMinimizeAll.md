# WinMinimizeAll / WinMinimizeAllUndo

Minimizes or unminimizes all windows.

``` Syntax
WinMinimizeAll
WinMinimizeAllUndo
```

On most systems, this is equivalent to Explorer\'s [Win]{.kbd}+[M]{.kbd}
and [Win]{.kbd}+[D]{.kbd} hotkeys.

## Related {#Related}

[WinMinimize](WinMinimize.htm), [GroupAdd](GroupAdd.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Minimizes all windows for 1 second and
unminimizes them.

    WinMinimizeAll
    Sleep 1000
    WinMinimizeAllUndo
:::
