1 print("Some print")
2 print("Other spring")
3let x = 200;
let y = 200;
let extraCanvas;
function setup() {
  createCanvas(400, 400);
  extraCanvas = createGraphics(400,400);
  extraCanvas.background(255,0,0);
  background(0);
}
 
function draw () {

  
  //No trails

  background(0);
  x+=random(-5,5);
  y-=random(-5,5);

  //trails
//if(mouseIsPressed) {
  extraCanvas.fill(255,130);
  extraCanvas.noStroke();
  let starX = random(width);
  let starY = random(height);
 extraCanvas.ellipse(starX,starY,10,10);
//extraCanvas.ellipse(mouseX,mouseY,60,60);
//}
 image(extraCanvas,0,0);
 fill(255,0,0);
 rectMode(CENTER);
 stroke(255);
 rect(x,y,20,30);
}

