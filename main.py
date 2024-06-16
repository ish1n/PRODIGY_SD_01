import tkinter as tk

def exit_app():
    window.destroy()

def convert():
    try:
        temp = float(e1.get())
        input_unit = input_var.get()
        output_unit = output_var.get()

        if input_unit == "Celsius":
            if output_unit == "Fahrenheit":
                result = ((temp * 9) / 5) + 32
            elif output_unit == "Kelvin":
                result = temp + 273.15
            else:
                result = temp

        elif input_unit == "Fahrenheit":
            if output_unit == "Celsius":
                result = ((temp - 32) * 5) / 9
            elif output_unit == "Kelvin":
                result = ((temp - 32) * 5) / 9 + 273.15
            else:
                result = temp

        elif input_unit == "Kelvin":
            if output_unit == "Celsius":
                result = temp - 273.15
            elif output_unit == "Fahrenheit":
                result = ((temp - 273.15) * 9) / 5 + 32
            else:
                result = temp

        t1.config(state='normal')
        t1.delete('1.0', tk.END)
        t1.insert(tk.END, result)
        t1.config(state='disabled')
    except ValueError:
        t1.config(state='normal')
        t1.delete('1.0', tk.END)
        t1.insert(tk.END, "Invalid input")
        t1.config(state='disabled')

window = tk.Tk()
window.geometry("350x300")
window.config(bg="#95D2B3")
window.resizable(width=False, height=False)
window.title('Temperature Converter')

l1 = tk.Label(window, text="Temperature Converter", font=("Arial", 15), fg="white", bg="black")
l2 = tk.Label(window, text="Enter temperature: ", font=("Arial", 10, "bold"), fg="white", bg="#F19ED2")

input_var = tk.StringVar(window)
input_var.set("Celsius")
input_menu = tk.OptionMenu(window, input_var, "Celsius", "Fahrenheit", "Kelvin")

output_var = tk.StringVar(window)
output_var.set("Fahrenheit")
output_menu = tk.OptionMenu(window, output_var, "Celsius", "Fahrenheit", "Kelvin")

e1 = tk.Entry(window, font=('Arial', 10))

btn1 = tk.Button(window, text="Convert!", font=("Arial", 10), command=convert)
btn2 = tk.Button(window, text="Exit application", font=("Arial", 10), command=exit_app)

t1 = tk.Text(window, state="disabled", width=20, height=1)

l1.pack(pady=10)
l2.pack()
e1.pack()
input_menu.pack(pady=5)
output_menu.pack(pady=5)
btn1.pack(pady=5)
t1.pack(pady=5)
btn2.pack(pady=10)

window.mainloop()
