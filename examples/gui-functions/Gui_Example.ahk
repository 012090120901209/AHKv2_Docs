/*
    AutoHotkey v2 Example: Gui
    Documentation: Gui.md
    Category: Gui Functions

    This example demonstrates practical usage of Gui.
    Modify and experiment to learn!
*/


; Simple GUI
myGui := Gui()
myGui.Add("Text", , "Enter your name:")
edit := myGui.Add("Edit", "w200")
btn := myGui.Add("Button", , "Submit")
btn.OnEvent("Click", Submit)
myGui.Show()

Submit(*) {
    global edit
    MsgBox "Hello " edit.Value
}


/*
    For complete documentation, see: Gui.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
