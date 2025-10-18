# ObjAddRef / ObjRelease

Increments or decrements an object\'s [reference
count](../Objects.htm#Reference_Counting).

``` Syntax
NewRefCount := ObjAddRef(Ptr)
NewRefCount := ObjRelease(Ptr)
```

## Parameters {#Parameters}

Ptr

:   Type: [Integer](../Concepts.htm#numbers)

    An unmanaged object pointer or COM interface pointer.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

These functions return the new reference count. This value should be
used **only** for debugging purposes.

## Related {#Related}

[Reference Counting](../Objects.htm#Reference_Counting)

Although the following articles discuss reference counting as it applies
to COM, they cover some important concepts and rules which generally
also apply to AutoHotkey objects:
[IUnknown::AddRef](https://learn.microsoft.com/windows/win32/api/unknwn/nf-unknwn-iunknown-addref),
[IUnknown::Release](https://learn.microsoft.com/windows/win32/api/unknwn/nf-unknwn-iunknown-release),
[Reference Counting
Rules](https://learn.microsoft.com/windows/win32/com/rules-for-managing-reference-counts).
