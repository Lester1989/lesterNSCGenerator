
basePath = '/var/www/FlaskApp'
baseURL = 'http://v22018117165076045.happysrv.de'



feedbackLoginCode = 'lesterliestfeedbacks'


headerPart ='''
<!DOCTYPE html>
<html>
<head>
<style>
body {
    background-color: whitesmoke;
    font-family:"Garamond";
    font-weight:500;
    padding: 15px;
    text-align: justify;
}
h1   {
    font-family:"Balthazar";
    font-size: 48px;
    text-shadow: 2px 2px 2px #AAAAAA;
    text-align:center;
}
h2   { font-family:"Balthazar";font-size: 36px;}
h3   { font-family:"Garamond"; color: darkred;font-variant: small-caps;border-top: 2px solid darkred;}
h4   { font-family:"Garamond"; color: darkred;font-variant: small-caps;border-top: 2px solid darkred;}
hr   { border: none; background: darkred; height:2px;}
div {border-style: none; padding:5px;}
a {
    font-weight:400;
}
a:hover{
    font-weight:800;
}
.button {
  display: inline-block;
  border-radius: 4px;
  background-color: darkred;
  border: none;
  color: #FFFFFF;
  text-align: center;
  font-size: 28px;
  padding: 20px;
  width: 250px;
  transition: all 0.5s;
  cursor: pointer;
  margin: 5px;
}

.button span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
}

.button span:after {
  content: '  >>';
  position: absolute;
  opacity: 0;
  top: 0;
  right: 0px;
  transition: 0.5s;
}

.button:hover span {
  padding-right: 25px;
}

.button:hover span:after {
  opacity: 1;
  right: 0;
}

.sidenav {
  height: 100%;
  width: 320px;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: whitesmoke;
  border-right: solid 4px darkred;
  overflow-x: hidden;
  padding-top: 00px;
}
.sidenav a {
  display: block;
  color: black;
  padding: 10px;
  text-decoration: none;
}

.sidenav a.active {
  background-color: darkred;
  color: white;
  font-weight:500;
}

.sidenav a:hover:not(.active) {
  background-color: #555;
  color: white;
  font-weight:400;
}
.sidenav a.mailTo {
  display: inline;
  color: black;
  padding: 0px;
  text-decoration: none;
}

div.content {
  margin-left: 320px;
  padding: 1px 16px;
}

@media screen and (max-width: 700px) {
  .sidenav {
    width: 100%;
    height: auto;
    position: relative;
    border-right: none;
    border-bottom: solid 4px darkred;
  }
  .sidenav a {float: left;}
  div.content {margin-left: 0;}

  .sidenav h4 {display:none;}
  .sidenav hr {display:none;}
  .sidenav p {display:none;}
  .sidenav img {display:none;}
}

@media screen and (max-width: 400px) {
  .sidenav {
    border-right: none;
    border-bottom: solid 4px darkred;
  }
  .sidenav a {
    text-align: center;
    float: none;
  }
  .sidenav h4 {display:none;}
  .sidenav hr {display:none;}
  .sidenav p {display:none;}
  .sidenav img {display:none;}
}
@media print
{

    body {margin: 0mm;}

    div.content {
        margin: 0;
    }

    body {
        background-color: white;
    }

    .no-print, .no-print *
    {
        display: none !important;
    }
}
</style>
</head>
'''
