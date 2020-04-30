const HTTP = new XMLHttpRequest();
const BASE = `${window.location.hostname}/api`

function test() {
    console.log(BASE)
    $.get(`${BASE}/AllUsers`, (res, status) => {
        console.log("res: ", res);
        console.log("status: ", status);
    });
}

$(document).ready(() => {
    $.ajax({
        url: "/api/AllUsers",
        success: () => {
            console.log("done")
        },
        error: (e) => {
            console.log("something went wrong: ", e)
        }
    });
});