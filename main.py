from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUiType
import sqlite3
import sys
from os.path import isfile
from datetime import datetime

# use .ui file without converting to .py
main_window, _ = loadUiType('main.ui')


# database for application
class Database:
    def __init__(self):
        # connect to sqlite3 database
        if not isfile('database.db'):
            con = sqlite3.connect('database.db')

        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

        # create user table
        self.cursor.execute("""create table if not exists 'user' (
                            username text primary key not null,
                            first_name text,
                            last_name text,
                            password text)""")

        # create client table
        self.cursor.execute("""create table if not exists 'client' (
                            client_id integer PRIMARY KEY AUTOINCREMENT not null,
                            client_name text,
                            email text,
                            phone_number text,
                            country text,
                            city text,
                            street text,
                            postal_code text,
                            VAT text,
                            client_type text)""")

        # create revenue table
        self.cursor.execute("""create table if not exists 'revenue' (
                            revenue_id integer primary key autoincrement not null,
                            invoice_id integer,
                            description text,
                            revenue_date text,
                            amount real,
                            income_type text,
                            expenses real,
                            FOREIGN KEY("invoice_id") REFERENCES "invoice"("invoice_id"))""")

        # create invoice table
        self.cursor.execute("""create table if not exists 'invoice' (
                            invoice_id integer primary key autoincrement not null,
                            client_id integer not null,
                            invoice_start_date text,
                            invoice_end_date text,
                            total_amount real,
                            taxes real,
                            sub_total real,
                            FOREIGN KEY("client_id") REFERENCES "client"("client_id"))""")

        # create item table
        self.cursor.execute("""create table if not exists 'item' (
                            invoice_id integer not null,
                            description text,
                            unit_cost text,
                            quantity text,
                            VAT_rate text,
                            item_type text,
                            total_amount text,
                            FOREIGN KEY("invoice_id") REFERENCES "invoice"("invoice_id"))""")

        # create expense table
        self.cursor.execute("""create table if not exists 'expense' (
                            revenue_id integer not null,
                            description text,
                            expense_date text,
                            expense_amount real,
                            FOREIGN KEY("revenue_id") REFERENCES "revenue"("revenue_id"))""")

        """
        self.ue('aa', '12-12-2020', '3000', 'personal')
        self.add_invoice(1, '1-1-2020', '1-10-2020', '20000', '10', '18000')
        self.add_item(1, 'aaa', '10', '2', '0', 'service', '20')
        self.add_expense(6 , 'mine', '', 2200)
        """



    # add user to the database
    def add_user(self, username, first_name, last_name, password):
        query = """insert into user (
                username,
                first_name,
                last_name,
                password)
                values (?, ?, ?, ?)"""
        self.cursor.execute(query, (username, first_name, last_name, password,))
        self.connection.commit()

    # add client to database
    def add_client(self, client_name, email, phone, county, city, street, postal_code, vat, client_type):
        query = """insert into client (
                client_name,
                email,
                phone_number ,
                country,
                city,
                street,
                postal_code,
                VAT,
                client_type)
                values (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        self.cursor.execute(query, (client_name, email, phone, county, city, street, postal_code, vat, client_type,))
        self.connection.commit()

    # add revenue to the database
    def add_revenue(self, description, date, amount, income_type):
        query = """insert into revenue (
                    invoice_id,
                    description,
                    revenue_date,
                    amount,
                    income_type,
                    expenses)
                    values (?, ?, ?, ?, ?, ?)"""
        self.cursor.execute(query, (0, description, date, amount, income_type, 0))
        self.connection.commit()

    # add invoice to the database
    def add_invoice(self, client_id, invoice_start_date, invoice_end_date, total_amount, VAT_rate, sub_total):
        query = """insert into invoice (
                    client_id,
                    invoice_start_date,
                    invoice_end_date,
                    total_amount,
                    VAT_rate,
                    sub_total)
                    values (?, ?, ?, ?, ?, ?)"""
        self.cursor.execute(query, (client_id, invoice_start_date, invoice_end_date, total_amount, VAT_rate, sub_total,))
        self.connection.commit()

    # add item to the database
    def add_item(self, invoice_id, description, unit_cost, quantity, VAT_rate, item_type, total_amount):
        query = """insert into item (
                    invoice_id,
                    description,
                    unit_cost,
                    quantity,
                    VAT_rate,
                    item_type,
                    total_amount)
                    values (?, ?, ?, ?, ?, ?, ?)"""
        self.cursor.execute(query, (invoice_id, description, unit_cost, quantity, VAT_rate, item_type, total_amount,))
        self.connection.commit()

    # add expense to the database
    def add_expense(self, revenue_id, description, expense_date, expense_amount):
        query = """insert into expense (
                    revenue_id,
                    description,
                    expense_date,
                    expense_amount)
                    values (?, ?, ?, ?)"""
        self.cursor.execute(query, (revenue_id, description, expense_date, expense_amount,))
        self.connection.commit()



    def delete_revenue(self, primary_key):
        query = "delete from revenue where revenue_id = ?"
        self.cursor.execute(query, (primary_key,))
        self.connection.commit()

    def delete_item(self, foreign_key, description):
        query = "delete from item where invoice_id = ? and description = ?"
        self.cursor.execute(query, (foreign_key, description,))
        self.connection.commit()

    def delete_expense(self, foreign_key, description):
        query = "delete from expense where expense_id = ? and description = ?"
        self.cursor.execute(query, (foreign_key, description,))
        self.connection.commit()



    def modify_revenue(self, revenue_id, description, date, amount, income_type, expense):
        query = """update revenue set 
                    description = ?,
                    date = ?,
                    amount = ?,
                    income_type = ?,
                    expenses = ? 
                    where revenue_id = ?"""
        self.cursor.execute(query, (description, date, amount, income_type, expense, revenue_id,))
        self.connection.commit()

    def modify_item(self, invoice_id, description, unit_cost, quantity, VAT_rate, item_type, total):
        query = """update item set 
                    description = ?,
                    unit_cost = ?,
                    quantity = ?,
                    VAT_rate = ?,
                    item_type = ?,
                    total_amount = ?
                    where invoice_id = ? and description = ?"""
        self.cursor.execute(query, (description, unit_cost, quantity, VAT_rate, item_type, total, invoice_id, description,))
        self.connection.commit()

    def modify_invoice(self, invoice_id, client_id, start_date, due_date, total_amount, taxes, sub_total):
        query = """update invoice set
                    invoice_start_date,
                    invoice_end_date,
                    total_amount,
                    taxes,
                    sub_total
                    where invoice_id = ? and client_id = ?"""
        self.cursor.execute(query, (start_date, due_date, total_amount, taxes, sub_total, invoice_id, client_id,))
        self.connection.commit()

    def modify_expense(self, revenue_id, description, expense_date, expense_amount):
        query = """update expense set
                    description = ?,
                    expense_date = ?,
                    expense_amount = ?
                    where revenue_id = ?"""
        self.cursor.execute(query, (description, expense_date, expense_amount, revenue_id, ))
        self.connection.commit()





    # find username
    def find_username(self, username):
        self.cursor.execute("""select * from user where username=?""", (username,))
        self.connection.commit()
        result = self.cursor.fetchall()
        if result:
            return True
        else:
            return False

    def find_invoice(self):
        self.cursor.execute("""select * from invoice""")
        self.connection.commit()
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            return None

    # find password
    def find_password(self, username, password):
        self.cursor.execute("""select * from user where username=? and password=?""", (username, password,))
        self.connection.commit()
        result = self.cursor.fetchall()
        if result:
            return True
        else:
            return False

    # find revenue rows
    def find_revenue(self):
        self.cursor.execute("""select * from revenue""")
        self.connection.commit()
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            return None

    # find client rows
    def find_client(self):
        self.cursor.execute("""select * from client""")
        self.connection.commit()
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            return None

    def get_invoice_id(self, client_id, total_amount):
        self.cursor.execute("""select * from invoice where client_id = ? and total_amount = ?""", (client_id, total_amount,))
        self.connection.commit()
        result = self.cursor.fetchall()
        if result:
            for x in result:
                return x[0]
        else:
            return None

    def search_client(self, word, search_type):
        if word:
            if search_type == 'Name':
                query = """select * from client where client_name = ?"""
                self.cursor.execute(query, (word,))
            elif search_type == 'Email':
                query = """select * from client where email = ?"""
                self.cursor.execute(query, (word,))
            elif search_type == 'Client Type':
                query = """select * from client where client_type = ?"""
                self.cursor.execute(query, (word,))
            elif search_type == 'Country':
                query = """select * from client where country = ?"""
                self.cursor.execute(query, (word,))
            elif search_type == 'City':
                query = """select * from client where city = ?"""
                self.cursor.execute(query, (word,))
            elif search_type == 'Postal Code':
                query = """select * from client where postal_code = ?"""
                self.cursor.execute(query, (word,))
            elif search_type == 'VAT':
                query = """select * from client where vat = ?"""
                self.cursor.execute(query, (word,))
        else:
            self.cursor.execute("""select * from client""")

        self.connection.commit()
        result = self.cursor.fetchall()
        return result


    # find item rows
    def find_item(self, word):
        self.cursor.execute("""select * from item where invoice_id=?""", (word,))
        self.connection.commit()
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            return None

    def find_expense(self):
        self.cursor.execute("""select * from expense""")
        self.connection.commit()
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            return None

    def find_expense_2(self, revenue_id):
        self.cursor.execute("""select * from expense where revenue_id = ?""", (revenue_id,))
        self.connection.commit()
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            return None


# creating instance of database
db = Database()
global_var1 = None
global_var2 = None
update_array = []
global_array = []

# main application class
class MainApp(QMainWindow, main_window):
    def __init__(self):
        # set home page as default first page

        # call the parent constructor
        QMainWindow.__init__(self)

        # setup the user interface
        self.setupUi(self)

        # center the window
        self.center_window()

        # handle button actions
        self.button_handler()

        # handle switch between pages
        self.page_handler()

        self.setWindowFlag(Qt.FramelessWindowHint)

    # position application window in center
    def center_window(self):
        # geometry of the main window
        frame_geometry = self.frameGeometry()

        # center point of screen
        center_point = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        frame_geometry.moveCenter(center_point)

        # top left of rectangle becomes top left of window centering it
        self.move(frame_geometry.topLeft())

        self.logout()

    # switch between pages
    def page_handler(self):
        # login page
        self.login_button_2.clicked.connect(lambda: self.page('signup_page'))
        self.login_exit.clicked.connect(lambda: self.page('exit'))

        self.Vinvoice_back.clicked.connect(lambda: self.page('main_page'))
        self.main_button_5.clicked.connect(lambda: self.page('Vinvoice_page'))
        # signup page
        self.signup_back.clicked.connect(lambda: self.page('login_page'))

        # main page (dashboard)
        self.main_back.clicked.connect(lambda: self.page('login_page'))
        self.main_button_1.clicked.connect(lambda: self.page('revenue_page'))
        self.main_button_2.clicked.connect(lambda: self.page('Aclient_page'))
        self.main_button_3.clicked.connect(lambda: self.page('Vclient_page'))
        self.main_button_4.clicked.connect(lambda: self.page('Ainvoice_page'))
        self.main_button_5.clicked.connect(lambda: self.page('Vinvoice_page'))
        self.main_button_6.clicked.connect(lambda: self.page('expense_page'))

        # revenue page
        self.revenue_button_1.clicked.connect(lambda: self.page('Arevenue_page'))
        self.revenue_button_5.clicked.connect(lambda: self.page('plot_page'))
        self.revenue_back.clicked.connect(lambda: self.page('main_page'))

        # add revenue page
        self.Arevenue_back.clicked.connect(lambda: self.page('revenue_page'))

        # modify revenue page
        self.Mrevenue_back.clicked.connect(lambda: self.page('revenue_page'))

        # plot page
        self.plot_back.clicked.connect(lambda: self.page('revenue_page'))

        # add client page
        self.Aclient_back.clicked.connect(lambda: self.page('main_page'))

        # view client page
        self.Vclient_back.clicked.connect(lambda: self.page('main_page'))

        # add invoice page
        self.Ainvoice_back.clicked.connect(lambda: self.page('main_page'))

        # add item page
        self.Aitem_back.clicked.connect(lambda: self.page('Ainvoice_page'))

        # modify item page
        self.Mitem_back.clicked.connect(lambda: self.page('Ainvoice_page'))

        # expense page
        self.expense_button_1.clicked.connect(lambda: self.page('Aexpense_page'))
        self.expense_back.clicked.connect(lambda: self.page('main_page'))
        self.expense_back_2.clicked.connect(lambda: self.page('revenue_page'))

        # add expense page
        self.Aexpense_button_1.clicked.connect(lambda: self.page('Vinvoice_page'))
        self.Aexpense_back.clicked.connect(lambda: self.page('expense_page'))

        # modify expense page
        self.Mexpense_button_1.clicked.connect(lambda: self.page('Vinvoice_page'))
        self.Mexpense_back.clicked.connect(lambda: self.page('expense_page'))

    # handle actions for each button
    def button_handler(self):
        # login page
        self.login_button_1.clicked.connect(self.login_method)

        # signup page
        self.signup_button_1.clicked.connect(self.signup_method)

        self.main_back.clicked.connect(self.logout)
        # revenue page
        self.revenue_button_2.clicked.connect(self.to_modify_revenue)
        self.revenue_button_3.clicked.connect(self.delete_revenue_method)
        self.revenue_button_4.clicked.connect(self.to_expense)
        self.revenue_button_6.clicked.connect(self.change_table_date)

        # add revenue page
        self.Arevenue_button_1.clicked.connect(self.add_revenue_method)

        # modify revenue page
        self.Mrevenue_button_1.clicked.connect(self.modify_revenue_method)

        # client view page
        self.Vclient_button_1.clicked.connect(self.search_client)
        self.Vclient_button_2.clicked.connect(self.select_client)

        # add invoice page
        self.Ainvoice_button_1.clicked.connect(self.to_client)
        self.Ainvoice_button_2.clicked.connect(self.to_add_item)
        self.Ainvoice_button_3.clicked.connect(self.to_modify_item)
        self.Ainvoice_button_4.clicked.connect(self.delete_item_method)
        self.Ainvoice_button_5.clicked.connect(self.cal_invoice)

        # add item page
        self.Aitem_button_1.clicked.connect(self.add_item_method)

        # modify item page
        self.Mitem_button_1.clicked.connect(self.modify_item_method)

    def logout(self):
        self.mainWindows.setCurrentWidget(self.login_page)
        self.login_input_1.clear()
        self.login_input_2.clear()

    def view_invoice_table(self, result):
        if result:
            self.view(self.Vinvoice_table, result)

    def logout(self):
        self.login_input_1.clear()
        self.login_input_2.clear()

        self.mainWindows.setCurrentWidget(self.login_page)


    def cal_invoice(self):
        data = []
        if self.Ainvoice_label_4.text() == 'Invoice ID':
            print('select client')
        else:
            self.Ainvoice_label_8.setText(str(400))
            self.Ainvoice_label_9.setText(str(0))
            self.Ainvoice_label_11.setText(str(400))




    def search_client(self):
        search_type = str(self.clientSearchType.currentText())
        search_param = self.searchParam.text()
        search_result = db.search_client(search_param, search_type)
        if search_param:
            self.Vclient_table.clear()
            self.set_client_table_2(search_result)
        else:
            self.Vclient_table.clear()
            self.set_client_table()

    # login method
    def login_method(self):
        entered_username = self.login_input_1.text()
        entered_password = self.login_input_2.text()

        username = db.find_username(entered_username)
        if username == False:
            print('Wrong username or password')
        else:
            password = db.find_password(entered_username, entered_password)
            if password is True:
                self.page('main_page')

    # signup method
    def signup_method(self):
        first_name = self.signup_input_1.text()
        last_name = self.signup_input_2.text()
        username = self.signup_input_3.text()
        password = self.signup_input_4.text()

        if first_name and last_name and username and password:
            similar = db.find_username(username)
            if similar == False:
                db.add_user(username, first_name, last_name, password)
                self.signup_message.setText('>>>>> Account Created <<<<<')
            else:
                self.signup_message.setText('User already taken')
        else:
            self.signup_message.setText('Complete form')




    def to_modify_revenue(self):
        for x in sorted(self.revenue_table.selectionModel().selectedRows()):
            name = x.data(0)
            if name:
                selected_item = self.revenue_table.currentRow()
                primary_key = self.revenue_table.item(selected_item, 0).text()
                description = self.revenue_table.item(selected_item, 1).text()
                date = self.revenue_table.item(selected_item, 3).text()
                amount = self.revenue_table.item(selected_item, 4).text()
                income_type = self.revenue_table.item(selected_item, 5).text()

                update_array.clear()
                update_array.append(primary_key)
                update_array.append(description)
                update_array.append(date)
                update_array.append(amount)
                update_array.append(income_type)
                self.page('Mrevenue_page')
        else:
            print('select row')

    def modify_revenue_method(self):
        description = self.Mrevenue_input_1.text()
        amount = float(self.Mrevenue_input_2.text())
        x = self.Mrevenue_date.date()
        date = x.toPyDate()
        if self.Arevenue_radio_1.isChecked():
            income_type = 'personal'
        elif self.Arevenue_radio_2.isChecked():
            income_type = 'non-professional'
        else:
            income_type = 'professional'

        if description and amount:
            db.modify_revenue(int(update_array[0]), description, date, amount, income_type)
        else:
            print('nothing')

    def delete_revenue_method(self):
        for x in sorted(self.revenue_table.selectionModel().selectedRows()):
            name = x.data(0)
            if name:
                selected_item = self.revenue_table.currentRow()
                primary_key = self.revenue_table.item(selected_item, 0).text()

                if primary_key:
                    db.delete_revenue(int(primary_key))
                    self.set_revenue_table()
            else:
                print('select row')

    def add_revenue_method(self):
        description = self.Arevenue_input_1.text()
        amount = float(self.Arevenue_input_2.text())
        x = self.Arevenue_date.date()
        date = x.toPyDate()
        income_type = ''

        if self.Arevenue_radio_1.isChecked():
            income_type = 'personal'
        elif self.Arevenue_radio_2.isChecked():
            income_type = 'non-professional'

        if description and amount:
            db.add_revenue(description, date, amount, income_type)
        else:
            print('nothing')

    def to_expense(self):
        for x in sorted(self.revenue_table.selectionModel().selectedRows()):
            name = x.data(0)
            if name:
                selected_item = self.revenue_table.currentRow()
                primary_key = self.revenue_table.item(selected_item, 0).text()
                global_var1 = primary_key
                self.page('expense_page')
                self.set_expense_table_2(db.find_expense_2(primary_key))
                self.expense_label_2.setText(primary_key)
                self.Aexpense_label_1.setText(primary_key)
                self.Aexpense_button_1.setEnabled(False)
            else:
                print('select row')

    def change_table_date(self):
        print()




    def to_modify_item(self):
        for x in sorted(self.Ainvoice_table.selectionModel().selectedRows()):
            name = x.data(0)
            if name:
                selected_item = self.Ainvoice_table.currentRow()
                primary_key = int(self.Ainvoice_table.item(selected_item, 0).text())
                description = self.Ainvoice_table.item(selected_item, 1).text()
                unit_cost = float(self.Ainvoice_table.item(selected_item, 2).text())
                quantity = int(self.Ainvoice_table.item(selected_item, 3).text())
                VAT_rate = int(self.Ainvoice_table.item(selected_item, 4).text())
                item_type = self.Ainvoice_table.item(selected_item, 5).text()
                total = float(self.Ainvoice_table.item(selected_item, 6).text())

                update_array.clear()
                update_array.append(primary_key)
                update_array.append(description)
                update_array.append(unit_cost)
                update_array.append(quantity)
                update_array.append(VAT_rate)
                update_array.append(item_type)
                update_array.append(total)
                self.page('Mitem_page')
            else:
                print('select row')

    def modify_item_method(self):
        description = self.Mitem_input_1.text()
        unit_cost = float(self.Mitem_input_2.text())
        quantity = int(self.Mitem_input_3.text())
        VAT_rate = int(self.Mitem_combo_1.currentText())
        item_type = self.Mitem_combo_2.currentText()

        if description and unit_cost and quantity:
            amount = unit_cost * quantity
            tax = (amount / 100) * VAT_rate
            total = amount + tax

            self.Mitem_label_4.setText(str(total))
            db.modify_item(update_array[0], description, unit_cost, quantity, VAT_rate, item_type, total)
            self.Mitem_input_1.setText('')
            self.Mitem_input_2.setText('')
            self.Mitem_input_3.setText('')

        self.set_item_table()


    def delete_item_method(self):
        for x in sorted(self.Ainvoice_table.selectionModel().selectedRows()):
            name = x.data(0)
            if name:
                selected_item = self.Ainvoice_table.currentRow()
                foreign_key = self.Ainvoice_table.item(selected_item, 0).text()
                description = self.Ainvoice_table.item(selected_item, 1).text()

                db.delete_item(int(foreign_key), description)
                self.set_item_table()
            else:
                print('select row')

    def to_add_item(self):
        if self.Ainvoice_label_4.text() == 'Invoice ID':
            print('go and choose a client')
        else:
            self.page('Aitem_page')


    def add_item_method(self):
            description = self.Aitem_input_1.text()
            unit_cost = float(self.Aitem_input_2.text())
            quantity = int(self.Aitem_input_3.text())
            VAT_rate = int(self.Aitem_combo_1.currentText())
            item_type = self.Aitem_combo_2.currentText()

            if description and unit_cost and quantity:
                amount = unit_cost * quantity
                tax = (amount / 100) * VAT_rate
                total = amount + tax
                self.Aitem_label_4.setText(str(total))

                db.add_item(global_array[2], description, unit_cost, quantity, VAT_rate, item_type, total)
                self.Aitem_input_1.setText('')
                self.Aitem_input_2.setText('')
                self.Aitem_input_3.setText('')
                self.set_item_table()


    def to_client(self):
        self.page('Vclient_page')
        self.Vclient_button_2.setEnabled(True)



    def select_client(self):
        for x in sorted(self.Vclient_table.selectionModel().selectedRows()):
            name = x.data(0)
            if name:
                selected_item = self.Vclient_table.currentRow()
                client_id = int(self.Vclient_table.item(selected_item, 0).text())
                client_name = self.Vclient_table.item(selected_item, 1).text()
                global_array.append(client_id)
                global_array.append(client_name)
                db.add_invoice(client_id, '', '', 0, 0, 0)

                invoice_id = db.get_invoice_id(client_id, 0)
                global_array.append(invoice_id)

                self.page('Ainvoice_page')
                self.Ainvoice_label_5.setText(global_array[1])
                self.Ainvoice_label_4.setText(str(global_array[2]))
                self.set_item_table()
            else:
                print('select client')






    def delete_expense_method(self):
        for x in sorted(self.expense_table.selectionModel().selectedRows()):
            name = x.data(0)
            if name:
                selected_item = self.expense_table.currentRow()
                foreign_key = self.expense_table.item(selected_item, 0).text()
                description = self.expense_table.item(selected_item, 1).text()
                if foreign_key:
                    db.delete_expense(int(foreign_key), description)
            else:
                print('select row')










    def set_revenue_table(self):
        result = db.find_revenue()
        if result:
            self.view(self.revenue_table, result)

    def set_client_table(self):
        result = db.find_client()
        if result:
            self.view(self.Vclient_table, result)

    def set_client_table_2(self, result):
        if result:
            self.view(self.Vclient_table, result)

    def set_item_table(self):
        result = db.find_item(global_array[2])
        if result:
            self.view(self.Ainvoice_table, result)

    def set_expense_table(self):
        result = db.find_expense()
        if result:
            self.view(self.expense_table, result)

    def set_expense_table_2(self, result):
        if result:
            self.view(self.expense_table, result)

    @staticmethod
    def view(widget_name, result):
        widget_name.setRowCount(0)

        for row_index, row_data in enumerate(result):
            widget_name.insertRow(row_index)
            for column_index, column_data in enumerate(row_data):
                widget_name.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))



















    def page(self, name):
        if name == 'login_page':
            self.mainWindows.setCurrentWidget(self.login_page)
        elif name == 'signup_page':
            self.mainWindows.setCurrentWidget(self.signup_page)
        elif name == 'main_page':
            self.mainWindows.setCurrentWidget(self.main_page)
        elif name == 'revenue_page':
            self.mainWindows.setCurrentWidget(self.revenue_page)
            self.set_revenue_table()
        elif name == 'Arevenue_page':
            self.mainWindows.setCurrentWidget(self.Arevenue_page)
        elif name == 'Mrevenue_page':
            self.mainWindows.setCurrentWidget(self.Mrevenue_page)
            self.Mrevenue_input_1.setText(global_array[1])
            self.Mrevenue_date.setDate(datetime.strptime(update_array[0], '%m-%d-%Y'))
            self.Mrevenue_input_2.setText(global_array[3])
            if global_array[4] == 'personal':
                self.Mrevenue_radio_1.setChecked(True)
            elif global_array[4] == 'non-professional':
                self.Mrevenue_radio_2.setChecked(True)
            else:
                self.Mrevenue_radio_3.setChecked(True)

        elif name == 'expense_page':
            self.mainWindows.setCurrentWidget(self.expense_page)
            self.set_expense_table()
            self.Aexpense_button_1.setEnabled(True)
            self.Aexpense_label_1.setText('')
            self.expense_label_2.setText('')

        elif name == 'Aexpense_page':
            self.mainWindows.setCurrentWidget(self.Aexpense_page)
        elif name == 'Mexpense_page':
            self.mainWindows.setCurrentWidget(self.Mexpense_page)
        elif name == 'plot_page':
            self.mainWindows.setCurrentWidget(self.plot_page)
        elif name == 'Aclient_page':
            self.mainWindows.setCurrentWidget(self.Aclient_page)
        elif name == 'Vclient_page':
            self.mainWindows.setCurrentWidget(self.Vclient_page)
            self.set_client_table()
            self.Vclient_button_2.setEnabled(False)
            self.Vclient_back.setEnabled(True)
        elif name == 'Ainvoice_page':
            self.mainWindows.setCurrentWidget(self.Ainvoice_page)
        elif name == 'Aitem_page':
            self.mainWindows.setCurrentWidget(self.Aitem_page)
        elif name == 'Mitem_page':
            self.mainWindows.setCurrentWidget(self.Mitem_page)
            self.Mitem_input_1.setText(str(update_array[1]))
            self.Mitem_input_2.setText(str(update_array[2]))
            self.Mitem_input_3.setText(str(update_array[3]))
            self.Mitem_label_4.setText(str(update_array[6]))
        elif name == 'Vinvoice_page':
            self.mainWindows.setCurrentWidget(self.Vinvoice_page)
            result = db.find_invoice()
            self.view_invoice_table(result)
        else:
            exit()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
