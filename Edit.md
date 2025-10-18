# Edit

Opens the current script for editing in the default editor.

``` Syntax
Edit
```

The Edit function opens the current script for editing using the
associated \"edit\" verb in the registry (or Notepad if no verb).
However, if an editor window appears to have the script already open
(based on its window title), that window is activated instead of opening
a new instance of the editor.

The default program, script or command line executed by the \"edit\"
verb can be changed via *Editor settings* in the
[Dash](../Program.htm#dash).

This function has no effect when operating from within a compiled
script.

On a related note, AutoHotkey syntax highlighting can be enabled for
[various editors](../misc/Editors.htm). In addition, context sensitive
help for AutoHotkey functions can be enabled in any editor via [this
example](../scripts/index.htm#ContextSensitiveHelp). Finally, your
productivity may be improved by using an auto-completion utility like
[the script by
boiler](https://www.autohotkey.com/boards/viewtopic.php?f=60&t=31484) or
[the script by
Helgef](https://www.autohotkey.com/boards/viewtopic.php?f=60&t=27882),
which works in almost any editor. It watches what you type and displays
menus and parameter lists, which does some of the typing for you and
reminds you of the order of parameters.

## Related {#Related}

[Reload](Reload.htm), [How to edit a script](../Program.htm#edit),
[Editors with AutoHotkey support](../misc/Editors.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Opens the script for editing.

    Edit
:::

::: {#ExDefaultEditor .ex}
[](#ExDefaultEditor){.ex_number} If your editor\'s command-line usage is
something like `Editor.exe "Full path of script.ahk"`{.no-highlight},
the following can be used to set it as the default editor for ahk files.
When you run the script, it will prompt you to select the executable
file of your editor.

    Editor := FileSelect(2,, "Select your editor", "Programs (*.exe)")
    if Editor = ""
        ExitApp
    RegWrite Format('"{1}" "%L"', Editor), "REG_SZ", "HKCR\AutoHotkeyScript\Shell\Edit\Command"
:::
