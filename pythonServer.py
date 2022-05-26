from http.server import BaseHTTPRequestHandler, HTTPServer

from datetime import datetime

import socket


#Test pythos server
#W celu wysłania zapytania do serwera należy w przeglądarce podać adres localhost:8000.

hostName = "localhost"

serverPort = 8000



#Podczas wysyłania zapytania (localhost:8000) do serwera, metoda generuje stronę html wyświetlaną klientowi, która prezentuje jego adres ip oraz datę.

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)

        self.send_header("Content-type", "text/html")

        self.end_headers()



        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))

        self.wfile.write(bytes("<p>Client data:</p>", "utf-8"))

        self.wfile.write(bytes("<p>Ip address: %s</p>" % socket.gethostbyname(socket.gethostname()), "utf-8"))

        self.wfile.write(bytes("<p>Client local date: %s</p>" % self.date_time_string(), "utf-8"))

        self.wfile.write(bytes("<body>", "utf-8"))

        self.wfile.write(bytes("</body></html>", "utf-8"))



#klasa main uruchamiana przy starcie, startuje serwer i zostawia przygotowane logi

if __name__ == "__main__":        

    webServer = HTTPServer((hostName, serverPort), MyServer)

    print("Server started at: %s"%(datetime.today().strftime('%Y-%m-%d %H:%M:%S')))

    print("Server started by Maciej Rybarczuk")

    print("Server is running on a port %s" % (serverPort))



    try:

        webServer.serve_forever()

    #crtl+c zamyka server

    except KeyboardInterrupt:

        pass



    webServer.server_close()

    print("Server stopped.")