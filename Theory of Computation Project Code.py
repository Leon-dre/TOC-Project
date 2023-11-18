#Leondre Bromfield- 2000070
#Daryn Brown- 2002414
#Cassandra Powell- 2005742
#Tichina Buckle - 1801448
#Daniel Nelson-


import pygame
import pygame_gui
import customtkinter

class TuringMachine(object):
    def __init__(self, tape = ""):
        self.tape = list(tape)
        self.current_state = 'start'
        self.head_position = 0
        self.state_transition = {
            ('start', '0'): ('start', '0', 1),
            ('start', '1'): ('start', '1', 1),
            ('start', ' '): ('reverse', ' ', -1),
            ('reverse', '0'): ('reverse', '1', -1),
            ('reverse', '1'): ('reverse', '0', -1),
            ('reverse', ' '): ('end', ' ', 1),
        }

    def step(self):
        char_under_head = self.tape[self.head_position]
        state_transition_key = (self.current_state, char_under_head)
        if state_transition_key in self.state_transition:
            self.current_state, new_char, move_direction = self.state_transition[state_transition_key]
            self.tape[self.head_position] = new_char
            self.head_position += move_direction

    def execute(self, screen, manager):
        clock = pygame.time.Clock()
        next_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)), text='Next', manager=manager)
        pygame.display.set_caption("Turing Machine Tape Visualization")

        while self.current_state != 'end':
            time_delta = clock.tick(60)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return ''.join(self.tape)
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == next_button:
                            self.step()
                            screen.fill((0, 0, 0))
                            font = pygame.font.Font(None, 36)
                            for i, bit in enumerate(self.tape):
                                tape_text = font.render(bit, True, (255, 255, 255))
                                screen.blit(tape_text, (20 + i * 20, 250))
                            head_text = font.render('^', True, (255, 0, 0))
                            screen.blit(head_text, (20 + self.head_position * 20, 300))
                            pygame.display.flip()

                manager.process_events(event)

            manager.update(time_delta)
            manager.draw_ui(screen)

            pygame.display.update()

        pygame.quit()
        return ''.join(self.tape)


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
    entryx.configure(state='normal')
    entryx.delete(0, 'end')
    entryx.insert(0, result)
    entryx.configure(state='disabled') 
    textbox.configure(state='normal')
    textbox.delete("0.0",'end')
    textbox.insert("0.0",steps)
    textbox.configure(state='disabled')

def reverse_binary():
    binary_input = entryx.get()
    pygame.init()
    pygame.display.set_caption('Turing Machine')
    screen = pygame.display.set_mode((800, 600))
    manager = pygame_gui.UIManager((800, 600))
    tm = TuringMachine(binary_input + " ")
    reversed_binary = tm.execute(screen, manager)
    print("Reversed binary value is: ", reversed_binary)
    entryy.configure(state='normal')
    entryy.delete(0, 'end')
    entryy.insert(0, reversed_binary)
    entryy.configure(state='disabled') 
    subtract_last_four_digits()

def subtract_last_four_digits():
    binary_x = entryx.get()
    binary_y_last_four_digits = entryy.get()[-5:]
    binary_x_int = int(binary_x, 2)
    binary_y_last_four_digits_int = int(binary_y_last_four_digits, 2)
    result_int = binary_x_int - binary_y_last_four_digits_int
    result_binary = bin(result_int)[2:]
    entryminus.configure(state='normal')
    entryminus.delete(0, 'end')
    entryminus.insert(0, f"{result_binary} ---> {result_int}")
    entryminus.configure(state='disabled') 

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("1000x700")
root.wm_title("Binary Converter")
   
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

#Title of window
name = customtkinter.CTkLabel(master=frame, text="Binary Converter", font=customtkinter.CTkFont(size=32, weight="bold"))
name.pack(pady=12, padx=10)

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

labeltext = customtkinter.CTkLabel(master=frame, text="Conversion Steps")
labeltext.pack(pady=4, padx=1)
textbox = customtkinter.CTkTextbox(master=frame, width=600)
textbox.pack(pady=4)

button2= customtkinter.CTkButton(master=frame, text="Reverse", command=reverse_binary)
button2.pack(pady=12, padx=10)

labely = customtkinter.CTkLabel(master=frame, text="Binary Y")
labely.pack(pady=1, padx=1)
entryy= customtkinter.CTkEntry(master=frame, state='disabled')
entryy.pack(pady=1, padx=1)

labelminus = customtkinter.CTkLabel(master=frame, text="X - (Last 4 Digits of Y)")
labelminus.pack(pady=3, padx=1)
entryminus= customtkinter.CTkEntry(master=frame, state='disabled')
entryminus.pack(pady=1, padx=1)

root.mainloop()
