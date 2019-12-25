from osgeo import gdal
from gdalconst import *
from pyproj import Proj
from gdal import GetDriverByName
import numpy
from numpy import nan_to_num
from numpy import add, subtract, divide, multiply
import math
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.misc as sm


class Agriculture:
    TAG = "[Agriculture.class]"
    open_B6 = None
    open_B5 = None
    open_B2 = None
    isOpenB6 = False
    isOpenB5 = False
    isOpenB2 = False

    crop_B6 = None
    crop_B5 = None
    crop_B2 = None

    correctionB6Reflectance = None
    correctionB5Reflectance = None
    correctionB2Reflectance = None

    agricultureResult = None
    listener = None
    isCropped = False
    isReflectance = False
    metadataPath = None
    cols = 0
    rows = 0
    output_cols = 0
    output_rows = 0

    lonStartCrop = 0
    latStartCrop = 0
    lonEndCrop = 0
    latEndCrop = 0

    lonStartDefault = 0
    latStartDefault = 0
    lonEndDefault = 0
    latEndDefault = 0

    isMtl = False

    B6MultiReflectance = 0
    B5MultiReflectance = 0
    B2MultiReflectance = 0

    B6AddReflectance = 0
    B5AddReflectance = 0
    B2AddReflectance = 0

    sunElevation = 0

    data_B6 = None
    data_B5 = None
    data_B4 = None

    dataB6Reflectance = None
    dataB5Reflectance = None
    dataB2Reflectance = None

    isAgriculture = False

    listener = None

    def __init__(self):
        print("Agriculture RGB Composite Instance Created")

    def OpenB6File(self, path):
        if "B6" in path:
            print(self.TAG, "Band 6 path: ", path)
            # self.open_B6 = gdal.Open(path, GA_ReadOnly)
            self.open_B6 = gdal.Open(path)
            self.isCropped = False
            self.isOpenB6 = True
            self.listener.showMessage("SWIR berhasil diinput")
        else:
            self.isOpenB6 = False
            self.listener.showErrorMessage("Terjadi kesalahan input SWIR")

    def OpenB5File(self, path):
        if "B5" in path:
            print(self.TAG, "Band 5 path: ", path)
            # self.open_B5 = gdal.Open(path, GA_ReadOnly)
            self.open_B5 = gdal.Open(path)
            self.isCropped = False
            self.isOpenB5 = True
            self.listener.showMessage("NIR berhasil diinput")
        else:
            self.isOpenB5 = False
            self.listener.showErrorMessage("Terjadi kesalahan input NIR")

    def OpenB2File(self, path):
        if "B2" in path:
            print(self.TAG, "Band 2 path: ", path)
            # self.open_B2 = gdal.Open(path, GA_ReadOnly)
            self.open_B2 = gdal.Open(path)
            self.isCropped = False
            self.isOpenB2 = True
            self.listener.showMessage("BLUE berhasil diinput")
        else:
            self.isOpenB2 = False
            self.listener.showErrorMessage("Terjadi kesalahan input BLUE")

    def OpenMtlFile(self, path):
        issue = []
        issue.clear()
        if "mtl" in path.lower():
            file = open(path, 'r')
            line = file.readlines()

            for x in line:
                if x.startswith("    REFLECTANCE_MULT_BAND_6"):
                    data = x.split()
                    result = data[2]
                    print("B6 Reflectance Mult: ", result)
                    self.B6MultiReflectance = result

                if x.startswith("    REFLECTANCE_MULT_BAND_5"):
                    data = x.split()
                    result = data[2]
                    print("B5 Reflectance Mult: ", result)
                    self.B5MultiReflectance = result

                if x.startswith("    REFLECTANCE_MULT_BAND_2"):
                    data = x.split()
                    result = data[2]
                    print("B2 Reflectance Mult: ", result)
                    self.B2MultiReflectance = result

                if x.startswith("    REFLECTANCE_ADD_BAND_6"):
                    data = x.split()
                    result = data[2]
                    print("B6 Reflectance Add: ", result)
                    self.B6AddReflectance = result

                if x.startswith("    REFLECTANCE_ADD_BAND_5"):
                    data = x.split()
                    result = data[2]
                    print("B5 Reflectance Add: ", result)
                    self.B5AddReflectance = result

                if x.startswith("    REFLECTANCE_ADD_BAND_2"):
                    data = x.split()
                    result = data[2]
                    print("B2 Reflectance Add: ", result)
                    self.B2AddReflectance = result

                if x.startswith("    SUN_ELEVATION"):
                    data = x.split()
                    result = data[2]
                    print("Sun Elevation: ", result)
                    self.sunElevation = result

            if self.B6MultiReflectance == 0:
                issue.append("REFLECTANCE_MULT_BAND_6 not found")
            if self.B5MultiReflectance == 0:
                issue.append("REFLECTANCE_MULT_BAND_5 not found")
            if self.B2MultiReflectance == 0:
                issue.append("REFLECTANCE_MULT_BAND_2 not found")
            if self.B6AddReflectance == 0:
                issue.append("REFLECTANCE_ADD_BAND_6 not found")
            if self.B5AddReflectance == 0:
                issue.append("REFLECTANCE_ADD_BAND_5 not found")
            if self.B2AddReflectance == 0:
                issue.append("REFLECTANCE_ADD_BAND_2 not found")
            if self.sunElevation == 0:
                issue.append("SUN_ELEVATION not found")

            if issue:
                issueBuf = ""
                for item in issue:
                    issueBuf += item + "\n"
                self.listener.showErrorMessage(
                    "Import mtl file failed\n\n" + issueBuf + "\n" + "Its caused by wrong mtl file imported")
                self.isMtl = False
            else:
                self.listener.showMessage("MTL berhasil diinput")
                self.isMtl = True
        else:
            self.listener.showErrorMessage("Wrong MTL file imported")

    def SetCropCoordinate(self, latStart, lonStart, latEnd, lonEnd):
        self.latStartCrop = latStart
        self.lonStartCrop = lonStart
        self.latEndCrop = latEnd
        self.lonEndCrop = lonEnd

    def CropImage(self):
        self.cols = self.open_B6.RasterXSize
        self.rows = self.open_B6.RasterYSize
        bands = self.open_B6.RasterCount
        self.listener.logMessage(
            "cols: {} | rows: {} | bands: {}".format(self.cols, self.rows, bands))

        gt = self.open_B6.GetGeoTransform()
        self.listener.logMessage("GeoTransform: " + str(gt))
        x0 = gt[0]
        y0 = gt[3]
        pwidth = gt[1]
        pheight = gt[5]
        x_end = self.cols * pwidth + x0
        y_end = self.cols * pheight + y0

        myProj = Proj(
            "+proj=utm +zone=50, +north +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
        lon, lat = myProj(x0, y0, inverse=True)
        y_utm, x_utm = myProj(lon, lat)
        self.listener.logMessage("Lat: {}, Lon: {}".format(lat, lon))
        self.listener.logMessage("x_utm: {} | y_utm: {}".format(x_utm, y_utm))

        x_mulai_crop_utm, y_mulai_crop_utm = myProj(
            self.lonStartCrop, self.latStartCrop)
        x_akhir_crop_utm, y_akhir_crop_utm = myProj(
            self.lonEndCrop, self.latEndCrop)
        print("x_mulai_crop_utm: ", x_mulai_crop_utm, "\ny_mulai_crop_utm: ", y_mulai_crop_utm, "\nx_akhir_crop_utm: ",
              x_akhir_crop_utm, "\nx_akhir_crop_utm: ", y_akhir_crop_utm)

        xoff = int((x_mulai_crop_utm - x0) / pwidth)
        yoff = int((y_mulai_crop_utm - y0) / pheight)
        self.listener.logMessage("xoff: {} | yoff: {}".format(xoff, yoff))

        self.output_cols = int((x_akhir_crop_utm - x_mulai_crop_utm) / pwidth)
        self.output_rows = int((y_akhir_crop_utm - y_mulai_crop_utm) / pheight)
        self.listener.logMessage("outpus_rows: {}, output_cols: {}".format(
            self.output_rows, self.output_cols))

        band_6 = self.open_B6.GetRasterBand(1)
        band_5 = self.open_B5.GetRasterBand(1)
        band_2 = self.open_B2.GetRasterBand(1)

        self.crop_B6 = band_6.ReadAsArray(
            xoff, yoff, self.output_cols, self.output_rows).astype(numpy.float)
        self.crop_B5 = band_5.ReadAsArray(
            xoff, yoff, self.output_cols, self.output_rows).astype(numpy.float)
        self.crop_B2 = band_2.ReadAsArray(
            xoff, yoff, self.output_cols, self.output_rows).astype(numpy.float)

        self.isCropped = True
        self.listener.showMessage("Sukses Crop")

    def StartCorrection(self):
        # band_6 = self.open_B6.GetRasterBand(1)
        # band_5 = self.open_B5.GetRasterBand(1)
        # band_2 = self.open_B2.GetRasterBand(1)

        band_6 = self.crop_B6
        band_5 = self.crop_B5
        band_2 = self.crop_B2

        B6MultiReflectance = float(self.B6MultiReflectance)
        B5MultiReflectance = float(self.B5MultiReflectance)
        B2MultiReflectance = float(self.B2MultiReflectance)

        B6AddReflectance = float(self.B6AddReflectance)
        B5AddReflectance = float(self.B5AddReflectance)
        B2AddReflectance = float(self.B2AddReflectance)

        sun_elevation = float(self.sunElevation)

        dataB6Reflectance = (band_6 * B6MultiReflectance) + B6AddReflectance
        dataB5Reflectance = (band_5 * B5MultiReflectance) + B5AddReflectance
        dataB2Reflectance = (band_2 * B2MultiReflectance) + B2AddReflectance

        print("dataB6Reflectance: ", str(dataB6Reflectance))
        print("dataB5Reflectance: ", str(dataB5Reflectance))
        print("dataB2Reflectance: ", str(dataB2Reflectance))

        self.correctionB6Reflectance = dataB6Reflectance / \
            math.sin(sun_elevation) * 65536
        self.correctionB5Reflectance = dataB5Reflectance / \
            math.sin(sun_elevation) * 65536
        self.correctionB2Reflectance = dataB2Reflectance / \
            math.sin(sun_elevation) * 65536

        print("correctionB6Reflectance: ", str(self.correctionB6Reflectance))
        print("correctionB5Reflectance: ", str(self.correctionB5Reflectance))
        print("correctionB2Reflectance: ", str(self.correctionB2Reflectance))

        self.isReflectance = True
        self.listener.showMessage("Sukses Koreksi Reflectance")

    def startAgricultureComposite(self):
        # image = []
        # data_B6_32 = self.correctionB6Reflectance.astype(numpy.float32)
        # image.append(data_B6_32)
        # data_B5_32 = self.correctionB5Reflectance.astype(numpy.float32)
        # image.append(data_B5_32)
        # data_B2_32 = self.correctionB2Reflectance.astype(numpy.float32)
        # image.append(data_B2_32)

        # band_6 = self.open_B6.GetRasterBand(1)
        # band_5 = self.open_B5.GetRasterBand(1)
        # band_2 = self.open_B2.GetRasterBand(1)

        # # Nyak tapi gelap
        # band_6_raw = self.open_B6
        # band_5_raw = self.open_B5
        # band_2_raw = self.open_B2

        # band_6 = self.norm(band_6_raw.ReadAsArray().astype(numpy.float))
        # band_5 = self.norm(band_5_raw.ReadAsArray().astype(numpy.float))
        # band_2 = self.norm(band_2_raw.ReadAsArray().astype(numpy.float))

        # rgb = numpy.dstack((band_6_raw, band_5_raw, band_2_raw))

        # band_6 = self.norm(self.crop_B6)
        # band_5 = self.norm(self.crop_B5)
        # band_2 = self.norm(self.crop_B2)

        band_6 = self.norm(self.correctionB6Reflectance)
        band_5 = self.norm(self.correctionB5Reflectance)
        band_2 = self.norm(self.correctionB2Reflectance)
        rgb = numpy.dstack((band_6, band_5, band_2))
        self.agricultureResult = rgb
        self.isAgriculture = True

        if self.listener is not None:
            self.listener.onRgbFinished(rgb)

    def showAgricultureComposite(self):
        rgb = self.agricultureResult
        if self.listener is not None:
            self.listener.onShowRgb(rgb)

    def SaveResult(self):
        geotiff = GetDriverByName('Gtiff')
        path = "tes.tif"
        output = geotiff.Create(path, self.output_cols,
                                self.output_rows, 1, gdal.GDT_Float32)
        output.SetGeoTransform(self.open_B6.GetGeoTransform())
        output_band = output.GetRasterBand(1)
        output_band.WriteArray(self.agricultureResult)
        print("File created successfully.")

    def norm(self, band):
        band_min, band_max = band.min(), band.max()
        return ((band - band_min)/(band_max - band_min))

    def MyListener(self, listener):
        self.listener = listener


class MyListener:
    def onRgbFinished(self, result):
        print("RGB Finished")
