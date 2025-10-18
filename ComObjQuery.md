# ComObjQuery

Queries a COM object for an interface or service.

``` Syntax
InterfaceComObj := ComObjQuery(ComObj, SID, IID)
InterfaceComObj := ComObjQuery(ComObj, IID)
```

## Parameters {#Parameters}

ComObj

:   Type: [Object](../Concepts.htm#objects) or
    [Integer](../Concepts.htm#numbers)

    A COM wrapper object, an interface pointer, or an object with a
    `Ptr` property which returns an interface pointer. See
    [ComValue](ComValue.htm) for details.

IID

:   Type: [String](../Concepts.htm#strings)

    An interface identifier (GUID) in the form
    \"{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}\".

SID

:   Type: [String](../Concepts.htm#strings)

    A service identifier in the same form as IID.

## Return Value {#Return_Value}

Type: [Object](../Concepts.htm#objects)

This function returns a COM wrapper object of type dependent on the IID
parameter.

  IID             Class                                     Variant Type                                    Description
  --------------- ----------------------------------------- ----------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------
  IID_IDispatch   `ComObject`{style="white-space:nowrap"}   [VT_DISPATCH (9)]{style="white-space:nowrap"}   Allows the script to call properties and methods of the object using normal [object syntax](../Objects.htm#Usage_Objects).
  Any other IID   `ComValue`{style="white-space:nowrap"}    [VT_UNKNOWN (13)]{style="white-space:nowrap"}   Provides only a `Ptr` property, which allows the object to be passed to [DllCall](DllCall.htm) or [ComCall](ComCall.htm).

## Error Handling {#Error_Handling}

An exception is thrown on failure, such as if the interface is not
supported.

## Remarks {#Remarks}

In its two-parameter mode, this function is equivalent to
[IUnknown::QueryInterface](https://learn.microsoft.com/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(refiid_void)).
When SID and IID are both specified, it internally queries for the
[IServiceProvider](https://learn.microsoft.com/previous-versions/windows/internet-explorer/ie-developer/platform-apis/cc678965(v=vs.85))
interface, then calls
[IServiceProvider::QueryService](https://learn.microsoft.com/previous-versions/windows/internet-explorer/ie-developer/platform-apis/cc678966(v=vs.85)).

[ComCall](ComCall.htm) can be used to call native interface methods.

## Related {#Related}

[ComCall](ComCall.htm), [ComObject](ComObject.htm),
[ComObjGet](ComObjGet.htm), [ComObjActive](ComObjActive.htm)

## Examples {#Examples}

::: {#ExClassName .ex}
[](#ExClassName){.ex_number} Determines the class name of an object.

    obj := ComObject("Scripting.Dictionary")

    MsgBox "Interface name: " ComObjType(obj, "name")

    IID_IProvideClassInfo := "{B196B283-BAB4-101A-B69C-00AA00341D07}"

    ; Request the object's IProvideClassInfo interface.
    try
        pci := ComObjQuery(obj, IID_IProvideClassInfo)
    catch
    {
        MsgBox "IProvideClassInfo interface not supported."
        return
    }

    ; Call GetClassInfo to retrieve a pointer to the ITypeInfo interface.
    ComCall(3, pci, "ptr*", &ti := 0)

    ; Wrap ti to ensure automatic cleanup.
    ti := ComValue(13, ti)

    ; Call GetDocumentation to get the object's full type name.
    ComCall(12, ti, "int", -1, "ptr*", &pname := 0, "ptr", 0, "ptr", 0, "ptr", 0)

    ; Convert the BSTR pointer to a usable string.
    name := StrGet(pname, "UTF-16")

    ; Clean up.
    DllCall("oleaut32\SysFreeString", "ptr", pname)
    pci := ti := ""

    ; Display the type name!
    MsgBox "Class name: " name
:::

::: {#ExIE .ex}
[](#ExIE){.ex_number} Automates an existing Internet Explorer window.

    sURL := "https://www.autohotkey.com/boards/"
    if WebBrowser := GetWebBrowser()
        WebBrowser.Navigate(sURL)

    GetWebBrowser()
    {
        ; Get a raw pointer to the document object of the top-most IE window.
        static msg := DllCall("RegisterWindowMessage", "Str", "WM_HTML_GETOBJECT")
        lResult := SendMessage(msg, 0, 0, "Internet Explorer_Server1", "ahk_class IEFrame")
        if !lResult
            return  ; IE not found.
        static IID_IHTMLDocument2 := GUID("{332C4425-26CB-11D0-B483-00C04FD90119}")
        static VT_UNKNOWN := 13
        DllCall("oleacc\ObjectFromLresult", "Ptr", lResult
            , "Ptr", IID_IHTMLDocument2, "Ptr", 0
            , "Ptr*", pdoc := ComValue(VT_UNKNOWN, 0))
        
        ; Query for the WebBrowserApp service. In this particular case,
        ; the SID and IID are the same, but it isn't always this way.
        static IID_IWebBrowserApp := "{0002DF05-0000-0000-C000-000000000046}"
        static SID_SWebBrowserApp := IID_IWebBrowserApp
        pweb := ComObjQuery(pdoc, SID_SWebBrowserApp, IID_IWebBrowserApp)
        
        ; Return the WebBrowser object as IDispatch for usability.
        ; This works only because IWebBrowserApp is derived from IDispatch.
        ; pweb will release its ptr automatically, so AddRef to counter that.
        ObjAddRef(pweb.ptr)
        static VT_DISPATCH := 9
        return ComValue(VT_DISPATCH, pweb.ptr)
    }

    GUID(sGUID) ; Converts a string to a binary GUID and returns it in a Buffer.
    {
        GUID := Buffer(16, 0)
        if DllCall("ole32\CLSIDFromString", "WStr", sGUID, "Ptr", GUID) < 0
            throw ValueError("Invalid parameter #1", -1, sGUID)
        return GUID
    }
:::
