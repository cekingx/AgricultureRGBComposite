import wx
import gui
from agriculture import Agriculture
import matplotlib.pyplot as plt
import earthpy.plot as ep


class MainFrame(gui.MainFrame):
    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)
        self.agriculture = Agriculture()
        self.agriculture.MyListener(self)

    # Event Handler
    def onCropButtonClick(self, event):
        # wx.MessageBox('Latitude Longitude masih kosong', 'Koordinat',
        #               wx.OK | wx.ICON_EXCLAMATION)
        latStart = self.latStartText.GetValue()
        lonStart = self.lonStartText.GetValue()
        latEnd = self.latEndText.GetValue()
        lonEnd = self.lonEndText.GetValue()
        if self.agriculture.isOpenB6 and self.agriculture.isOpenB5 and self.agriculture.isOpenB2 and self.agriculture.isMtl:
            if latStart != "" and lonStart != "" and latEnd != "" and lonEnd != "":
                self.agriculture.SetCropCoordinate(latStart, lonStart, latEnd, lonEnd)
                self.agriculture.CropImage()
            else:
                self.showErrorMessage("Koordinat masih ada kosong")
        else:
            self.showErrorMessage("File yang dibutuhkan masih kosong")

    def onReflectanceButtonClick(self, event):
        # wx.MessageBox('File yang dibutuhkan masih kosong', 'File',
        #               wx.OK | wx.ICON_EXCLAMATION)
        if self.agriculture.isCropped:
            self.agriculture.StartCorrection()
        else:
            self.showErrorMessage("Belum Melakukan Crop")
            

    def onCompositeButtonClick(self, event):
        if self.agriculture.isReflectance:
            self.agriculture.startAgricultureComposite()
        else:
            self.showErrorMessage("Belum Melakukan Koreksi Reflectance")

    def onShowButtonClick(self, event):
        # showFrame = ShowFrame(None)
        # showFrame.Show(True)
        if self.agriculture.isAgriculture:
            self.agriculture.showAgricultureComposite()
        else:
            self.showErrorMessage("Belum melakukan RGB Composite")
            

    def onSaveButtonClick(self, event):
        # self.agriculture.SaveResult()
        # print(self.agriculture.agricultureResult)
        if self.agriculture.isAgriculture:
            self.showMessage("File disimpan dengan nama RGBAgriculture.tif")
        else:
            self.showErrorMessage("Belum melakukan RGB Composite")

    def onSwirFileChanged(self, event):
        path = event.GetPath()
        self.agriculture.OpenB6File(path)
        self.agriculture.isOpenB6 = True

    def onNirFileChanged(self, event):
        path = event.GetPath()
        self.agriculture.OpenB5File(path)
        self.agriculture.isOpenB5 = True

    def onBlueFileChanged(self, event):
        path = event.GetPath()
        self.agriculture.OpenB2File(path)
        self.agriculture.isOpenB2 = True

    def onMtlFileChanged(self, event):
        path = event.GetPath()
        self.agriculture.OpenMtlFile(path)
        self.agriculture.isMtl = True

    # Listener function

    def showMessage(self, message):
        self.logMessage(message)
        wx.MessageBox(message, "Info",
                      wx.OK | wx.ICON_INFORMATION)

    def showErrorMessage(self, message):
        self.logMessage(message)
        wx.MessageBox(message, "Error", wx.OK | wx.ICON_ERROR)

    def logMessage(self, message):
        print(self.agriculture.TAG, message)

    def onRgbFinished(self, result):
        # ep.plot_rgb(result, rgb=[0, 1, 2])
        plt.imshow(result)
        plt.savefig("RGBAgriculture.tif", dpi=300, quality=99)
        self.showMessage("Sukses RGB Composite")

    def onShowRgb(self, result):
        plt.show()


class ShowFrame(gui.ShowFrame):
    def __init__(self, parent):
        gui.ShowFrame.__init__(self, parent)


app = wx.App(False)
frame = MainFrame(None)
frame.Show(True)
app.MainLoop()
