from tkinter import*
from database import *
import random
class waiter(base):
    __tablename__="waiters"
    id=Column(Integer, primary_key=True)
    name=Column(String(250),nullable=False)

    def __init__(self,name):
        self.name=name 
        self.window1=Tk()
        self.window1.config(bg="#375362")
        self.window1.config(padx=20,pady=20)
        self.order=Button(self.window1,text="order"
        ,bg="#375362",fg="white",font=("Arial",10,"italic"),
        command=self.grid_order_page)
        self.order.grid(row=0,column=2)
        self.order_page=[]
        self.window1.mainloop()
    def define_table_number(self):
        targed_table=select(Table)
        tables=[]
        with engine.connect() as conn:
            for row in conn.execute(targed_table):
                tables.append(row.number)
            table_number=random.choice(tables)
        return table_number
    def define_customers_number(self,table_number):
        customers_number=0
        targed_table=select(Table)
        with engine.connect() as conn:
            for row in conn.execute(targed_table):
                if row.number==table_number:
                    customers_number=random.randint(1,row.seats)
                    break
        return customers_number
    def take_food_order(self,customers_number):
        targed_table_food=session.query(Food).all()
        targed_table_drink=session.query(Drinks).all()
        order=[]
        for element in range(customers_number):
            choice=[]
            customer_food_choice=random.choice(targed_table_food)
            customer_drink_choice=random.choice(targed_table_drink)
            choice.append(customer_food_choice.name+" "+customer_food_choice.type)
            choice.append(customer_drink_choice.name+" "+customer_drink_choice.size)
            choice.append(customer_food_choice.price)
            choice.append(customer_drink_choice.price)
            order.append(choice)
        return order
    def create_order_page(self):
        table_number=self.define_table_number()
        customers_number=self.define_customers_number(table_number)
        food_order=self.take_food_order(customers_number)
        ###
        Order_label=Label(self.window1,text="Order",bg="#375362",fg="white",font=("Arial",10,"italic"))
        table_number_lable=Label(self.window1,text=f"Table number: {table_number}"
        ,bg="#375362",fg="white",font=("Arial",10,"italic"))
        customer_number_label=Label(self.window1,text=f"customers_number: {customers_number}"
        ,bg="#375362",fg="white",font=("Arial",10,"italic"))
        self.order_page.append(Order_label)
        self.order_page.append(table_number_lable)
        self.order_page.append(customer_number_label)
        for element in food_order:
            customer_order=Label(self.window1,text=f"{element[0]} {element[1]} ",
            bg="#375362",fg="white",font=("Arial",10,"italic"))
            self.order_page.append(customer_order)
        return self.order_page
    def grid_order_page(self):
        order=self.create_order_page()
        row=1
        for element in order:
            element.grid(row=row, column=0)
            row+=1
    