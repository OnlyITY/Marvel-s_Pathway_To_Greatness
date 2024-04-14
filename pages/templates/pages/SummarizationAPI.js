
        ts="35201529" // TimeStamp should we change this?
        // Move this information to a config ?
        apikey="83cba64ddb32d65ba2c813bde03c4044"
        md5_hash="76801623818d7ac2534f4686fa0c13fb"
        
        //fetch('https://gateway.marvel.com:443/v1/public/characters/%s') 
        //.then(response => response.json())
        //.then(data => console.log(data))
        //.catch(error => console.error(error));
        // Search for name=Hulk then print the response text

        async function getCharacterInfo(name, callback) {
            let characterInfo  = await fetch("https://gateway.marvel.com:443/v1/public/characters/%${name}" )
         
            let showcharacterInfo = await characterInfo.json();
            return showcharacterInfo;
        }
        
       async function getCharacterComics(name, callback) {
            let characterComics  = await fetch("https://gateway.marvel.com:443/v1/public/characters/%s/comics " + name )
         
            let showcharacterComics = await characterComics.json();
            return showcharacterComics;
        }

       async function getCharacterEvents(name, callback) {
            let characterEvents  = await fetch("https://gateway.marvel.com:443/v1/public/characters/%s/events${name}" )
         
            let showcharacterEvents = await characterEvents.json();
            return showcharacterEvents;
        }

        async function getComicIssue(issueId, callback) {
            let ComicIssue  = await fetch("https://gateway.marvel.com:443/v1/public/comics/%s${issueId}" )
         
            let showComicIssue = await ComicIssue.json();
            return showComicIssue;
        }

        function ggetCharacterInfo(name) {
            fetch("https://gateway.marvel.com:443/v1/public/characters/%" + name )
            .then(e => e.text())
            
            
            return e;
        }