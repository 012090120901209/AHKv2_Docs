# GetKeyName

Retrieves the name/text of a key.

``` Syntax
Name := GetKeyName(KeyName)
```

## Parameters {#Parameters}

KeyName

:   Type: [String](../Concepts.htm#strings)

    This can be just about any single character from the keyboard or one
    of the key names from the [key list](../KeyList.htm). Examples: B,
    5, LWin, RControl, Alt, Enter, Escape.

    Alternatively, this can be an explicit virtual key code such as
    vkFF, an explicit scan code such as sc01D, or a combination of VK
    and SC (in that order) such as vk1Bsc001. Note that these codes must
    be in hexadecimal.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the name of the specified key, or blank if the key
is invalid or unnamed.

## Related {#Related}

[GetKeyVK](GetKeyVK.htm), [GetKeySC](GetKeySC.htm),
[GetKeyState](GetKeyState.htm), [Key List](../KeyList.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Retrieves and reports the English name of
[Esc]{.kbd}.

    MsgBox GetKeyName("Esc") ; Shows Escape
    MsgBox GetKeyName("vk1B") ; Shows also Escape
:::
