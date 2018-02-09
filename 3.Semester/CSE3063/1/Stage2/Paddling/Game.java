/*
 *		@author Oguzhan BOLUKBAS - 150114022 - Marmara University C.S.E.
 * 
 * 		CSE3063 - Object Oriented Software Design Project #1
 * 
 * 		Start time: 2016/10/24 - 01:05 a.m.
 * 		End time: 2016/11/17 - 22:07 p.m.
 * 
 * 		This program is a game which is like Brick Braker or Dxball
 * 	With entering "a", "s" and "d" character, the paddle moves and game is played.
 * 	"a" character is to move left, "d" character is to move right, "s" character is
 * 	to stay at same position and throwing the ball when it is stacked
 * 
 */

public class Game{

	public static char[][] grid  = new char[24][51];
	
	public static void main(String[] args) {
		
		Board board = new Board();
		
		board.play();
		
	}
	
}