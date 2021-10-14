from tkinter import *
root=Tk()
root.geometry("350x350")
root.title("COVID-19 Tracker")

def showdata():
    from matplotlib import pyplot as plt
    import matplotlib.patches as mpatches
    from covid import Covid

    covid=Covid()

    cases=[]
    confirmed=[]
    active=[]
    deaths=[]
    recovered=[]

    try:
        root.update()
        countries=data.get()
        country_names=countries.strip()
        country_names=country_names.replace(" ",",")
        country_names=country_names.split(",")

        for x in country_names:
            cases.append(covid.get_status_by_country_name(x))
            root.update()
        for y in cases:
            confirmed.append(y["Confirmed"])
            active.append(y["Active"])
            deaths.append(y["Deaths"])
            recovered.append(y["Recovered"])

        confirmed_patch=mpatches.Patch(color='green',label='Confirmed')
        recovered_patch=mpatches.Patch(color='red',label='Recovered')
        active_patch=mpatches.Patch(color='blue',label='Active')
        deaths_patch=mpatches.Patch(color='black',label='Deaths')

        plt.legend(handles=[confirmed_patch,recovered_patch,active_patch,deaths_patch])

        for x in range(len(country_names)):
            plt.bar(country_names[x],confirmed[x],color='green')
            if recovered[x]>active[x]:
                plt.bar(country_names[x],recovered[x],color='red')
                plt.bar(country_names[x], active[x], color='blue')
            else:
                plt.bar(country_names[x],active[x],color='blue')
                plt.bar(country_names[x], recovered[x], color='red')
                plt.bar(country_names[x], deaths[x], color='black')

        plt.title('Country Covid Cases')
        plt.xlabel('Country Name')
        plt.ylabel('Cases (in Millions)')
        plt.show()
    except Exception as e:
        data.set("Enter Correct Details Again")

Label(root,text="Enter all countries names \n for whom you want to get \nCovid-19 Data",font="Consolas 15 bold").pack()
Label(root,text="Enter Country Name:").pack()
data = StringVar()
data.set("Seperate Country Names using Comma or Space")
entry=Entry(root, textvariable=data,width=50).pack()
Button(root,text="Get Data",command=showdata).pack()
root.mainloop()


