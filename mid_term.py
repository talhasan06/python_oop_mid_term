import random
class Star_Cinema:
    hall_list=[]

    def entry_hall(self,hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    
    def __init__(self,rows,cols,hall_no):
        self.seats={}
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        # Star_Cinema.entry_hall(self)

    def entry_show(self,id,movie_name,time):
        info=(id,movie_name,time)
        self.show_list.append(info)
        seats=[[0 for j in range(self.cols)] for i in range(self.rows)]
        self.seats[id]=seats

    def book_seats(self,id,user_choice):
        if id in self.seats:
            for seat in user_choice:
                row,col=seat
                if self.seats[id][row][col]==0:
                    self.seats[id][row][col]=1
                    print("booking confirmed")
                else:
                    print("not available")
        else:
            print("show not found")

    def view_show_list(self):
        for show in self.show_list:
            print(f"ID: {show[0]} Movie: {show[1]} Time: {show[2]}")

    def view_available_seats(self,id):
        if id in self.seats:
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.seats[id][i][j] == 0:
                        print(f"({i},{j})")
        else:
            print("show not found")

hall1 = Hall(3,4,1)
cinema=Star_Cinema()
cinema.entry_hall(hall1)
hall1.entry_show(111,"Challu maal","9:00 PM")
hall1.view_show_list()
hall1.view_available_seats(111)
hall1.book_seats(111,[(0,0)])
hall1.view_available_seats(111)
