from argparse import ArgumentParser
import sys
from src.Logger import Logger

class helpOnDefaultParser(ArgumentParser):
	def error(self, message):
		sys.stderr.write('error: %s\n' % message)
		self.print_help()
		sys.exit(2)

def start():
	logger.debugMsg("I'm working!")

if __name__ == "__main__":
	parser = helpOnDefaultParser(prog="Legion")
	crawlORsearch = parser.add_mutually_exclusive_group()
	crawlORsearch.add_argument("-c","--crawl-url",help="URL that will be used as seed for web crawling",type=str)
	crawlORsearch.add_argument("-f","--find-image",help="File location / URL of image used to find similar images",type=str)
	parser.add_argument("-D","--debug",action="store_true",help="Enable debug logging")
	args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
	logger = Logger("Main",args.debug)
	start()