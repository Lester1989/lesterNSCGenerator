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

.tree * {margin: 0; padding: 0;}

.tree ul {
	padding-top: 20px; position: relative;
	
	transition: all 0.5s;
	-webkit-transition: all 0.5s;
	-moz-transition: all 0.5s;
}

.tree li {
	float: left; text-align: center;
	list-style-type: none;
	position: relative;
	padding: 20px 5px 0 5px;
	
	transition: all 0.5s;
	-webkit-transition: all 0.5s;
	-moz-transition: all 0.5s;
}

.tree li::before, .tree li::after{
	content: '';
	position: absolute; top: 0; right: 50%;
	border-top: 1px solid #ccc;
	width: 50%; height: 20px;
}
.tree li::after{
	right: auto; left: 50%;
	border-left: 1px solid #ccc;
}

.tree li:only-child::after, .tree li:only-child::before {
	display: none;
}

.tree li:only-child{ padding-top: 0;}

.tree li:first-child::before, .tree li:last-child::after{
	border: 0 none;
}

.tree li:last-child::before{
	border-right: 1px solid #ccc;
	border-radius: 0 5px 0 0;
	-webkit-border-radius: 0 5px 0 0;
	-moz-border-radius: 0 5px 0 0;
}

.tree li:first-child::after{
	border-radius: 5px 0 0 0;
	-webkit-border-radius: 5px 0 0 0;
	-moz-border-radius: 5px 0 0 0;
}

.tree ul ul::before{
	content: '';
	position: absolute; top: 0; left: 50%;
	border-left: 1px solid #ccc;
	width: 0; height: 20px;
}

.tree li a{
	border: 1px solid #ccc;
	padding: 5px 10px;
	text-decoration: none;
	color: #666;
	font-family: arial, verdana, tahoma;
	font-size: 11px;
	display: inline-block;
	
	border-radius: 5px;
	-webkit-border-radius: 5px;
	-moz-border-radius: 5px;
	
	transition: all 0.5s;
	-webkit-transition: all 0.5s;
	-moz-transition: all 0.5s;
}

.tree li a:hover, .tree li a:hover+ul li a {
	background: #c8e4f8; color: #000; border: 1px solid #94a0b4;
}

.tree li a:hover+ul li::after, 
.tree li a:hover+ul li::before, 
.tree li a:hover+ul::before, 
.tree li a:hover+ul ul::before{
	border-color:  #94a0b4;
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