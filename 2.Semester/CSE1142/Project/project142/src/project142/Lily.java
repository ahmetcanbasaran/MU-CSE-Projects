package project142;

import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.image.ImageObserver;
import javax.swing.ImageIcon;

public class Lily {
    
    Image lily = new ImageIcon(getClass().getResource("/project142/imagepackage/lily.png")).getImage();
    
    int lilyX = 1169;
    int lilyY = 425;
    
    public Lily(){        
    }
    
    public Lily(int lilyX, int lilyY){

        this.lilyX = lilyX;
        this.lilyY = lilyY;
        
    }
    
    public void drawLily(Graphics g, ImageObserver o){
            
       Graphics2D g2d = (Graphics2D) g.create();     
       
       g2d.drawImage(lily, lilyX, lilyY, o);
       
    }

}