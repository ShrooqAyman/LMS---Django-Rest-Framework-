function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// Use csrf token while doing post request, this will prevent 500 Server Error
$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


$.ajax({
    url: "http://127.0.0.1:8000/customer/api/UserIssueAPI/",
    dataType: "json",
    success: function(response) {

        let trHTML = '';
        $.each(response, function(i, item) {
            trHTML += `<tr>
            <td><strong>` + item.slug + `</strong></td>
            <td>` + item.book + `</td>
            <td> 
            <button class='btn btn-success update btn-sm' id ="` + item.id + `" data-toggle='modal' data-target=''>Issue</button> 
           </td>
           
          </tr>`;

        });
        $('#myIssues').append(trHTML);
    },

});
//All Books API

$.ajax({
    url: "http://127.0.0.1:8000/library/api/Books/",
    dataType: "json",
    success: function(response) {
        let trHTML = '';
        $.each(response, function(i, item) {
            trHTML += `<tr>
            <td><strong>` + item.isbn + `</strong></td>
            <td>` + item.title + `</td>
            <td>` + item.author + `</td>
            <td><span class="badge bg-label-primary me-1">` + item.status + `</span></td>
           
            <td> 
            <button class='btn btn-success update btn-sm' id ="` + item.id + `" data-toggle='modal' data-target='#editBookModal'>Update</button> 
            <button class='btn btn-danger btn-sm delete' id ="` + item.id + `" data-toggle='modal' data-target='#deleteProduct'>Delete</button>
           </td>
           
          </tr>`;

        });
        $('#Book-Records').append(trHTML);
    }

});


$.ajax({
    url: "http://127.0.0.1:8000/library/api/Books/",
    dataType: "json",
    success: function(response) {
        let trHTML = '';
        $.each(response, function(i, item) {
            trHTML += `<tr>
            <td><strong>` + item.isbn + `</strong></td>
            <td>` + item.title + `</td>
            <td>` + item.author + `</td>
            <td><span class="badge bg-label-primary me-1">` + item.status + `</span></td>
          </tr>`;

        });
        $('#booksTable').append(trHTML);
    }
});
$.ajax({
    url: "http://127.0.0.1:8000/customer/api/UserAPI/",
    dataType: "json",
    success: function(response) {
        let trHTML = '';
        $.each(response, function(i, item) {
            trHTML += `<tr>
            <td>` + item.username + `</td>
            <td>` + item.email + `</td>
          </tr>`;

        });
        $('#customers').append(trHTML);
    }
});
// fill category select input
$('#create').click(function() {
    $("#add-Book").trigger('reset');

    $.ajax({
        url: "http://127.0.0.1:8000/library/api/Categorys/",
        dataType: "json",
        success: function(response) {
            let trHTML = '';
            $.each(response, function(i, item) {
                trHTML += `<option value="` + item.id + `">` + item.name + `</option>`;

            });
            $('#category').append(trHTML);
        },

    });
    $.ajax({
        url: "http://127.0.0.1:8000/library/api/shelfs/",
        dataType: "json",
        success: function(response) {
            let trHTML = '';
            $.each(response, function(i, item) {
                trHTML += `<option value="` + item.id + `">` + item.name + `</option>`;

            });
            $('#shelf').append(trHTML);
        },

    });

});

//Save New Book Button
$(function() {
    $('#addBook').on('submit', function(e) {



        e.preventDefault();

        let myurl = "http://localhost:8000/library/api/Books/add/";

        $.ajax({
            type: 'POST',
            url: myurl,
            data: $("#addBook :input").serializeArray(),
            dataType: "json",
            success: function(data) {
                alert("Book Added!");
                console.log(data);

                //location.reload();
            },
            error: function(data) {
                alert("Book Not Added!");

                console.log(data);
                //location.reload();
            }
        });
    });
});

//Edit Books API
$('#Book-Records').on('click', '.update', function(e) {

    e.preventDefault();
    $.ajax({
        url: "http://127.0.0.1:8000/library/api/Categorys/",
        dataType: "json",
        success: function(response) {
            let trHTML = '';
            $.each(response, function(i, item) {
                trHTML += `<option value="` + item.id + `">` + item.name + `</option>`;

            });
            $('#category').append(trHTML);
        },

    });
    $.ajax({
        url: "http://127.0.0.1:8000/library/api/shelfs/",
        dataType: "json",
        success: function(response) {
            let trHTML = '';
            $.each(response, function(i, item) {
                trHTML += `<option value="` + item.id + `">` + item.name + `</option>`;

            });
            $('#shelf').append(trHTML);
        },

    });
    let id = $(this).attr('id');
    $('input[id=Myid]').val(id);

    let myurl = "http://localhost:8000/library/api/Books/" + id + "/";

    $("#title").change(function() {
        $('input[name=title]').val($(this).val());
    });
    $("#category").change(function() {
        $('select[name=category]').val($(this).val());
    });
    $("#status").change(function() {
        $('select[name=status]').val($(this).val());
    });


    $.ajax({
        async: true,
        url: myurl,
        method: 'GET',
        success: function(result) {
            $('input[name="title"]').val(result.title);
            $('select[name="category"]').val(result.category);
            $('select[name=status]').val(result.status);
        }
    });

});

