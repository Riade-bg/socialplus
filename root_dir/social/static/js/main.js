    var search_term
    var csrftoken = Cookies.get('csrftoken');
    var webSocketBridge
    $(document).ready(function() {
        webSocketBridge = new channels.WebSocketBridge();
        webSocketBridge.connect('/notify/');
        webSocketBridge.listen(function(action, stream) {
            console.log("Response", action.username_who_like);
            if (action.event == "New Like") {
                $('.fa-dot-circle').css({
                    "display": "block"
                })
                $('div.dropdown-menu').prepend(action.html)
            }
        })


        $('.q').val('')
        $('[data-toggle="tooltip"]').tooltip()
        $('.notification-container').click(function() {
            // window.open($(this).attr("href"), '_blank');
            console.log($(this).attr("href"))
        });
        $('.reactions').click(function(e) {
            e.preventDefault()
            var this_ = $(this)
            var likeUrl = this_.attr("data-href")
            var id = parseInt(this_.attr("data-id"))
            getLike(this_, likeUrl, id)
        })
        $(".actions > a").click(function(e) {
            e.preventDefault()
            var this_ = $(this)
            var url = this_.attr("data-url")
            postDelete(this_, url)
        })
        $(".bk").click(function(e) {
            e.preventDefault()
            var this_ = $(this)
            var url = this_.attr("data-url")
            var id = this_.attr("data-id")
            bookmark(this_, url, id)
        })
        $('.cancel-search').click(function(e) {
            $('.q').val('')
            $('.search-results').css({
                'display': "none",
            })
            $(this).css({
                'display': "none",
            })
        })
        $('.q').keyup(function(e) {
            search_term = $(this).val()
            getData();
            if (search_term != '') {
                $('.search-results').css({
                        'display': "block",
                    }),
                    $('.cancel-search').css({
                        'display': "block",
                    })
            } else {
                $('.search-results').css({
                        'display': "none",
                    }),
                    $('.cancel-search').css({
                        'display': "none",
                    })
            }

        });
    })

    function getData() {
        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
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
            url: $('.q').attr('data-url'),
            data: {
                "search_term": search_term
            },
            success: function(result) {
                $('.search-results').empty()
                $('.search-results').append(result)
            }
        })
    }

    function getLike(this_, likeUrl, id) {
        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
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
            url: likeUrl,
            data: {
                "id": id
            },
            success: function(result) {
                this_.find('.counter').text(result)
            }
        })
    }

    function postDelete(this_, delUrl) {
        $.ajax({
            method: 'GET',
            url: delUrl,
            data: {},
            success: function(result) {
                location.reload();
            }
        })
    }

    function bookmark(this_, url, id) {
        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
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
            url: url,
            data: {
                "id": id
            },
            success: function(result) {
                console.log(window.location.pathname)
                if (window.location.pathname == "/home/bookmarks/") {
                    location.reload();
                }
                $('.side-menu').prepend(result)
            }
        })
    }