import socket
import select
import sys
import os

#Process in coming request by parsing
def process_http_header(socket):
    print('processing connection', socket.fileno())
    message = socket.recv(1024)
    
    #turn byte-like to string operable
    message = message.decode('unicode_escape')
    #check for valid Get request
    messageBad = False #assume the request is good prove bad
    lines = message.split("\r\n")
    headerList = lines.pop(0).split(" ")
    #checking request             
    if(len(headerList) != 3):
        messageBad = True
        return None
    if("GET" != headerList[0]):
        messageBad = True
    for i in range(0, len(lines) - 2):
        if(lines[i] != ""):
            temp = lines[i].split(": ")
            if(len(temp) != 2):
                messageBad = True
    #last two lines should be '' after splitting
    if(lines.pop() != "" or lines.pop() != ""):
        messageBad = True
    #outputs either None or valid uri as specified in assignment
    if(messageBad):
        return None
    else:
        uri = headerList[1]
        return uri

#part of program that functions as the server
##accepts connections, takes requests, and processes
def server(hostname, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((hostname, port))
    server_socket.listen(5)

    client_sockets = []
    running = True
    while running == True:
        rlist_input = [server_socket, sys.stdin]
        rlist_input.extend(client_sockets)
        #blocking and selecting connections to accept
        print('blocking on select', [x.fileno() for x in rlist_input])
        rlist_output, _, _ = select.select(rlist_input, [], [])
        print('resuming on select', [x.fileno() for x in rlist_input])

        for s in rlist_output:
            if s == server_socket:
                print('accepted connection')
                connection, client_address = server_socket.accept()
                client_sockets.append(connection)
            elif s == sys.stdin:
                message = input()
                if message == 'exit':
                    running = False
                    break
            else:
                uri = process_http_header(s)   
                #if message is bad throw error to browser
                if(uri == None):
                    #bad request error
                    message = "HTTP/1.1 400 Bad Request\r\nContent-Type: test/html\r\n\r\n<html><head></head><h1>400 Bad Request</h1></body></html>"
                    s.send(message.encode())
                    #close connection
                    s.close
                    client_sockets.remove(s)
                else:
                    fileDir = "static"   
                    fileDir += uri
                    tempString = "./"+fileDir
                    #checks for requested file in static directory
                    if(not os.path.isfile(tempString)):
                        #throw file not found error
                        message = "HTTP/1.1 404 File Not Found\r\nContent-Type: test/html\r\n\r\n<html><head></head><h1>404 File Not Found</h1></body></html>"
                        s.send(message.encode())
                        #close connection
                        s.close
                        client_sockets.remove(s)
                    else:
                        hFile = open(fileDir)
                        htmlContent = ""
                        for line in hFile:
                            htmlContent += line

                        #where response will go (header first then html file)
                        message = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
                        s.send(message.encode())
                        message = htmlContent
                        s.send(message.encode())
                        s.close()
                        client_sockets.remove(s)

    server_socket.close()


def main():
    #catch bad input
    if(len(sys.argv) != 3):
        print("error: please initialize with IP address and port ID")
        return
    if("." not in sys.argv[1]):
        print("error argv[1] requires an IP address")
        return
    if(not sys.argv[2].isdigit()):
        print("error argv[2] requires a Port ID")
        return
    
    hostname = sys.argv[1] 
    port = int(sys.argv[2])
    server(hostname, port)

if __name__ == '__main__':
    main()
