from tkinter import*
from tkinter import messagebox
from database import *
class ui_manager:
    def __init__(self):
        self.window=Tk()
        self.window.title("Menu")
        self.window.config(bg="#375362")
        self.window.config(padx=20,pady=20)
        self.food_order=[]
        self.drink_order=[]
        self.order=[]
        self.main_page_list=[]
        self.tables_buttons_list=[]
        self.menu_page=[]
        self.food_page=[]
        self.drink_page=[]
        self.grid_main_page()
        self.window.mainloop()
    def create_main_page_button(self):
        main_menu=Label(self.window,text="Main Menu",bg="#375362",fg="white",font=("Arial",10,"italic"))      
        neu_order=Button(self.window,text="new Order",width=9,bg="#375362",fg="white",font=("Arial",10,"italic")
        ,command=self.grid_table_page)
        modifie_order=Button(self.window,text="modifie Order",bg="#375362",fg="white",font=("Arial",10,"italic")
        ,command=self.grid_modifie_order_page)
        cancel_order=Button(self.window,text="Cancel Order",bg="#375362",fg="white",font=("Arial",10,"italic"))
        self.main_page_list.append(main_menu)
        self.main_page_list.append(neu_order)
        self.main_page_list.append(modifie_order)
        self.main_page_list.append(cancel_order)
        return self.main_page_list
    def grid_main_page(self):
        row=1
        column=0
        list=self.create_main_page_button()
        list[0].grid(row=0,column=0)
        for element in list[1:]:
            element.grid(row=row,column=column)
            column+=1
            if column==3:
                row+=1
                column=0
    def erase_main_page(self):
        x=0
        for element in self.main_page_list: 
            if x==0:
                element.destroy()
            else:
                element.grid_forget()
            x+=1
        self.main_page_list.clear()
    def button_functions(self,table_number):
        self.get_table_number(table_number)
        self.grid_menu_page()
    def get_table_number(self,table_number):
        if len(self.order)>0:
            self.order.clear()
        list=table_number
        self.order.append(list)
        print(self.order)
    def create_table_page_button(self):
        Home=Button(self.window,text="Home",width=9,bg="#375362",fg="white",font=("Arial",10,"italic")
        ,command=self.go_home_from_table_page)
        back=Button(self.window,text="back",width=9,bg="#375362",fg="white",font=("Arial",10,"italic")
        ,command=self.go_home_from_table_page)
        table = select(Table)
        table_label=Label(self.window,text='Tables :',bg="#375362",fg="white",font=("Arial",10,"italic"))
        self.tables_buttons_list.append(table_label)
        with engine.connect() as conn:
            for row in conn.execute(table):
                text=f"{row.number}"
                table_button=Button(self.window,text=text,bg="#375362",fg="white",font=("Arial",10,"italic")
                ,command=lambda table_number=text:self.button_functions(table_number))
                self.tables_buttons_list.append(table_button)
                if row.empty==False:
                    table_button.config(state=DISABLED)
        self.tables_buttons_list.append(Home)
        self.tables_buttons_list.append(back)
        return self.tables_buttons_list
    def grid_table_page(self):
        try:
            self.erase_main_page()
        except:
            pass
        list=self.create_table_page_button()
        list[0].grid(row=0,column=0)
        row=1
        column=0
        for element in list[1:]:
            element.grid(row=row,column=column)
            column+=1
            if row==1 and column==3:
                row+=1
                column=0
            if row==2 and column==2:
                row+=1
                column=0
    def erase_table_page(self):
        x=0
        for element in self.tables_buttons_list: 
            if x==0:
                element.destroy()
            else:
                element.grid_forget()
            x+=1
        self.tables_buttons_list.clear()
    def go_home_from_table_page(self):
        self.erase_table_page()
        self.grid_main_page()
    def create_menu_page(self):
        Home=Button(self.window,text="Home",width=9,bg="#375362",fg="white",font=("Arial",10,"italic")
        ,command=self.go_home_from_menu)
        back=Button(self.window,text="back",width=9,bg="#375362",fg="white",font=("Arial",10,"italic")
        ,command=self.back_from_menu_page)
        menu=Label(self.window,text="Menu",bg="#375362",fg="white",font=("Arial",10,"italic"))
        food_button=Button(self.window,text="food",bg="#375362",fg="white",font=("Arial",10,"italic")
        ,command=self.grid_food_button)
        drinks_button=Button(self.window,text="drinks",bg="#375362",fg="white",font=("Arial",10,"italic")
        ,command=self.grid_drink_button)
        Validate_button=Button(self.window,text="validate",bg="#375362",fg="white",font=("Arial",10,"italic")
        ,command=self.save_order_in_data)
        self.menu_page.append(menu)
        self.menu_page.append(food_button)
        self.menu_page.append(drinks_button)
        self.menu_page.append(Validate_button)
        self.menu_page.append(Home)
        self.menu_page.append(back)
        return self.menu_page
    def grid_menu_page(self):
        self.erase_table_page()
        list=self.create_menu_page()
        list[0].grid(row=0,column=0)
        row=1
        column=0
        for element in list[1:]:
            element.grid(row=row,column=column)
            column+=1
            if row==2 and column==1:
                row+=1
                column=0
            if column==2:
                row+=1
                column=0
    def erase_menu_page(self):
        x=0
        for element in self.menu_page:
            if x==0:
                element.destroy()
            else:
                element.grid_forget()
            x+=1
        self.menu_page.clear()
    def go_home_from_menu(self):
        self.erase_menu_page()
        self.grid_main_page()
    def back_from_menu_page(self):
        self.erase_menu_page()
        self.grid_table_page()
    def create_food_button(self):
        Home=Button(self.window,text="Home",width=9,bg="#375362",fg="white",font=("Arial",10,"italic"),
        command=self.go_home_from_food_page)
        back=Button(self.window,text="back",width=9,bg="#375362",fg="white",font=("Arial",10,"italic"),
        command=self.go_back_from_food_page)
        correct=Button(self.window,text="C",width=9,bg="#375362",fg="white",font=("Arial",10,"italic"),
        command=lambda:self.correct_order(self.food_order))
        table = select(Food)
        food_label=Label(self.window,text="Food :",bg="#375362",fg="white",font=("Arial",10,"italic"))
        self.food_page.append(food_label)
        with engine.connect() as conn:
            for row in conn.execute(table):
                price=row.price
                text=f'{row.name} {row.type}'
                food_button=Button(self.window,text=text
                ,bg="#375362",fg="white",font=("Arial",10,"italic")
                ,command=lambda button_text=text,price=price: self.get_food_order(button_text,price))
                self.food_page.append(food_button)
        self.food_page.append(correct)
        self.food_page.append(Home)
        self.food_page.append(back)
        return self.food_page
    def grid_food_button(self):
        try:
            self.erase_menu_page()
        except:
            pass
        list=self.create_food_button()
        list[0].grid(row=0,column=0)
        row=1
        column=0
        for element in list[1:]:
            element.grid(row=row,column=column)
            column+=1
            if row==4 and column==1:
                column=0
                row+=1
            if column==3:
                column=0
                row+=1
    def erase_food_page(self):
        x=0
        for element in self.food_page:
            if x==0:
                element.destroy()
            else:
                element.grid_forget()
            x+=1
        self.food_page.clear()
    def erase_drink_page(self):
        x=0
        for element in self.drink_page:
            if x==0:
                element.destroy()
            else:
                element.grid_forget()
            x+=1
        self.drink_page.clear()
    def go_home_from_food_page(self):
        self.erase_food_page()
        self.grid_main_page()
    def go_back_from_food_page(self):
        self.erase_food_page()
        self.grid_menu_page()
    def create_drink_button(self):
        Home=Button(self.window,text="Home",width=9,bg="#375362",fg="white",font=("Arial",10,"italic"),
        command=self.go_home_from_drink_page)
        back=Button(self.window,text="back",width=9,bg="#375362",fg="white",font=("Arial",10,"italic"),
        command=self.go_back_from_drink_page)
        correct=Button(self.window,text="C",width=9,bg="#375362",fg="white",font=("Arial",10,"italic"),
        command=lambda:self.correct_order(self.drink_order))
        table = select(Drinks)
        drink_label=Label(self.window,text="Drinks :",bg="#375362",fg="white",font=("Arial",10,"italic"))
        self.drink_page.append(drink_label)
        with engine.connect() as conn:
            for row in conn.execute(table):
                price=row.price
                text=f'{row.name} {row.size}'
                drink_button=Button(self.window,text=text,
                bg="#375362",fg="white",font=("Arial",10,"italic"),
                command=lambda button_text=text, price=price: self.get_drink_order(button_text,price))
                self.drink_page.append(drink_button)
        self.drink_page.append(correct)
        self.drink_page.append(Home)
        self.drink_page.append(back)
        return self.drink_page
    def grid_drink_button(self):
        self.erase_menu_page()
        list=self.create_drink_button()
        list[0].grid(row=0,column=0)
        row=1
        column=0
        for element in list[1:]:
            element.grid(row=row,column=column)
            column+=1
            if row==3 and column==1:
                column=0
                row+=1
            if column==3:
                column=0
                row+=1
    def go_home_from_drink_page(self):
        self.erase_drink_page()
        self.grid_main_page()
    def go_back_from_drink_page(self):
        self.erase_drink_page()
        self.grid_menu_page()
    def get_food_order(self,button_text,price):
        food_choice=[]
        food_choice.append(button_text)
        food_choice.append(price)
        self.food_order.append(food_choice)
        print(self.food_order)
    def get_drink_order(self,button_text,price):
        drink_choice=[]
        drink_choice.append(button_text)
        drink_choice.append(price)
        self.drink_order.append(drink_choice)
        print(self.drink_order)
    def correct_order(self,list):
        list.remove(list[-1])
    def save_order(self):
        self.order.append(self.food_order)
        self.order.append(self.drink_order)
        return self.order
    def clear_lists(self):
        self.food_order.clear()
        self.drink_order.clear()
        self.order.clear()
    def get_total(self,list):
        amount=0.0
        for order in list:
            for price in order:
                amount+=price[1]
        return amount
    def save_order_in_data(self):
        order=self.save_order()
        table_number=order[0]
        list=order[1:]
        print(list)
        total=self.get_total(list)
        create_new_row(table_number,list,total)
        update_table(table_number,list,False)
        self.clear_lists()
    ####
    def create_modifie_order_page(self):
        self.modifie_order_page=[]
        label_order_number=Label(self.window,text="please,insert the order's number"
        ,bg="#375362",fg="white",font=("Arial",20,"italic"))
        search_entry=Entry(width=35)
        search_button=Button(self.window,text="search"
        ,bg="#375362",fg="white",font=("Arial",20,"italic")
        ,command=lambda:self.check_order_number(search_entry))
        self.modifie_order_page.append(label_order_number)
        self.modifie_order_page.append(search_entry)
        self.modifie_order_page.append(search_button)
        return self.modifie_order_page   
    def grid_modifie_order_page(self):
        self.erase_main_page()
        self.modifie_order_page=self.create_modifie_order_page()
        row=0
        for element in self.modifie_order_page:
            element.grid(row=row,column=0)
            row+=1
    def erase_modifie_order_page(self):
        x=0
        for element in self.modifie_order_page: 
            if x==0:
                element.destroy()
            else:
                element.grid_forget()
            x+=1
        self.modifie_order_page.clear()
    def create_modifie_page(self,table_number):
        self.modifie_page=[]
        label=Label(self.window, text="what do you want to be modified ? "
        ,bg="#375362",fg="white",font=("Arial",20,"italic"))
        self.modifie_page.append(label)
        table_button=Button(self.window,text="table_number"
        ,bg="#375362",fg="white",font=("Arial",20,"italic")
        ,command=lambda:self.grid_modifie_page_tableNumber(table_number))
        order_button=Button(self.window,text="order"
        ,bg="#375362",fg="white",font=("Arial",20,"italic"))
        self.modifie_page.append(table_button)
        self.modifie_page.append(order_button)
        return self.modifie_page
    def grid_modifie_page(self,table_number):
        self.erase_modifie_order_page()
        self.modifie_page=self.create_modifie_page(table_number)
        row=0
        for element in self.modifie_page:
            element.grid(row=row,column=0)
            row+=1
    def erase_modifie_page(self):
        x=0
        for element in self.modifie_page:
            if x==0:
                element.destroy()
            else:
                element.grid_forget()
            x+=1
        self.modifie_page.clear()
    def read_order_number_from_user(self,search_entry):
            self.window.update()
            try:
                user_input=int(search_entry.get())
            except ValueError:
                messagebox.showinfo(title="error",message=f"{search_entry.get()} is not a integer")
                return False
            return user_input
    def check_order_number(self,search_entry):
        order_number=self.read_order_number_from_user(search_entry)
        element_found=False
        if order_number!=False:
            table=select(Order)
            with engine.connect() as conn:
                for row in conn.execute(table):
                    if row.number==order_number:
                        self.grid_modifie_page(row.table_number)
                        element_found=True
                        break
            if element_found==False:
                messagebox.showinfo(title="error",
                message=f"order number {search_entry.get()} is not found")
    def create_modifie_page_tableNumber(self,table_number):
        self.modifie_page_tableNumber_list=[]
        label=Label(self.window, text="Please enter the new table's number"
        ,bg="#375362",fg="white",font=("Arial",20,"italic"))
        tableNumber_entry=Entry(width=35)
        tableNumber_button=Button(self.window,text="modifie"
        ,bg="#375362",fg="white",font=("Arial",20,"italic")
        ,command=lambda:self.check_new_TableNumber(tableNumber_entry,table_number))
        self.modifie_page_tableNumber_list.append(label)
        self.modifie_page_tableNumber_list.append(tableNumber_entry)
        self.modifie_page_tableNumber_list.append(tableNumber_button)
        return self.modifie_page_tableNumber_list 
    def grid_modifie_page_tableNumber(self,table_number):
        self.erase_modifie_page()
        self.modifie_page_tableNumber_list=self.create_modifie_page_tableNumber(table_number)
        row=0
        for element in self.modifie_page_tableNumber_list:
            element.grid(row=row,column=0)
            row+=1
    def read_newTable_entry(self,tableNumber_entry):
        self.window.update()
        try:
            user_input=int(tableNumber_entry.get())
        except ValueError:
            messagebox.showinfo(title="error",message=f"'{tableNumber_entry.get()}' is not a integer")
            return False
        return user_input
    def check_new_TableNumber(self,tableNumber_entry,table_number):
        new_tableNumber=self.read_newTable_entry(tableNumber_entry)
        element_found=False
        if new_tableNumber!=False:
            table=select(Table)
            with engine.connect() as conn:
                for row in conn.execute(table):
                    if row.number==new_tableNumber:
                        element_found=True
                        if row.empty==False:
                            element_found
                            messagebox.showinfo(title="error",
                            message=f"table number {tableNumber_entry.get()} is not empty")
                        else:
                            self.modifie_new_table(row.number,table_number)
                        break
            if element_found==False:
                        messagebox.showinfo(title="error",
                        message=f"table number {tableNumber_entry.get()} is not found")
    def get_old_order(self,table_number):
        table=select(Table)
        with engine.connect() as conn:
            for row in conn.execute(table):
                if row.number==table_number:
                    copied_order=row.order
        return copied_order
    def modifie_new_table(self,new_table_number,table_number):
        update_table(new_table_number,self.get_old_order(table_number),False)   
        update_table(table_number,[],True)       
        self.modifie_table_number_in_order_class(table_number,new_table_number)
    def modifie_table_number_in_order_class(self,table_number,new_table_number):
        update_order(table_number,new_table_number)
class cashier(base):
    __tablename__="cashiers"
    id=Column(Integer, primary_key=True)
    name=Column(String(250),nullable=False)

    def __init__(self,name,machine:ui_manager):
        self.name=name 
        self.machine=machine
        machine.grid_main_page()
        machine.window.mainloop()          
