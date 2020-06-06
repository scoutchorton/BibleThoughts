//Cory Gross - https://stackoverflow.com/questions/1144783/how-to-replace-all-occurrences-of-a-string-in-javascript
String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.split(search).join(replacement);
};

//Firebase init
console.clear();
firebase.initializeApp({apiKey:"AIzaSyA_nCeLJUNyXRGfzVXpPGJKUompqG4e1Yc",authDomain:"biblethoughts-7d344.firebaseapp.com",databaseURL:"https://biblethoughts-7d344.firebaseio.com",projectId:"biblethoughts-7d344",storageBucket:"biblethoughts-7d344.appspot.com",messagingSenderId:"65731658950"});

//Variables
function eId(i){return document.getElementById(i)};

	//Variables

	//Functions
	//Firebase management
var db = firebase.database().ref();	//Reference to Firebase database
db.child("/BibleThoughts/admins").on('value',function(adminResponse) {	//Get data from admins and run code on udpate
	db.child('/BibleThoughts/posts/').on('value',function(postsResponse) {	//Get data from posts and run code on update
		var postsData = postsResponse.val();	//Data from posts
		var adminData = adminResponse.val();	//Data from admins
		eId("posts").innerHTML = "";	//Reset HTML inside posts element
		let id = 0	//Start counter for the id of the post
		for(let postData of postsData) {	//Iterate though all posts data (except the first because there is no data), also https://flaviocopes.com/how-to-get-index-in-for-of-loop/
			if(postData) {	//If there is data for that post
				var authorID = Object.keys(postData)[0];	//Get the ID of the author from the post information
				postData = postData[authorID];	//Sets the post data to the data at the ID
				var authorName = adminData[authorID];	//Get the name of the author from the author data
				var postTitle = Object.keys(postData)[0];	//Get the key of the data
				var postContent = postData[postTitle];	//Get the data at the post's title
				let postElement = document.createElement('div');
				postElement.innerHTML = `<div id=\"post-${id}\" class=\"post\"><span>${postTitle}<i onclick="copy(this)" class="material-icons">link</i></span><span>By ${(authorName) ? authorName : "unknown author"}</span><span></span></div>`;	//Gets the HTML for the post using string templates
				postElement.children[0].children[2].innerHTML = postContent
				let afterElemenet = eId("posts").insertBefore(postElement.children[0], (eId("posts").childElementCount)? eId("posts").children[0] : null)
			}
			id += 1;	//Increase the id counter
		}
		if(location.hash){	//If the URL has an id to scroll to
			eId(location.hash.substring(1)).scrollIntoView();	//Scroll to that post's id
		}
	});
});

	//Copy link to clipboard for that post
function copy(element) {
	try {
		location.hash = element.parentElement.parentElement.id;	//Set the hash (id to go to) to the id of the post
		eId('copyme').value = location.href;	//Take advantage of offscreen notification element to set the url to go to
		eId('copyme').select();	//Select the notification
		eId('copyme').setSelectionRange(0,99999);	//Mobile compatability
		document.execCommand('copy');	//Copy the text
		alert('Link copied!');
		eId('copyme').blur();
	} catch(e) {
	}
}
