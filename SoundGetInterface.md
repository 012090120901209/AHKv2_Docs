# SoundGetInterface

Retrieves a native COM interface of a sound device or component.

``` Syntax
InterfacePtr := SoundGetInterface(IID, Component, Device)
```

## Parameters {#Parameters}

IID

:   Type: [String](../Concepts.htm#strings)

    An interface identifier (GUID) in the form
    \"{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}\".

Component

:   Type: [String](../Concepts.htm#strings) or
    [Integer](../Concepts.htm#numbers)

    If blank or omitted, an interface implemented by the device itself
    will be retrieved. Otherwise, specify the component\'s display name
    and/or index, e.g. `1`, `"Line in"` or `"Line in:2"`.

    For further details, see [Component (Sound
    Functions)](Sound.htm#component).

Device

:   Type: [String](../Concepts.htm#strings) or
    [Integer](../Concepts.htm#numbers)

    If blank or omitted, it defaults to the system\'s default device for
    playback (which is not necessarily device 1). Otherwise, specify the
    device\'s display name and/or index, e.g. `1`, `"Speakers"`,
    `"Speakers:2"` or `"Speakers (Example HD Audio)"`.

    For further details, see [Device (Sound
    Functions)](Sound.htm#device).

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

On success, the return value is an interface pointer.

If the interface is not supported, the return value is zero.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the device or
component could not be found. Otherwise, an [OSError](Error.htm#OSError)
is thrown on failure.

## Remarks {#Remarks}

The interface is retrieved from one of the following sources:

-   If *Component* is omitted,
    [IMMDevice::Activate](https://learn.microsoft.com/windows/win32/api/mmdeviceapi/nf-mmdeviceapi-immdevice-activate)
    is called to retrieve the interface.
-   [QueryInterface](https://learn.microsoft.com/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q))
    is called for the Connector identified by *Component*, and if
    successful, the interface pointer is returned. This can be used to
    retrieve the
    [IPart](https://learn.microsoft.com/windows/win32/api/devicetopology/nn-devicetopology-ipart)
    or
    [IConnector](https://learn.microsoft.com/windows/win32/api/devicetopology/nn-devicetopology-iconnector)
    interface of the Connector.
-   [IPart::Activate](https://learn.microsoft.com/windows/win32/api/devicetopology/nf-devicetopology-ipart-activate)
    is called for each Subunit unique to the given *Component*. For
    example, *IID* can be `"{7FB7B48F-531D-44A2-BCB3-5AD5A134B3DC}"` to
    retrieve the IAudioVolumeLevel interface, which provides access to
    per-channel volume level controls.

Once the interface pointer is retrieved, [ComCall](ComCall.htm) can be
used to call its methods. Refer to the Windows SDK header files to
identify the correct method index.

The interface pointer must be released by passing it to
[ObjRelease](ObjAddRef.htm) when it is no longer needed. This can be
done by \"wrapping\" it with [ComValue](ComValue.htm). The wrapped value
(an object) can be passed directly to [ComCall](ComCall.htm).

    Interface := ComValue(13, InterfacePtr)

## Related {#Related}

[Sound Functions](Sound.htm), [DeviceTopology
API](https://learn.microsoft.com/windows/win32/coreaudio/devicetopology-api)

## Examples {#Examples}

::: {#ExPeakMeter .ex}
[](#ExPeakMeter){.ex_number} Peak meter. A tooltip is displayed with the
current peak value, except when the peak value is zero (no sounds are
playing).

    ; IAudioMeterInformation
    audioMeter := SoundGetInterface("{C02216F6-8C67-4B5B-9D00-D008E73E0064}")
    if audioMeter
    {
        try loop  ; Until the script exits or an error occurs.
        {
            ; audioMeter->GetPeakValue(&peak)
            ComCall 3, audioMeter, "float*", &peak:=0
            ToolTip peak > 0 ? peak : ""
            Sleep 15
        }
        ObjRelease audioMeter
    }
    else
        MsgBox "Unable to get audio meter"
:::
