import java.util.Scanner;

public class Board{
		
	public Board(){
		
		super();
		
	}
		
	String[][] board = new String[24][14];
	
	Ball ball = new Ball(21, 6);
	
	Paddle paddle = new Paddle(22, 4);
	
	Brick[][] bricks = new Brick[8][4];
	
	String destroyedBrickColor = "";
	int brickNumber =  8 * 4;
	int oddMove = 0;
	int round = 0;
	int ballCase = 0;
	
	//Generate special and normal bricks
	public void makeBrick(){
		
		int x = 0;
		int y = 0;
		
		//For x coordinates
		for(int i = 3; i <= 10 ; i++ ){
			
			//For y coordinates
			for(int j = 3; j <= 10; j += 2){
				
				if( x == 0 && y == 0 || x == 3 && y ==  3){
					
					bricks[x][y] = new RedBrick(i, j);
				
				} else if( x == 0 && y == 3 || x == 6 && y == 3){
					
					bricks[x][y] = new BlueBrick(i, j);
				
				} else if( x == 3 && y == 0 || x == 7 && y == 2){
					
					bricks[x][y] = new YellowBrick(i, j);
				
				} else if( x == 5 && y == 2){				
					
					bricks[x][y] = new GreenBrick(i, j);				

				} else {
					
					bricks[x][y] = new Brick(i, j);
					
				}	
				
				y++;
				
			}
			
			y = 0;
			x++;
			
		}
		
	}	
	
	
	//Fill the array with characters of special shapes or space
	public void map(){
			
		for(int i = 0; i < 24; i++){
			
			for(int j = 0; j < 14; j++){
		
				board[i][j] = " ";	
	
			}
			
		}
					
		//Fence, paddle and ball
		for(int i = 0; i < 24; i++){
			
			for(int j = 0; j < 14; j++){
				
				//For fence
				if(i == 0 || j == 0 || i == 23 || j == 13)
				
					board[i][j] = "*";
				
				//For ball
				else if(i == ball.x && j == ball.y)
				
					board[i][j] = "O";
				
				//For paddle
				else if(i == paddle.x && j >= paddle.y && j <= paddle.y + 5 )
					
					board[i][j] = "-";	
					
				//For bricks
				//This loop for x coordinates of bricks
				for(int k = 0; k < 8 ; k++){
					
					//This loop for y coordinates of bricks
					for(int m = 0; m < 4; m++){
					
						if(bricks[k][m].x == i && bricks[k][m].y == j){
							
							//Make two character for one brick in board[][]
							for(int n = 0; n < 2; n++){
								
								if(bricks[k][m] instanceof RedBrick){
									
									board[i][j + n] = "R";
									
								} else if(bricks[k][m] instanceof BlueBrick){
									
									board[i][j + n] = "B";
									
								} else if(bricks[k][m] instanceof GreenBrick){
									
									board[i][j + n] = "G";
									
								} else if(bricks[k][m] instanceof YellowBrick){
									
									board[i][j + n] = "Y";
									
								} else{
								
									board[i][j + n] = "#";
								
								}
								
							}	//End of n loop
							
						}	//End of if condition
					
					}	//End of m loop
						
				}	//End of k loop
				
			}	//End of j loop
			
		}	//End of i loop
		
	}	//End of method
	
	//This method supports to change initial definitions after any change
	public void update(){
		
		map();
		
		clearConsole();
		
		draw();
		
	}
	
	//Print to board on the screen
	public void draw(){
		
		for(int i = 0; i < 24; i++){
			
			for(int j = 0; j < 14; j++){
		
				System.out.print(board[i][j]);
			
			}
			
			System.out.println();
		
		}	
			
	}
	
