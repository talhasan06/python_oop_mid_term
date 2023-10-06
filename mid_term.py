
class Star_Cinema:
    hall_list=[]

    def entry_hall(self,hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    
    def __init__(self,rows,cols,hall_no):
        self._seats={}
        self._show_list=[]
        self._rows=rows
        self._cols=cols
        self._hall_no=hall_no

    def _entry_show(self,id,movie_name,time):
        info=(id,movie_name,time)
        self._show_list.append(info)
        seats=[[0 for j in range(self._cols)] for i in range(self._rows)]
        self._seats[id]=seats

    def book_seats(self,id,user_choice):
        if id in self._seats:
            for seat in user_choice:
                row,col=seat
                if self._seats[id][row][col]==0:
                    self._seats[id][row][col]=1
                    print("Congratulations booking confirmed")
                else:
                    print("Error: Already Booked")
        else:
            print("Error: ID or Seat no invalid !! check again")

    def view_show_list(self):
        for show in self._show_list:
            print(f"ID: {show[0]} Movie: {show[1]} Time: {show[2]}")

    def view_available_seats(self,id):
        if id in self._seats:
            for i in range(self._rows):
                for j in range(self._cols):
                    if self._seats[id][i][j] == 0:
                        print(f"Seats: ({i},{j})")
        else:
            print("Error: show not found")

hall_1 = Hall(3,4,1)
cinema=Star_Cinema()
cinema.entry_hall(hall_1)
hall_1._entry_show(111,"Openheimer","9:00 PM")
hall_1._entry_show(121,"Jawan","11:00 PM")
hall_1._entry_show(131,"Sujon majhi","1:00 PM")

print("1. VIEW ALL SHOW TODAY")
print("2. VIEW AVAILABLE SEATS")
print("3. BOOK TICKET")
print("4. EXIT")

n=int(input("ENTER OPTION: "))

while(n!=4):
    
    if (n==1):
        hall_1.view_show_list()
        print("-----------------")
    elif (n==2):
        show_id=int(input("ENTER SHOW ID: "))
        hall_1.view_available_seats(show_id)
        print("-----------------")
    elif (n==3):
        show_id=int(input("ENTER SHOW ID: "))
        row=int(input("Enter row: "))
        col=int(input("Enter column: "))
        hall_1.book_seats(show_id,[(col,row)])
        print("-----------------")

    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")
    print("-----------------")
    n=int(input("ENTER OPTION: "))
    print("-----------------")
