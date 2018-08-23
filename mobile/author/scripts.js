//Tools
function eId(i){return document.getElementById(i)};
//Web App Links
window.onload=function(){
	var a=document.getElementsByTagName("a");
	for(var i=0;i<a.length;i++){
		if(!a[i].onclick&&a[i].getAttribute("target")!="_blank"){
			a[i].onclick=function(){
				window.location=this.getAttribute("href");
				return false;
			}
		}
	}
	eId('logout').addEventListener('click',function(){
		firebase.auth().signOut();
	});
}
// Initialize Firebase
console.clear();firebase.initializeApp({apiKey:"AIzaSyA_nCeLJUNyXRGfzVXpPGJKUompqG4e1Yc",authDomain:"biblethoughts-7d344.firebaseapp.com",databaseURL:"https://biblethoughts-7d344.firebaseio.com",projectId:"biblethoughts-7d344",storageBucket:"biblethoughts-7d344.appspot.com",messagingSenderId:"65731658950"});
var db=firebase.database().ref();
//Functions
function setFrame(addr){eId('wkspFrame').src=addr;document.getElementById('nav').classList.remove('onscreen')}
function greet(){firebase.auth().onAuthStateChanged(function(user){if(user){eId('top').childNodes[2].innerHTML=eId('top').childNodes[2].innerHTML.replace("?user?",user.displayName);}});};
