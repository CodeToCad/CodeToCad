# This file is automatically generated for code intellisense only.
# It does not reflect the actual implementation.

from __future__ import annotations
from collections.abc import Iterator

from . import core


class PDFSheetsExport:
    """
    The various options that define which sheets to print.
    """

    def __init__(self):
        pass

    AllPDFSheetsExport = 0
    SelectedPDFSheetsExport = 1
    CurrentPDFSheetExport = 2
    RangePDFSheetsExport = 3


class DrawingExportManager(core.Base):
    """
    Provides support to export the drawing in various formats.
    """

    def __init__(self):
        pass

    @staticmethod
    def cast(arg) -> DrawingExportManager:
        return DrawingExportManager()

    def createPDFExportOptions(self, filename: str) -> PDFExportOptions:
        """
        Defines the various settings for a STEP export.
        filename : The name of the file to export to. Use settings on the returned PDFExportOptions
        object to change other settings.
        Returns a PDFExportOptions object if successful and null if it should fail.
        """
        return PDFExportOptions()

    def execute(self, exportOptions: DrawingExportOptions) -> bool:
        """
        Executes the export operation to create the file in the format specified by the input ExportOptions object.
        exportOptions : A DrawingExportOptions object that is created using one of the create methods on the DrawingExportManager object.
        This defines the type of export and defines the options supported for that file type.
        Returns true if the export was successful.
        """
        return bool()


class DrawingExportOptions(core.Base):
    """
    The base class for the different drawing export types.  This class is never directly used
    in an export because you need the specific export type to specify the type of
    export to be performed.
    """

    def __init__(self):
        pass

    @staticmethod
    def cast(arg) -> DrawingExportOptions:
        return DrawingExportOptions()

    @property
    def filename(self) -> str:
        """
        Gets and sets the filename that the exported file will be written to.
        """
        return str()

    @filename.setter
    def filename(self, value: str):
        """
        Gets and sets the filename that the exported file will be written to.
        """
        pass


class Drawing(core.Product):
    """
    Object that represents the drawing specific data within a drawing document.
    """

    def __init__(self):
        pass

    @staticmethod
    def cast(arg) -> Drawing:
        return Drawing()

    @property
    def exportManager(self) -> DrawingExportManager:
        """
        Returns the DrawingExportManager for this drawing.  You use the ExportManager
        to export the drawing in various formats.
        """
        return DrawingExportManager()


class DrawingDocument(core.Document):
    """
    Object that represents a Fusion 360 drawing document.
    """

    def __init__(self):
        pass

    @staticmethod
    def cast(arg) -> DrawingDocument:
        return DrawingDocument()

    @property
    def drawing(self) -> Drawing:
        """
        Returns the Drawing product object associated with this drawing document.
        """
        return Drawing()


class PDFExportOptions(DrawingExportOptions):
    """
    Defines the inputs needed to export the drawing as PDF.
    """

    def __init__(self):
        pass

    @staticmethod
    def cast(arg) -> PDFExportOptions:
        return PDFExportOptions()

    @property
    def sheetsToExport(self) -> PDFSheetsExport:
        """
        Defines which sheets to export.  Defaults to AllPDFSheets which
        will create a single PDF file containing all sheets in the drawing.

        the SelectedPDFSheets and CurrentPDFSheet options are dependent on
        the current selections in the user interface.

        To set this to RangePDFSheets, use the sheetRange property to define
        the range of sheets to print.
        """
        return PDFSheetsExport()

    @sheetsToExport.setter
    def sheetsToExport(self, value: PDFSheetsExport):
        """
        Defines which sheets to export.  Defaults to AllPDFSheets which
        will create a single PDF file containing all sheets in the drawing.

        the SelectedPDFSheets and CurrentPDFSheet options are dependent on
        the current selections in the user interface.

        To set this to RangePDFSheets, use the sheetRange property to define
        the range of sheets to print.
        """
        pass

    @property
    def sheetRange(self) -> str:
        """
        Defines the range of sheets to export. This can be a string like
        "1-3" or "1-2,5" where you can define a range of sheets and also
        specific sheets. Setting this property will automatically set
        the sheetsToExport setting to SelectedPDFSheets.
        """
        return str()

    @sheetRange.setter
    def sheetRange(self, value: str):
        """
        Defines the range of sheets to export. This can be a string like
        "1-3" or "1-2,5" where you can define a range of sheets and also
        specific sheets. Setting this property will automatically set
        the sheetsToExport setting to SelectedPDFSheets.
        """
        pass

    @property
    def openPDF(self) -> bool:
        """
        Specifies that the PDF file will be opened after export.
        """
        return bool()

    @openPDF.setter
    def openPDF(self, value: bool):
        """
        Specifies that the PDF file will be opened after export.
        """
        pass

    @property
    def useLineWeights(self) -> bool:
        """
        Specifies if line weights should be used in the exported PDF file.
        """
        return bool()

    @useLineWeights.setter
    def useLineWeights(self, value: bool):
        """
        Specifies if line weights should be used in the exported PDF file.
        """
        pass