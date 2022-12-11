from tkinter import *

root = Tk()
root.geometry("1350x690+0+0")
root.resizable(False, False)
root.title("WELCOME TO DUPSAL RESORT")
root.config(bg='firebrick4')

# ===========================FRAMES==================
topFrame = Frame(root, bd=10, relief=RIDGE, bg='firebrick4')
topFrame.pack(side=TOP)

labelTitle = Label(topFrame, text='DUPSAL RESORT', font=('arial', 30, 'bold'), fg='yellow',
                   bg='red4', width=54, bd=9)
labelTitle.grid(row=0, column=0)

menuFrame = Frame(root, bd=10, relief=RIDGE, bg='red4')
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame, bd=4, relief=RIDGE, bg='red4')
costFrame.pack(side=BOTTOM)

foodFrame = LabelFrame(menuFrame, text='Food', font=('arial', 19, 'bold'), bd=10, fg='red4',relief=RIDGE)
foodFrame.pack(side=LEFT)

drinkFrame = LabelFrame(menuFrame, text='Drink', font=('arial', 19, 'bold'), bd=10, relief=RIDGE)
drinkFrame.pack(side=LEFT)

foodcontFrame = LabelFrame(menuFrame, text='Food', font=('arial', 19, 'bold'), bd=10, fg='red4', relief=RIDGE)
foodcontFrame.pack(side=LEFT)

rightFrame = Frame(root, bd=15, relief=RIDGE)
rightFrame.pack(side=RIGHT)

calcuFrame = Frame(rightFrame, bd=1, relief=RIDGE)
calcuFrame.pack()

receiptFrame = Frame(rightFrame, bd=4, relief=RIDGE)
receiptFrame.pack()

buttonFrame = Frame(rightFrame, bd=3, relief=RIDGE)
buttonFrame.pack()

# Variable
salad = IntVar()
calamari = IntVar()
smalplate = IntVar()
bigplate = IntVar()
grillcrab = IntVar()
smallobster = IntVar()
mediumlobstr = IntVar()
largelobstr = IntVar()
marinatedT = IntVar()
crabsop = IntVar()
shrimps = IntVar()
sides = IntVar()
vegetawildr = IntVar()
qur = IntVar()
vegetablesup = IntVar()
pastaWitVegetable = IntVar()
dupsalspecial = IntVar()
organicpasta = IntVar()
fruitsalad = IntVar()
ice = IntVar()
others = IntVar()
# ================================FOOD_CHECK_BUTTONS=========================================
saladbtncheck = Checkbutton(foodFrame, text='Salad', font=('arial', 15, 'bold'), onvalue=1, offvalue=0, variable=salad)
saladbtncheck.grid(row=0, column=0, sticky=W)

calambtncheck = Checkbutton(foodFrame, text='Calamari', font=('arial', 15, 'bold'), onvalue=1,
                            offvalue=0, variable=calamari)
calambtncheck.grid(row=1, column=0, sticky=W)
# Capaccio
smalplatbtncheck = Checkbutton(foodFrame, text='Small Plate', font=('arial', 15, 'bold'), onvalue=1,
                               offvalue=0, variable=smalplate)
smalplatbtncheck.grid(row=2, column=0, sticky=W)

bigplatebtncheck = Checkbutton(foodFrame, text='Big Plate', font=('arial', 15, 'bold'), onvalue=1,
                               offvalue=0, variable=bigplate)
bigplatebtncheck.grid(row=3, column=0, sticky=W)

grilcrabbtncheck = Checkbutton(foodFrame, text='Grilled Crab', font=('arial', 15, 'bold'),
                               onvalue=1, offvalue=0, variable=grillcrab)
grilcrabbtncheck.grid(row=4, column=0, sticky=W)

smallobsterbtncheck = Checkbutton(foodFrame, text='Small Lobster', font=('arial', 15, 'bold'),
                                  onvalue=1, offvalue=0, variable=smallobster)
smallobsterbtncheck.grid(row=5, column=0, sticky=W)

mediumlobstrbtncheck = Checkbutton(foodFrame, text='Medium Lobster', font=('arial', 15, 'bold'),
                                   onvalue=1, offvalue=0, variable=mediumlobstr)
mediumlobstrbtncheck.grid(row=6, column=0, sticky=W)

