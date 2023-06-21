


 Project by P5JS
function setup() {
  createCanvas(600, 400);
}
var star = {
  x:300,
  y:200,
  xspeed:-3,
  yspeed:4
} 
function draw() {
  background(0);
  move();
  bounce();
  display();
function move() {
  star.x = star.x + star.xspeed;
  star.y = star.y + star.yspeed;

}
function bounce() {
  if(star.x > width || star.x < 0) {
    star.xspeed = star.xspeed * -1; 
  }
  if(star.y > height || star.y < 0) {
    star.yspeed = star.yspeed * -1;
}
}
Qfunction display() {
  
  stroke(235);
  strokeWeight(4);
  fill(random(255));
  ellipse(star.x, star.y,24,24);
}
}
