let hippoStatus = "in";

const getWeatherData = (location) => {
    const url = "https://www.ronsouthwick.com/weather-api";
    const payload = {"location": location};
    const headers = {"Content-type": "application/json", "host": "ronsouthwick.com"};

    fetch(url, {method: 'POST', body: JSON.stringify(payload), headers: headers})
        .then(response => {
            if (response.status === 400) throw Error("I couldn't find");
            else if (!response.ok) throw Error("I think something's wrong. Sorry.");
            return response.json()
        })
        .then(data => populateSpeechBubble(data))
        .catch(error => {
            if (!error.message.includes("couldn't find")) location = "";
            populateSpeechBubble( {error: error.message, location: location} );
        });
    toggleHippo();
}

const setWeatherImage = (condition = null) => {
    const container = document.querySelector("#container");
    if (condition)  container.style.backgroundImage = `url("images/${condition}.gif")`;
    else container.style.background = "";
}

const populateSpeechBubble = (payload) => {
    const speechBubble = document.getElementById("bubble");
    const {condition, location, temperature, error} = payload;
    let message = `<p>Hmmm... ${error} ${location}</p>`;
    if (!error) {
        message = `<p>The weather in ${location} is ${condition}!</p>\n<p>It's ${temperature}&deg;F out here!</p>`;
        setWeatherImage(condition);
    }
    speechBubble.innerHTML = message;
    setTimeout(()=> speechBubble.classList.add("load"), 5000);
}

const toggleHippo = () => {
    if (hippoStatus === "moving") return;
    hippoStatus = "moving";
    const house = document.getElementById("house");

    if (!house.src.includes("_open")) {
        house.src = "images/house_open.gif";
        setTimeout(()=> hippoStatus = "out", 5000);
    } else {
        const speechBubble = document.getElementById("bubble");
        house.src = "images/house_close.gif";
        speechBubble.classList.remove("load");
        setTimeout(()=> hippoStatus = "in", 5000);
    }
};

const hippoGoesIn = () => {
    if (hippoStatus === "out") toggleHippo();
    else if (hippoStatus === "moving") setTimeout(hippoGoesIn, 1000);
};

const hippoComesOut = () => {
    if (hippoStatus === "in") {
        const locationInput = document.querySelector("#loc");
        const location = locationInput.value;
        locationInput.blur();
        getWeatherData(location);
    } else if (hippoStatus === "moving") setTimeout(hippoComesOut, 1000);
}

const registerEvents = (event) => {
    const locationInput = document.querySelector("#loc");
    locationInput.addEventListener("focus", hippoGoesIn);

    const form = document.querySelector('form');
    form.addEventListener("submit", (event => {
        event.preventDefault();
        hippoComesOut();
    }))
};

window.addEventListener("DOMContentLoaded", registerEvents);