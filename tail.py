#!/usr/bin/env python3
import sys
from os import stat
from time import sleep

class Tail():

	def __init__(self, fname):
		self.fname = fname
		self.file = open(fname, 'r')
		self.exit = False
		self.where = self.file.tell()
		self.size = stat(self.fname).st_size

	def reset(self):
		self.file.close()
		self.file = open(self.fname, 'r')
		self.where = self.file.tell()

	def __iter__(self):
		while not self.exit:
			self.where = self.file.tell()
			line = self.file.readline()

			if not line:
				sleep(1)
				self.file.seek(self.where)
				if stat(self.fname).st_size < self.size:
					self.reset()
					yield "File Truncate Detected"
			else:
				self.size = stat(self.fname).st_size
				yield line

	def __enter__(self):
		return self

	def __exit__(self, *args):
		pass


if __name__ == '__main__':
	with Tail(sys.argv[1]) as t:
		for l in t:
			print(l)
			if "quit" in l:
				t.exit = True
