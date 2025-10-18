# Function Objects

\"Function object\" usually means any of the following:

-   A [Func](../lib/Func.htm) or [Closure](../Functions.htm#closures)
    object, which represents an actual [function](../Functions.htm);
    either built-in or defined by the script.
-   A user-defined object which can be called like a function. This is
    sometimes also referred to as a \"functor\".
-   Any other object which can be called like a function, such as a
    [BoundFunc object](#BoundFunc) or a JavaScript function object
    returned by a COM method.

Function objects can be used with the following:

-   [CallbackCreate](../lib/CallbackCreate.htm)
-   [Gui events](../lib/GuiOnEvent.htm)
-   [For \... in](../lib/For.htm)
-   [HotIf](../lib/HotIf.htm)
-   [Hotkey](../lib/Hotkey.htm)
-   [Hotstring](../lib/Hotstring.htm)
-   [InputHook](../lib/InputHook.htm) (OnEnd, OnChar, OnKeyDown,
    OnKeyUp)
-   [Menu.Add](../lib/Menu.htm#Add)
-   [OnClipboardChange](../lib/OnClipboardChange.htm)
-   [OnError](../lib/OnError.htm)
-   [OnExit](../lib/OnExit.htm)
-   [OnMessage](../lib/OnMessage.htm)
-   [RegEx callouts](RegExCallout.htm)
-   [SetTimer](../lib/SetTimer.htm)
-   [Sort](../lib/Sort.htm)

To determine whether an object appears to be callable, use one of the
following:

-   `Value.HasMethod()` works with all AutoHotkey values and objects by
    default, but allows HasMethod to be overridden for some objects or
    classes. For COM objects, this will typically fail (throw an
    exception or produce the wrong result) unless the COM object is
    actually an AutoHotkey object from another process.
-   `HasMethod(Value)` works with all AutoHotkey values and objects and
    cannot be overridden, but will return false if the presence of a
    *Call* method cannot be determined. An exception is thrown if
    *Value* is a [ComObject](../lib/ComObject.htm).

## User-Defined {#User-Defined}

User-defined function objects must define a *Call* method containing the
implementation of the \"function\".

    class YourClassName {
        Call(a, b) {  ; Declare parameters as needed, or an array*.
            ;...
            return c
        }
        ;...
    }

This applies to *instances* of *YourClassName*, such as the object
returned by `YourClassName()`. Replacing `Call` with `static Call` would
instead override what occurs when *YourClassName* itself is called.

### Examples {#User-Defined-Examples}

The following example defines a function array which can be called; when
called, it calls each element of the array in turn.

    class FuncArrayType extends Array {
        Call(params*) {
            ; Call a list of functions.
            for fn in this
                fn(params*)
        }
    }

    ; Create an array of functions.
    funcArray := FuncArrayType()
    ; Add some functions to the array (can be done at any point).
    funcArray.Push(One)
    funcArray.Push(Two)
    ; Create an object which uses the array as a method.
    obj := {method: funcArray}
    ; Call the method (and consequently both One and Two).
    obj.method("2nd")
    ; Call it as a function.
    (obj.method)("1st", "2nd")

    One(param1, param2) {
        ListVars
        MsgBox
    }
    Two(param1, param2) {
        ListVars
        MsgBox
    }

## BoundFunc Object {#BoundFunc}

Acts like a function, but just passes predefined parameters to another
function.

There are two ways that BoundFunc objects can be created:

-   By calling the [Func.Bind](../lib/Func.htm#Bind) method, which binds
    parameter values to a function.
-   By calling the [ObjBindMethod](../lib/ObjBindMethod.htm) function,
    which binds parameter values and a method name to a target object.

BoundFunc objects can be called as shown in the example below. When the
BoundFunc is called, it calls the function or method to which it is
bound, passing a combination of bound parameters and the caller\'s
parameters. Unbound parameter positions are assigned positions from the
caller\'s parameter list, left to right. For example:

    fn := RealFn.Bind(1)  ; Bind first parameter only
    fn(2)      ; Shows "1, 2"
    fn.Call(3) ; Shows "1, 3"

    fn := RealFn.Bind( , 1)  ; Bind second parameter only
    fn(2, 0)   ; Shows "2, 1, 0"
    fn.Call(3) ; Shows "3, 1"
    fn(, 4)    ; Error: 'a' was omitted

    RealFn(a, b, c?) {
        MsgBox a ", " b (IsSet(c) ? ", " c : "")
    }

[ObjBindMethod](../lib/ObjBindMethod.htm) can be used to bind to a
method even when it isn\'t possible to retrieve a reference to the
method itself. For example:

    Shell := ComObject("Shell.Application")
    RunBox := ObjBindMethod(Shell, "FileRun")
    ; Show the Run dialog.
    RunBox

For a more complex example, see
[SetTimer](../lib/SetTimer.htm#ExampleClass).

Other properties and methods are inherited from [Func](../lib/Func.htm),
but do not reflect the properties of the target function or method
(which is not required to be implemented as a function). The BoundFunc
acts as an anonymous variadic function with no other formal parameters,
similar to the [fat arrow function](../Variables.htm#fat-arrow) below:

    Func_Bind(fn, bound_args*) {
        return (args*) => (args.InsertAt(1, bound_args*), fn(args*))
    }
