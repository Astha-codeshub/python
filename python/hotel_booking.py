import tkinter as tk

rooms={
    "101 -Single": 1200,
    "102 -Double": 2000,
    "103 -Deluxe": 3000,
    "104 -Suite": 5000
    }

def book_room():
    name = name_entry.get().strip()
    room = room_var.get() 

    if not name:
        result.config(text="Enter guest name ❌")
        return

    price=rooms[room]

    result.config(
        text=f"✅ BOOKING CONFIRMED\n\n"
        f"Guest: {name}\n"
        f"Room: {room}\n"
        f"Price: ₹{price}/Day")

root=tk.Tk()
root.title("HOTEL BOOKING SYSTEM")
root.geometry("500x500")

tk.Label(
    root,
    text="🏨 HOTEL BOOKING",
    font=("Arial", 24, "bold")
).pack(pady=30)

tk.Label(root ,text="Guest Name").pack()

name_entry=tk.Entry(
    root,font=("Arial", 15)
)
name_entry.pack(pady=10)
room_var=tk.StringVar(
    value="101 -Single"
)

tk.Label(
    root,
    text="Select Room", font=("Arial", 12)).pack(pady=5)


room_menu=tk.OptionMenu(
    root,
    room_var,
    *rooms.keys()
)
room_menu.config(
    font=("Arial", 12)
)
room_menu.pack(pady=15)

tk.Button(
    root,
    text="BOOK ROOM",
    command=book_room,
    font=("Arial", 13, "bold")
).pack(pady=20)

result=tk.Label(
    root,
    text="Enter details",
    font=("Arial", 15,"bold"),
    justify="center"
)
result.pack(pady=20)

root.mainloop()
