from Tkinter import *
import bluetooth

print "Buscando Dispositivos bluetooth..."
print ""
nearby_devices = bluetooth.discover_devices()
num = 0
print "Seleccione el dispositvo para trabajar..."
for i in nearby_devices:
	num+=1
	print num , ": " , bluetooth.lookup_name( i )

selection = input("> ") - 1
print "Selecciono el dispositivo", bluetooth.lookup_name(nearby_devices[selection])
bd_addr = nearby_devices[selection]

port = 1

class Application(Frame):

    sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

    def disconnect(self):
        self.sock.close()
        
    def on(self):
        data = "b"
        self.sock.send(data)

    def off(self):
        data = "L"
        self.sock.send(data)
   
    def onLeft(self):
        data = "l"
        self.sock.send(data)

    def onStop(self):
        data = "s"
        self.sock.send(data)

    def onRight(self):
        data = "r"
        self.sock.send(data)

    def onFowrard(self):
        data = "f"
        self.sock.send(data)

    def onBack(self):
        data = "b"
        self.sock.send(data)

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Salir"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.disconnectFrom = Button(self)
        self.disconnectFrom["text"] = "stop"
        self.disconnectFrom["fg"]   = "red"
        self.disconnectFrom["command"] =  self.onStop

        self.disconnectFrom.pack({"side": "left"})

        self.turnOn = Button(self)
        self.turnOn["text"] = "left",
        self.turnOn["fg"] = "green"
        self.turnOn["command"] = self.onLeft


        self.turnOn.pack({"side": "left"})

        self.turnOff = Button(self)
        self.turnOff["text"] = "right"
        self.turnOff["fg"] = "blue"
        self.turnOff["command"] = self.onRight

        self.turnOff.pack({"side": "left"})

        self.turnOff = Button(self)
        self.turnOff["text"] = "forward"
        self.turnOff["fg"] = "black"
        self.turnOff["command"] = self.onFowrard

        self.turnOff.pack({"side": "left"})

        self.turnOff = Button(self)
        self.turnOff["text"] = "back"
        self.turnOff["fg"] = "green"
        self.turnOff["command"] = self.onBack

        self.turnOff.pack({"side": "left"})

    def __init__(self, master=None):
        self.sock.connect((bd_addr, port))
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()