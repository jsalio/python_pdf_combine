
import sys
from tkinter.tix import Tk
from app_ui import AppUi
from tools import convertImageToPdf

ui = AppUi()
root:Tk
deactivate_ui = False

deactivate_ui = sys.argv[1] == 'not-ui'

if deactivate_ui :
   convertImageToPdf(sys.argv[2], sys.argv[3])
else :
    root = ui.Build_UI();
    root.mainloop()