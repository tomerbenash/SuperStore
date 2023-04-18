import tkinter
import SuperStore
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Laptop import Laptop
from Smartphone import Smartphone


class EmptyStringError(Exception):
    pass


def onclick():
    my_listbox.delete(0,END)
    if my_combo.get() == "All Products":
        for item in SuperStore.newsuper.products:
            my_listbox.insert(END, item)
    elif my_combo.get() == "Laptops":
        for item in SuperStore.newsuper.get_all_laptops():
            my_listbox.insert(END, item)
    elif my_combo.get() == "Smartphone":
        for item in SuperStore.newsuper.get_all_phones():
            my_listbox.insert(END, item)
    elif my_combo.get() == "Shirts":
        for item in SuperStore.newsuper.get_all_shirts():
            my_listbox.insert(END, item)

def bonus_click():
    messagebox.showinfo("Informatin", f"{SuperStore.newsuper.phone_average_price()}")

# def create_product():
#     product_id = txt.get()
#     product_brand = brand.get()
#     product_model = model.get()
#     product_year = combo_year.get()
#     product_price = price.get()
#     product_cpu = cpu.get()
#     product_hdd = hdd.get()
#     product_screen = screen.get()
#     new_product = Laptop(product_id, product_brand, product_model,
#                              product_year, product_price, product_cpu, product_hdd, product_screen)
#     SuperStore.newsuper += new_product


    # product_cellnet = cell_net.get()
    # product_cores = cores.get()
    # product_cam = cam.get()
    # new_product = Smartphone(product_id, product_brand, product_model,
    #                               product_year, product_price, product_cellnet, product_cores, product_cam)
    # SuperStore.newsuper += new_product



root = Tk()
root.title("SuperStore")
root.geometry("1000x800")

l0 = Label(root, text='Super Store', font=("Ariel bold", 50), fg="blue")
l0.grid(row=0, column=0)

l1 = Label(root, text='Products', font=("New Times Roman", 20))
l1.grid(row=1,column=0)

my_combo=ttk.Combobox(root, values=["All Products", "Laptops", "Smartphone", "Shirts"], width=10)
my_combo.grid(row=2, column=0)
my_combo.bind("")

my_listbox = Listbox(root, width=40)
my_listbox.grid(row=3,column=2)

btn1 = tkinter.Button(root, text="Display Products", width=10, height=2, command=onclick)
btn1.grid(row=2, column=1)


l2 = Label(root, text="Create New Product", font=("New Times Roman", 20))
l2.grid(row=4, column=0)


label_id = Label(root, text="Id")
label_id.grid(row=6,column=0)

label_price = Label(root, text="Price")
label_price.grid(row=6, column=1)

label_brand = Label(root, text="Brand")
label_brand.grid(row=6, column=2)

label_model = Label(root, text="Model")
label_model.grid(row=6, column=3)

txt = Entry(root, width=10) #id
price = Entry(root, width=10)
brand = Entry(root, width=10)
model = Entry(root, width=10)

txt.grid(row=7, column=0) #id
price.grid(row=7, column=1)
brand.grid(row=7, column=2)
model.grid(row=7, column=3)


label_year = Label(root, text="Year")
label_year.grid(row=8,column=0)

years_lst = []
for i in range(1970,2024):
    years_lst.append(str(i))

combo_year=ttk.Combobox(root, values=years_lst, width=10)
combo_year.grid(row=9, column=0)
combo_year.bind("")

product_var = StringVar()
product_values = {"Laptop":"L", "Smartphone":"S"}
current_row = 11

def on_select():
    entreis = [cell_net, cores, cam, cpu, hdd, screen]
    for entry in entreis:
        entry.config(state='normal')
    if product_var.get() == 'L':
        cell_net.config(state='disabled'), cores.config(state='disabled'), cam.config(state='disabled')
    elif product_var.get() == 'S':
        cpu.config(state='disabled'), hdd.config(state='disabled'), screen.config(state='disabled')


for text,value in product_values.items():
    r = Radiobutton(root, text=text, value=value, variable=product_var, command=on_select)
    r.grid(sticky=W, row=current_row, column=0)
    current_row+=2

label_cpu = Label(root, text="CPU")
label_cpu.grid(row=10, column=1)

label_hdd = Label(root, text="Hard disk")
label_hdd.grid(row= 10, column=2)

