const button = document.getElementById("graph");
button.addEventListener("click", e => {
    document.getElementById("img").src = "";
    const fx = document.getElementById("Fx").value;
    const fy = document.getElementById("Fy").value;
    const skip = 2;
    const url = "https://vector-field.herokuapp.com/?fx=" + fx + "&fy=" + fy + "&skip=" + skip;
    console.log(url);
    document.getElementById("img").src = url;
});
