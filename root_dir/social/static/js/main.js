    var search_term
    var csrftoken = Cookies.get('csrftoken');
    var webSocketBridge

    $(document).ready(function() {


        webSocketBridge = new channels.WebSocketBridge();
        webSocketBridge.connect('/notify/');
        webSocketBridge.listen(function(action, stream) {
            if (action.event == "New Like") {
                $('.fa-dot-circle').css({
                    "display": "block"
                })
                $('span.empty').remove()
                $('div.dropdown-menu').prepend(action.html)
            }
        })

        $('.profile-update-input').change(function() {
            $('#form').submit()
        })
        $("html, body").animate({ scrollTop: 0 }, function() {
            $('body').css({ 'overflow': 'hidden' })
        });
        $('.dropzone').on({
            dragover: function(e) {
                e.stopPropagation();
                e.preventDefault();
                $(this).css({
                    "background": "#e6f5e9",
                    "transition": "all ease-in-out 300ms"
                })
                return false;
            },
            dragleave: function(e) {
                e.stopPropagation();
                e.preventDefault();
                $(this).css({
                    "background": "transparent"
                })
                return false;
            },
            drop: function(e) {
                e.stopPropagation();
                e.preventDefault();
                var file = e.originalEvent.dataTransfer.files;
                $("input.file-upload-input").prop("files", e.originalEvent.dataTransfer.files);
                $('label.file-upload').text(file[0]['name'])
                $('.clear-files').css({
                    "display": "block"
                }).click(function(e) {
                    $('label.file-upload').text("Drag Your File Here Or Click To Upload")
                    $(".dropzone").css({
                        "background": "transparent"
                    })
                    $(this).css({
                        "display": "none"
                    })
                })
            }
        })
        $('.q').val('')
        $('[data-toggle="tooltip"]').tooltip()
        $('.notification-container').click(function() {
            window.open($(this).attr("href"));
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
        $('.menu-toggler').click(function() {
            $('div.overlay').fadeToggle(200, function() {
                $('div.side-menu-responsive').toggle(200)
            })
        })
        $('.overlay').click(function() {
            $('div.side-menu-responsive').toggle(200, function() {
                $('div.overlay').fadeToggle(200)
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
                if (window.location.pathname == "/home/bookmarks/") {
                    location.reload();
                }
                $('.container-home').prepend(result)
                $(".alert-success").fadeTo(2000, 500).slideUp(500, function() {
                    $(".alert-success").slideUp(500);
                    $('button.close').click()
                });
            }
        })
    }