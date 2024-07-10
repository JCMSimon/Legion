from queue import Queue

class Crawler():
	def __init__(self,startURL:str) -> None:
		self.currentURL = startURL
		self.todo:Queue = Queue(0)