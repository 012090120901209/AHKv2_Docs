# Loop Reg

Retrieves the contents of the specified registry subkey, one item at a
time.

``` Syntax
Loop Reg KeyName , Mode
```

## Parameters {#Parameters}

KeyName

:   Type: [String](../Concepts.htm#strings)

    The full name of the registry key, e.g.
    `"HKLM\Software\SomeApplication"`.

    This must start with HKEY_LOCAL_MACHINE (or HKLM), HKEY_USERS (or
    HKU), HKEY_CURRENT_USER (or HKCU), HKEY_CLASSES_ROOT (or HKCR), or
    HKEY_CURRENT_CONFIG (or HKCC).

    To access a [remote registry](#remote), prepend the computer name
    and a backslash, e.g. `"\\workstation01\HKLM"`.

Mode

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, only values are included and subkeys are not
    recursed into. Otherwise, specify one or more of the following
    letters:

    -   K = Include keys.
    -   V = Include values. Values are also included if both K and V are
        omitted.
    -   R = Recurse into subkeys. If R is omitted, keys and values
        within subkeys of *KeyName* are not included.

## Remarks {#Remarks}

A registry loop is useful when you want to operate on a collection
registry values or subkeys, one at a time. The values and subkeys are
retrieved in reverse order (bottom to top) so that
[RegDelete](RegDelete.htm) and [RegDeleteKey](RegDeleteKey.htm) can be
used inside the loop without disrupting the loop.

The following variables exist within any registry loop. If an inner
registry loop is enclosed by an outer registry loop, the innermost
loop\'s registry item will take precedence:

  Variable                Description
  ----------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  A_LoopRegName           Name of the currently retrieved item, which can be either a value name or the name of a subkey. Value names displayed by Windows RegEdit as \"(Default)\" will be retrieved if a value has been assigned to them, but A_LoopRegName will be blank for them.
  A_LoopRegType           The type of the currently retrieved item, which is one of the following words: KEY (i.e. the currently retrieved item is a subkey not a value), REG_SZ, REG_EXPAND_SZ, REG_MULTI_SZ, REG_DWORD, REG_QWORD, REG_BINARY, REG_LINK, REG_RESOURCE_LIST, REG_FULL_RESOURCE_DESCRIPTOR, REG_RESOURCE_REQUIREMENTS_LIST, REG_DWORD_BIG_ENDIAN (probably rare on most Windows hardware). It will be empty if the currently retrieved item is of an unknown type.
  A_LoopRegKey            The full name of the key which contains the current loop item. For remote registry access, this value will [not]{.underline} include the computer name.
  A_LoopRegTimeModified   The time the current subkey or any of its values was last modified. Format [YYYYMMDDHH24MISS](FileSetTime.htm). This variable will be empty if the currently retrieved item is not a subkey (i.e. *A_LoopRegType* is not the word KEY).

When used inside a registry loop, the following functions can be used in
a simplified way to indicate that the currently retrieved item should be
operated upon:

  -----------------------------------------------------------------------------
  Syntax                                    Description
  ----------------------------------------- -----------------------------------
  `Value := `[`RegRead`](RegRead.htm)`()`   Reads the current item. If the
                                            current item is a key, an exception
                                            is thrown.

  [`RegWrite`](RegWrite.htm)` Value`\       Writes to the current item. If
  [`RegWrite`](RegWrite.htm)                *Value* is omitted, the item will
                                            be made 0 or blank depending on its
                                            type. If the current item is a key,
                                            an exception is thrown and the
                                            registry is not modified.

  [`RegDelete`](RegDelete.htm)              Deletes the current item if it is a
                                            value. If the current item is a
                                            key, its default value will be
                                            deleted instead.

  [`RegDeleteKey`](RegDeleteKey.htm)        Deletes the current item if it is a
                                            key. If the current item is a
                                            value, the key which *contains*
                                            that value will be deleted,
                                            including all subkeys and values.

  `RegCreateKey`                            Targets a key as described above
                                            for RegDeleteKey. If the key is
                                            deleted during the loop,
                                            RegCreateKey can be used to
                                            recreate it. Otherwise,
                                            RegCreateKey merely verifies that
                                            the script has write access to the
                                            key.
  -----------------------------------------------------------------------------

When accessing a remote registry (via the *KeyName* parameter described
above), the following notes apply:

-   The target machine must be running the Remote Registry service.
-   Access to a remote registry may fail if the target computer is not
    in the same domain as yours or the local or remote username lacks
    sufficient permissions (however, see below for possible
    workarounds).
-   Depending on your username\'s domain, workgroup, and/or permissions,
    you may have to connect to a shared device, such as by mapping a
    drive, prior to attempting remote registry access. Making such a
    connection \-- using a remote username and password that has
    permission to access or edit the registry \-- may as a side-effect
    enable remote registry access.
-   If you\'re already connected to the target computer as a different
    user (for example, a mapped drive via user Guest), you may have to
    terminate that connection to allow the remote registry feature to
    reconnect and re-authenticate you as your own currently logged-on
    username.

The One True Brace (OTB) style may optionally be used, which allows the
open-brace to appear on the same line rather than underneath. For
example: `Loop Reg "HKLM\Software\AutoHotkey", "V" {`.

See [Loop](Loop.htm) for information about [Blocks](Block.htm),
[Break](Break.htm), [Continue](Continue.htm), and the A_Index variable
(which exists in every type of loop).

The loop may optionally be followed by an [Else](Else.htm) statement,
which is executed if no registry items of the specified type were found
(i.e. the loop had zero iterations).

## Related {#Related}

[Loop](Loop.htm), [Break](Break.htm), [Continue](Continue.htm),
[Blocks](Block.htm), [RegRead](RegRead.htm), [RegWrite](RegWrite.htm),
[RegDelete](RegDelete.htm), [RegDeleteKey](RegDeleteKey.htm),
[SetRegView](SetRegView.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Retrieves the contents of the specified
registry subkey, one item at a time.

    Loop Reg, "HKEY_LOCAL_MACHINE\Software\SomeApplication"
        MsgBox A_LoopRegName
:::

::: {#ExRegDelete .ex}
[](#ExRegDelete){.ex_number} Deletes Internet Explorer\'s history of
URLs typed by the user.

    Loop Reg, "HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\TypedURLs"
        RegDelete
:::

::: {#ExTest .ex}
[](#ExTest){.ex_number} A working test script.

    Loop Reg, "HKCU\Software\Microsoft\Windows", "R KV"  ; Recursively retrieve keys and values.
    {
        if A_LoopRegType = "key"
            value := ""
        else
        {
            try
                value := RegRead()
            catch
                value := "*error*"
        }
        Result := MsgBox(A_LoopRegName " = " value " (" A_LoopRegType ")`n`nContinue?",, "y/n")
    }
    Until Result = "No"
:::

::: {#ExRegSearch .ex}
[](#ExRegSearch){.ex_number} Recursively searches the entire registry
for particular value(s).

    RegSearch("Notepad")

    RegSearch(Target)
    {
        Loop Reg, "HKEY_LOCAL_MACHINE", "KVR"
        {
            if !CheckThisRegItem()  ; It told us to stop.
                return
        }
        Loop Reg, "HKEY_USERS", "KVR"
        {
            if !CheckThisRegItem()  ; It told us to stop.
                return
        }
        Loop Reg, "HKEY_CURRENT_CONFIG", "KVR"
        {
            if !CheckThisRegItem()  ; It told us to stop.
                return
        }
        ; Note: I believe HKEY_CURRENT_USER does not need to be searched if
        ; HKEY_USERS is being searched. Similarly, HKEY_CLASSES_ROOT provides a
        ; combined view of keys from HKEY_LOCAL_MACHINE and HKEY_CURRENT_USER, so
        ; searching all three isn't necessary.

        CheckThisRegItem()
        {
            if A_LoopRegType = "KEY"  ; Remove these two lines if you want to check key names too.
                return true
            try
                RegValue := RegRead()
            catch
                return true
            if InStr(RegValue, Target)
            {
                Result := MsgBox(
                (
                "The following match was found:
                " A_LoopRegKey "\" A_LoopRegName "
                Value = " RegValue "
                
                Continue?"
                ),, "y/n")
                if Result = "No"
                    return false  ; Tell our caller to stop searching.
            }
            return true
        }
    }
:::
