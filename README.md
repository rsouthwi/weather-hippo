# weather-hippo
_A river horse delivering the weather._

Meet Lustine!  She loves to help, but she can be a little shy.

![](frontend/images/house_open.gif)

## Front End
To run the front end locally, using docker:

* `docker build -t hippo-frontend .`
* `docker run -d -p 3000:80 hippo-frontend`

And you should be able to access the site via a browser by going to [http://localhost:3000](http://localhost:3000)

When you're done:

* `docker stop $(docker ps -q --filter ancestor=hippo-frontend )`