->Capture Filter
     host facebook.com and tcp
     host facebook.com and port 443 (using first, Display Filter: tcp.port == 443)
->Display Filter
     tcp.flags.syn == 1 || tcp.flags.push == 1 || tcp.flags.reset == 1
     tcp.port == 443


--> Statistics --> Capture File properties

http://www.testingmcafeesites.com/

https://www.studocu.com/in/messages/question/4043513/capture-packets-using-wireshark-write-the-exact-packet-capture-filter-expressions-to-accomplish-the
----------------

ssl.handshake.type == 1 (client hello)
ssl.handshake.type == 2 (server hello)
ssl.handshake.type == 16 (client key exchange)
ssl.record.content_type == 21 (alert)



THEORY:
     SYN and RST: It's unusual to see a packet both initiating a connection (SYN) and resetting it (RST) simultaneously.

    SYN and PSH: A SYN packet is typically part of the connection initiation process, and it doesn't usually contain application data (PSH).

    PSH and RST: It's unusual to have a packet both pushing data to the application (PSH) and resetting the connection (RST) at the same time.
