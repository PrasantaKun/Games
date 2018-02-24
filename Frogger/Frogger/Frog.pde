class Frog extends Rectangle {

  Log attached = null;
  Frog(float x, float y, float w) {
    super(x, y, w, w);
  }

  void attached(Log log) {
    attached = log;
  }

  void show() {
    fill(0,255,0);
    rect(x, y, w, w);
  }
  
  void update() {
    if(attached != null){
       frog.x += attached.speed;
    }
    
    frog.x = constrain(x, 0, width-w);
  }

  void move(float xDirection, float yDirection) {
    x += xDirection*grid;
    y += yDirection*grid;
  }
}