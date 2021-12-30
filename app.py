from flask import Flask, render_template_string, request, jsonify, g, redirect


app = Flask(__name__)



@app.route('/currentStock',methods=['GET'])
def currentStock():
    html = """
<meta  name='viewport' content='width=device-width, initial-scale=0.8, shrink-to-fit=yes'>
<body style="background-color:#131316" ></body>

<style>
  .back-box {
    border-radius: 15px;
    background: rgb(61, 145, 255);
    height:255;
    width: 225;
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
    margin-top:7px;
    margin-bottom:7px;     
  }

  .main-div{
    text-align: center;
    display: inline-block;
    transition: all .50s linear;
  }
  .caption{
    font-size: 1.03em;
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
    height: 60px;
    text-align: center;
    background-color:#aaaaaa;
    color: #131316;
    border:none;
    font-family: 'Rubik', sans-serif;
    font-size: 27px;
    margin-top:20px;
    margin-bottom:10px; 

  }

  .full-view{
    position: fixed;
    top: 50%;
    left: 50%;
    -webkit-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    width: 700;
    height: 400;
    border:none;
    border-radius: 15px;
    background-color:#131316;
    display: none;
  }

  .full-view-alt{
    position: absolute;
    margin-left: 20px;
    margin-top:10px;
    overflow: hidden;
  }
  .full-view-caption{
    margin-top:35px;
    text-align: center;
    font-size: 2em;
    font-family: 'Rubik', sans-serif; 
    color: white;
  }
  form{
    text-align: center;
    font-family: 'Rubik', sans-serif;
    margin-left: 400px;
    display:block;
    font-family: 'Rubik', sans-serif;
  }

  select{
    text-align: center;
    font-family: 'Rubik', sans-serif;
    margin-top:80px;
    margin-bottom:15px;
    width: 250px;
    height:30px;
    display:block;
    color: white;
    background-color:#aaaaaa;
    font-size: 1em;
    border:none;
    border-radius: 5px;
  }
  .email{
    text-align: center;
    font-family: 'Rubik', sans-serif;
    margin-bottom:15px;
    width: 250px;
    height:30px;
    display:block;
    color: white;
    background-color:#aaaaaa;
    border:none;
    border-radius: 5px;
    font-size: 1em;
  }
  .submit{
    text-align: center;
    font-family: 'Rubik', sans-serif;
    width: 250px;
    height:30px;
    display:block;
    color: white;
    background-color:#aaaaaa;
    border:none;
    border-radius: 5px;
    font-size: 1em;
  }
  @media only screen and (max-width: 775px) {
    .full-view{
      position: fixed;
      top: 50%;
      left: 50%;
      -webkit-transform: translate(-50%, -50%);
      transform: translate(-50%, -50%);
      width: 340;
      height: 450;
      border:none;
      border-radius: 15px;
      background-color:#131316;
      display: none;
    }
    .full-view-alt{
      position: fixed;
      margin-left: 20px;
      margin-top:-10px;
      overflow: hidden;
    }
    .full-view-caption{
      margin-top:35px;
      text-align: center;
      font-size: 2em;
      font-family: 'Rubik', sans-serif; 
      color: white;
    }
    form{
      position: relative;
      text-align: center;
      font-family: 'Rubik', sans-serif;
      margin-top:220px;
      margin-left: 43px;
      display:block;
      font-family: 'Rubik', sans-serif;
    }
  
    select{
      text-align: center;
      font-family: 'Rubik', sans-serif;
      margin-top:80px;
      margin-bottom:6px;
      width: 250px;
      height:30px;
      display:block;
      color: rgb(255, 255, 255);
      background-color:#aaaaaa;
      font-size: 1em;
      border:none;
      border-radius: 5px;
    }
    .email{
      text-align: center;
      font-family: 'Rubik', sans-serif;
      margin-bottom:6px;
      width: 250px;
      height:30px;
      display:block;
      color: white;
      background-color:#aaaaaa;
      border:none;
      border-radius: 5px;
      font-size: 1em;
    }
    .submit{
      text-align: center;
      font-family: 'Rubik', sans-serif;
      width: 250px;
      height:30px;
      display:block;
      color: white;
      background-color:#aaaaaa;
      border:none;
      border-radius: 5px;
      font-size: 1em;
    }
 
  }
  ::placeholder {
    color: #ffffff;
    opacity: 1; /* Firefox */
  }
  ::-ms-input-placeholder {
    color: #ffffff;
  }
</style>

<div class="lds-ring"><div></div><div></div><div></div><div></div></div>


<script>

  function showFull(image,product){
    if (image == false){
      document.querySelector('.full-view').style.display = "none"
    }
    else{
      if (document.querySelector('.full-view').style.display == 'none'){
        document.querySelector('.full-view').style.display = "inline-block"

      }
      else{
        if (document.querySelector('.full-view-alt').alt == product){document.querySelector('.full-view').style.display = "none"}
        
      }
      document.querySelector('.full-view-alt').alt = product
      document.querySelector('.full-view-alt').src = image
      document.querySelector('.full-view-caption').innerHTML = product
      
    }
  }

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
      document.querySelector('.full-view').style.display = "none"
      cycleCaptions()
    };
</script>


<div class='search-bar'>
  <input  class='searchbar' name='searchbar' id='searchbar' type='search' placeholder='Search' value="" onkeypress='findSearch(document.getElementById("searchbar").value)' onclick='showFull(false,false)'>
</div>


<div class='full-view' >
  <div class="full-view-caption" ></div>
  <img class='full-view-alt'alt="" src=""width="320" onclick='showFull(false,false)' >
  <form>
    <select name="sizes" id="sizes" >
      <option value="sizes">Select A Size</option>
      <option value="UK 5">UK 5</option>
      <option value="UK 6">UK 6</option>
      <option value="UK 9">UK 9</option>
    </select>
    <input class='email' name='email' id='email' type='text' placeholder='Email / Instagram' value="">
    <input class='submit' type='submit' name='submit' id='submit'value="Enquire">
  </form>
  
</div>

<div class='main-div' >
    <div class='back-box' onclick='showFull("Photos/pandadunklow.png","Dunk Low Black White")'>
        <img alt="Panda dunk low" src="Photos/pandadunklow.png"width="200" height="150">
        <div class="caption" >Dunk Low Black White</div>
    </div>

    <div class='back-box' onclick='showFull("Photos/pandadunklowgs.png","Dunk Low Black White (GS)")'>
        <img alt="Panda dunk low gs" src="Photos/pandadunklowgs.png"width="200" height="150">
        <div class="caption">Dunk Low Black White (GS)</div>
    </div>

    <div class='back-box' onclick='showFull("Photos/dunklowunc.png","Dunk Low UNC Men")'>
      <img alt="Unc dunk mens" src="Photos/dunklowunc.png"width="200" height="150">
      <div class="caption">Dunk Low UNC Men</div>
    </div>

    <div class='back-box' onclick='showFull("Photos/dunklowspartan.png","Dunk Low Spartan Men")'>
        <img alt="Spartan dunk mens" src="Photos/dunklowspartan.png"width="200" height="150">
        <div class="caption">Dunk Low Spartan Men</div>
    </div>

    <div class='back-box' onclick='showFull("Photos/sbdunkfog.png","SB Dunk Low FOG Men")'>
      <img alt="Sb dunk low fog mens" src="Photos/sbdunkfog.png"width="200" height="150">
      <div class="caption">SB Dunk Low FOG Men</div>
    </div>

    <div class='back-box' onclick='showFull("Photos/jordan1midgreengrey.png","Jordan 1 Mid Grey Green")'>
        <img alt="Grey green mid" src="Photos/jordan1midgreengrey.png"width="190" height="150">
        <div class="caption">Jordan 1 Mid Grey Green</div>
    </div>

    <div class='back-box' onclick='showFull("Photos/jordan1midcurdory.png","Jordan 1 Mid Curdory")'>
        <img alt="curdory mid" src="Photos/jordan1midcurdory.png"width="200" height="150">
        <div class="caption">Jordan 1 Mid Curdory</div>
    </div>

    <div class='back-box' onclick='showFull("Photos/jordan1midsmokegrey.png","Jordan 1 Mid Smoke Grey")'>
        <img alt="Smoke grey mid" src="Photos/jordan1midsmokegrey.png"width="210" height="150">
        <div class="caption">Jordan 1 Mid Smoke Grey</div>
    </div>

    <div class='back-box' onclick='showFull("Photos/jordan1midtealgs.png","Jordan 1 Mid Teal (GS)")'>
        <img alt="Teal mid gs" src="Photos/jordan1midtealgs.png"width="220" height="150">
        <div class="caption">Jordan 1 Mid Teal (GS)</div>
    </div>

    <div class='back-box' onclick='showFull("Photos/jordan1midgymgreygs.png","Jordan 1 Mid Gym Red (GS)")'>
      <img alt="Gym red mid gs" src="Photos/jordan1midgymgreygs.png"width="180" height="150">   
      <div class="caption">Jordan 1 Mid Gym Red (GS)</div>
    </div>

    <div class='back-box' onclick='showFull("Photos/jordan1royalwhitegs.png","Jordan 1 Mid Royal (GS)")'>
      <img alt="Royal mid gs" src="Photos/jordan1royalwhitegs.png"width="200" height="150" >
      <div class="caption">Jordan 1 Mid Royal (GS)</div>
    </div>

    <div class='back-box' onclick='showFull("Photos/jordan1midcoralgs.png","Jordan 1 Coral (GS)")'>
      <img alt="coral mid gs" src="Photos/jordan1midcoralgs.png"width="200" height="150">
      <div class="caption">Jordan 1 Coral (GS)</div>
    </div>

    <div class='back-box' onclick='showFull("Photos/jordan1lowunc.png","Jordan 1 Unc Low")'>
      <img alt="Unc Low" src="Photos/jordan1lowunc.png"width="200" height="150">
      <div class="caption">Jordan 1 Unc Low</div>
    </div>

    <div class='back-box' onclick='showFull("Photos/jordan1lowwolfgrey.png","Jordan 1 Wolf Grey Low")'>
      <img alt="Wolf grey low" src="Photos/jordan1lowwolfgrey.png"width="200" height="150">
      <div class="caption">Jordan 1 Wolf Grey Low</div>
    </div>

    <div class='back-box' onclick='showFull("Photos/jordan11coolgrey.png","Jordan 11 Cool Grey Mens")'>
      <img alt="jordan 11 cool grey mens" src="Photos/jordan11coolgrey.png"width="200" height="150">
      <div class="caption">Jordan 11 Cool Grey Mens</div>
    </div>

    <div class='back-box' onclick='showFull("Photos/jordan4shimmer.png","Jordan 4 Shimmer Womens")'>
      <img alt="jordan 4 shimmer" src="Photos/jordan4shimmer.png"width="200" height="150">
      <div class="caption">Jordan 4 Shimmer Womens</div>  
    </div>
  
    <div class='back-box' onclick='showFull("Photos/jordan4oreo.png","Jordan 4 Oreo Mens")'>
      <img alt="jordan 4 oreo" src="Photos/jordan4oreo.png"width="200" height="150">
      <div class="caption">Jordan 4 Oreo Mens</div>  
    </div>
  
    <div class='back-box' onclick='showFull("Photos/jordan4lightning.png","Jordan 4 Lightning Mens")'>
      <img alt="jordan 4 lightning" src="Photos/jordan4lightning.png"width="200" height="150">
      <div class="caption">Jordan 4 Lightning Mens</div>  
    </div>

    <div class='back-box' onclick='showFull("Photos/yzslidepure.png","Yeezy Slide Pure")'>
      <img alt="yeezy slide pure" src="Photos/yzslidepure.png"width="200" height="150">
      <div class="caption">Yeezy Slide Pure</div>    
    </div>

    <div class='back-box' onclick='showFull("Photos/yzyslideochre.png","Yeezy Slide Ochre")'>
      <img alt="yeezy slide ochre" src="Photos/yzyslideochre.png"width="200" height="150">
      <div class="caption">Yeezy Slide Ochre</div>   
    </div>
  
    <div class='back-box' onclick='showFull("Photos/yzyfoamochre.png","Yeezy Foam Runner Ochre")'>
      <img alt="yeezy foam runner" src="Photos/yzyfoamochre.png"width="200" height="150">
      <div class="caption">Yeezy Foam Runner Ochre</div>   
    </div>

    <div class='back-box' onclick='showFull("Photos/nb550whitegrey.png","New Balance 550 White Grey")'>
      <img alt="new balance 550 white grey" src="Photos/nb550whitegrey.png"width="200" height="150">
      <div class="caption">New Balance 550 White Grey</div>   
    </div>
</div>




    """
    return render_template_string(html.replace('Photos/','https://raw.githubusercontent.com/KhushC-03/my-stock/main/Photos/'))

if __name__ == "__main__":
    app.run()
