# RegDeleteKey

Deletes a subkey from the registry.

``` Syntax
RegDeleteKey KeyName
```

## Parameters {#Parameters}

KeyName

:   Type: [String](../Concepts.htm#strings)

    The full name of the registry key, e.g.
    `"HKLM\Software\SomeApplication"`.

    This must start with HKEY_LOCAL_MACHINE (or HKLM), HKEY_USERS (or
    HKU), HKEY_CURRENT_USER (or HKCU), HKEY_CLASSES_ROOT (or HKCR), or
    HKEY_CURRENT_CONFIG (or HKCC).

    To access a [remote registry](LoopReg.htm#remote), prepend the
    computer name and a backslash, e.g. `"\\workstation01\HKLM"`.

    *KeyName* can be omitted only if a [registry loop](LoopReg.htm) is
    running, in which case it defaults to the key of the current loop
    item. If the item is a subkey, the full name of that subkey is used
    by default.

## Error Handling {#Error_Handling}

An [OSError](Error.htm#OSError) is thrown on failure.

[A_LastError](../Variables.htm#LastError) is set to the result of the
operating system\'s GetLastError() function.

## Remarks {#Remarks}

**Warning:** Deleting from the registry is potentially dangerous -
please exercise caution!

To retrieve and operate upon multiple registry keys or values, consider
using a [registry loop](LoopReg.htm).

Within a [registry loop](LoopReg.htm), RegDeleteKey does not necessarily
delete the current loop item. If the item is a subkey, `RegDeleteKey()`
deletes the key itself. If the item is a value, `RegDeleteKey()` deletes
the key which *contains* that value, including all subkeys and values.

For details about how to access the registry of a remote computer, see
the remarks in [registry loop](LoopReg.htm#remote).

To delete entries from the 64-bit sections of the registry in a 32-bit
script or vice versa, use [SetRegView](SetRegView.htm).

## Related {#Related}

[RegCreateKey](RegCreateKey.htm), [RegDelete](RegDelete.htm),
[RegRead](RegRead.htm), [RegWrite](RegWrite.htm), [registry
loop](LoopReg.htm), [SetRegView](SetRegView.htm),
[IniDelete](IniDelete.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Deletes a subkey from the registry.

    RegDeleteKey "HKEY_LOCAL_MACHINE\Software\SomeApplication"
:::
