# from django.test import TestCase

# Create your tests here.
import zpl
from zebra import Zebra
import qrcode

class QRLabelMaker:
    def __init__(self, height = 25, width = 100) -> None:        
        self.label = zpl.Label(height, width)
        self.qr_contents = ['Wishes you a great day!!!. Best wishes from Ant teams.'] * 4
        
    def set_text_slot1(self, text):
        self.qr_contents[0] = text
        
    def set_text_slot2(self, text):
        self.qr_contents[1] = text
        
    def set_text_slot3(self, text):
        self.qr_contents[2] = text
        
    def set_text_slot4(self, text):
        self.qr_contents[3] = text
            
    def prepare_label(self):
        self.label.origin(0, 0)
        img1 = qrcode.make(self.qr_contents[0])
    
        self.label.write_graphic(img1, 23, 23)
        self.label.endorigin()
        
        self.label.origin(2, 22)
        self.label.write_text(self.qr_contents[0][-12:], char_height=2, char_width=3)
        self.label.endorigin()

        self.label.origin(25, 0)
        img2 = qrcode.make(self.qr_contents[1])
        # self.label.barcode('Q', self.qr_contents[1], height= 22 ,magnification=6)
        self.label.write_graphic(img2, 23, 23)
        self.label.endorigin()
        
        self.label.origin(27, 22)
        self.label.write_text(self.qr_contents[1][-12:], char_height=2, char_width=3)
        self.label.endorigin()


        self.label.origin(50, 0)
        img3 = qrcode.make(self.qr_contents[2])
        # self.label.barcode('Q', self.qr_contents[2], height= 22 ,magnification=6)
        self.label.write_graphic(img3, 23, 23)
        self.label.endorigin()
        
        self.label.origin(52, 22)
        self.label.write_text(self.qr_contents[2][-12:], char_height=2, char_width=3)
        self.label.endorigin()


        self.label.origin(75, 0)
        img4 = qrcode.make(self.qr_contents[3])
        # self.label.barcode('Q', self.qr_contents[3], height= 22 ,magnification=6)
        self.label.write_graphic(img4, 23, 23)
        self.label.endorigin()
        
        self.label.origin(77, 22)
        self.label.write_text(self.qr_contents[3][-12:], char_height=2, char_width=3)
        self.label.endorigin()
        
    def get_output(self):
        self.prepare_label()
        return self.label.dumpZPL()
    
    def preview(self):
        self.prepare_label()
        self.label.preview()



qrlabel = QRLabelMaker()
qrlabel.set_text_slot1("6759c7ac-cd1b-480a-9648-a915de544bb2")
qrlabel.set_text_slot2("068babfe-1662-4bb5-af79-05b05e655f80")
qrlabel.set_text_slot3("b5fd206e-973f-4488-b0e9-7d4c79582dde")
qrlabel.set_text_slot4("d48cec04-dc6c-4dfc-beac-f395de727f7c")
# qrlabel.preview() 

z = Zebra()
Q=z.getqueues()

queue = 'ZDesigner ZD420-300dpi ZPL (Copy 1)'
# z.setqueue(Q[0])
z.setqueue(queue)
z.output(qrlabel.get_output())


