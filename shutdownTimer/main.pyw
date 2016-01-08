import sys
from code import TimerGuiView, TimerGuiCtrl, Day2Day, create_app


# load GUI and ask for the time till shutdown
app = create_app(sys.argv)
guiView = TimerGuiView()
guiView.setWindowTitle("Shutdown Timer App")
guiView.setFixedSize(300,200)
guiCtrl = TimerGuiCtrl(guiView)

guiCtrl.view.show()
app.exec_()

# run timer
if guiCtrl.ready :
    guiCtrl.sleepTime()
    # shutdown computer
    print "Time is up !!!"
    d2d = Day2Day()
    d2d.shutdown()
else:
    print "No time given - quiting.."