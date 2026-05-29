async function askAI() {

    const question =
        document.getElementById("question").value;

    document.getElementById(
        "userQuestion"
    ).innerText = question;

    const response = await fetch(
        "/ai-response",
        {
            method: "POST",
            headers: {
                "Content-Type":
                "application/json"
            },
            body: JSON.stringify({
                question: question
            })
        }
    );

    const data =
        await response.json();

    document.getElementById(
        "aiResponse"
    ).innerText =
        data.response;
}