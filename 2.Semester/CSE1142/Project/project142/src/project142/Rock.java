package project142;

import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.image.ImageObserver;
import javax.swing.ImageIcon;

public class Rock {
    
    Image rock = new ImageIcon(getClass().getResource("/project142/imagepackage/rock.png")).getImage();
    
    int rockX = 1170;
    int rockY = 355;
    
    public Rock(){   
        
    }
    
    public Rock(int rockX, int rockY){
       
        this.rockX = rockX;
        this.rockY = rockY;
    
    }

    public void drawRock(Graphics g, ImageObserver o){
            
       Graphics2D g2d = (Graphics2D) g.create();     
       
       g2d.drawImage(rock, rockX, rockY, o);
       
    }
    
}