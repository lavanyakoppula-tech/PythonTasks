async function askBot(){

    let question =
    document.getElementById("question").value;

    if(question.trim()==="")
    {
        return;
    }

    let chatBox =
    document.getElementById("chat-box");

    chatBox.innerHTML +=
    `<div class="user">
        👤 ${question}
    </div>`;

    let response =
    await fetch("/ask",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            question:question
        })

    });

    let data =
    await response.json();

    chatBox.innerHTML +=
    `<div class="bot">
        🤖 ${data.response}
    </div>`;

    document.getElementById("question").value="";

    chatBox.scrollTop =
    chatBox.scrollHeight;
}