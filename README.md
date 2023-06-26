# weather-hippo
_A river horse delivering the weather._

Meet Lustine!  She loves to help, but she can be a little shy.

![](frontend/images/house_open.gif)

I originally created this app in PHP as the "skills assessment" portion of my interview to join the Motley Fool.  
The challenge was to create some sort of front-end interface that allowed a user to input a location, send that location
to some weather api and return the result.  My concept was a "digital [weather rock](https://en.wikipedia.org/wiki/Weather_rock)"
that only reported the current state of the weather (rather than a forecast or anything more useful), using an animation
of Lustine, a cartoon character I created for my young daughter, to deliver the news.
I have since decided to revisit this and rewrite it as opportunity to learn about Docker and Terraform while introducing
Lustine on my website (coming soon!)

## Front End
To run the front end locally, using docker:

* `docker build -t hippo-frontend .`
* `docker run -d -p 3000:80 hippo-frontend`

And you should be able to access the site via a browser by going to [http://localhost:3000](http://localhost:3000)

When you're done:

* `docker stop $(docker ps -q --filter ancestor=hippo-frontend )`

## Back End
[See backend documentation](weather-api/README.md).