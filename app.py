from flask import Flask, render_template_string, request, jsonify, g, redirect


app = Flask(__name__)



@app.route('/currentStock',methods=['GET'])
def currentStock():
    html = """
<meta  name='viewport' content='width=device-width, initial-scale=0.8, shrink-to-fit=yes'>
<body style="background-color:#131316"></body>

<style>
  .back-box {
    border-radius: 15px;
    background: rgb(61, 145, 255);
    height:250;
    width: 220;
    display:inline-block;  
    margin-top:10px;
    margin-bottom:10px;
    margin-left: 4px;
    margin-right: 4px;
  }
  img {
    border-radius: 15px;
    display: inline-block;
    background-color: transparent;
    margin-top:10px;
    margin-bottom:10px;     
  }

  .main-div{
    text-align: center;
    display: inline-block;
    transition: all .50s linear;
  }
  .caption{
    font-size: 1em;
    color:white;
    font-family: 'Rubik', sans-serif;
    overflow:hidden;
  }

  .search-bar{
    text-align: center;
  }
  .searchbar{
    border-radius: 5px;
    width: 70%;
    height: 9%;
    background-color:#727272;
    border:none;
    font-family: 'Rubik', sans-serif;
    font-size: 27px;
    margin-top:10px;
    margin-bottom:10px;  
  }
  ::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
    color: #131316;
    opacity: 1; /* Firefox */
  }
  ::-ms-input-placeholder { /* Microsoft Edge */
    color: #131316;
  }
</style>


<div class='search-bar'>
  <input class='searchbar' name='searchbar' id='searchbar' type='search' placeholder='Search' value="" onkeypress='findSearch(document.getElementById("searchbar").value)'>
</div>

<script>
  function findSearch(letter){
      console.log(letter);
      var captions = document.querySelectorAll('.caption'),i;
      var boxes = document.querySelectorAll('.back-box');
      if (document.getElementById("searchbar").value == ''){for (ii = 0; ii < boxes.length; ++ii) {boxes[ii].style.display = 'inline-block';}}
      for (i = 0; i < captions.length; ++i) {
        if (captions[i].innerHTML.includes(letter)){boxes[i].style.display = 'inline-block';}
        else if  (captions[i].innerHTML.toLowerCase().includes(letter)){boxes[i].style.display = 'inline-block';}
        else{boxes[i].style.display = 'none';}
    }
  }
  function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  async function cycleCaptions(){
    var captions = document.querySelectorAll('.caption'),i;
    var boxes = document.querySelectorAll('.back-box');
    let x = 5;
    while (x < 10){
      for (i = 0; i < captions.length; ++i) {    
        if (document.getElementById("searchbar").value == ''){for (ii = 0; ii < boxes.length; ++ii) {boxes[ii].style.display = 'inline-block';}}
        document.getElementById('searchbar').placeholder = " "+captions[i].innerHTML;
        await sleep(1100);
        if (document.getElementById("searchbar").value == ''){for (ii = 0; ii < boxes.length; ++ii) {boxes[ii].style.display = 'inline-block';}}
      }}}
    window.onload = function() {
      cycleCaptions()
    };
</script>



<div class='main-div'>
    <div class='back-box'>
        <img alt="Panda dunk low" src="Photos/pandadunklow.png"width="200" height="150">
        <div class="caption">Dunk Low Black White</div>
    </div>

    <div class='back-box'>
        <img alt="Panda dunk low gs" src="Photos/pandadunklowgs.png"width="200" height="150">
        <div class="caption">Dunk Low Black White (GS)</div>
    </div>

    <div class='back-box'>
      <img alt="Unc dunk mens" src="Photos/dunklowunc.png"width="200" height="150">
      <div class="caption">Dunk Low UNC Men</div>
    </div>

    <div class='back-box'>
        <img alt="Spartan dunk mens" src="Photos/dunklowspartan.png"width="200" height="150">
        <div class="caption">Dunk Low Spartan Men</div>
    </div>

    <div class='back-box'>
      <img alt="Sb dunk low fog mens" src="Photos/sbdunkfog.png"width="200" height="150">
      <div class="caption">SB Dunk Low FOG Men</div>
    </div>

    <div class='back-box'>
        <img alt="Grey green mid" src="Photos/jordan1midgreengrey.png"width="190" height="150">
        <div class="caption">Jordan 1 Mid Grey Green</div>
    </div>

    <div class='back-box'>
        <img alt="curdory mid" src="Photos/jordan1midcurdory.png"width="200" height="150">
        <div class="caption">Jordan 1 Mid Curdory</div>
    </div>

    <div class='back-box'>
        <img alt="Smoke grey mid" src="Photos/jordan1midsmokegrey.png"width="210" height="150">
        <div class="caption">Jordan 1 Mid Smoke Grey</div>
    </div>

    <div class='back-box'>
        <img alt="Teal mid gs" src="Photos/jordan1midtealgs.png"width="220" height="150">
        <div class="caption">Jordan 1 Mid Teal (GS)</div>
    </div>

    <div class='back-box'>
      <img alt="Gym red mid gs" src="Photos/jordan1midgymgreygs.png"width="180" height="150">   
      <div class="caption">Jordan 1 Mid Gym Red (GS)</div>
    </div>

    <div class='back-box'>
      <img alt="Royal mid gs" src="Photos/jordan1royalwhitegs.png"width="200" height="150" >
      <div class="caption">Jordan 1 Mid Royal (GS)</div>
    </div>

    <div class='back-box'>
      <img alt="coral mid gs" src="Photos/jordan1midcoralgs.png"width="200" height="150">
      <div class="caption">Jordan 1 Coral (GS)</div>
    </div>

    <div class='back-box'>
      <img alt="Unc Low" src="Photos/jordan1lowunc.png"width="200" height="150">
      <div class="caption">Jordan 1 Unc Low</div>
    </div>

    <div class='back-box'>
      <img alt="Wolf grey low" src="Photos/jordan1lowwolfgrey.png"width="200" height="150">
      <div class="caption">Jordan 1 Wolf Grey Low</div>
    </div>

    <div class='back-box'>
      <img alt="jordan 11 cool grey mens" src="Photos/jordan11coolgrey.png"width="200" height="150">
      <div class="caption">Jordan 11 Cool Grey Mens</div>
    </div>

    <div class='back-box'>
      <img alt="jordan 4 shimmer" src="Photos/jordan4shimmer.png"width="200" height="150">
      <div class="caption">Jordan 4 Shimmer Womens</div>  
    </div>
  
    <div class='back-box'>
      <img alt="jordan 4 oreo" src="Photos/jordan4oreo.png"width="200" height="150">
      <div class="caption">Jordan 4 Oreo Mens</div>  
    </div>
  
    <div class='back-box'>
      <img alt="jordan 4 lightning" src="Photos/jordan4lightning.png"width="200" height="150">
      <div class="caption">Jordan 4 Lightning Mens</div>  
    </div>

    <div class='back-box'>
      <img alt="yeezy slide pure" src="Photos/yzslidepure.png"width="200" height="150">
      <div class="caption">Yeezy Slide Pure</div>    
    </div>

    <div class='back-box'>
      <img alt="yeezy slide ochre" src="Photos/yzyslideochre.png"width="200" height="150">
      <div class="caption">Yeezy Slide Ochre</div>   
    </div>
  
    <div class='back-box'>
      <img alt="yeezy foam runner" src="Photos/yzyfoamochre.png"width="200" height="150">
      <div class="caption">Yeezy Foam Runner Ochre</div>   
    </div>

    <div class='back-box'>
      <img alt="new balance 550 white grey" src="Photos/nb550whitegrey.png"width="200" height="150">
      <div class="caption">New Balance 550 White Grey</div>   
    </div>
</div>
   
    """
    return render_template_string(html.replace('Photos/','https://raw.githubusercontent.com/KhushC-03/my-stock/main/Photos/'))

if __name__ == "__main__":
    app.run()
