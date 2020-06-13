$(function () {
    "use strict";
    // for better performance - to avoid searching in DOM
    var content = $('#content');
    var input = $('#input');
    var status = $('#status');

    // if user is running mozilla then use it's built-in WebSocket
    window.WebSocket = window.WebSocket || window.MozWebSocket;
    // if browser doesn't support WebSocket, just show
    // some notification and exit
    if (!window.WebSocket) {
      content.html($('<p>',
        { text:'Sorry, but your browser doesn\'t support WebSocket.'}
      ));
      input.hide();
      $('span').hide();
      return;
    }
    // open connection
    var connection = new WebSocket('ws://192.168.168.101:8085');
    connection.onerror = function (error) {
      // just in there were some problems with connection...
      content.html($('<p>', {
        text: 'Sorry, but there\'s some problem with your '
           + 'connection or the server is down.'
      }));
    };
    var up = document.getElementById('btn up');
    var down= document.getElementById('btn down');
    var left= document.getElementById('btn left');
    var right= document.getElementById('btn right');
    var stop= document.getElementById('btn stop');

    //add event listener
    up.addEventListener('click', function() {
        connection.send(JSON.stringify({"val": "tiltFrontDown", "type": "controlSig"}))
    });

    down.addEventListener('click', function(event) {
        connection.send(JSON.stringify({"val": "tiltBackDown", "type": "controlSig"}))
      });

    left.addEventListener('click', function(event) {
        connection.send(JSON.stringify({"val": "panLeftDown", "type": "controlSig"}))
    });
    right.addEventListener('click', function(event) {
      connection.send(JSON.stringify({"val": "panRightDown", "type": "controlSig"}))
    });
    stop.addEventListener('click', function(event) {
      connection.send(JSON.stringify({"val": "stop", "type": "controlSig"}))
    });
 
    // // most important part - incoming messages
    // connection.onmessage = function (message) {
    //   // try to parse JSON message. Because we know that the server
    //   // always returns JSON this should work without any problem but
    //   // we should make sure that the massage is not chunked or
    //   // otherwise damaged.
    //   try {
    //     var json = JSON.parse(message);
    //   } catch (e) {
    //     console.log('Invalid JSON: ', message);
    //     return;
    //   }
    //   // NOTE: if you're not sure about the JSON structure
    //   // check the server source code above
    //   // first response from the server with user's color
		// console.log(msg);
    //   if (json.type === 'controlSig') { 
    //     status.text('Sending command');
    //     // from now user can start sending messages
    //   } else if (json.type === 'chat') { // entire message history
    //     // insert every single message to the chat window
    //     status.text('Chat');
    //   } else {
    //     console.log('Hmm..., I\'ve never seen JSON like this:', json);
    //   }
    // };


    // /**
    //  * Send message when user presses Enter key
    //  */
    // input.keydown(function(e) {
    //   if (e.keyCode === 13) {
    //     var msg = $(this).val();
    //     if (!msg) {
    //       return;
    //     }
    //     // send the message as an ordinary text
    //     connection.send(msg);
    //     $(this).val('');
    //     // disable the input field to make the user wait until server
    //     // sends back response
    //     input.attr('disabled', 'disabled');
    //     // we know that the first message sent from a user their name
    //     if (myName === false) {
    //       myName = msg;
    //     }
    //   }
    // });

    /**
     * This method is optional. If the server wasn't able to
     * respond to the in 3 seconds then show some error message 
     * to notify the user that something is wrong.
     */
    setInterval(function() {
      if (connection.readyState !== 1) {
        status.text('Error');
        input.attr('disabled', 'disabled').val(
            'Unable to communicate with the WebSocket server.');
      }
    }, 3000);

  });