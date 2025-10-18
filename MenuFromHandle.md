# MenuFromHandle

Retrieves the [Menu or MenuBar object](Menu.htm) corresponding to a
Win32 menu handle.

``` Syntax
Menu := MenuFromHandle(Handle)
```

## Parameters {#Parameters}

Handle

:   Type: [Integer](../Concepts.htm#numbers)

    A handle to a Win32 menu (of type `HMENU`).

## Remarks {#Remarks}

If the handle is invalid or does not correspond to a menu created by
this script, the function returns an empty string.

## Related {#Related}

[Win32 Menus](Menu.htm#Win32_Menus), [Menu/MenuBar object](Menu.htm),
[Menu.Handle](Menu.htm#Handle), [Menu()](Menu.htm#Call)
