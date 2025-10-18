# ComObject

Creates a COM object.

``` Syntax
ComObj := ComObject(CLSID , IID)
```

`ComObject` itself is a [class](Class.htm) derived from `ComValue`, but
is used only to create or identify COM objects.

## Parameters {#Parameters}

CLSID

:   Type: [String](../Concepts.htm#strings)

    CLSID or human-readable Prog ID of the COM object to create.

IID

:   Type: [String](../Concepts.htm#strings)

    If omitted, it defaults to
    `"{00020400-0000-0000-C000-000000000046}"` (IID_IDispatch).
    Otherwise, specify the identifier of the interface to return. In
    most cases this is omitted.

## Return Value {#Return_Value}

Type: [Object](../Concepts.htm#objects)

This function returns a COM wrapper object of type dependent on the IID
parameter.

  IID             Class                                     Variant Type                                    Description
  --------------- ----------------------------------------- ----------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------
  IID_IDispatch   `ComObject`{style="white-space:nowrap"}   [VT_DISPATCH (9)]{style="white-space:nowrap"}   Allows the script to call properties and methods of the object using normal [object syntax](../Objects.htm#Usage_Objects).
  Any other IID   `ComValue`{style="white-space:nowrap"}    [VT_UNKNOWN (13)]{style="white-space:nowrap"}   Provides only a `Ptr` property, which allows the object to be passed to [DllCall](DllCall.htm) or [ComCall](ComCall.htm).

## Error Handling {#Error_Handling}

An exception is thrown on failure, such as if a parameter is invalid or
the object does not support the interface specified by *IID*.

## Related {#Related}

[ComValue](ComValue.htm), [ComObjGet](ComObjGet.htm),
[ComObjActive](ComObjActive.htm), [ComObjConnect](ComObjConnect.htm),
[ComObjArray](ComObjArray.htm), [ComObjQuery](ComObjQuery.htm),
[ComCall](ComCall.htm), [CreateObject (Microsoft
Docs)](https://learn.microsoft.com/previous-versions/dcw63t7z(v=vs.85))

## Examples {#Examples}

For a long list of v1.1 examples, see [this archived forum
thread](https://www.autohotkey.com/board/topic/56987-).

::: {#ExIE .ex}
[](#ExIE){.ex_number} Launches an instance of Internet Explorer, makes
it visible and navigates to a website.

    ie := ComObject("InternetExplorer.Application")
    ie.Visible := true  ; This is known to work incorrectly on IE7.
    ie.Navigate("https://www.autohotkey.com/")
:::

::: {#ExWallpaper .ex}
[](#ExWallpaper){.ex_number} Retrieves the path of the desktop\'s
current wallpaper.

    AD_GETWP_BMP := 0
    AD_GETWP_LAST_APPLIED := 0x00000002
    CLSID_ActiveDesktop := "{75048700-EF1F-11D0-9888-006097DEACF9}"
    IID_IActiveDesktop := "{F490EB00-1240-11D1-9888-006097DEACF9}"
    cchWallpaper := 260
    GetWallpaper := 4

    AD := ComObject(CLSID_ActiveDesktop, IID_IActiveDesktop)
    wszWallpaper := Buffer(cchWallpaper * 2)
    ComCall(GetWallpaper, AD, "ptr", wszWallpaper, "uint", cchWallpaper, "uint", AD_GETWP_LAST_APPLIED)
    Wallpaper := StrGet(wszWallpaper, "UTF-16")
    MsgBox "Wallpaper: " Wallpaper
:::
