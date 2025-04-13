import tkinter as tk
from tkinter import ttk
from tkinter import font


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

# Main window setup with improved appearance
root = tk.Tk()
root.title("KBSM Basis Converter")
root.configure(padx=20, pady=20)  # Add padding around all elements

# Make the root window resizable
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create a custom style
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat")
style.configure("TLabel", padding=5)
style.configure("TFrame", padding=10)

# Create main frame to hold everything
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky="nsew")

# Configure main frame to expand
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(3, weight=1)  # Let the output section expand

# Define a better font
default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=10)
root.option_add("*Font", default_font)

# Input Section with frame
input_frame = ttk.LabelFrame(main_frame, text="Input", padding=10)
input_frame.grid(row=0, column=0, sticky="nsew", pady=(0, 15))
input_frame.columnconfigure(0, weight=1)  # Make input expand horizontally

ttk.Label(input_frame, text="Enter LaTeX Input:").grid(row=0, column=0, sticky="w", pady=(0, 5))
latexEntry = tk.Text(input_frame, height=3, width=50, relief="solid", borderwidth=1)
latexEntry.grid(row=1, column=0, columnspan=3, pady=(0, 10), padx=5, sticky="nsew")

# Parameters Section
params_frame = ttk.LabelFrame(main_frame, text="Parameters", padding=10)
params_frame.grid(row=1, column=0, sticky="nsew", pady=(0, 15))

# Basis selection
ttk.Label(params_frame, text="Select Basis:").grid(row=0, column=0, sticky="w", padx=(0, 10))
basisNumberVar = tk.IntVar(value=0)
basisNumberEntry = ttk.Entry(params_frame, textvariable=basisNumberVar, width=8)
basisNumberEntry.grid(row=0, column=1, sticky="w", padx=5)

basisSignVar = tk.StringVar(value="+")
basisSignDropdown = ttk.Combobox(params_frame, textvariable=basisSignVar, values=["+", "-"], width=5)
basisSignDropdown.grid(row=0, column=2, padx=5)

# c value selection
ttk.Label(params_frame, text="Select c:").grid(row=1, column=0, sticky="w", padx=(0, 10), pady=(10, 0))
cVar = tk.IntVar(value=0)
cEntry = ttk.Entry(params_frame, textvariable=cVar, width=8)
cEntry.grid(row=1, column=1, sticky="w", padx=5, pady=(10, 0))

# Action buttons in their own frame
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=2, column=0, sticky="nsew", pady=(0, 15))

processButton = ttk.Button(button_frame, text="Convert", command=processInput)
processButton.grid(row=0, column=0, padx=10)

# Output Section
output_frame = ttk.LabelFrame(main_frame, text="Output", padding=10)
output_frame.grid(row=3, column=0, sticky="nsew", pady=(0, 15))
output_frame.columnconfigure(0, weight=1)  # Make output expand horizontally

ttk.Label(output_frame, text="LaTeX Output:").grid(row=0, column=0, sticky="w", pady=(0, 5))
outputEntry = tk.Text(output_frame, height=3, width=50, relief="solid", borderwidth=1)
outputEntry.grid(row=1, column=0, columnspan=3, pady=(0, 10), padx=5, sticky="nsew")

copyButton = ttk.Button(output_frame, text="Copy to Clipboard", command=copyToClipboard)
copyButton.grid(row=2, column=0, pady=(0, 5))

# Start the application
root.mainloop()
