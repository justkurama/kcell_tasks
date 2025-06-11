$(document).ready(function () {
    $("#createForm").submit(function (e) {
        e.preventDefault();
        $.post("/create", $(this).serialize(), function () {
            location.reload();  // можно заменить на динамическое обновление
        });
    });

    $(".resolveBtn").click(function () {
        const li = $(this).closest("li");
        const id = li.data("id");
        $.post(`/resolve/${id}`, function () {
            li.html(`<strong>${li.find("strong").text()}</strong> — resolved`);
        });
    });
});
