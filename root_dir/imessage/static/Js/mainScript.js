var reciever
var csrftoken = Cookies.get('csrftoken');
var endpoint = 'ws://' + window.location.host + '/chat/'
var socket = new WebSocket(endpoint)
var webSocketBridge
$(document).ready(function() {
    socket.onmessage = function(e) {
        $('div.msg').append(e.data)
    }
    socket.onopen = function(e) {}
    socket.onerror = function(e) {}
    socket.onclose = function(e) {}
    getMsges($('.msg-head'))
    $('div.msg-head').click(function(e) {
        getMsges($(this))
    })
    $('div.uper-msg-head').click(function(e) {
        getMsges($(this))
    })
    $('.send').click(function(e) {
        $('.msg-input').attr('reciever', reciever)
        var text = $('.msg-input').val()
        sendMsg(reciever, text)
    })
})


function sendMsg(reciever, text) {
    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    $.ajax({
        method: 'POST',
        url: "../send_imessage/",
        data: {
            "reciever": reciever,
            "message": text
        },
        success: function(result) {
            if (result.status == 505) {
                $('.msg-input').css({
                    'border': "1px solid red"
                })
            } else {
                $('.msg').append(result)
                $("div.msg").scrollTop($("div.msg")[0].scrollHeight)
                $('.msg-input').val('')
            }
        }
    })
}

function getMsges(this_) {
    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    reciever = this_.attr('data-id')
    user = this_.attr('data-user')
    $.ajax({
        method: 'POST',
        url: "../chat/",
        data: {
            "reciever": reciever,
            "user": user
        },
        success: function(result) {
            $('.msg-input').val('')
            $('.msg').empty()
            $('.msg').prepend(result)
            $("div.msg").scrollTop($("div.msg")[0].scrollHeight)
        }
    })
}