let classifier;

let video;

let label = "Chargement du modèle";
let oldLabel = "Chargement du modèle";
let compteurLabel = 0;

let imageModelURL = "https://teachablemachine.withgoogle.com/models/7IwsQtkQ2/";

let connectBtn, disconnectBtn, heartButton, arrowButton;

let message="";

function preload() {
  ml5.setBackend('webgl');
  classifier = ml5.imageClassifier(imageModelURL + "model.json");
}

function setup() {
  createCanvas(640, 480);

  video = createCapture(VIDEO, { flipped: true });
  video.size(640, 480);
  video.hide();

  classifier.classifyStart(video, gotResult);
  
  
  //microbit
  microBit = new uBitWebUSB();

  microBit.onConnect(function(){
    console.log("connected");
  });

  microBit.onDisconnect(function(){
    console.log("disconnected");
  });

  
  connectBtn = createButton("connect");
  connectBtn.mousePressed(function(){microBit.connectDevice()});
  disconnectBtn = createButton("disconnect");
  disconnectBtn.mousePressed(function(){microBit.disconnectDevice()});
  
  
  console.log("Press 'S' to trigger the function");
}

function draw() {
  // Each video frame is painted on the canvas
  image(video, 0, 0);

  // Printing class with the highest probability on the canvas
  fill(255, 255, 0);
  textSize(32);
  text(label, 20, 50);
  fill(0, 0, 0);
  textSize(40);
  text(message, 20, 150);
}

// A function to run when we get the results
function gotResult(results) {
  // Update label variable which is displayed on the canvas
  oldLabel = label ;
  label = results[0].label;
  if(label == oldLabel){
    compteurLabel = compteurLabel+1;
  }
  else{
    compteurLabel =0;
  }
  if(compteurLabel>20){
    if(label=="Santa"){
      print("ok")
      microBit.sendSerial("IA");    
      message="OK";
    }
    else if(label=="Paul no Santa"){
      message = "Il lui faut son bonnet";
    }
    else{
      message="";
    }
  }
  
}

function keyPressed() {
  if (key === 's' || key === 'S') {
    message="secret key :-) ";
    microBit.sendSerial("IA"); 
    label="";
  }
}
