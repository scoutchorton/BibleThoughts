//Cory Gross - https://stackoverflow.com/questions/1144783/how-to-replace-all-occurrences-of-a-string-in-javascript
String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.split(search).join(replacement);
};

//Firebase init
console.clear();firebase.initializeApp({apiKey:"AIzaSyA_nCeLJUNyXRGfzVXpPGJKUompqG4e1Yc",authDomain:"biblethoughts-7d344.firebaseapp.com",databaseURL:"https://biblethoughts-7d344.firebaseio.com",projectId:"biblethoughts-7d344",storageBucket:"biblethoughts-7d344.appspot.com",messagingSenderId:"65731658950"});

//Variables
var db=firebase.database().ref();
function eId(i){return document.getElementById(i)};
var template="<div id=\"post-?id?\" class=\"post\"><span>?title?</span><span>By ?author?</span><span>?message?</span></div>";

//Functions
db.child("/BibleThoughts/admins").on('value',function(s){/*eId("aData").innerHTML=JSON.stringify(s.val(););*/
	db.child('/BibleThoughts/posts/').on('value',function(z){
		var d=z.val();
		var aD=s.val();
		eId("posts").innerHTML="";
		for(var i=Object.keys(d).length-1;i>=0;i--){
			var pI=Object.keys(d)[i];
			var pD=d[pI];var aI=Object.keys(pD)[0];var aN=aD[aI];var pT=Object.keys(pD[aI])[0];var pC=pD[aI][pT];
			t=template;t=t.replace("?message?",pC);t=t.replace("?id?",Object.keys(d)[i]);t=t.replace("?title?",pT);
			if(aN!==undefined){t=t.replace("?author?",aN);}else{t=t.replace("?author?","unknown author")}
			eId("posts").innerHTML+=t;
		}
		if(location.href.indexOf('#')>-1){
			eId(location.href.split('#')[1]).scrollIntoView();
		}
	});
});
