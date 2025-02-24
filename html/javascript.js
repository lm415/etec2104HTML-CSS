console.log("JavaScript loaded!");

function foo()
{
    console.log("Button clicked!");
    let email = document.getElementById("email").value;
    if (!email.includes("@"))
    {
        alert("Bad email!");
        return;
    }
    let emailCheck = email.split("@");

    if (emailCheck[0].length < 1)
    {
        alert("Bad email!");
        return;
    }

    if (emailCheck[1].length < 1)
        {
            alert("Bad email!");
            return;
        }
    
    alert("Account made!")
}