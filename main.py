import wx
import gui
from agriculture import Agriculture
import matplotlib.pyplot as plt
import earthpy.plot as ep
import re


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
                self.agriculture.SetCropCoordinate(
                    latStart, lonStart, latEnd, lonEnd)
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
            # result = self.agriculture.agricultureResult
            # self.showMessage("File disimpan dengan nama RGBAgriculture.tif")
            saveFileDialog = wx.FileDialog(self, "Save Image file", wildcard="PNG files (*.png)|*.png|TIF files (*.tif)|*.tif|JPG files (*.JPG)|*.jpg",
                                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

            if (saveFileDialog.ShowModal() == wx.ID_OK):
                path = saveFileDialog.GetPath()
                print(path)
                self.agriculture.saveAgricultureComposite(
                    path)
                # self.showMessage("File has been saved.")
            else:
                self.showMessageError("Aborted")
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
        # plt.savefig("D:\RGBAgriculture.tif", dpi=300, quality=99)
        # plt.savefig("RGBAgriculture.png", dpi=300)
        # plt.savefig("RGBAgriculture.jpg", dpi=200, quality=80)
        self.showMessage("Sukses RGB Composite")

    def onShowRgb(self, result):
        self.agriculture.agricultureResult = result
        plt.show()

    def onSaveRgb(self, result, path):
        png = re.search("\.(png)$", path)
        jpg = re.search("\.(jpg)$", path)
        tif = re.search("\.(tif)$", path)

        if png != None:
            plt.savefig(path, dpi=300)
            text = path + " sukses disimpan"
            self.showMessage(text)
        elif jpg != None:
            plt.savefig(path, dpi=200, quality=80)
            text = path + " sukses disimpan"
            self.showMessage(text)
        elif tif != None:
            plt.savefig(path, dpi=300, quality=99)
            text = path + " sukses disimpan"
            self.showMessage(text)


class ShowFrame(gui.ShowFrame):
    def __init__(self, parent):
        gui.ShowFrame.__init__(self, parent)


app = wx.App(False)
frame = MainFrame(None)
frame.Show(True)
app.MainLoop()
