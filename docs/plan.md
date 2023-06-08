## A plan
This project is to convert my old [TechSpandex Skills Assessment](https://github.com/rsouthwi/Fool-Me) to something
more contemporary.  This project was initially written in PHP.  I'd like to convert it to something where I get to 
experiment with Terraform, AWS Lambda, S3, and API Gateway.

## Steps
* recreate the html interface including:
  * html and styles to display the house
  * a form to accept location (or postalcode)
  * javascript to reach out to an api
  * stubs to test
* build an api interface to get the weather
  * this should be a Lambda behind API Gateway
  * this should be a GET endpoint
  * that only accepts requests from the ronsouthwick.com domain
  * api endpoint:
     * https://api.weatherapi.com/v1/current.json?key={api_key}&q={city or zip}&aqi=no
     * api_key available by logging into https://www.weatherapi.com/my/
     * https://www.weatherapi.com/docs/conditions.json
* use terraform to provision and deploy the resources