// Buttons to connect/disconnect to micro:bit
let connectBtn;
let disconnectBtn;

let microBit;

let messagerecu="";
let messageenvoye="";

let myInput;
let sendMessageBtn;

// Variables pour le paysage enneigé
let snowflakes = [];
let song;
let chainDetected= false;


// Précharger la chanson de Noël
function preload() {
  song = loadSound('./jingle_bells.mp3'); // Assurez-vous d'avoir un fichier audio "jingle_bells.mp3"
}

function setup() {
  createCanvas(1200, 1200);
  

  microBit = new uBitWebUSB();

  microBit.onConnect(function(){
    console.log("connected");
  });

  microBit.onDisconnect(function(){
    console.log("disconnected");
  });

  
  microBit.onReceiveSerial(receiveSerialMessage);

  //boutons connexion
  connectBtn = createButton("connect");
  connectBtn.mousePressed(function(){microBit.connectDevice()});
  disconnectBtn = createButton("disconnect");
  disconnectBtn.mousePressed(function(){microBit.disconnectDevice()});
  
  createElement("p");
  //champ texte à envoyer en serial
  myInput = createInput();
  sendMessageBtn=createButton("envoyer message");
  sendMessageBtn.mousePressed(sendMessage);
  
  textSize(25);
  
  // Configuration initiale
  noStroke();
  fill(255);
  textSize(32);
  
}

function draw() {
  text(messagerecu,20,60);//on écrit le message reçu par serial
  
  background(10, 10, 50); // Ciel nocturne

  if (chainDetected) {
    // Afficher le paysage enneigé
    drawSnow();
    

    // Démarrer la chanson si elle n'est pas déjà jouée
    if (!song.isPlaying()) {
      song.loop();
    }
  } else {
    // Instructions si la chaîne n'est pas détectée
    textAlign(CENTER);
    fill(255);
    text("Connectez la chaîne humaine pour voir la magie !", width / 2, height / 2);

    // Stopper la chanson
    if (song.isPlaying()) {
      song.stop();
    }
  }
  
}

function sendMessage(){
  //vérification du input et envoie par serial
  messageenvoye = myInput.value();
  if(messageenvoye.length>0){
    console.log("envoie en serial du message "+messageenvoye);
    microBit.sendSerial(messageenvoye);
  }
}

function receiveSerialMessage(receivedData){
    messagerecu = str(receivedData)+' à ' + hour() + ":" + minute()+":"+second();
    //console.log(messagerecu);
    if(str(receivedData).includes("chain"))  chainDetected = true
    
  }







// Dessiner les flocons de neige
function drawSnow() {
    fill(255);
    textSize(30);
    text("Le code pour ton cadeau est 111",100,100);
  let t = frameCount / 60; // Temps

  // Ajouter de nouveaux flocons de neige
  for (let i = 0; i < random(1, 5); i++) {
    snowflakes.push(new snowflake());
  }

  // Boucle sur les flocons de neige
  for (let flake of snowflakes) {
    flake.update(t); // Mise à jour
    flake.display(); // Affichage
  }
  
}

// Classe pour les flocons de neige
class snowflake {
  constructor() {
    this.posX = random(0, width);
    this.posY = random(-50, 0);
    this.size = random(2, 5);
    this.speed = random(1, 3);
  }

  update(time) {
    this.posY += this.speed;

    // Réinitialiser les flocons en haut de l'écran
    if (this.posY > height) {
      this.posY = random(-50, 0);
      this.posX = random(0, width);
    }
  }

  display() {
    ellipse(this.posX, this.posY, this.size);
  }
}

function keyPressed() {
  if (key === 's' || key === 'S') {
    console.log("secret key :-) ");
    chainDetected = true;
  }
}