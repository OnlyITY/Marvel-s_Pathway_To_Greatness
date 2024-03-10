
const express = require("express");
const path = require("path");

const app = express();
const server = require("http").createServer(app);

app.use(express.static(path.join(__dirname+"jsonstuff")))

io.on("connection", function(socket){
    socket.on("newUser", function(Username){
        socket.broadcast.emit("update", Username + "joined the conversation");
    });

    socket.on("exitiser", function(Username){
        socket.broadcast.emit("update", Username + "exited the conversation");
    });

    socket.on("chat", function(message){
        socket.broadcast.emit("chat", message);
    });
});

server.listen(5000);