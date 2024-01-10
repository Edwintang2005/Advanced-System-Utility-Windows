##Modules used
import tkinter as tk
import psutil


##Functions

def ramvalue():
    ram = psutil.virtual_memory()
    ram = float(ram[2])
    return ram

def introShow():
    introFrame.pack()
    cpuFrame.pack_forget()
    ramFrame.pack_forget()
    menuWholeFrame.pack_forget()
    systemInfo.pack_forget()
    advice.pack_forget()
    cpuButton.configure(text = 'Show CPU')
    ramButton.configure(text ='Show RAM')
    systemInfoButton.configure(text ='Show System Information')
    adviceButton.configure(text = 'Show Advice')
    
def closeIntro():
    introFrame.pack_forget()
    menuWholeFrame.pack(side = tk.LEFT, expand = tk.TRUE, fill = tk.BOTH)
    cpuShowHide()
    ramShowHide()
    infoShowHide()
    adviceShowHide()

def menuShowHide():
    menuShown = menu.winfo_ismapped()
    if menuShown == True:
        menu.pack_forget()
    else:
        menu.pack()

def cpuShowHide():
    cpuShown = cpuFrame.winfo_ismapped()
    if cpuShown == True:
        cpuFrame.pack_forget()
        cpuButton.configure(text = 'Show CPU')
    else:
        cpuFrame.pack(side = tk.RIGHT, expand = tk.TRUE, pady = padding)
        cpuButton.configure(text = 'Hide CPU')

def ramShowHide():
    ramShown = ramFrame.winfo_ismapped()
    if ramShown ==True:
        ramFrame.pack_forget()
        ramButton.configure(text = 'Show RAM')
    else:
        ramFrame.pack(side = tk.RIGHT, expand = tk.TRUE, pady = padding)
        ramButton.configure(text = 'Hide RAM')
        
def infoShowHide():
    infoShown = systemInfo.winfo_ismapped()
    if infoShown == True:
        systemInfo.pack_forget()
        systemInfoButton.configure(text = 'Show System Information')
    else:
        systemInfo.pack(side = tk.RIGHT, expand = tk.TRUE, pady = padding)
        systemInfoButton.configure(text = 'Hide System Information')

def adviceShowHide():
    adviceShown = advice.winfo_ismapped()
    if adviceShown == False:
        advice.pack(side = tk.RIGHT, expand = tk.TRUE, pady = padding)
        adviceButton.configure(text = 'Hide Advice')
    else:
       advice.pack_forget()
       adviceButton.configure(text = 'Show Advice')


##Variables used
a = 0
padding = 10
backgroundColour = '#0066b4'
textColour = 'white'
buttonThickness = 0
cpu = []
cpu = psutil.cpu_percent(interval = None,percpu = False)
ram = ramvalue()

cpuCount = psutil.cpu_count(logical = 'TRUE')
ram2 = psutil.virtual_memory()
totalRam = ram2[0]
totalRam = totalRam / 1073741824
totalRam = round(totalRam, 3)

freeRam = ram2[1]
freeRam = freeRam /1073741824
freeRam = round(freeRam, 1)

doBattery = False
battery = psutil.sensors_battery()

if battery is not None:
    doBattery = True
else:
    doBattery = False

if doBattery == True:
    percent = battery[0]
    secsleft = battery[1]
    secsleft = secsleft / 60
    secsleft = round(secsleft, 2)
    secsleft = int(secsleft)
    charging = battery[2]
    
else:
    doBattery = False

diskUsage = psutil.disk_usage('/')
freeSpace = diskUsage[2]
freeSpace = freeSpace / 1073741824
freeSpace = round(freeSpace, 1)


##Advice decisions

batteryAdvice = 'None'
if doBattery == True:
    if percent < 20:
        if charging == True:
            batteryAdvice = 'Your power levels are healthy!'
        elif charging == False:
            batteryAdvice = 'Charge your battery to improve performance!'
        else:
            batteryAdvice = 'Charger sensor not working!'
    else:
        batteryAdvice = 'Your battery level is healthy!'
else:
    batteryAdvice = 'You have no battery on your device. \n No advice available!'



ramAdvice = 'None'
if ram > 95:
    ramAdvice = 'Close some unused programs to free up RAM!'
else:
    ramAdvice = 'Your RAM usage is healthy!'


