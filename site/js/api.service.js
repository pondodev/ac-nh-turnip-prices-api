const BASE = "/api"

$(document).ready(() => {
    let _userId = sessionStorage.getItem("userId");
    let url = window.location.href.split('/');
    if (_userId == null && url[url.length - 1] != "login") { // user not logged in
        window.location.href = "/login";
    } else if (_userId != null) { // user logged in
        $.ajax({
            type: "GET",
            url: `${BASE}/User`,
            data: {
                userId: _userId
            },
            success: (res) => {
                $("#user-welcome").text(res.username);
            },
            error: (e) => {
                $("#user-welcome").text("name not found");
                console.log(`${e.status} error: ${e.statusText}`, e);
            }
        });
    }
});

function LoginUser() {
    _username = $("#login-username").val();
    let toPost = {
        username: _username
    };

    $.ajax({
        type: "POST",
        url: `${BASE}/Login`,
        data: JSON.stringify(toPost),
        contentType: "application/json",
        processData: false,
        success: (res) => {
            // set session and redirect to index
            sessionStorage.setItem("userId", res.userId);
            window.location.href = "/";
        },
        error: (e) => {
            console.log(`${e.status} error: ${e.statusText}`, e);
            alert("uh oh something went wrong that's not good");
        }
    });
}

function SignUpUser() {
    _username = $("#signup-username").val();
    let toPost = {
        username: _username
    };

    $.ajax({
        type: "POST",
        url: `${BASE}/User`,
        data: JSON.stringify(toPost),
        contentType: "application/json",
        processData: false,
        success: (res) => {
            // set session and redirect to index
            sessionStorage.setItem("userId", res.userId);
            window.location.href = "/";
        },
        error: (e) => {
            console.log(`${e.status} error: ${e.statusText}`, e);
        }
    });
}