import pygame, sys, zipfile, shutil

def load(dataPack):
	nameList = []
	data = {}
	with zipfile.ZipFile(dataPack, "r", zipfile.ZIP_DEFLATED) as zf:
		zf.extractall("temp")
		nameList = zf.namelist()
	for name in nameList:
		if name.endswith(".png"):
			data[name.rstrip(".png")] = pygame.image.load("temp/%s" % name)
		elif name.endswith(".mp3"):
			data[name.rstrip(".mp3")] = pygame.mixer.Sound("temp/%s" % name)
	shutil.rmtree("temp")
	return data

class Character:
	def __init__(self, name, dataPack, x0, y0):
		self.name = name
		self.dataPack = load(dataPack)
		self.x, self.y = x0, y0
		self.score = 0
	def draw(self, screen):
		pass
	def interact(self):
		pass
	def keyDown(self, key):
		pass

class Player:
	def __init__(self, name, dataPack, x0, y0):
		self.name = name
		self.dataPack = load(dataPack)
		self.x, self.y = x0, y0

class Framework:
	def __init__(self):
		self.cList = []
	def addC(self, c):
		self.cList.append(c)

pygame.init()

c = Character("Kev", "res/kev.pak", 0, 0)