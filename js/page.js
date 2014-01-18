function loadPage(html) {
    $.ajax({
        url: html + " #container",
    }).done(function (data) {
        $("#container").html(data);
    });
};