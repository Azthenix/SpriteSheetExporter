from krita import *

class MyExtension(Extension):

	def __init__(self, parent):
		super().__init__(parent)

	def setup(self):
		pass

	def createActions(self, window):
		action = window.createAction("myAction", "SpriteSheet Exporter", "tools/scripts")
		action.triggered.connect(self.exportDocument)
		pass

	def exportDocument(self):
		doc =  Krita.instance().activeDocument()
		if doc is not None:
			sheet = self.compileLayers(doc)
			fileName = QFileDialog.getSaveFileName()[0]
			sheet.exportImage(fileName, InfoObject())
	
	def compileLayers(self, doc):
		doc.refreshProjection()
		topNodes = doc.topLevelNodes()
		w = doc.width()
		h = doc.height()
		res = doc.resolution()

		sheet = Krita.instance().createDocument(w, h, doc.name() + "Sheet", doc.colorModel(), doc.colorDepth(), doc.colorProfile(), res)
		layer = sheet.createNode('bruh', 'paintlayer')
		sheet.rootNode().addChildNode(layer, None)

		row = 0

		for node in topNodes:
			nType = node.type()
			sH = sheet.height()
			col = 0

			if(sH <= ((row) * h)):
				sheet.resizeImage(0, 0, sheet.width(), sH+h)
			if(nType == 'grouplayer'):
				for column in node.childNodes():
					sW = sheet.width()

					if(sW <= ((col) * w)):
						sheet.resizeImage(0, 0, sW+w, sheet.height())

					data = column.projectionPixelData(0, 0, w, h)
					layer.setPixelData(data, col*w, row*h, w, h)
					col += 1
			elif(nType == 'paintlayer'):
				data = node.projectionPixelData(0, 0, w, h)
				layer.setPixelData(data, col*w, row*h, w, h)

			row += 1
		
		sheet.refreshProjection()

		return sheet
	
	def calculateDimensions(topNodes):
		pass

# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(MyExtension(Krita.instance()))