	//If the ball has hit yellow brick, it also explodes neighbours of this brick
	public void explode(int t, int r){
		
		int x = -1;
		int y = -1;
		
		//We need 8 different condition to check of every aspect
		for(int k = 0; k < 8; k++){
		
			if(k == 0){				//Up and left aspect
				x= -1;
				y= -1;
			} else if(k == 1){		//Left aspect
				x= 0;
				y= -1;
			} else if(k == 2){		//Down and left aspect
				x= +1;
				y= -1;
			} else if(k == 3){		//Up aspect
				x= -1;
				y= 0;
			} else if(k == 4){		//Bottom aspect
				x= +1;
				y= 0;
			} else if(k == 5){		//Up and right aspect
				x= -1;
				y= +1;
			} else if(k == 6){		//Right aspect 
				x= 0;
				y= +1;
			} else if(k == 7){		//Down and right aspect
				x= +1;
				y= +1;
			}	
			
			//Check the values in order to not get ArrayOutOfIndexException
			//And check whether neighbours are exist
			if((t + x) != -1 && (t + x) != 8 && (r + y) != -1 && (r + y) != 4 &&
					bricks[t + x][r + y].x != -1 && bricks[t + x][r + y].y != -1){
			
				//Delete the brick
				for(int c = 0; c < 2; c++){
					
					board[bricks[t + x][r + y].x][bricks[t + x][r + y].y + c] = " ";
					
				}
				
				//Change their coordinates
				bricks[t + x][r + y].x = -1;
				bricks[t + x][r + y].y = -1;
				
				brickNumber--;
			
				//Find  color of the deleted brick
				destroyedBrickColor = defineColor(bricks[t + x][r + y]);
				
				if(destroyedBrickColor == "RED"){
					
					oddMove = 30;
					
				} else if(destroyedBrickColor == "BLUE"){
					
					ball.willStick = true;
					
				} else if(destroyedBrickColor == "YELLOW"){
					
					explode(t,r);
					
				} else if(destroyedBrickColor == "GREEN"){
					
					ball.canDestroy = true;
					
				} else{}
				
			}	
				
		}	//End of for loop	
			
	}	//End of method
	
	
	public final static void clearConsole() {
		
		for (int i = 0; i < 25; i++) {
			
			System.out.println();
			
		}
		
	}
	
	
	public void gameOver() {
		
		System.out.println("Game Over :(");
		
		System.exit(0);
		
	}
	
	//To find color of exploded or deleted brick
	public String defineColor(Shape unit){
		
		if(unit instanceof RedBrick)
			return "RED";
		else if(unit instanceof YellowBrick)
			return "YELLOW";
		else if(unit instanceof GreenBrick)
			return "GREEN";
		else if(unit instanceof BlueBrick)
			return "BLUE";
		else 
			return "DEFAULT";
		
	}
	
