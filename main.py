
# https://ttkbootstrap.readthedocs.io/en/version-0.5/gallery/simple_data_entry_form.html
# https://www.youtube.com/playlist?list=PLfZw_tZWahjxz8pbtxqjNQvuNPZEM25Qm
import tkinter
from tkinter import ttk

from ttkbootstrap import Style


class Application(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.title('Simple data entry form')
        self.style = Style('darkly')
        self.form = EntryForm(self)
        self.form.pack(fill='both', expand=True)


class EntryForm(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(padding=(20, 10))
        self.columnconfigure(2, weight=1)

        # form variables
        self.fsurl = tkinter.StringVar(value='', name='fsurl')
        self.fagurl = tkinter.StringVar(value='', name='fagurl')
        self.plurl = tkinter.StringVar(value='', name='plurl')
        self.oldgrave = tkinter.StringVar(value='', name='oldgrave')

        # form headers
        ttk.Label(self, text='Please enter Populated Places information', width=60).grid(columnspan=3, pady=10)

        # create label/entry rows
        for i, label in enumerate(['fsurl', 'fagurl', 'plurl', 'oldgrave']):
            ttk.Label(self, text=label.title()).grid(row=i + 1, column=0, sticky='ew', pady=10, padx=(0, 10))
            ttk.Entry(self, textvariable=label).grid(row=i + 1, column=1, columnspan=2, sticky='ew')

        # submit button
        self.submit = ttk.Button(self, text='Submit', style='success.TButton', command=self.print_form_data)
        self.submit.grid(row=5, column=0, sticky='ew', pady=10, padx=(0, 10))

        # cancel button
        self.cancel = ttk.Button(self, text='Cancel', style='danger.TButton', command=self.quit)
        self.cancel.grid(row=5, column=1, sticky='ew')

    def print_form_data(self):
        print(self.fsurl.get(), self.fagurl.get(), self.plurl.get(), self.oldgrave.get())


if __name__ == '__main__':
    Application().mainloop()