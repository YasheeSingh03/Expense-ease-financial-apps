import tkinter as tk
from tkinter import messagebox, simpledialog, font
from datetime import datetime
import json
from PIL import Image, ImageTk
import random
import webbrowser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class BudgetApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Budgeting App")
        self.root.geometry('1750x1000')
        self.transactions = {}  # Dictionary to store transactions for each name

        # Load and display background image
        self.set_background_image(r"C:\Users\Yashee Singh\OneDrive\Desktop\Monthly-Money-Routine-10-Budgeting-Steps.webp")

        # Create login frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.place(x=500, y=270, height=300)

        opening_label = tk.Label(self.login_frame, text="Expense Ease", font=("Times New Roman", 56, "bold"),
                                 bg="burlywood2")
        custom_font = font.Font(opening_label, opening_label.cget("font"))
        custom_font.configure(underline=True)
        opening_label.configure(font=custom_font)
        opening_label.pack()

        self.username_label = tk.Label(self.login_frame, text="Username:", font=("Times", 15, "bold italic"),
                                       bg="burlywood3")
        self.username_label.place(x=85, y=160)
        self.username_entry = tk.Entry(self.login_frame, font=("Times", 15, "bold italic"), width=20)
        self.username_entry.place(x=210, y=160)

        self.password_label = tk.Label(self.login_frame, text="Password:", font=("Times", 15, "bold italic"),
                                       bg="burlywood3")
        self.password_label.place(x=85, y=200)
        self.password_entry = tk.Entry(self.login_frame, show="*", font=("Times", 15, "bold italic"), width=20)
        self.password_entry.place(x=210, y=200)

        self.login_button = tk.Button(self.login_frame, text="LOGIN", command=self.authenticate_user,
                                      font=("Times", 12, "bold italic"), bg="honeydew4")
        self.login_button.place(x=230, y=250)
        self.sign_up_button = tk.Button(self.login_frame, text="SIGN UP", command=self.sign_up,
                                        font=("Times", 12, "bold italic"), bg="honeydew4")
        self.sign_up_button.place(x=340, y=250)

        self.load_transactions()
        # Bind the Enter key to the entry fields for login
        self.username_entry.bind('<Return>', lambda event: self.password_entry.focus())
        self.password_entry.bind('<Return>', lambda event: self.authenticate_user())
    
    def sign_up(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Ask for phone number
        phone_number = simpledialog.askstring("Sign Up", "Enter your phone number:")
        if phone_number:
            # Generate OTP
            otp = ''.join(random.choices('0123456789', k=6))

            # Send OTP to email (Replace 'your_email@gmail.com' and 'your_password' with your email credentials)
            sender_email = 'your_email@gmail.com'
            receiver_email = phone_number + '@sms_gateway.com'  # Replace 'sms_gateway.com' with the actual SMS gateway domain
            password = 'your_password'
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = 'OTP Verification'
            body = f'Your OTP for sign-up: {otp}'
            message.attach(MIMEText(body, 'plain'))
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, password)
                text = message.as_string()
                server.sendmail(sender_email, receiver_email, text)
                server.quit()
                messagebox.showinfo("OTP Sent", "An OTP has been sent to your phone number. Please check your messages.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "Phone number is required for sign-up.")

    def set_background_image(self, image_path):
        # Load background image and resize it to fit the screen
        background_image = Image.open(image_path)
        background_image = background_image.resize((1750, 1000))
        self.background_photo = ImageTk.PhotoImage(background_image)

        # Create a label to hold the background image and place it in the root window
        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def authenticate_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Dummy authentication (replace with your authentication logic)
        if username == "Allies" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome, Allies!")
            self.show_main_app()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

    def show_main_app(self):
        # Destroy login frame
        self.login_frame.destroy()

        # Create a frame for the main application window
        self.main_app_frame = tk.Frame(self.root)
        self.main_app_frame.place(x=160, y=0, height=800, width=1200)
        o = tk.Label(self.main_app_frame, text="NOTE :1. Click on the buttons for respective policies. \n  2. For Tips,right click anywhere on the screen. ",
                     bg="darkgray")
        o.place(x=470, y=710)

        opening_label = tk.Label(self.main_app_frame, text="Expense Ease", font=("Times New Roman", 56, "bold"),
                                 bg="burlywood2")
        custom_font = font.Font(opening_label, opening_label.cget("font"))
        custom_font.configure(underline=True)
        opening_label.configure(font=custom_font)
        opening_label.pack()

        self.name_label = tk.Label(self.main_app_frame, text="Name:", font=("Times", 15, "bold italic"),
                                   bg="burlywood3")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.main_app_frame, font=("Times", 15, "bold italic"), width=60)
        self.name_entry.pack()

        self.income_label = tk.Label(self.main_app_frame, text="Income:", font=("Times", 15, "bold italic"),
                                     bg="burlywood3")
        self.income_label.pack()
        self.income_entry = tk.Entry(self.main_app_frame, font=("Times", 15, "bold italic"), width=60)
        self.income_entry.pack()

        self.expense_label = tk.Label(self.main_app_frame, text="Expense:", font=("Times", 15, "bold italic"),
                                      bg="burlywood3")
        self.expense_label.pack()
        self.expense_entry = tk.Entry(self.main_app_frame, font=("Times", 15, "bold italic"), width=60)
        self.expense_entry.pack()

        self.category_label = tk.Label(self.main_app_frame, text="Category:", font=("Times", 15, "bold italic"),
                                       bg="burlywood3")
        self.category_label.pack()
        self.category_var = tk.StringVar(self.main_app_frame)
        self.category_var.set("Select Category")
        self.category_menu = tk.OptionMenu(self.main_app_frame, self.category_var, "Food", "Transportation", "Housing",
                                           "Utilities", "Entertainment", "Education", "Grocery", "Other")
        self.category_menu.config(width=95)
        self.category_menu.pack()

        self.source_label = tk.Label(self.main_app_frame, text="Source of Income:", font=("Times", 15, "bold italic"),
                                     bg="burlywood3")
        self.source_label.pack()
        self.source_entry = tk.Entry(self.main_app_frame, font=("Times", 15, "bold italic"), width=60)
        self.source_entry.pack()

        self.savings_goal_button = tk.Button(self.main_app_frame, text="SET SAVING GOAL", command=self.set_savings_goal,
                                             font=("Helvetica", 12, "bold italic"), bg="tan2")
        self.savings_goal_button.place(x=500, y=500)

        self.add_button = tk.Button(self.main_app_frame, text="ADD", command=self.add_transaction,
                                    font=("Times", 12, "bold italic"), bg="honeydew4")
        self.add_button.place(x=560, y=415)

        self.delete_button = tk.Button(self.main_app_frame, text="DELETE", command=self.delete_transaction,
                                       font=("Times", 12, "bold italic"), bg="honeydew4")
        self.delete_button.place(x=500, y=455)

        self.clear_button = tk.Button(self.main_app_frame, text="CLEAR", command=self.clear_transactions,
                                      font=("Times", 12, "bold italic"), bg="honeydew4")
        self.clear_button.place(x=590, y=455)

        self.show_button = tk.Button(self.main_app_frame, text="SHOW DETAILS", command=self.show_details,
                                     font=("Times", 12, "bold italic"), bg="honeydew4")
        self.show_button.place(x=360, y=500)

        self.forecast_button = tk.Button(self.main_app_frame, text="FORECAST", command=self.forecast,
                                         font=("Times", 12, "bold italic"), bg="honeydew4")
        self.forecast_button.place(x=670, y=500)


        # Load the image and store a reference to it
        self.lic_image = Image.open(r"C:\Users\Yashee Singh\OneDrive\Desktop\Life_Insurance_Corporation_of_India_(logo).svg.png")
        self.lic_image = self.lic_image.resize((160, 100))  # Resize the image if necessary
        self.lic_photo = ImageTk.PhotoImage(self.lic_image)

        # Create the LIC button with the image and command
        self.lic_button = tk.Button(self.main_app_frame, font=("Times", 13, "bold"), image=self.lic_photo,
                                    width=160, height=100, bg="thistle3", command=self.lic_button_clicked)
        self.lic_button.place(x=110, y=580)

        # Load the mutual fund image and store a reference to it
        self.mutual_image = Image.open(r"C:\Users\Yashee Singh\OneDrive\Desktop\images.jpeg")
        self.mutual_image = self.mutual_image.resize((160, 100))  # Resize the image if necessary
        self.mutual_photo = ImageTk.PhotoImage(self.mutual_image)

        # Create the mutual fund button with the image and command
        self.mutual_button = tk.Button(self.main_app_frame, font=("Times", 13, "bold"), image=self.mutual_photo,
                                       width=160, height=100, bg="thistle3", command=self.mutual_button_clicked)
        self.mutual_button.place(x=310, y=580)

        # Load the Bajaj image and store a reference to it
        self.bajaj_image = Image.open(r"C:\Users\Yashee Singh\OneDrive\Desktop\imag.jpeg.jpg")
        self.bajaj_image = self.bajaj_image.resize((160, 100))  # Resize the image if necessary
        self.bajaj_photo = ImageTk.PhotoImage(self.bajaj_image)

        # Create the Bajaj button with the image and command
        self.bajaj_button = tk.Button(self.main_app_frame, font=("Times", 13, "bold"), image=self.bajaj_photo,
                                      width=160, height=100, bg="thistle3", command=self.bajaj_button_clicked)
        self.bajaj_button.place(x=510, y=580)

        # Load the BA image and store a reference to it
        self.ba_image = Image.open(r"C:\Users\Yashee Singh\OneDrive\Desktop\u.jpg")
        self.ba_image = self.ba_image.resize((160, 100))  # Resize the image if necessary
        self.ba_photo = ImageTk.PhotoImage(self.ba_image)

        # Create the BA button with the image and command
        self.ba_button = tk.Button(self.main_app_frame, font=("Times", 13, "bold"), image=self.ba_photo,
                                   width=160, height=100, bg="thistle3", command=self.ba_button_clicked)
        self.ba_button.place(x=710, y=580)

        self.emi_image = Image.open(r"C:\Users\Yashee Singh\OneDrive\Desktop\what-is-an-emi-717x404.webp")
        self.emi_image = self.emi_image.resize((160, 100))  # Resize the image if necessary
        self.emi_photo = ImageTk.PhotoImage(self.emi_image)

        # Create the mutual fund button with the image and command
        self.emi_button = tk.Button(self.main_app_frame, font=("Times", 13, "bold"), image=self.emi_photo,
                                       width=160, height=100, bg="thistle3",command=self.emi)
        self.emi_button.place(x=910, y=580)

        # Budget tips and advice dropdown menu
        self.tips_menu = tk.Menu(root, tearoff=0)
        self.tips_menu.add_command(label="Tip 1: Create a budget plan", command=self.show_tip_1)
        self.tips_menu.add_command(label="Tip 2: Track your expenses", command=self.show_tip_2)
        self.tips_menu.add_command(label="Tip 3: Limit impulse purchases", command=self.show_tip_3)
        self.tips_menu.add_command(label="Tip 4: Use cashback and rewards", command=self.show_tip_4)
        self.tips_menu.add_command(label="Tip 5: Review and adjust your budget regularly", command=self.show_tip_5)

        self.root.bind("<Button-3>", self.show_tips_menu)

        # Add a menu option for setting the savings goal
        self.menu_bar = tk.Menu(root)
        self.menu_bar.add_command(label="Set Savings Goal", command=self.set_savings_goal)
        root.config(menu=self.menu_bar)

        # Load transactions from file
        self.load_transactions()

    def show_tips_menu(self, event):
        self.tips_menu.post(event.x_root, event.y_root)

    def show_tip_1(self):
        messagebox.showinfo("Tip 1", "Create a budget plan: For your income level, it's important to create a detailed budget plan to manage your expenses effectively.")

    def show_tip_2(self):
        messagebox.showinfo("Tip 2", "Track your expenses: Keep track of all your expenses to understand where your money is going.")

    def show_tip_3(self):
        messagebox.showinfo("Tip 3", "Limit impulse purchases: Avoid making impulse purchases by sticking to your budget plan.")

    def show_tip_4(self):
        messagebox.showinfo("Tip 4", "Use cashback and rewards: Take advantage of cashback offers and rewards programs to save money.")

    def show_tip_5(self):
        messagebox.showinfo("Tip 5", "Review and adjust your budget regularly: Review your budget regularly and make adjustments as needed.")

    def set_savings_goal(self):
        # Prompt the user to input their savings goal amount
        savings_goal = simpledialog.askfloat("Set Savings Goal", "Enter your savings goal amount:")
        if savings_goal is not None:
            self.savings_goal = savings_goal
            messagebox.showinfo("Savings Goal", f"Your savings goal is set to: {savings_goal}")

    def add_transaction(self):
        name = self.name_entry.get()
        income = self.income_entry.get()
        expense = self.expense_entry.get()
        category = self.category_var.get()
        source_of_income = self.source_entry.get()  # Retrieve the source of income

        try:
            income = float(income)
            expense = float(expense)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
            return

        difference = income - expense

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        messagebox.showinfo("Success", "Transaction successfully added!")
        # Calculate net income after deducting tax
        if income > 500000:  # If income exceeds 5 lakhs, deduct 5% tax from the amount exceeding 5 lakhs
            tax_amount = (income - 500000) * 0.05
            net_income = income - tax_amount
        else:
            net_income = income

        # Initialize balance for name if it doesn't exist
        if name not in self.transactions:
            self.transactions[name] = {"balance": 0, "transactions": []}

        self.transactions[name]["balance"] += net_income - expense

        # Check if savings goal is set
        if hasattr(self, 'savings_goal') and self.transactions[name]["balance"] >= self.savings_goal:
            self.transactions[name]["savings_goal"] = "Savings goal met!"
            messagebox.showinfo("Congratulations", f"Congratulations, {name}! You have achieved your savings goal.")
        elif hasattr(self, 'savings_goal') and self.transactions[name]["balance"] < self.savings_goal:
            self.transactions[name]["savings_goal"] = "Savings goal not met!"
            messagebox.showinfo("Savings Goal Update", f"Sorry, {name}. You have not met your savings goal yet.")

        transaction_info = {"timestamp": timestamp, "income": net_income, "expense": expense, "category": category,
                            "source_of_income": source_of_income}  # Include source_of_income in transaction details
        self.transactions[name]["transactions"].append(transaction_info)

        self.update_transaction_display(name, timestamp, net_income, expense, category, source_of_income)  # Pass source_of_income to update_transaction_display

        self.name_entry.delete(0,tk.END)
        self.income_entry.delete(0, tk.END)
        self.expense_entry.delete(0, tk.END)
        self.source_entry.delete(0, tk.END)
        self.category_var.set("Select Category")

        # Save transactions to file
        self.save_transactions()

    def delete_transaction(self):
        name = self.name_entry.get()
        category = self.category_var.get()
        transactions = self.transactions.get(name, {}).get("transactions", [])
        if not transactions:
            messagebox.showerror("Error", "No transactions found for this name")
            return

        for idx, transaction in enumerate(transactions):
            if transaction['category'] == category:
                del self.transactions[name]["transactions"][idx]
                break

        self.update_transaction_display(name)  # Update displayed transactions
        self.save_transactions()  # Save transactions to file

    def clear_transactions(self):
        name = self.name_entry.get()
        if name in self.transactions:
            del self.transactions[name]
            self.update_transaction_display(name)  # Update displayed transactions
            self.save_transactions()  # Save transactions to file

    def highlight_categories(self, event):
        self.category_menu.selection_clear()

    def update_transaction_display(self, name, timestamp=None, income=None, expense=None, category=None,
                                    source_of_income=None):
        if name not in self.transactions:
            return

        self.transactions_text.config(state=tk.NORMAL)  # Enable editing to insert new transactions
        self.transactions_text.delete(1.0, tk.END)  # Clear existing content

        for transaction in self.transactions[name]["transactions"]:
            self.transactions_text.insert(tk.END, f"Name: {name}\n")
            self.transactions_text.insert(tk.END, f"Date & Time: {transaction['timestamp']}\n")
            self.transactions_text.insert(tk.END, f"Income: {transaction['income']}\n")
            self.transactions_text.insert(tk.END, f"Expense: {transaction['expense']}\n")
            self.transactions_text.insert(tk.END, f"Category: {transaction['category']}\n")
            self.transactions_text.insert(tk.END,
                                          f"Source of Income: {transaction['source_of_income']}\n")  # Display source of income
            self.transactions_text.insert(tk.END, "\n" + "-" * 50 + "\n")

        # Scroll to the end of the text widget
        self.transactions_text.see(tk.END)

        self.transactions_text.config(state=tk.DISABLED)  # Disable editing after updating

    def save_transactions(self):
        with open("transactions.json", "w") as file:
            json.dump(self.transactions, file)

    def load_transactions(self):
        try:
            with open("transactions.json", "r") as file:
                self.transactions = json.load(file)
        except FileNotFoundError:
            pass

    def show_details(self):
        name = self.name_entry.get()

        if name in self.transactions:
            
            messagebox.showinfo("Transaction Details", json.dumps(self.transactions[name], indent=4))
        else:
            messagebox.showerror("Error", "No transactions found for this name")
            
    def forecast(self):
        # Get the name entered by the user
        name = self.name_entry.get()

        if name not in self.transactions:
            messagebox.showerror("Error", "No transactions found for this name")
            return

        transactions = self.transactions[name]["transactions"]
        last_balance = self.transactions[name]["balance"]

        # Calculate average income and expense over the last few transactions
        num_transactions = len(transactions)
        total_income = sum(transaction["income"] for transaction in transactions)
        total_expense = sum(transaction["expense"] for transaction in transactions)

        if num_transactions == 0:
            messagebox.showerror("Error", "No transactions found for forecasting")
            return

        avg_income = total_income / num_transactions
        avg_expense = total_expense / num_transactions

        # Calculate average monthly change in income and expense
        monthly_changes_income = [(transactions[i]["income"] - transactions[i - 1]["income"]) for i in
                                  range(1, len(transactions))]
        monthly_changes_expense = [(transactions[i]["ixpense"] - transactions[i - 1]["expense"]) for i in
                                   range(1, len(transactions))]

        avg_monthly_change_income = sum(monthly_changes_income) / len(
            monthly_changes_income) if monthly_changes_income else 0
        avg_monthly_change_expense = sum(monthly_changes_expense) / len(
            monthly_changes_expense) if monthly_changes_expense else 0

        # Forecast future income, expense, and savings
        num_months = 6  # Number of months for forecasting
        forecast_data = []
        projected_balance = last_balance
        for month in range(1, num_months + 1):
            # Add variability to projected income and expense based on historical trends
            projected_income = max(avg_income + random.uniform(-0.1 * avg_income, 0.1 * avg_income), 0)
            projected_expense = max(avg_expense + random.uniform(-0.1 * avg_expense, 0.1 * avg_expense), 0)

            projected_balance += (projected_income - projected_expense)

            forecast_data.append({
                "Month": month,
                "Projected Income": projected_income,
                "Projected Expense": projected_expense,
                "Projected Balance": projected_balance
            })
        
           

        # Display forecast data in a table
        forecast_str = "\n".join([json.dumps(entry, indent=4) for entry in forecast_data])
        messagebox.showinfo("Forecast", forecast_str)

    def emi(self):
        emi_window=tk.Toplevel(self.root)
        emi_window.title("EMI CALCULATOR")
        emi_window.geometry("900x445")
        lic_image_path = r"C:\Users\Yashee Singh\OneDrive\Desktop\What-is-EMI.jpg"
        lic_image = Image.open(lic_image_path)
        lic_image = lic_image.resize((900, 445))  # Resize the image if necessary
        lic_photo = ImageTk.PhotoImage(lic_image)

    # Create a label to display the image
        lic_image_label = tk.Label(emi_window, image=lic_photo)
        lic_image_label.image = lic_photo  # Keep a reference to the image to prevent it from being garbage collected
        lic_image_label.pack()


        lic_label = tk.Label(emi_window, text="EMI CALCULATOR ", font=("Georgia",20,"bold"))
        lic_label.place(x=300,y=30)
        self.principal_label = tk.Label(emi_window, text="Loan Amount:",font=("Georgia",15))
        self.principal_label.place(x=300,y=110)
        self.principal_entry = tk.Entry(emi_window,width=30)
        self.principal_entry.place(x=530,y=115)

        self.term_label = tk.Label(emi_window, text="Interest Rate:",font=("Georgia",15))
        self.term_label.place(x=300,y=150)
        self.term_entry = tk.Entry(emi_window,width=30)
        self.term_entry.place(x=530,y=155)

        self.amount=tk.Label(emi_window,text="Number of years:",font=("Georgia",15))
        self.amount.place(x=300,y=190)
        self.amount_entry=tk.Entry(emi_window,width=30)
        self.amount_entry.place(x=530,y=195)

        self.calculate_button = tk.Button(emi_window, text="Calculate", command=self.calculate_emi,font=("Times",12),bg="burlywood2")
        self.calculate_button.place(x=475,y=250)


    def calculate_emi(self):
        try:
            principal = int(self.principal_entry.get())
            rate= int(self.term_entry.get())
            years=int(self.amount_entry.get())
            monthly_rate = rate / 12 / 100
    
    # Calculate EMI
            emi = principal * monthly_rate * ((1 + monthly_rate) ** years) / (((1 + monthly_rate) ** years) - 1)
            
            messagebox.showinfo("EMI",f"The EMI amount after {years} years will be: ₹{emi:,.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values")    
 

    def lic_button_clicked(self):
        lic_window = tk.Toplevel(self.root)
        lic_window.title("LIC Details")
        lic_window.geometry("900x445")
        lic_image_path = r"C:\Users\Yashee Singh\OneDrive\Desktop\WhatsApp Image 2024-04-11 at 17.06.15_745c6f76.jpg"
        lic_image = Image.open(lic_image_path)
        lic_image = lic_image.resize((900, 445))  # Resize the image if necessary
        lic_photo = ImageTk.PhotoImage(lic_image)

    # Create a label to display the image
        lic_image_label = tk.Label(lic_window, image=lic_photo)
        lic_image_label.image = lic_photo  # Keep a reference to the image to prevent it from being garbage collected
        lic_image_label.pack()

        lic_label = tk.Label(lic_window, text="LIC's NEW MONEY BACK PLAN ", font=("Georgia",20,"bold"))
        lic_label.place(x=300,y=30)
        self.principal_label = tk.Label(lic_window, text="Money to be invested:",font=("Georgia",15))
        self.principal_label.place(x=300,y=110)
        self.principal_entry = tk.Entry(lic_window,width=30)
        self.principal_entry.place(x=530,y=115)

        self.term_label = tk.Label(lic_window, text="For how many years:",font=("Georgia",15))
        self.term_label.place(x=300,y=150)
        self.term_entry = tk.Entry(lic_window,width=30)
        self.term_entry.place(x=530,y=155)
 
        self.calculate_button = tk.Button(lic_window, text="Calculate", command=self.calculate_maturity,font=("Times",12),bg="burlywood2")
        self.calculate_button.place(x=475,y=200)

        def open_lic_website():
            webbrowser.open("https://www.policybazaar.com/lic-of-india/lic-jeevan-money-back-plan-20-years-calculator/") 
        show_details_button = tk.Button(lic_window, text="Show Details", command=open_lic_website, font=("Times", 12),bg="burlywood2")
        show_details_button.place(x=466,y=280)

        def open_youtube():
            webbrowser.open("https://youtu.be/Rj3MkF-dEPo?si=yHnqXgQnhk36Tv_9")  # Replace YOUR_VIDEO_ID_HERE with the actual video ID
        youtube_button = tk.Button(lic_window, text="Watch Video", command=open_youtube, font=("Times", 12),bg="red")
        youtube_button.place(x=465,y=240)
    
    def calculate_maturity(self):
        try:
            principal = int(self.principal_entry.get())
            years = int(self.term_entry.get())
            interest_rate = 5 
            r = interest_rate / 100
            A = principal * (1 + r) ** years
            messagebox.showinfo("Maturity Amount", f"The maturity amount after {years} years will be: ₹{A:,.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for principal amount")    
    def mutual_button_clicked(self):
        lic_window = tk.Toplevel(self.root)
        lic_window.title("Mutual funds Details")
        lic_window.geometry("900x445")
        lic_image_path = r"C:\Users\Yashee Singh\OneDrive\Desktop\WhatsApp Image 2024-04-11 at 16.39.31_a2600ee7.jpg"
        lic_image = Image.open(lic_image_path)
        lic_image = lic_image.resize((900, 445))  # Resize the image if necessary
        lic_photo = ImageTk.PhotoImage(lic_image)

    # Create a label to display the image
        lic_image_label = tk.Label(lic_window, image=lic_photo)
        lic_image_label.image = lic_photo  # Keep a reference to the image to prevent it from being garbage collected
        lic_image_label.pack()

        lic_label = tk.Label(lic_window, text="HDFC LIFE SAMPOORAN NIVESH ", font=("Georgia",20,"bold"))
        lic_label.place(x=300,y=30)
        self.principal_label = tk.Label(lic_window, text="Money to be invested:",font=("Georgia",15))
        self.principal_label.place(x=300,y=110)
        self.principal_entry = tk.Entry(lic_window,width=20)
        self.principal_entry.place(x=530,y=115)

        self.term_label = tk.Label(lic_window, text="For how many years:",font=("Georgia",15))
        self.term_label.place(x=300,y=150)
        self.term_entry = tk.Entry(lic_window)
        self.term_entry.place(x=530,y=155)

        self.calculate_button = tk.Button(lic_window, text="Calculate", command=self.maturity,font=("Times",12),bg="burlywood2")
        self.calculate_button.place(x=470,y=200)

        def open_youtube():
            webbrowser.open("https://youtu.be/nBB5IKQ-vuo?si=2fTJ3dAXXW00XJL0")  # Replace YOUR_VIDEO_ID_HERE with the actual video ID
        youtube_button = tk.Button(lic_window, text="Watch Video", command=open_youtube, font=("Times", 12),bg="red")
        youtube_button.place(x=465,y=240)

        def open_lic_website():
            webbrowser.open("https://www.hdfclife.com/ulip-plans/sampoorn-nivesh-ulip-policy") 
        show_details_button = tk.Button(lic_window, text="Show Details", command=open_lic_website, font=("Times", 12),bg="burlywood2")
        show_details_button.place(x=466,y=280)

    def maturity(self):
        try:
            principal = float(self.principal_entry.get())
            years = int(self.term_entry.get())
            interest_rate = 5 
            r = interest_rate / 100
            A = principal * (1 + r) ** years
            messagebox.showinfo("Maturity Amount", f"The maturity amount after {years} years will be: ₹{A:,.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for principal amount")    
        
    def bajaj_button_clicked(self):
        lic_window = tk.Toplevel(self.root)
        lic_window.title("Bajaj Details")
        lic_window.geometry("900x445")
        lic_image_path = r"C:\Users\Yashee Singh\OneDrive\Desktop\WhatsApp Image 2024-04-11 at 17.10.03_0f1e0187.jpg"
        lic_image = Image.open(lic_image_path)
        lic_image = lic_image.resize((900, 445))  # Resize the image if necessary
        lic_photo = ImageTk.PhotoImage(lic_image)

    # Create a label to display the image
        lic_image_label = tk.Label(lic_window, image=lic_photo)
        lic_image_label.image = lic_photo  # Keep a reference to the image to prevent it from being garbage collected
        lic_image_label.pack()


        lic_label = tk.Label(lic_window, text="BAJAJ ALLIANCE YOUNG ASSURE ", font=("Georgia",20,"bold"))
        lic_label.place(x=300,y=30)
        self.principal_label = tk.Label(lic_window, text="Money to be invested:",font=("Georgia",15))
        self.principal_label.place(x=300,y=110)
        self.principal_entry = tk.Entry(lic_window,width=20)
        self.principal_entry.place(x=530,y=115)

        self.term_label = tk.Label(lic_window, text="For how many years:",font=("Georgia",15))
        self.term_label.place(x=300,y=150)
        self.term_entry = tk.Entry(lic_window)
        self.term_entry.place(x=530,y=155)

        self.calculate_button = tk.Button(lic_window, text="Calculate", command=self.maturity,font=("Times",12),bg="burlywood2")
        self.calculate_button.place(x=470,y=200)

        def open_youtube():
            webbrowser.open("https://youtu.be/fsGWR7CMDGw?si=jJ0HlFLiSjJs2a7R")  # Replace YOUR_VIDEO_ID_HERE with the actual video ID
        youtube_button = tk.Button(lic_window, text="Watch Video", command=open_youtube, font=("Times", 12),bg="red")
        youtube_button.place(x=465,y=240)

        def open_lic_website():
            webbrowser.open("https://www.bajajallianzlife.com/content/dam/balic/pdf/child-plans/young-assure-brochure.pdf") 
        show_details_button = tk.Button(lic_window, text="Show Details", command=open_lic_website, font=("Times", 12),bg="burlywood2")
        show_details_button.place(x=466,y=280)
   
    def maturity(self):
        try:
            principal = float(self.principal_entry.get())
            years = int(self.term_entry.get())
            interest_rate = 5 
            r = interest_rate / 100
            A = principal * (1 + r) ** years
            messagebox.showinfo("Maturity Amount", f"The maturity amount after {years} years will be: ₹{A:,.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for principal amount")    
        
    def ba_button_clicked(self):
        lic_window = tk.Toplevel(self.root)
        lic_window.title("Life Insurance Details")
        lic_window.geometry("900x445")
        lic_image_path = r"C:\Users\Yashee Singh\OneDrive\Desktop\WhatsApp Image 2024-04-11 at 16.55.32_c8b281f9.jpg"
        lic_image = Image.open(lic_image_path)
        lic_image = lic_image.resize((900, 755))  # Resize the image if necessary
        lic_photo = ImageTk.PhotoImage(lic_image)

    # Create a label to display the image
        lic_image_label = tk.Label(lic_window, image=lic_photo)
        lic_image_label.image = lic_photo  # Keep a reference to the image to prevent it from being garbage collected
        lic_image_label.pack()

        lic_label = tk.Label(lic_window, text="SBI LIFE e-shield ", font=("Georgia",20,"bold"))
        lic_label.place(x=300,y=30)
        self.principal_label = tk.Label(lic_window, text="Money to be invested:",font=("Georgia",15))
        self.principal_label.place(x=300,y=110)
        self.principal_entry = tk.Entry(lic_window,width=20)
        self.principal_entry.place(x=530,y=115)

        self.term_label = tk.Label(lic_window, text="For how many years:",font=("Georgia",15))
        self.term_label.place(x=300,y=150)
        self.term_entry = tk.Entry(lic_window)
        self.term_entry.place(x=530,y=155)

        self.calculate_button = tk.Button(lic_window, text="Calculate", command=self.maturity,font=("Times",12),bg="burlywood2")
        self.calculate_button.place(x=475,y=200)

        def open_youtube():
            webbrowser.open("https://youtu.be/cnWJa5kpQNk?si=eVnpA2LDCTiCe_O3")  # Replace YOUR_VIDEO_ID_HERE with the actual video ID
        youtube_button = tk.Button(lic_window, text="Watch Video", command=open_youtube, font=("Times", 12),bg="red")
        youtube_button.place(x=465,y=240)

        def open_lic_website():
            webbrowser.open("https://www.sbilife.co.in/en/online-insurance-plans/eshield-next") 
        show_details_button = tk.Button(lic_window, text="Show Details", command=open_lic_website, font=("Times", 12),bg="burlywood2")
        show_details_button.place(x=466,y=280)

    def maturity(self):
        try:
            principal = float(self.principal_entry.get())
            years = int(self.term_entry.get())
            interest_rate = 5 
            r = interest_rate / 100
            A = principal * (1 + r) ** years
            messagebox.showinfo("Maturity Amount", f"The maturity amount after {years} years will be: ₹{A:,.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for principal amount")    
        
    def save_transactions(self):
        with open("transactions.json", "w") as file:
            json.dump(self.transactions, file)

    def load_transactions(self):
        try:
            with open("transactions.json", "r") as file:
                self.transactions = json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, initialize transactions as an empty dictionary
            self.transactions = {}
    
root = tk.Tk()
app = BudgetApp(root)
root.mainloop()