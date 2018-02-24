class Log extends Car {

  Log(float x, float y, float w, float h, float s) {
    super(x, y, w, h, s);
    speed = s;
  }

  void show() {
    fill(0, 255, 0, 100);
    rect(x, y, w, h);
  }
}