largelobstrbtncheck = Checkbutton(foodFrame, text='Large Lobster', font=('arial', 15, 'bold'),
                                  onvalue=1, offvalue=0, variable=largelobstr)
largelobstrbtncheck.grid(row=7, column=0, sticky=W)

marinatedTbtncheck = Checkbutton(foodFrame, text='Marinated_T_P', font=('arial', 15, 'bold'),
                                 onvalue=1, offvalue=0, variable=marinatedT)
marinatedTbtncheck.grid(row=8, column=0, sticky=W)

crabsopbtncheck = Checkbutton(foodFrame, text='Crab Soup', font=('arial', 15, 'bold'),
                                 onvalue=1, offvalue=0, variable=crabsop)
crabsopbtncheck.grid(row=9, column=0, sticky=W)

saladent = Entry(foodFrame, bd=10, width=10, font=('arial', 10, 'bold'),relief=RIDGE,)
saladent.grid(row=0, column=1)

calamaent = Entry(foodFrame, bd=10, width=10, font=('arial', 10, 'bold'),relief=RIDGE,)
calamaent.grid(row=1, column=1)

smalplatent = Entry(foodFrame, bd=10, width=10, font=('arial', 10, 'bold'),relief=RIDGE,)
smalplatent.grid(row=2, column=1)

bigplatent = Entry(foodFrame, bd=10, width=10, font=('arial', 10, 'bold'),relief=RIDGE,)
bigplatent.grid(row=3, column=1)

grilcrabent = Entry(foodFrame, bd=10, width=10, font=('arial', 10, 'bold'),relief=RIDGE,)
grilcrabent.grid(row=4, column=1)

smallobent = Entry(foodFrame, bd=10, width=10, font=('arial', 10, 'bold'),relief=RIDGE,)
smallobent.grid(row=5, column=1)

medilobent = Entry(foodFrame, bd=10, width=10, font=('arial', 10, 'bold'),relief=RIDGE,)
medilobent.grid(row=6, column=1)

largelobent = Entry(foodFrame, bd=10, width=10, font=('arial', 10, 'bold'),relief=RIDGE,)
largelobent.grid(row=7, column=1)

marinatedTent = Entry(foodFrame, bd=10, width=10, font=('arial', 10, 'bold'),relief=RIDGE,)
marinatedTent.grid(row=8, column=1)

crabsopent = Entry(foodFrame, bd=10, width=10,font=('arial', 10, 'bold'), relief=RIDGE,)
crabsopent.grid(row=9, column=1)

# ==============================NEXT FOOD FRAME WIDGET====================================
shrimpbtncheck = Checkbutton(foodcontFrame, text='Shrimps', font=('arial', 15, 'bold'),
                             onvalue=1, offvalue=0, variable=shrimps)
shrimpbtncheck.grid(row=0, column=0, sticky=W)

sidesbtncheck = Checkbutton(foodcontFrame, text='Sidess', font=('arial', 15, 'bold'),
                             onvalue=1, offvalue=0, variable=sides)
sidesbtncheck.grid(row=1, column=0, sticky=W)

vegetaWricebtncheck = Checkbutton(foodcontFrame, text='Vegetable and Wild', font=('arial', 15, 'bold'),
                             onvalue=1, offvalue=0, variable=vegetawildr)
vegetaWricebtncheck.grid(row=2, column=0, sticky=W)

# Name not complete
qurbtncheck = Checkbutton(foodcontFrame, text='Qura', font=('arial', 15, 'bold'),
                             onvalue=1, offvalue=0, variable=qur)
qurbtncheck.grid(row=3, column=0, sticky=W)

vegetasupbtncheck = Checkbutton(foodcontFrame, text='Vegetable Soup', font=('arial', 15, 'bold'),
                             onvalue=1, offvalue=0, variable=vegetablesup)
vegetasupbtncheck.grid(row=4, column=0, sticky=W)

# PASTA:
pastaWitVegetablebtncheck = Checkbutton(foodcontFrame, text='Pasta Vegetable', font=('arial', 15, 'bold'),
                             onvalue=1, offvalue=0, variable=pastaWitVegetable)
pastaWitVegetablebtncheck.grid(row=5, column=0, sticky=W)

