def create_product():
    entries1 = [entry_id, entry_model, entry_price, entry_brand, entry_cpu, entry_screen, entry_hardisk]
    entries2 = [entry_id, entry_model, entry_price, entry_brand, entry_cr, entry_cn, entry_nc]
    lb_errore.configure(text='')
    try:
        if var.get() == 'L':
            if type(super_store.store.get_product(int(entry_id.get()))) is super_store.Laptop:
                lb_errore.configure(text='The product already exist',fg='red')
            elif type(super_store.store.get_product(int(entry_id.get()))) is super_store.Smartphone:
                lb_errore.configure(text='The product already exist', fg='red')


            else:
                new_lp = super_store.Laptop(int(entry_id.get()),entry_brand.get(),entry_model.get(),
                                            int(year_comb.get()),int(entry_price.get()),entry_cpu.get()
                                             ,entry_hardisk.get(),
                                            entry_screen.get())

                super_store.store += new_lp
                messagebox.showinfo(message=f"The laptop is {new_lp}")

        elif var.get() == 'S':
            if type(super_store.store.get_product(int(entry_id.get()))) is super_store.Smartphone:
                lb_errore.configure(text='The product already exist',fg='red')
            elif type(super_store.store.get_product(int(entry_id.get()))) is super_store.Laptop:
                lb_errore.configure(text='The product already exist', fg='red')
            else:
                new_lp = super_store.Smartphone(int(entry_id.get()), entry_brand.get(), entry_model.get(),
                                            int(year_comb.get()), int(entry_price.get()), entry_cn.get(),
                                                entry_nc.get(),
                                                entry_cr.get())
                super_store.store += new_lp
                messagebox.showinfo(message=f"The smartphone is {new_lp}")
        else:
            lb_errore.configure(text='You need to choose laptop or smartphone',fg='red')

    except ValueError:
        lb_errore.configure(text='Try to put numbers in correct fields',fg='red')

    except Exception :

        lb_errore.configure(text='somthing went wrong',fg='red')
    if var.get() == 'L':
        for entry in entries1:
            if entry.get() == '':
                entry.configure(bg='red')
                lb_errore.configure(text='you need to put somthing in the field',fg='red')
            else:
                entry.configure(bg='white')
    if var.get() == 'S':
        for entry in entries2:
            if entry.get() == '':
                entry.configure(bg='red')
                lb_errore.configure(text='you need to put somthing in the field', fg='red')
            else:
                entry.configure(bg='white')
    for entry in entries1:
        entry.delete(0,END)
    for entry in entries2:
        entry.delete(0,END)
    year_comb.delete(0,END)