storageAdvice = 'None'
if freeSpace < 0.5:
    storageAdvice = 'Free up space on hard drive to improve performance!'
else:
    storageAdvice = 'Your storage use is healthy!'


##Refresh functions
def refresh():
    global a
    if a == 0:
        refresh_cpuPerformance()
        refresh_ramUsed()
        refresh_batteryInfo()
        a = 1
    else:
        a = 1
    
    
def refresh_cpuPerformance():
    cpu = psutil.cpu_percent(interval = None,percpu = False)
    cpuPerformance.configure(text = ("performance: " + str(cpu) + "%"))
    cpuRefresh = window.after(1000, refresh_cpuPerformance)

def refresh_ramUsed():
    ram = ramvalue()
    ramUsed.configure(text = ("Ram used: " + str(ram) + '%'))
    ramRefresh = window.after(1000, refresh_ramUsed)

def refresh_batteryInfo():
    doBattery = False
    battery = psutil.sensors_battery()

    if battery is not None:
        doBattery = True
    else:
        doBattery = False
        
    if doBattery == True:
        percent = battery[0]
        secsleft = battery[1]
        secsleft = secsleft / 60
        secsleft = round(secsleft, 2)
        secsleft = int(secsleft)
        charging = battery[2]
        batteryPercentlabel.configure(text = ('Current battery level: ' + str(percent) + '%'))

        if charging == True:
            timeRemainingLabel.configure( text = ("You're device is charging!"))
        else:
            timeRemainingLabel.configure( text = ('You have ' + str(secsleft) + ' mins of battery remaining!'))

        if percent < 20:
            if charging == True:
                batteryAdvice = 'Your power levels are healthy!'
            elif charging == False:
                batteryAdvice = 'Charge your battery to improve performance!'
            else:
                batteryAdvice = 'Charger sensor not working!'
        else:
            batteryAdvice = 'Your battery level is healthy!'
    else:
        doBattery = False
    batteryAdviceLabel.configure(text = batteryAdvice)
    batteryRefresh = window.after(1000, refresh_batteryInfo)
##Base window
window = tk.Tk()
window.title("System Resource Monitor")
window.configure(bg = backgroundColour)

##intro image
try:
    logo = tk.PhotoImage(file = "app icon.png")
except:
    logo = ''


##making frames
introFrame = tk.Frame(window)
introFrame.configure(bg = 'white')
introFrame.pack()

cpuFrame = tk.Frame(window)
cpuFrame.configure(bg = backgroundColour)

ramFrame = tk.Frame(window)
ramFrame.configure(bg = backgroundColour)

menuWholeFrame = tk.Frame(window)
menuWholeFrame.configure(bg = 'white')

menuButtonFrame = tk.Frame(menuWholeFrame)
menuButtonFrame.configure(bg = 'white')
menuButtonFrame.pack()

menu = tk.Frame(menuWholeFrame)
menu.configure(bg = 'white')
menu.pack()

systemInfo = tk.Frame(window)
systemInfo.configure(bg = backgroundColour)

advice = tk.Frame(window)
advice.configure(bg = backgroundColour)

## Intro
if type(logo) == str:
    logoLabel = tk.Label(introFrame, text = logo)
    logoLabel.pack()
else:
    logoLabel = tk.Label(introFrame, image = logo)
    logoLabel.pack()

introLabel = tk.Label(introFrame,
                       text = ("""
Welcome to Edwin's system Monitoring Tool!


The menu will be on the left, through the buttons on the left, you can toggle show or hide cpu, ram, system information and advice as well as starting to fetch information.
The fetch data button refreshes ram and cpu every second, please don't spam this button!
This application was designed to help you access performance information easier and help give you advice to improve system performance.
Once you have read this, please click the button below to start using the program. Enjoy!
- Edwin """),
                       fg = 'black',
                       background = 'white')
introLabel.pack()

closeIntroButton = tk.Button(introFrame, text = 'OK! Close introduction!',
                             bd = 2,
                             command = closeIntro)
closeIntroButton.pack()


##Menu
menuButton = tk.Button(menuButtonFrame, text = 'MENU',
                       bd = buttonThickness,
                       bg = 'white',
                       command = menuShowHide)

menuButton.pack(pady = 6)

