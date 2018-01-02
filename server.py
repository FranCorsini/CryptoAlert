from threading import Thread


class serverApp(Thread):

	def run(self):
		app.run()

	def __init__(self, listener):
		Thread.__init__(self)
		tweetListener = listener

