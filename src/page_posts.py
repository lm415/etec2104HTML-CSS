def get(): return """
<!DOCTYPE html>
<html>
<head>
<style>

div.dialog {
    
    border: 2px double black;
    background: white;
    padding-top: 0em;
    padding-left: 1em;
    padding-right: 1em;
    padding-bottom: 1em;

    /* center the div vertically and horizontally
       ref: https://stackoverflow.com/a/13356401 */
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;

    /* set size of dialog */
    width: 40vw;
    height: 40vh;

    overflow: auto;

    /* offset x, offset y, blur radius, color*/
    box-shadow: 1em 1em 0.5em rgba(0,0,0,0.5);
    
    z-index: 10;
}

.title {
    font-weight: bold;
    text-align: center;
    margin-bottom: 1em;
    background: blue;
    color: white;
    padding: 0.5em;
}
div.Buffer {
    overflow: auto;
    margin-bottom: 4em;
}
div.button {
    padding-top: 1em;
    padding-left: 5em;
    height: 5em;
    background: lightgrey;
    text-align: left;
    position: relative;
    
}

div.button2 {
    padding-top: 1em;
    padding-left: 5em;
    height: 5em;
    background: darkgrey;
    text-align: left;
    position: relative;
    
}

</style>

<div class="dialog">
    <div class="title">Posts</div>
    <div class="button">
    <img src="/html/EMOJI.png" height="64" width="64" style="position: absolute; left: 1em;">Posted(5 days ago) Views(13)
    </button></div>
    <div class="button2"><img src="/html/EMOJI.png" height="64" width="64" style="position: absolute; left: 1em;">Posted(3 days ago) Views(4)
    </button></div>
    <div class="button"><img src="/html/EMOJI.png" height="64" width="64" style="position: absolute; left: 1em;">Posted(14 days ago) Views(54)
    </button></div>
    <div class="button2"><img src="/html/EMOJI.png" height="64" width="64" style="position: absolute; left: 1em;">Posted(43 days ago) Views(0)
    </button></div>
    <div class="button"><img src="/html/EMOJI.png" height="64" width="64" style="position: absolute; left: 1em;">Posted(1 days ago) Views(2)
    </button></div>
    <div class="button2"><img src="/html/EMOJI.png" height="64" width="64" style="position: absolute; left: 1em;">Posted(6 days ago) Views(3)
    </button></div>
    <div class="button"><img src="/html/EMOJI.png" height="64" width="64" style="position: absolute; left: 1em;">Posted(5 days ago) Views(2)
    </button></div>
    <div class="button2"><img src="/html/EMOJI.png" height="64" width="64" style="position: absolute; left: 1em;">Posted(16 days ago) Views(76)
    </button></div>
    <div class="button"><img src="/html/EMOJI.png" height="64" width="64" style="position: absolute; left: 1em;">Posted(12 days ago) Views(5)
    </button></div>
    <div class="button2"><img src="/html/EMOJI.png" height="64" width="64" style="position: absolute; left: 1em;">Posted(18 days ago) Views(32)
    </button></div>
</div>
     
</body>
</html>
""" 