	//It takes inputs, makes changes, and calls update method
	public void play(){
		
		int x = -1;
		int y = 1;
		
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		
		//Generate bricks
		makeBrick();
		
		while(true){
			
			//Rearrange the board[][] and print it on the screen
			update();
			
			if(round % 2 == 0 || oddMove > 0 || ball.canMove == false){
				
				switch(sc.next()){
				
					//Move the paddle to left
					case ("a"):
					
						if(paddle.y == 1)
							break;
					
						//Delete the paddle position before change 
						board[paddle.x][paddle.y + 5] = " ";
						
						//Move to right with decreasing y-coordinates
						paddle.y -= 1;
						
						//Change y-coor. of the ball if it is sticked 
						if(ball.canMove == false){
							
							ballCase = -1;
							
						}
						
						break;
						
					
					case ("s"):
						
						//Throw the ball if it is sticked
						if(ball.canMove == false){
						
							ball.canMove = true;
							ball.willStick = false;
							
						}
						
						break;
						
					//Opposite of "a"	
					case ("d"):
						
						if( paddle.y + 5 == 12)
							break;
						
						board[paddle.x][paddle.y] = " ";
						
						paddle.y += 1;
						
						if(ball.canMove == false){
							
							ballCase = +1;
							
						}
						
						break;
						
						
					default:
											
						break;
		
				}	//End of switch-case
				
			}	//End of if condition
			
			//Delete the previous position of ball
			board[ball.x][ball.y] = " ";
			
			//For bouncing from fence
			if(ball.canMove == true){
			
				//For bouncing from the fence-sides
				if(ball.y == 12 || ball.y == 1){
					
					y *= -1;
				
				//For bouncing from the upside of fence
				} 
				
				if(ball.x == 1){
					
					x *= -1;
				
				}	
			
			}	
				
			//For bouncing from the paddle when hitting normally
			if((x > 0) && (ball.x == 21) && 
					(ball.y >= paddle.y && ball.y <= paddle.y + 5)){
				
				x *= -1;
			
				if(ball.willStick == true){
					
					ball.canMove = false;
					
				}
				
			}	
				
			//For bouncing from the paddle when diagonal hitting
			if((x > 0) && (ball.x == 21) && 
					(ball.y + 1 == paddle.y || ball.y - 1 == paddle.y + 5)){
				
				x *= -1;
				y *= -1;
				
				if(ball.willStick == true){
					
					ball.canMove = false;
					
				}
			
			}	
			
			
			//This loop for x-coordinate of bricks
			for(int t = 0; t < 8; t++){
				
				//This loop for y-coordinate of bricks
				for(int r = 0; r < 4; r++){
					
					//When ball goes up and left
					if(x == -1 && y == -1){
					
						//When hitting the brick from bottom-side
						if((ball.x - 1 == bricks[t][r].x) && (ball.y >= bricks[t][r].y) &&
								(ball.y <= bricks[t][r].y + 1)){
							
							//Delete the brick which is hit
							for(int b = 0; b < 2; b++){
								
								board[bricks[t][r].x][bricks[t][r].y + b] = " ";
								
							}
							
							//Find color of the destroyed brick
							destroyedBrickColor = defineColor(bricks[t][r]);
							
							//Set it's coordinates to -1
							bricks[t][r].x = -1;
							bricks[t][r].y = -1;
							
							//Decrease brick number
							brickNumber--;
							
							//Bounce if the ball cannot destroy
							if(ball.canDestroy != true){
								x *= -1;
							}
								
						//When hitting the brick from right side
						} else if((ball.x == bricks[t][r].x) && (ball.y - 2 ==  bricks[t][r].y)){
							
							for(int b = 0; b < 2; b++){
								
								board[bricks[t][r].x][bricks[t][r].y + b] = " ";
								
							}
							
							destroyedBrickColor = defineColor(bricks[t][r]);
							
							bricks[t][r].x = -1;
							bricks[t][r].y = -1;
							
							brickNumber--;

							if(ball.canDestroy != true){
								y *= -1;
							}
						
						//When diagonal hitting the brick 	
						} else if((ball.x - 1 == bricks[t][r].x) && (ball.y - 2 ==  bricks[t][r].y) &&
									(bricks[t+1][r].x == -1 && bricks[t+1][r].y == -1)){
							
							for(int b = 0; b < 2; b++){
								
								board[bricks[t][r].x][bricks[t][r].y + b] = " ";
								
							}
							
							destroyedBrickColor = defineColor(bricks[t][r]);
							
							bricks[t][r].x = -1;
							bricks[t][r].y = -1;
							
							brickNumber--;

							if(ball.canDestroy != true){
								y *= -1;
								x *= -1;
							}
							
						}
					
						
						
					//When ball goes up and right	
					} else if(x == -1 && y == +1){
						
						//When hitting the brick from bottom-side
						if((ball.x - 1 == bricks[t][r].x) && (ball.y >= bricks[t][r].y) &&
								(ball.y <= bricks[t][r].y + 1)){
							
							for(int b = 0; b < 2; b++){
								
								board[bricks[t][r].x][bricks[t][r].y + b] = " ";
								
							}
							
							destroyedBrickColor = defineColor(bricks[t][r]);
							
							bricks[t][r].x = -1;
							bricks[t][r].y = -1;
							
							brickNumber--;

							if(ball.canDestroy != true){
								x *= -1;
							}
						
						//When hitting from left side	
						} else if((ball.x == bricks[t][r].x) && (ball.y + 1 ==  bricks[t][r].y)){
							
							for(int b = 0; b < 2; b++){
								
								board[bricks[t][r].x][bricks[t][r].y + b] = " ";
								
							}
							
							destroyedBrickColor = defineColor(bricks[t][r]);
							
							bricks[t][r].x = -1;
							bricks[t][r].y = -1;
							
							brickNumber--;

							if(ball.canDestroy != true){
								y *= -1;
							}
						
						//When diagonal hitting the brick	
						} else if((ball.x - 1 == bricks[t][r].x) && (ball.y + 1 ==  bricks[t][r].y) &&
								(bricks[t+1][r].x == -1 && bricks[t+1][r].y == -1)){
							
							for(int b = 0; b < 2; b++){
								
								board[bricks[t][r].x][bricks[t][r].y + b] = " ";
								
							}
							
							destroyedBrickColor = defineColor(bricks[t][r]);
							
							bricks[t][r].x = -1;
							bricks[t][r].y = -1;
							
							brickNumber--;

							if(ball.canDestroy != true){
								x *= -1;
								y *= -1;
							}
							
						}

					
						
					//When ball goes down and left
					} else if(x == +1 && y == -1){
						
						//When hitting the brick from up-side
						if((ball.x + 1 == bricks[t][r].x) && (ball.y >= bricks[t][r].y) &&
								(ball.y <= bricks[t][r].y + 1)){
							
							for(int b = 0; b < 2; b++){
								
								board[bricks[t][r].x][bricks[t][r].y + b] = " ";
								
							}
							
							destroyedBrickColor = defineColor(bricks[t][r]);
							
							bricks[t][r].x = -1;
							bricks[t][r].y = -1;
							
							brickNumber--;
							
							if(ball.canDestroy != true){
								x *= -1;
							}
												
						} else if((ball.x == bricks[t][r].x) && (ball.y - 2 ==  bricks[t][r].y)){
							
							for(int b = 0; b < 2; b++){
								
								board[bricks[t][r].x][bricks[t][r].y + b] = " ";
								
							}
							
							destroyedBrickColor = defineColor(bricks[t][r]);
							
							bricks[t][r].x = -1;
							bricks[t][r].y = -1;
							
							brickNumber--;

							if(ball.canDestroy != true){
								y *= -1;
							}
							
						} else if((ball.x + 1 == bricks[t][r].x) && (ball.y - 2 ==  bricks[t][r].y)){
							
							for(int b = 0; b < 2; b++){
								
								board[bricks[t][r].x][bricks[t][r].y + b] = " ";
								
							}
							
							destroyedBrickColor = defineColor(bricks[t][r]);
							
							bricks[t][r].x = -1;
							bricks[t][r].y = -1;
							brickNumber--;
							
							if(ball.canDestroy != true){
								x *= -1;
								y *= -1;
							}
							
						}
						
						
					//When ball goes down and right	
					}else if(x == +1 && y == +1){
						
						if((ball.x + 1 == bricks[t][r].x) && (ball.y >= bricks[t][r].y) &&
								(ball.y <= bricks[t][r].y + 1)){
							
							for(int b = 0; b < 2; b++){
								
								board[bricks[t][r].x][bricks[t][r].y + b] = " ";
								
							}
							
							destroyedBrickColor = defineColor(bricks[t][r]);
							
							bricks[t][r].x = -1;
							bricks[t][r].y = -1;
							
							brickNumber--;

							if(ball.canDestroy != true){
								x *= -1;
							}
												
						} else if((ball.x == bricks[t][r].x) && (ball.y +1 ==  bricks[t][r].y)){
							
							for(int b = 0; b < 2; b++){
								
								board[bricks[t][r].x][bricks[t][r].y + b] = " ";
								
							}
							
							destroyedBrickColor = defineColor(bricks[t][r]);
							
							bricks[t][r].x = -1;
							bricks[t][r].y = -1;
							
							brickNumber--;

							if(ball.canDestroy != true){
								y *= -1;
							}
							
						} else if((ball.x + 1 == bricks[t][r].x) && (ball.y + 1 ==  bricks[t][r].y)){
							
							for(int b = 0; b < 2; b++){
								
								board[bricks[t][r].x][bricks[t][r].y + b] = " ";
								
							}
							
							destroyedBrickColor = defineColor(bricks[t][r]);
							
							bricks[t][r].x = -1;
							bricks[t][r].y = -1;
							
							brickNumber--;

							if(ball.canDestroy != true){
								x *= -1;
								y *= -1;
							}
							
						}
						
					}
						
					if(destroyedBrickColor == "RED"){
						
						oddMove = 30;
						
					} else if(destroyedBrickColor == "BLUE"){
						
						ball.willStick = true;
						
					} else if(destroyedBrickColor == "YELLOW"){
						
						explode(t,r);
						
					} else if(destroyedBrickColor == "GREEN"){
						
						ball.canDestroy = true;
						
					} else{}
					
				}	//End of r loop
				
			}	//End of t loop
			
			round++;
			
			oddMove--;
			
			//Change coordinates of ball
			if(ball.canMove == true){
				
				ball.x += x;
				ball.y += y;
				
			} else {
				
				if(paddle.y != 1 && paddle.y + 5 != 13){
					ball.y += ballCase;
				}
				
			}
			
			if(ball.x == 23 || ball.y == 13){
				
				gameOver();
			
			}
			
			if(brickNumber == 0){
				
				System.out.println("You win :)");
				System.exit(0);
				
			}
				
		}	//End of while
		
	}	//End of play method
	
}	//End of class