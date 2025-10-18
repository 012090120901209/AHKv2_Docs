# ComObjFromPtr

Wraps a raw
[IDispatch](https://learn.microsoft.com/windows/win32/api/oaidl/nn-oaidl-idispatch)
pointer (COM object) for use by the script.

``` Syntax
ComObj := ComObjFromPtr(DispPtr)
```

## Parameters {#Parameters}

DispPtr

:   Type: [Integer](../Concepts.htm#numbers)

    A non-null interface pointer for IDispatch or a derived interface.

## Return Value {#Returns}

Type: [ComObject](ComObject.htm)

Returns a wrapper object containing the [variant
type](ComObjType.htm#vt) VT_DISPATCH and the given pointer.

Wrapping a COM object enables the script to interact with it more
naturally, using [object syntax](../Objects.htm#Usage_Objects). However,
the majority of scripts do not need to do this manually since a wrapper
object is created automatically by [ComObject](ComObject.htm),
[ComObjActive](ComObjActive.htm), [ComObjGet](ComObjGet.htm) and any COM
method which returns an object.

## Remarks {#Remarks}

The wrapper object assumes responsibility for automatically releasing
the pointer when appropriate. This function [queries](ComObjQuery.htm)
the object for its IDispatch interface; if one is returned, *DispPtr* is
immediately released. Therefore, if the script intends to use the
pointer after calling this function, it must call
[`ObjAddRef`](ObjAddRef.htm)`(DispPtr)` first.

**Known limitation:** Each time a COM object is wrapped, a new wrapper
object is created. Comparisons and assignments such as `obj1 == obj2`
and `arr[obj1] := value` treat the two wrapper objects as unique, even
when they contain the same COM object.

## Related {#Related}

[ComObject](ComObject.htm), [ComValue](ComValue.htm),
[ComObjGet](ComObjGet.htm), [ComObjConnect](ComObjConnect.htm),
[ComObjFlags](ComObjFlags.htm), [ObjAddRef/ObjRelease](ObjAddRef.htm),
[ComObjQuery](ComObjQuery.htm), [GetActiveObject (Microsoft
Docs)](https://learn.microsoft.com/windows/win32/api/oleauto/nf-oleauto-getactiveobject)