introButton = tk.Button(menu, text = 'Show Introduction',
                        bd = buttonThickness,
                        bg = 'white',
                        command = introShow)
introButton.pack(pady = 3)

start = tk.Button(menu, text ='Start fetching data!',
                  bd = buttonThickness,
                  bg = 'white',
                  command = refresh
                  )
start.pack(pady = 3)

systemInfoButton = tk.Button(menu, text = 'Show System Info',
                             bd = buttonThickness,
                             bg = 'white',
                             command = infoShowHide)
systemInfoButton.pack(pady = 3)

cpuButton = tk.Button(menu, text = 'Show CPU',
                      bd = buttonThickness,
                      bg = 'white',
                      command = cpuShowHide)
cpuButton.pack(pady = 3)

ramButton = tk.Button(menu, text = 'Show RAM',
                      bd = buttonThickness,
                      bg = 'white',
                      command = ramShowHide)
ramButton.pack(pady = 3)

adviceButton = tk.Button(menu, text = 'Show Advice',
                         bd = buttonThickness,
                         bg = 'white',
                         command = adviceShowHide)
adviceButton.pack(pady = 3)

##System Info
if doBattery == True:
    batteryPercentlabel = tk.Label(systemInfo,
                                   text = ('Current battery level: ' + str(percent) + '%'),
                                   fg = textColour,
                                   background = backgroundColour)
    batteryPercentlabel.pack()

    if charging == True:
        timeRemainingLabel = tk.Label(systemInfo,
                                  text = ("You're device is charging!"),
                                  fg = textColour,
                                  background = backgroundColour)
        timeRemainingLabel.pack()
    else:
        timeRemainingLabel = tk.Label(systemInfo,
                                  text = ('You have ' + str(secsleft) + ' mins of battery remaining!'),
                                  fg = textColour,
                                  background = backgroundColour)
        timeRemainingLabel.pack()
else:
    doBattery == False

cpuCountLabel = tk.Label(systemInfo,
                         text = ('Number of cpus: ' + str(cpuCount) + '!'),
                         fg = textColour,
                         background = backgroundColour)
cpuCountLabel.pack()

totalMemoryLabel = tk.Label(systemInfo,
                            text = ('Total amount of RAM: ' + str(totalRam) + 'GB'),
                            fg = textColour,
                            background = backgroundColour)
totalMemoryLabel.pack()

storageLeftLabel = tk.Label(systemInfo,
                            text = ('Total Storage left: '+ str(freeSpace) + 'GB'),
                            fg = textColour,
                            background = backgroundColour)

storageLeftLabel.pack()

##CPU performance
cpuLabel = tk.Label(
    cpuFrame, text = 'CPU performance (percentage)',
    fg = textColour,
    background = backgroundColour
    )
cpuLabel.pack()


cpuPerformance = tk.Label(
    cpuFrame, text =  ("performance: " + str(cpu) +'%'),
    background = backgroundColour,
    fg = textColour
    )
cpuPerformance.pack()



##RAM usage
ramLabel = tk.Label(
    ramFrame, text = 'RAM usage (Percentage)',
    fg = textColour,
    background = backgroundColour
    )
ramLabel.pack()

ramUsed = tk.Label(
    ramFrame, text =  ("Ram used: " + str(ram) + '%'),
    background = backgroundColour,
    fg = textColour
    )
ramUsed.pack()

##Advice
adviceLabel = tk.Label(
    advice, text = 'Some things you can do to improve performance is:',
    fg = textColour,
    background = backgroundColour)
adviceLabel.pack()

batteryAdviceLabel = tk.Label(
    advice, text = batteryAdvice,
    fg = textColour,
    background = backgroundColour)
batteryAdviceLabel.pack()

ramAdviceLabel = tk.Label(
    advice, text = ramAdvice,
    fg = textColour,
    background = backgroundColour)
ramAdviceLabel.pack()

storageAdviceLabel = tk.Label(
    advice, text = storageAdvice,
    fg = textColour,
    bg = backgroundColour)
storageAdviceLabel.pack()

conclusionLabel = tk.Label(
    advice, text = 'If everything is healthy, your PC should be performing well. \n  \n If your PC still does not perform well, consider contacting manufacturer.',
    fg = textColour,
    bg = backgroundColour
    )
conclusionLabel.pack()

window.mainloop()
