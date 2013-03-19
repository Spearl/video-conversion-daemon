#!/usr/bin/python
from socket import socket, AF_INET, SOCK_STREAM
import xmlrpclib
import sys

def main():
	server = xmlrpclib.ServerProxy("http://localhost:8080")
	s = socket(AF_INET, SOCK_STREAM)
	print server.convert(sys.argv[1], sys.argv[2])



if __name__ == '__main__':
	if len(sys.argv) != 3:
		print "Fail! Give me infile and outfile!"
		exit()
	main()