label_screen = Label(root, text="Screen")
label_screen.grid(row=10, column=3)

cpu = Entry(root, width=10)
hdd = Entry(root, width=10)
screen = Entry(root, width=10)

cpu.grid(row=11, column=1)
hdd.grid(row=11,column=2)
screen.grid(row=11, column=3)

label_cell = Label(root, text="Cellular Network")
label_cell.grid(row=12, column=1)

label_cores = Label(root, text="Number of cores")
label_cores.grid(row=12, column=2)

label_cam = Label(root, text="Camera resolution")
label_cam.grid(row=12, column=3)

cell_net = Entry(root, width=10)
cores = Entry(root, width=10)
cam = Entry(root, width=10)

cell_net.grid(row=13, column=1)
cores.grid(row=13, column=2)
cam.grid(row=13, column=3)

def create_product():
    entries = [txt, brand, model, price, cell_net, cores, cam, cpu, hdd, screen]
    entries2 = [brand,model,price]
    try:
        for entry in entries:
            if entry.get() == '':
                entry.configure(bg='red')
        if product_var.get() == 'L':
            product_id = txt.get()
            product_brand = brand.get()
            product_model = model.get()
            product_year = combo_year.get()
            product_price = price.get()
            product_cpu = cpu.get()
            product_hdd = hdd.get()
            product_screen = screen.get()

            for entry2 in entries2:
                if entry2.get() == '':
                    raise EmptyStringError

            if type(SuperStore.newsuper.get_product(int(product_id))) is Laptop or type((SuperStore.newsuper.get_product(int(product_id)))) is Smartphone:
                l3.configure(text="product already exists", bg='red')


            else:
                new_product = Laptop(product_id, product_brand, product_model,
                                     product_year, product_price, product_cpu, product_hdd, product_screen)
                SuperStore.newsuper += new_product
                messagebox.showinfo("Information", f"{new_product}")
                for entry in entries:
                    entry.delete(0, END)
                combo_year.set("")
                l3.configure(text='')
                for entry in entries:
                    entry.configure(bg='white')

        elif product_var.get() == 'S':
            product_id = txt.get()
            product_brand = brand.get()
            product_model = model.get()
            product_year = combo_year.get()
            product_price = price.get()
            product_cellnet = cell_net.get()
            product_cores = cores.get()
            product_cam = cam.get()

            for entry2 in entries2:
                if entry2.get() == '':
                    raise EmptyStringError

            if type(SuperStore.newsuper.get_product(int(product_id))) is Smartphone or type(SuperStore.newsuper.get_product(int(product_id))) is Laptop:
                l3.configure(text="product already exists", bg='red')
            else:
                new_product = Smartphone(product_id, product_brand, product_model,
                                   product_year, product_price, product_cellnet, product_cores, product_cam)
                SuperStore.newsuper += new_product
                messagebox.showinfo("Information", f"{new_product}")
                for entry in entries:
                    entry.delete(0, END)
                combo_year.set("")
                l3.configure(text='')
                for entry in entries:
                    entry.configure(bg='white')
        else:
            l3.configure(text="you need to choose laptop/smartphone", bg='red')

    except ValueError:
        l3.configure(text="incorrect fields.", bg='red')

    except EmptyStringError:
        l3.configure(text="EMPTY FIELD", bg='red')






        # entries = [txt, brand, model, price, cell_net, cores, cam, cpu, hdd, screen]
        # for entry in entries:
        #     entry.delete(0, END)
        # combo_year.set("")



btn2 = tkinter.Button(root, text="Create", width=10, height=2, command=create_product)
btn2.grid(row=14, column=4)


# def on_select():
#     entreis = [cell_net, cores, cam, cpu, hdd, screen]
#     for entry in entreis:
#         entry.config(state='normal')
#     if product_var.get() == 'L':
#         cell_net.config(state='disabled'), cores.config(state='disabled'), cam.config(state='disabled')
#     elif product_var.get() == 'S':
#         cpu.config(state='disabled'), hdd.config(state='disabled'), screen.config(state='disabled')


#product_var.trace("w", lambda name, index, mode, var=product_var: on_select(product_var))

l3 = Label(root, text='')
l3.grid(row=5, column=0)

btn3 = tkinter.Button(root, text="BoNUS", width=10, height=2, command=bonus_click)
btn3.grid(row=15, column=2)







root.mainloop()






