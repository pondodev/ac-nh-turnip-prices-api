const BASE = "/api"

$(document).ready(() => {
    let _userId = sessionStorage.getItem("userId");
    if (_userId == null) {
        // TODO: goto login page
    } else {
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