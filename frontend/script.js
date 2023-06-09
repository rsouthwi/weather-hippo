let hippoStatus = "in";

const toggleHippo = () => {
    if (hippoStatus === "moving") return;
    hippoStatus = "moving";
    const house = document.getElementById("house");
    const speechBubble = document.getElementById("bubble");
    if (!house.src.includes("_open")) {
        house.src = "images/house_open.gif";
        speechBubble.innerHTML = "<p>The weather in Alexandria is smokey!</p>\n<p>It's 75&deg;F out here!</p>"
        setTimeout(()=> speechBubble.classList.add("load"), 5000);
        setTimeout(()=> hippoStatus = "out", 5000);
    } else {
        house.src = "images/house_close.gif";
        speechBubble.classList.remove("load");
        setTimeout(()=> hippoStatus = "in", 5000);
    }
};