//Save Edited Book Button
$(function() {
    $('#editBook').on('submit', function(e) {
        e.preventDefault();

        let id = $("#Myid").attr("value");
        console.log(id);

        let myurl = "http://localhost:8000/library/api/Books/edit/" + id + "/";

        $.ajax({
            type: 'PUT',
            url: myurl,
            data: $("#editBook :input").serializeArray(),
            dataType: "json",
            success: function(data) {
                alert("Book Updated!");
                //location.reload();
            },
            error: function(data) {
                alert("Book Not Updated!");
                //location.reload();
            }
        });
    });
});

//Delete Books API
$('#Book-Records').on('click', ".delete", function(e) {
    e.preventDefault();

    let id = $(this).attr('id');
    $('input[id=Myid]').val(id);
    console.log(id)

    let myurl = "http://localhost:8000/library/api/Books/" + id + "/";

    $.ajax({
        async: true,
        url: myurl,
        method: 'GET',
        success: function(result) {
            $('input[name="id"]').val(result.id);
        }
    });

});

//Save Delete Books Button
$(function() {
    $('#deleteBook').on('submit', function(e) {
        e.preventDefault();

        let id = $("#Myid").attr("value");
        console.log(id);

        let myurl = "http://localhost:8000/library/api/Books/delete/" + id + "/";

        $.ajax({
            async: true,
            url: myurl,
            method: 'DELETE',
            success: function(result) {
                location.reload();
            },
            error: function(result) {
                alert("Book Not Deleted!");
                location.reload();
            }
        });

    });
});

//fill shelf table
$.ajax({
    url: "http://127.0.0.1:8000/library/api/shelfs/",
    dataType: "json",
    success: function(response) {
        let trHTML = '';
        $.each(response, function(i, item) {
            trHTML += `<tr>
            <td><strong>` + item.slug + `</strong></td>
            <td>` + item.name + `</td>
           
            <td> 
            <button class='btn btn-success update btn-sm' id ="` + item.id + `" data-toggle='modal' data-target='#EditShelfModal'>Update</button> 
            <button class='btn btn-danger btn-sm delete' id ="` + item.id + `" data-toggle='modal' data-target='#deleteShelfModal'>Delete</button>
           </td>
           
          </tr>`;

        });
        $('#shelfs-Records').append(trHTML);
    },

});

$('#createShelf').click(function() {
    $("#addSelf").trigger('reset');

});

//Save New shelf Button
$(function() {
    $('#addShelf').on('submit', function(e) {
        e.preventDefault();

        let myurl = "http://localhost:8000/library/api/shelf/add/";

        $.ajax({
            type: 'POST',
            url: myurl,
            data: $("#addShelf :input").serializeArray(),
            dataType: "json",
            success: function(data) {
                alert("Shelf Added!");
                console.log(data);
                location.reload();
            },
            error: function(data) {
                alert("Shelf Not Added!");
                console.log(data);
                location.reload();
            }
        });
    });
});

//Edit shelf API
$('#shelfs-Records').on('click', '.update', function(e) {

    e.preventDefault();

    let id = $(this).attr('id');
    $('input[id=Myid]').val(id);

    let myurl = "http://localhost:8000/library/api/shelf/" + id + "/";

    $("#name").change(function() {
        $('input[name=name]').val($(this).val());
    });
    $("#slug").change(function() {
        $('input[name=slug]').val($(this).val());
    });



    $.ajax({
        async: true,
        url: myurl,
        method: 'GET',
        success: function(result) {
            $('input[name="name"]').val(result.name);
            $('input[name="slug"]').val(result.slug);

        }
    });

});

//Save Edited shelf Button
$(function() {
    $('#editShelf').on('submit', function(e) {
        e.preventDefault();

        let id = $("#Myid").attr("value");

        let myurl = "http://localhost:8000/library/api/shelf/edit/" + id + "/";

        $.ajax({
            type: 'PUT',
            url: myurl,
            data: $("#editShelf :input").serializeArray(),
            dataType: "json",
            success: function(data) {
                alert("shelf Updated!");
                location.reload();
            },
            error: function(data) {
                alert("shelf Not Updated!");
                location.reload();
            }
        });
    });
});

