# ObjBindMethod

Creates a [BoundFunc object](../misc/Functor.htm#BoundFunc) which calls
a method of a given object.

``` Syntax
BoundFunc := ObjBindMethod(Obj , Method, Params)
```

## Parameters {#Parameters}

Obj

:   Type: [Object](../Concepts.htm#objects)

    Any object.

Method

:   Type: [String](../Concepts.htm#strings)

    A method name. If omitted, the bound function calls *Obj* itself.

*Params*

:   Any number of parameters.

## Remarks {#Remarks}

For details and examples, see [BoundFunc
object](../misc/Functor.htm#BoundFunc).
