package project142;

import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.image.ImageObserver;
import javax.swing.ImageIcon;

public class Frog {
    
    Image frog1 = new ImageIcon(getClass().getResource("/project142/imagepackage/frog1.png")).getImage();
    Image frog2 = new ImageIcon(getClass().getResource("/project142/imagepackage/frog2.png")).getImage();
    Image frog3 = new ImageIcon(getClass().getResource("/project142/imagepackage/frog3.png")).getImage();
    
    int frogX = 80;
    int frogY = 335;
    
    public Frog(){
        
        super();
        
    }

    public void drawFrog(Graphics g, ImageObserver o, int frogNum){
            
       Graphics2D g2d = (Graphics2D) g.create();
       
       if (frogNum == 1){
           
           g2d.drawImage(frog1, frogX, frogY, o);
           
       } else if (frogNum == 2){
           
           g2d.drawImage(frog2, frogX, frogY, o);
           
       } else if (frogNum == 3){
           
           g2d.drawImage(frog3, frogX, frogY, o);
           
       }
       
    }
    
}