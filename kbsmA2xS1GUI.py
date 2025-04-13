import tkinter as tk
from tkinter import ttk

from backend.latexToLinearCombination import laTeXToLinearCombination
import backend.dataStructures
from backend.toBasis import toBasis

def processInput():
    latexInput = latexEntry.get("1.0", tk.END).strip()
    basisNumber = basisNumberVar.get()
    basisSign = basisSignVar.get()
    c_value = cVar.get()

    if (basisSign == "+"):
        basisSign = 1
    if (basisSign == "-"):
        basisSign = -1
    # algorithm

    basisInfo = backend.dataStructures.basisInformation(basisNumber, c_value, basisSign)

    linearCombination = laTeXToLinearCombination(latexInput)

    outputLinearCombination = toBasis(basisInfo, linearCombination)

    outputText = backend.dataStructures.LinearCombination.strLatex(outputLinearCombination)

    outputEntry.delete("1.0", tk.END)
    outputEntry.insert("1.0", outputText)

def copyToClipboard():
    root.clipboard_clear()
    root.clipboard_append(outputEntry.get("1.0", tk.END).strip())
    root.update()

# Main window
root = tk.Tk()
root.title("KBSM Basis Converter")

# LaTeX Input
tk.Label(root, text="Enter LaTeX Input:").grid(row=0, column=0, sticky="w")
latexEntry = tk.Text(root, height=2, width=40)
latexEntry.grid(row=1, column=0, columnspan=2)

# Basis Selection
tk.Label(root, text="Select Basis:").grid(row=2, column=0, sticky="w")
basisNumberVar = tk.IntVar(value=0)
basisNumberEntry = tk.Entry(root, textvariable=basisNumberVar, width=5)
basisNumberEntry.grid(row=2, column=1, sticky="w")

tk.Label(root, text="Select c:").grid(row=3, column=0, sticky="w")  # Changed row to 3
cVar = tk.IntVar(value=0)
cEntry = tk.Entry(root, textvariable=cVar, width=5)
cEntry.grid(row=3, column=1, sticky="w")

basisSignVar = tk.StringVar(value="+")
basisSignDropdown = ttk.Combobox(root, textvariable=basisSignVar, values=["+", "-"], width=3)
basisSignDropdown.grid(row=2, column=2)

# Process Button
processButton = tk.Button(root, text="Convert", command=processInput)
processButton.grid(row=4, column=0, columnspan=2, pady=5)

# Output Display
tk.Label(root, text="LaTeX Output:").grid(row=5, column=0, sticky="w")  # Changed from 4 to 5
outputEntry = tk.Text(root, height=2, width=40)
outputEntry.grid(row=6, column=0, columnspan=2)  # Changed from 5 to 6

# Copy Button
copyButton = tk.Button(root, text="Copy to Clipboard", command=copyToClipboard)
copyButton.grid(row=7, column=0, columnspan=2, pady=5)  # Changed from 6 to 7

root.mainloop()
