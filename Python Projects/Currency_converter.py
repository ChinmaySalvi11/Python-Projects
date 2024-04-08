import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        # Top Frame
        top_frame = tk.Frame(root,bg="Blue", pady=10)
        title_label = tk.Label(top_frame, text="Currency Converter", font=("Helvetica", 14,"bold"), bg="Blue", fg="white",width="21")
        title_label.pack()
        top_frame.pack(fill="x")
        top_frame.place(x=510,y=45)

        # Main Frame
        main_frame = tk.Frame(root, padx=14, pady=20, bd=2, relief="groove")
        

        self.amount_label = tk.Label(main_frame, text="Amount:")
        self.amount_label.grid(row=0, column=0, pady=10)

        self.amount_entry = tk.Entry(main_frame)
        self.amount_entry.grid(row=0, column=1, pady=10)

        self.from_currency_label = tk.Label(main_frame, text="From Currency:")
        self.from_currency_label.grid(row=1, column=0, pady=5)

        self.from_currency_combobox = ttk.Combobox(main_frame, values=[], state="readonly")
        self.from_currency_combobox.grid(row=1, column=1, pady=5)

        self.to_currency_label = tk.Label(main_frame, text="To Currency:")
        self.to_currency_label.grid(row=2, column=0, pady=5)

        self.to_currency_combobox = ttk.Combobox(main_frame, values=[], state="readonly")
        self.to_currency_combobox.grid(row=2, column=1, pady=5)

        self.result_label = tk.Label(main_frame, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.convert_button = tk.Button(main_frame, text="Convert", command=self.convert, bg="Blue", fg="white",font=("Helvetica", 13,"bold"))
        self.convert_button.grid(row=4, column=0, columnspan=4, pady=17)

        main_frame.pack(pady=85)

        # Set Currency Combobox values
        self.set_currency_combobox_values()

    def set_currency_combobox_values(self):
        # You may want to fetch the currency codes dynamically from an API
        # For demonstration purposes, I'm using a static list
        currencies = ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "INR"]

        self.from_currency_combobox['values'] = currencies
        self.from_currency_combobox.set("USD")  # Set default value

        self.to_currency_combobox['values'] = currencies
        self.to_currency_combobox.set("EUR")  # Set default value

    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_combobox.get().upper()
            to_currency = self.to_currency_combobox.get().upper()

            c = CurrencyRates()
            rate = c.get_rate(from_currency, to_currency)
            result = round(amount * rate, 2)

            self.result_label.config(text=f"Converted Amount: {result} {to_currency}")
        except ValueError:
            self.result_label.config(text="Please enter valid numeric values.")
        except Exception as e:
            self.result_label.config(text=f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