// delete shelf
$('#shelfs-Records').on('click', ".delete", function(e) {
    e.preventDefault();

    let id = $(this).attr('id');
    $('input[id=Myid]').val(id);
    console.log(id)

    let myurl = "http://localhost:8000/library/api/shelf/" + id + "/";

    $.ajax({
        async: true,
        url: myurl,
        method: 'GET',
        success: function(result) {
            $('input[name="id"]').val(result.id);
        }
    });

});

// save delete shelf
$(function() {
    $('#deleteShelf').on('submit', function(e) {
        e.preventDefault();

        let id = $("#Myid").attr("value");
        console.log(id);

        let myurl = "http://localhost:8000/library/api/shelf/delete/" + id + "/";

        $.ajax({
            async: true,
            url: myurl,
            method: 'DELETE',
            success: function(result) {
                location.reload();
            },
            error: function(result) {
                alert("Shelf Not Deleted!");
                location.reload();
            }
        });

    });
});

// fill category table
$.ajax({
    url: "http://127.0.0.1:8000/library/api/Categorys/",
    dataType: "json",
    success: function(response) {
        let trHTML = '';
        $.each(response, function(i, item) {
            trHTML += `<tr>
            <td><strong>` + item.slug + `</strong></td>
            <td>` + item.name + `</td>
           
            <td> 
            <button class='btn btn-success update btn-sm' id ="` + item.id + `" data-toggle='modal' data-target='#editProduct'>Update</button> 
            <button class='btn btn-danger btn-sm delete' id ="` + item.id + `" data-toggle='modal' data-target='#deleteProduct'>Delete</button>
           </td>
           
          </tr>`;

        });
        $('#category-Records').append(trHTML);
    },

});

$('#createCategory').click(function() {
    $("#addCategory").trigger('reset');

});

//Save New Category
$(function() {
    $('#addCategory').on('submit', function(e) {
        e.preventDefault();

        let myurl = "http://localhost:8000/library/api/Category/add/";

        $.ajax({
            type: 'POST',
            url: myurl,
            data: $("#addCategory :input").serializeArray(),
            dataType: "json",
            success: function(data) {
                alert("Category Added!");
                location.reload();
            },
            error: function(data) {
                alert("Category Not Added!");
                location.reload();
            }
        });
    });
});

// register
$(function() {
    $('#register').on('submit', function(e) {
        e.preventDefault();
        let myurl = "http://localhost:8000/api/register/";
        $.ajax({
            type: 'POST',
            url: myurl,
            data: $("#register :input").serializeArray(),
            dataType: "json",
            success: function(data) {
                alert("User Added!");
                window.location.href = "http://localhost:8000/login";
            },
            error: function(data) {
                alert("User Not Added!");
            }
        });
    });
});

// login
$(function() {
    $('#login').on('submit', function(e) {
        e.preventDefault();
        let myurl = "http://localhost:8000/api/login/";
        $.ajax({
            type: 'POST',
            url: myurl,
            data: $("#login :input").serializeArray(),
            dataType: "json",
            success: function(data) {
                alert("User login!");
                window.location.href = "http://localhost:8000/dashboard";
            },
            error: function(data) {
                alert("User Not login!");
            }
        });
    });
});

// fill book in select input
$.ajax({
    url: "http://127.0.0.1:8000/library/api/Books/",

    dataType: "json",
    success: function(response) {
        let trHTML = '';
        $.each(response, function(i, item) {
            trHTML += `<option value="` + item.id + `">` + item.title + `</option>`;
        });
        $('#books').append(trHTML);
    },

});

// fill username in select input
$.ajax({
    url: "http://127.0.0.1:8000/issues/api/users/",

    dataType: "json",
    success: function(response) {
        let trHTML = '';
        $.each(response, function(i, item) {
            trHTML += `<option value="` + item.id + `">` + item.username + `</option>`;

        });
        $('#username').append(trHTML);
    },

});

//create issue
$(function() {
    $('#issue').on('submit', function(e) {
        e.preventDefault();

        let myurl = "http://localhost:8000/issues/api/issue/add/";

        $.ajax({
            type: 'POST',
            url: myurl,
            data: $("#issue :input").serializeArray(),
            dataType: "json",
            success: function(data) {
                alert("issue created!");
            },
            error: function(data) {
                alert("issue Not created!");
            }
        });
    });
});