dupsalspecialbtncheck = Checkbutton(foodcontFrame, text='Dupsal Special', font=('arial', 15, 'bold'),
                             onvalue=1, offvalue=0, variable=dupsalspecial)
dupsalspecialbtncheck.grid(row=6, column=0, sticky=W)

organicpastabtncheck = Checkbutton(foodcontFrame, text='Organic Pasta', font=('arial', 15, 'bold'),
                             onvalue=1, offvalue=0, variable=organicpasta)
organicpastabtncheck.grid(row=7, column=0, sticky=W)

fruitsaladbtncheck = Checkbutton(foodcontFrame, text='Fruit Salad', font=('arial', 15, 'bold'),
                             onvalue=1, offvalue=0, variable=fruitsalad)
fruitsaladbtncheck.grid(row=8, column=0, sticky=W)

icebtncheck = Checkbutton(foodcontFrame, text='Ice Cream', font=('arial', 15, 'bold'),
                             onvalue=1, offvalue=0, variable=ice)
icebtncheck.grid(row=9, column=0, sticky=W)

othersbtncheck = Checkbutton(foodcontFrame, text='Others', font=('arial', 15, 'bold'),
                             onvalue=1, offvalue=0, variable=others)
othersbtncheck.grid(row=10, column=0, sticky=W)

# Entry label
shrimpent = Entry(foodcontFrame, bd=10, width=10, font=('arial', 10, 'bold'),relief=RIDGE,)
shrimpent.grid(row=0, column=1)

sidebent = Entry(foodcontFrame, bd=10, width=10, font=('arial', 10, 'bold'),relief=RIDGE,)
sidebent.grid(row=1, column=1)

vegetWilent = Entry(foodcontFrame, bd=10, width=10, font=('arial', 10, 'bold'),relief=RIDGE,)
vegetWilent.grid(row=2, column=1)

qurent = Entry(foodcontFrame, bd=10, width=10, font=('arial', 10, 'bold'),relief=RIDGE,)
qurent.grid(row=3, column=1)

vegsupent = Entry(foodcontFrame, bd=10, width=10,font=('arial', 10, 'bold'), relief=RIDGE,)
vegsupent.grid(row=4, column=1)

pastavegetaent = Entry(foodcontFrame, bd=10, width=10, font=('arial', 10, 'bold'),relief=RIDGE,)
pastavegetaent.grid(row=5, column=1)

dupspecialent = Entry(foodcontFrame, bd=10, width=10, font=('arial', 10, 'bold'),relief=RIDGE,)
dupspecialent.grid(row=6, column=1)

orgaPastaent = Entry(foodcontFrame, bd=10, width=10, font=('arial', 10, 'bold'),relief=RIDGE,)
orgaPastaent.grid(row=7, column=1)

fruitsaladent = Entry(foodcontFrame, bd=10, width=10, font=('arial', 10, 'bold'),relief=RIDGE,)
fruitsaladent.grid(row=8, column=1)

iceent = Entry(foodcontFrame, bd=10, width=10, font=('arial', 10, 'bold'),relief=RIDGE,)
iceent.grid(row=9, column=1)

qurent = Entry(foodcontFrame, bd=10, width=10, font=('arial', 10, 'bold'),relief=RIDGE,)
qurent.grid(row=10, column=1)


# ===============cost labels and entries====================================================
costFood = Label(costFrame, text='Cost of Food', font=('arial', 18, 'bold'), fg='white', bg='red4')
costFood.grid(row=0, column=0)

costDrink = Label(costFrame, text='Cost of Drink', font=('arial', 18, 'bold'), fg='white', bg='red4')
costDrink.grid(row=1, column=0)

costCakes = Label(costFrame, text='Cost of Cake', font=('arial', 18, 'bold'), fg='white', bg='red4')
costCakes.grid(row=2, column=0)

lblcostfood = Entry(costFrame, font=('arial', 18, 'bold'), bd=5, relief=RIDGE)
lblcostfood.grid(row=0, column=1)

lblcostfood = Entry(costFrame, font=('arial', 18, 'bold'), bd=5, relief=RIDGE)
lblcostfood.grid(row=1, column=1)

lblcostfood = Entry(costFrame, font=('arial', 18, 'bold'), bd=5, relief=RIDGE)
lblcostfood.grid(row=2, column=1)

root.mainloop()
