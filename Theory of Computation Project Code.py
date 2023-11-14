#Leondre Bromfield

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1000x700")
root.wm_title("Binary Converter")

def convert_to_binary():
   
    # Get the decimal number from the entry field
    decimal_number = float(entry1.get())
    # Initialize the result string with an empty string
    result = ''
    # Initialize the steps string with an empty string
    steps = ''
    count = 0
    
    # Use a while loop to repeatedly divide the decimal number by 2 until it becomes 0
    # The code sequentially executes instructions that manipulate the contents of these registers. For example, the decimal_number is repeatedly divided by 2, and the remainder is calculated and appended to the result string. These operations are similar to how a register machine operates on its registers.
    while decimal_number > 0:
        # Calculate the remainder of the division
        remainder = decimal_number % 2
        # Convert the remainder to an integer and append it to the beginning of the result string
        result = str(int(remainder)) + result
        count = count + 1        
        # Append the current step of the conversion to the steps string
        steps += "Step {0} --> Current Decimal: {1:<15f} Remainder: {2:<15f} Binary: {3:<15s}\n".format(count, decimal_number, remainder, result)
        
        # Update the decimal_number for the next iteration
        decimal_number = decimal_number // 2

    # Show the converted binary number in entryx
    entryx.configure(state='normal')
    entryx.delete(0, 'end')
    entryx.insert(0, result)
    entryx.configure(state='disabled')

    # Reverse the binary string and show it in entryy
    reversed_result = result[::-1]
    entryy.configure(state='normal')
    entryy.delete(0, 'end')
    entryy.insert(0, reversed_result)
    entryy.configure(state='disabled')
    
    #show steps for conversion in the text box
    textbox.configure(state='normal')
    textbox.delete("0.0",'end')
    textbox.insert("0.0",steps)
    textbox.configure(state='disabled')
        
        
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

#text field for input
entry1= customtkinter.CTkEntry(master=frame, placeholder_text="Enter Decimal Number")
entry1.pack(pady=12, padx=10)

#button for conversion
button= customtkinter.CTkButton(master=frame, text="Convert", command=convert_to_binary)
button.pack(pady=12, padx=10)

# Add labels for entryx and entryy
labelx = customtkinter.CTkLabel(master=frame, text="Binary X")
labelx.pack(pady=1, padx=1)
entryx= customtkinter.CTkEntry(master=frame, state='disabled')
entryx.pack(pady=1, padx=1)

labely = customtkinter.CTkLabel(master=frame, text="Binary Y")
labely.pack(pady=1, padx=1)
entryy= customtkinter.CTkEntry(master=frame, state='disabled')
entryy.pack(pady=1, padx=1)

labeltext = customtkinter.CTkLabel(master=frame, text="Conversion Steps")
labeltext.pack(pady=4, padx=1)
textbox = customtkinter.CTkTextbox(master=frame, width=600)
textbox.pack(pady=4)

labelminus = customtkinter.CTkLabel(master=frame, text="X - (Last 4 Digits of Y)")
labelminus.pack(pady=3, padx=1)
entryminus= customtkinter.CTkEntry(master=frame, state='disabled')
entryminus.pack(pady=1, padx=1)

root.mainloop()
