Frog frog;
Car[] cars;
Log[] logs;

float grid = 50;


void setup() {
  size(550, 550);
  resetGame();
  cars = new Car[7];
  logs = new Log[8];
  int index = 0;

  // ROW 1
  for (int i = 0; i < 2; i++) {
    float x = i * 300;
    cars[index] = new Car(x, width-grid*2, grid*2, grid, 2);
    index++;
  }

  // ROW 2
  for (int i = 0; i < 2; i++) {
    float x = i * 250 + 250;
    cars[index] = new Car(x, width-grid*3, grid, grid, -3.5);
    index++;
  }

  // ROW 3
  for (int i = 0; i < 3; i++) {
    float x = i * 200;
    cars[index] = new Car(x, width-grid*4, grid, grid, 1.7);
    index++;
  }

  // ROW 5
  index = 0;
  for (int i = 0; i < 2; i++) {
    float x = i * 500;
    logs[index] = new Log(x, width-grid*6, grid*3, grid, 2.5);
    index++;
  }

  // ROW 6
  for (int i = 0; i < 3; i++) {
    float x = i * 200;
    logs[index] = new Log(x, width-grid*7, grid*2, grid, -2);
    index++;
  }

  // ROW 6
  for (int i = 0; i < 2; i++) {
    float x = i * 300;
    logs[index] = new Log(x, width-grid*8, grid*2, grid, 1.8);
    index++;
  }
  
  // ROW 7
  for (int i = 0; i < 1; i++) {
    float x = i * 200;
    logs[index] = new Log(x, width-grid*9, grid*1.5, grid, -4);
    index++;
  }
}

void resetGame() {
  frog = new Frog(width/2-grid/2, height-grid, grid);
  frog.attached(null);
}

void draw() {
  background(50);
  fill(0,0,255,150);
  rect(0, grid*2, width, grid*4);
  fill(255, 100);
  rect(0, width-grid, width, grid);
  rect(0, width-grid*5, width, grid);
  rect(0, width-grid*11, width, grid*2);
  
  for (Car car : cars) {
    car.show();
    car.update();
    if (car.intersects(frog)) {
      resetGame();
    }
  }
  for (Log log : logs) {
    log.show();
    log.update();
  }
  if (frog.y < height-grid*5 && frog.y > grid) {
    boolean ok = false;
    for (Log log : logs) {
      if (frog.intersects(log)) {
        ok = true;
        frog.attached(log);
      }
    }
    if (!ok) {
      resetGame();
    }
  } else {
    frog.attached(null);
  }
  frog.show();
  frog.update();
}

void keyPressed() {
  if (keyCode == UP) {
    frog.move(0, -1);
  } else if (keyCode == DOWN) {
    frog.move(0, 1);
  } else if (keyCode == RIGHT) {
    frog.move(1, 0);
  } else if (keyCode == LEFT) {
    frog.move(-1, 0);
  }
}