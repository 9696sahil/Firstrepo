from tkinter import *
import tkinter.messagebox
import MiniProject_Backend

class Movie:
    def __init__(self, root):
        self.root = root
        self.root.title("MOVIE TICKET BOOKING SYSTEM")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="black")

        Movie_ID = StringVar()
        Movie_Name = StringVar()
        Date = StringVar()
        Time = StringVar()
        Hall_Name = StringVar()
        Seat_no = StringVar()
        Booking_id = StringVar()
        Total_amount = StringVar()

        # Functions
        def iExit():
            iExit = tkinter.messagebox.askyesno("MOVIE TICKET BOOKING SYSTEM", "Are you sure?")
            if iExit > 0:
                root.destroy()
            return

        def clcdata():
            self.txtMovie_ID.delete(0, END)
            self.txtMovie_Name.delete(0, END)
            self.txtDate.delete(0, END)
            self.txtTime.delete(0, END)
            self.txtHall_Name.delete(0, END)
            self.txtSeat_no.delete(0, END)
            self.txtBooking_id.delete(0, END)
            self.txtTotal_amount.delete(0, END)

        def adddata():
            if len(Movie_ID.get()) != 0:
                MiniProject_Backend.AddMovieRec(Movie_ID.get(), Movie_Name.get(), Date.get(), Time.get(), Hall_Name.get(), Seat_no.get(), Booking_id.get(), Total_amount.get())
                MovieList.delete(0, END)
                MovieList.insert(END, (Movie_ID.get(), Movie_Name.get(), Date.get(), Time.get(), Hall_Name.get(), Seat_no.get(), Booking_id.get(), Total_amount.get()))

        def disdata():
            MovieList.delete(0, END)
            for row in MiniProject_Backend.ViewMovieData():
                MovieList.insert(END, row)

        def movierec(event):
            global sd
            searchmovie = MovieList.curselection()[0]
            sd = MovieList.get(searchmovie)

            self.txtMovie_ID.delete(0, END)
            self.txtMovie_ID.insert(END, sd[1])
            self.txtMovie_Name.delete(0, END)
            self.txtMovie_Name.insert(END, sd[2])
            self.txtDate.delete(0, END)
            self.txtDate.insert(END, sd[3])
            self.txtTime.delete(0, END)
            self.txtTime.insert(END, sd[4])
            self.txtHall_Name.delete(0, END)
            self.txtHall_Name.insert(END, sd[5])
            self.txtSeat_no.delete(0, END)
            self.txtSeat_no.insert(END, sd[6])
            self.txtBooking_id.delete(0, END)
            self.txtBooking_id.insert(END, sd[7])
            self.txtTotal_amount.delete(0, END)
            self.txtTotal_amount.insert(END, sd[8])

        def deldata():
            if len(Movie_ID.get()) != 0:
                MiniProject_Backend.DeleteMovieRec(sd[0])
                clcdata()
                disdata()

        def updata():
            if len(Movie_ID.get()) != 0:
                MiniProject_Backend.UpdateMovieData(sd[0], Movie_ID.get(), Movie_Name.get(), Date.get(), Time.get(), Hall_Name.get(), Seat_no.get(), Booking_id.get(), Total_amount.get())
                disdata()

        # Frames
        MainFrame = Frame(self.root, bg="black")
        MainFrame.grid()

        TFrame = Frame(MainFrame, bd=5, padx=54, pady=8, bg="black", relief=RIDGE)
        TFrame.pack(side=TOP)

        self.TFrame = Label(TFrame, font=('Arial', 51, 'bold'), text="MOVIE TICKET BOOKING SYSTEM", bg="black", fg="orange")
        self.TFrame.grid()

        BFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="black", relief=RIDGE)
        BFrame.pack(side=BOTTOM)

        DFrame = Frame(MainFrame, bd=2, width=1300, height=400, padx=20, pady=20, bg="black", relief=RIDGE)
        DFrame.pack(side=BOTTOM)

        DFrameL = LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Movie Info\n", fg="white")
        DFrameL.pack(side=LEFT)

        DFrameR = LabelFrame(DFrame, bd=2, width=450, height=300, padx=31, pady=3, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Movie Details\n", fg="white")
        DFrameR.pack(side=RIGHT)

        # Labels & Entry Boxes
        self.lblMovie_ID = Label(DFrameL, font=('Arial', 18, 'bold'), text="Movie ID:", padx=2, pady=2, bg="black", fg="orange")
        self.lblMovie_ID.grid(row=0, column=0, sticky=W)
        self.txtMovie_ID = Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Movie_ID, width=39, bg="black", fg="white")
        self.txtMovie_ID.grid(row=0, column=1)

        self.lblMovie_Name = Label(DFrameL, font=('Arial', 18, 'bold'), text="Movie Name:", padx=2, pady=2, bg="black", fg="orange")
        self.lblMovie_Name.grid(row=1, column=0, sticky=W)
        self.txtMovie_Name = Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Movie_Name, width=39, bg="black", fg="white")
        self.txtMovie_Name.grid(row=1, column=1)

        self.lblDate = Label(DFrameL, font=('Arial', 18, 'bold'), text="Date:", padx=2, pady=2, bg="black", fg="orange")
        self.lblDate.grid(row=2, column=0, sticky=W)
        self.txtDate = Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Date, width=39, bg="black", fg="white")
        self.txtDate.grid(row=2, column=1)

        self.lblTime = Label(DFrameL, font=('Arial', 18, 'bold'), text="Time:", padx=2, pady=2, bg="black", fg="orange")
        self.lblTime.grid(row=3, column=0, sticky=W)
        self.txtTime = Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Time, width=39, bg="black", fg="white")
        self.txtTime.grid(row=3, column=1)

        self.lblHall_Name = Label(DFrameL, font=('Arial', 18, 'bold'), text="Hall Name:", padx=2, pady=2, bg="black", fg="orange")
        self.lblHall_Name.grid(row=4, column=0, sticky=W)
        self.txtHall_Name = Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Hall_Name, width=39, bg="black", fg="white")
        self.txtHall_Name.grid(row=4, column=1)

        self.lblSeat_no = Label(DFrameL, font=('Arial', 18, 'bold'), text="Seat No:", padx=2, pady=2, bg="black", fg="orange")
        self.lblSeat_no.grid(row=5, column=0, sticky=W)
        self.txtSeat_no = Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Seat_no, width=39, bg="black", fg="white")
        self.txtSeat_no.grid(row=5, column=1)

        self.lblBooking_id = Label(DFrameL, font=('Arial', 18, 'bold'), text="Booking Id:", padx=2, pady=2, bg="black", fg="orange")
        self.lblBooking_id.grid(row=6, column=0, sticky=W)
        self.txtBooking_id = Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Booking_id, width=39, bg="black", fg="white")
        self.txtBooking_id.grid(row=6, column=1)

        self.lblTotal_amount = Label(DFrameL, font=('Arial', 18, 'bold'), text="Total Amount:", padx=2, pady=2, bg="black", fg="orange")
        self.lblTotal_amount.grid(row=7, column=0, sticky=W)
        self.txtTotal_amount = Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Total_amount, width=39, bg="black", fg="white")
        self.txtTotal_amount.grid(row=7, column=1)

        # ListBox & ScrollBar
        sb = Scrollbar(DFrameR)
        sb.grid(row=0, column=1, sticky='ns')

        MovieList = Listbox(DFrameR, width=41, height=16, font=('Arial', 12, 'bold'), yscrollcommand=sb.set, bg="black", fg="white")
        MovieList.bind('<<ListboxSelect>>', movierec)
        MovieList.grid(row=0, column=0, padx=8)
        sb.config(command=MovieList.yview)

        # Buttons
        btnAddData = Button(BFrame, text="Add New", font=('Arial', 20, 'bold'), height=1, width=10, bd=4, command=adddata, bg="black", fg="white")
        btnAddData.grid(row=0, column=0)

        btnDisplayData = Button(BFrame, text="Display", font=('Arial', 20, 'bold'), height=1, width=10, bd=4, command=disdata, bg="black", fg="white")
        btnDisplayData.grid(row=0, column=1)

        btnClearData = Button(BFrame, text="Clear", font=('Arial', 20, 'bold'), height=1, width=10, bd=4, command=clcdata, bg="black", fg="white")
        btnClearData.grid(row=0, column=2)

        btnDeleteData = Button(BFrame, text="Delete", font=('Arial', 20, 'bold'), height=1, width=10, bd=4, command=deldata, bg="black", fg="white")
        btnDeleteData.grid(row=0, column=3)


        btnUpdateData = Button(BFrame, text="Update", font=('Arial', 20, 'bold'), height=1, width=10, bd=4, command=updata, bg="black", fg="white")
        btnUpdateData.grid(row=0, column=5)

        btnExit = Button(BFrame, text="Exit", font=('Arial', 20, 'bold'), height=1, width=10, bd=4, command=iExit, bg="black", fg="white")
        btnExit.grid(row=0, column=6)

if __name__ == '__main__':
    root = Tk()
    application = Movie(root)
    root.mainloop()
